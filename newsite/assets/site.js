/* ============================================================
   METHOD ACTING CENTER — JS partagé (site v2)
   - menu mobile
   - apparitions au scroll
   - formulaire de contact (Web3Forms)
   ============================================================ */
(function(){
  "use strict";

  /* >>> Collez ici la clé Web3Forms (la même que la landing JPO) <<< */
  var WEB3FORMS_KEY = "32e0909e-41ce-41e3-9071-bd30e997e69f";

  /* ---- menu mobile ---- */
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.querySelector(".nav-menu");
  if(toggle && menu){
    toggle.addEventListener("click", function(){
      menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", menu.classList.contains("open") ? "true" : "false");
    });
    menu.querySelectorAll("a").forEach(function(a){
      a.addEventListener("click", function(){ menu.classList.remove("open"); });
    });
  }

  /* ---- hauteur du bloc fixe (bandeau + header) pour les ancres ---- */
  var topbar=document.querySelector(".topbar");
  function setTopbarH(){ if(topbar) document.documentElement.style.setProperty("--topbar-h", topbar.offsetHeight+"px"); }
  setTopbarH(); window.addEventListener("resize", setTopbarH); window.addEventListener("load", setTopbarH);

  /* ---- apparitions au scroll ---- */
  var reveals = [].slice.call(document.querySelectorAll("[data-reveal]"));
  if("IntersectionObserver" in window && reveals.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold:0.12, rootMargin:"0px 0px -8% 0px" });
    reveals.forEach(function(el){ io.observe(el); });
  } else { reveals.forEach(function(el){ el.classList.add("in"); }); }

  /* ---- formulaire de contact ---- */
  var form = document.getElementById("contact-form");
  if(form){
    var ok = document.getElementById("contact-success");
    var errBox = document.getElementById("contact-error");
    function field(n){ var el=form.querySelector('[name="'+n+'"]'); return el?String(el.value||"").trim():""; }
    form.addEventListener("submit", function(e){
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]'); var label = btn?btn.innerHTML:"";
      if(errBox){ errBox.style.display="none"; }
      var payload = {
        access_key: WEB3FORMS_KEY,
        subject: "Nouveau message — site Method Acting Center",
        from_name: "Site Method Acting Center",
        "Prénom": field("prenom"),
        "Nom": field("nom"),
        "Email": field("email"),
        "Téléphone": field("telephone") || "—",
        "Parcours": field("parcours") || "—",
        "Comment nous a connus": field("source") || "—",
        "Message": field("message") || "—",
        botcheck: (function(){ var b=form.querySelector('[name="botcheck"]'); return b?b.checked:false; })()
      };
      if(!WEB3FORMS_KEY){ if(window.console) console.warn("Web3Forms: clé manquante."); showOk(); return; }
      if(btn){ btn.disabled=true; btn.innerHTML="Envoi en cours…"; }
      fetch("https://api.web3forms.com/submit", {
        method:"POST", headers:{"Content-Type":"application/json","Accept":"application/json"},
        body: JSON.stringify(payload)
      }).then(function(r){ return r.json(); }).then(function(d){
        if(d && d.success){ showOk(); } else { throw new Error((d&&d.message)||"echec"); }
      }).catch(function(){
        if(btn){ btn.disabled=false; btn.innerHTML=label; }
        if(errBox){ errBox.style.display=""; errBox.scrollIntoView({behavior:"smooth",block:"center"}); }
      });
    });
    function showOk(){ if(ok){ form.style.display="none"; ok.style.display=""; ok.scrollIntoView({behavior:"smooth",block:"center"}); } }
  }

  /* ---- formulaire d'inscription JPO (ateliers + créneaux) ---- */
  /* JPO de décembre (rentrée de janvier 2027) : le planning horaire détaillé sera publié
     prochainement — on réserve l'atelier + le jour, le bureau confirme le créneau par email. */
  var JPO_DAYS = ["Samedi 12 déc.","Dimanche 13 déc.","Indifférent (l'un ou l'autre)"];
  var JPO_ATELIERS = [
    { id:"emotionnel",   seg:"#cf5a54", name:"Faire jaillir de vraies émotions", tech:"Acting · Travail Émotionnel",                     slots:JPO_DAYS },
    { id:"scene",        seg:"#cf5a54", name:"Donner vie à un texte",            tech:"Acting · Travail de Scène",                       slots:JPO_DAYS },
    { id:"impro",        seg:"#cf5a54", name:"Inventer dans l'instant",          tech:"Acting · Improvisation",                          slots:JPO_DAYS },
    { id:"amateur",      seg:"#4b4b4b", name:"Oser vous libérer",                 tech:"Acting Amateur",                                  slots:JPO_DAYS },
    { id:"srda",         seg:"#4a6fb5", name:"Écrire & réaliser vos films",      tech:"Scénario, Réalisation & Direction d'acteurs",     slots:JPO_DAYS },
    { id:"english",      seg:"#5f7a3a", name:"Jouer vrai, en anglais",           tech:"Acting in English",                               slots:JPO_DAYS },
    { id:"screenwriting",seg:"#5f7a3a", name:"Écrire pour l'écran, en anglais",  tech:"Screenwriting in English",                        slots:JPO_DAYS }
  ];
  function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }
  function initJpo(){
    var form=document.getElementById("jpo-form"); if(!form) return;
    var list=document.getElementById("jpo-list"), recap=document.getElementById("jpo-recap"),
        ok=document.getElementById("jpo-success"), errBox=document.getElementById("jpo-error"),
        successRecap=document.getElementById("jpo-success-recap");
    list.innerHTML = JPO_ATELIERS.map(function(a){
      var opts='<option value="">— Je ne réserve pas cet atelier —</option>'+a.slots.map(function(s){return '<option value="'+esc(s)+'">'+esc(s)+'</option>';}).join("");
      return '<div class="book-row" style="--seg:'+a.seg+'">'+
        '<div class="book-name"><strong>'+esc(a.name)+'</strong><span class="book-cat">'+esc(a.tech)+'</span></div>'+
        '<select class="book-select" data-name="'+esc(a.name)+'" data-tech="'+esc(a.tech)+'">'+opts+'</select></div>';
    }).join("");
    var selects=[].slice.call(list.querySelectorAll("select"));
    function chosen(){ return selects.filter(function(s){return s.value;}).map(function(s){return {name:s.getAttribute("data-name"), tech:s.getAttribute("data-tech"), slot:s.value};}); }
    function field(n){ var el=form.querySelector('[name="'+n+'"]'); return el?String(el.value||"").trim():""; }
    function updateRecap(){
      var ch=chosen();
      if(!ch.length){ recap.className="book-recap"; recap.textContent="Aucun atelier sélectionné pour l’instant."; return; }
      recap.className="book-recap active";
      recap.innerHTML=ch.length+" atelier"+(ch.length>1?"s":"")+" : "+ch.map(function(c){return "<strong>"+esc(c.name)+"</strong> ("+esc(c.slot)+")";}).join(" · ");
    }
    selects.forEach(function(s){ s.addEventListener("change",updateRecap); });
    updateRecap();
    form.addEventListener("submit",function(e){
      e.preventDefault();
      var ch=chosen();
      if(!ch.length){ recap.className="book-recap warn"; recap.textContent="Choisissez au moins un atelier (avec son créneau) avant d’envoyer."; recap.scrollIntoView({behavior:"smooth",block:"center"}); return; }
      var btn=form.querySelector('button[type="submit"]'), label=btn?btn.innerHTML:"";
      if(errBox) errBox.style.display="none";
      var payload={
        access_key: WEB3FORMS_KEY,
        subject: "Inscription JPO — "+((field("prenom")+" "+field("nom")).trim()||"sans nom"),
        from_name: "Inscriptions JPO · Method Acting Center",
        "Prénom": field("prenom"), "Nom": field("nom"), "Email": field("email"),
        "Téléphone": field("telephone")||"—",
        "Ateliers réservés": ch.map(function(c){return "• "+c.tech+" — "+c.slot;}).join("\n"),
        "Comment nous a connus": field("source")||"—",
        "Message": field("message")||"—",
        botcheck: (function(){ var b=form.querySelector('[name="botcheck"]'); return b?b.checked:false; })()
      };
      function done(){ if(successRecap) successRecap.innerHTML="Merci&nbsp;! Nous avons bien reçu votre demande pour "+ch.length+" atelier"+(ch.length>1?"s":"")+". Un membre de l’équipe vous confirme votre place très vite."; form.style.display="none"; ok.style.display=""; ok.scrollIntoView({behavior:"smooth",block:"center"}); }
      if(!WEB3FORMS_KEY){ if(window.console) console.warn("Web3Forms: clé manquante."); done(); return; }
      if(btn){ btn.disabled=true; btn.innerHTML="Envoi en cours…"; }
      fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(payload)})
        .then(function(r){return r.json();}).then(function(d){ if(d&&d.success){done();}else{throw new Error((d&&d.message)||"echec");} })
        .catch(function(){ if(btn){btn.disabled=false;btn.innerHTML=label;} if(errBox){errBox.style.display="";errBox.scrollIntoView({behavior:"smooth",block:"center"});} });
    });
  }
  initJpo();

  /* ---- formulaires génériques : cours d'essai, stages, inscription ---- */
  function bindForm(cfg){
    var form=document.getElementById(cfg.id); if(!form) return;
    var base=cfg.id.replace(/-form$/,"");
    var ok=document.getElementById(base+"-success"), errBox=document.getElementById(base+"-error"), recap=document.getElementById(base+"-recap");
    function field(n){ var el=form.querySelector('[name="'+n+'"]'); return el?String(el.value||"").trim():""; }
    function checked(n){ return [].slice.call(form.querySelectorAll('input[name="'+n+'"]:checked')).map(function(c){return c.value;}); }
    if(recap && cfg.recapName){
      var boxes=[].slice.call(form.querySelectorAll('input[name="'+cfg.recapName+'"]'));
      function updateRecap(){
        var ch=checked(cfg.recapName);
        if(!ch.length){ recap.className="book-recap"; recap.textContent=cfg.recapEmpty; return; }
        recap.className="book-recap active";
        recap.innerHTML=ch.length+" "+cfg.recapUnit+(ch.length>1?"s":"")+" : "+ch.map(function(c){return "<strong>"+esc(c)+"</strong>";}).join(" · ")+(cfg.recapHint&&ch.length>2?"<br><span style=\"color:var(--muted)\">"+cfg.recapHint+"</span>":"");
      }
      boxes.forEach(function(b){ b.addEventListener("change",updateRecap); });
      updateRecap();
    }
    form.addEventListener("submit",function(e){
      e.preventDefault();
      if(cfg.validate){ var msg=cfg.validate(field,checked); if(msg){ if(recap){ recap.className="book-recap warn"; recap.textContent=msg; recap.scrollIntoView({behavior:"smooth",block:"center"}); } else { alert(msg); } return; } }
      var btn=form.querySelector('button[type="submit"]'), label=btn?btn.innerHTML:"";
      if(errBox) errBox.style.display="none";
      var name=(field("prenom")+" "+field("nom")).trim()||"sans nom";
      var payload={ access_key:WEB3FORMS_KEY, subject:cfg.subject+" — "+name, from_name:cfg.from };
      cfg.fields.forEach(function(f){ payload[f[0]] = (typeof f[1]==="function" ? f[1](field,checked) : field(f[1])) || "—"; });
      payload.botcheck=(function(){ var b=form.querySelector('[name="botcheck"]'); return b?b.checked:false; })();
      function done(){ form.style.display="none"; if(ok){ ok.style.display=""; ok.scrollIntoView({behavior:"smooth",block:"center"}); } }
      if(!WEB3FORMS_KEY){ if(window.console) console.warn("Web3Forms: clé manquante."); done(); return; }
      if(btn){ btn.disabled=true; btn.innerHTML="Envoi en cours…"; }
      fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(payload)})
        .then(function(r){return r.json();}).then(function(d){ if(d&&d.success){done();}else{throw new Error((d&&d.message)||"echec");} })
        .catch(function(){ if(btn){btn.disabled=false;btn.innerHTML=label;} if(errBox){errBox.style.display="";errBox.scrollIntoView({behavior:"smooth",block:"center"});} });
    });
  }
  function joinList(list){ return list.length ? list.map(function(v){return "• "+v;}).join("\n") : ""; }

  bindForm({
    id:"essai-form", subject:"Cours d'essai", from:"Cours d'essai · Method Acting Center",
    recapName:"atelier", recapUnit:"atelier", recapEmpty:"Aucun atelier sélectionné pour l’instant.",
    recapHint:"Vous avez droit à 2 essais gratuits : le bureau vous précisera les conditions au-delà.",
    validate:function(field,checked){ return checked("atelier").length ? "" : "Cochez au moins un atelier à tester avant d’envoyer."; },
    fields:[["Ateliers à tester",function(f,c){return joinList(c("atelier"));}],["Préférence","preference"],["Prénom","prenom"],["Nom","nom"],["Email","email"],["Téléphone","telephone"],["Message","message"],["Comment nous a connus","source"]]
  });
  bindForm({
    id:"stages-form", subject:"Réservation stage", from:"Stages · Method Acting Center",
    recapName:"stage", recapUnit:"stage", recapEmpty:"Aucun stage coché pour l’instant.",
    validate:function(field,checked){ return checked("stage").length ? "" : "Cochez au moins un stage avant d’envoyer."; },
    fields:[["Stages",function(f,c){return joinList(c("stage"));}],["Prénom","prenom"],["Nom","nom"],["Email","email"],["Téléphone","telephone"],["Message","message"],["Comment nous a connus","source"]]
  });
  /* compte à rebours « J-x » des prochains stages */
  [].slice.call(document.querySelectorAll(".next-count[data-date]")).forEach(function(el){
    var d=new Date(el.getAttribute("data-date")+"T00:00:00"), now=new Date(); now.setHours(0,0,0,0);
    var days=Math.round((d-now)/86400000);
    el.textContent = days>1 ? "J-"+days : days===1 ? "Demain" : days===0 ? "Aujourd’hui" : "";
  });

  /* boutons « Réserver ce stage » et ?stage= : cochent le(s) stage(s) dans le formulaire */
  (function(){
    var form=document.getElementById("stages-form"); if(!form) return;
    var boxes=[].slice.call(form.querySelectorAll('input[name="stage"]')); if(!boxes.length) return;
    var tmp=document.createElement("textarea");
    function decode(t){ tmp.innerHTML=t; return tmp.value; }
    function norm(t){ return decode(t).replace(/\s+/g," ").trim(); }
    function tick(box, ms){
      if(!box) return;
      box.checked=true; box.dispatchEvent(new Event("change",{bubbles:true}));
      var row=box.closest(".pick"); if(row){ row.classList.add("is-prefilled"); setTimeout(function(){ row.classList.remove("is-prefilled"); }, ms||2500); }
    }
    /* arrivée depuis une autre page (landings…) : ?stage=a|b|scenario|camera|hiver|printemps (plusieurs séparés par des virgules) */
    try{
      var KEYS={a:"Stage A", b:"Stage B", scenario:"Stage Scénario", camera:"Acting Caméra", hiver:"intensif d’hiver", printemps:"intensif de printemps", ete:"intensif d’été"};
      var q=new URLSearchParams(location.search).get("stage");
      if(q){ q.toLowerCase().split(",").forEach(function(key){ var needle=KEYS[key.trim()]; if(!needle) return;
        tick(boxes.filter(function(b){ return norm(b.value).indexOf(needle)>=0; })[0], 4000); }); }
    }catch(e){}
    [].slice.call(document.querySelectorAll("[data-stage]")).forEach(function(b){
      b.addEventListener("click",function(){
        var want=norm(b.getAttribute("data-stage"));
        tick(boxes.filter(function(x){ return norm(x.value)===want; })[0]);
      });
    });
  })();

  bindForm({
    id:"inscription-form", subject:"Demande d'inscription", from:"Inscriptions · Method Acting Center",
    recapName:"programme", recapUnit:"programme", recapEmpty:"Aucun programme coché pour l’instant — vous pouvez aussi ne choisir que des cours ponctuels.",
    validate:function(field,checked){ return (checked("programme").length||checked("option").length) ? "" : "Cochez au moins un programme ou un cours ponctuel avant d’envoyer."; },
    fields:[["Programmes",function(f,c){ return joinList(c("programme").map(function(v){ if(/Scénario/.test(v)) return v+" — "+f("scenario_annee"); if(/Acting/.test(v)) return v+" — "+f("acting_annee"); return v; })); }],["Cours ponctuels",function(f,c){return joinList(c("option"));}],["Rentrée souhaitée","rentree"],["Créneaux préférés","creneau"],["Prénom","prenom"],["Nom","nom"],["Email","email"],["Téléphone","telephone"],["Message","message"],["Comment nous a connus","source"]]
  });
})();
