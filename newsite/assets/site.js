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
  var JPO_ATELIERS = [
    { id:"emotionnel",   seg:"#cf5a54", name:"Faire jaillir de vraies émotions", tech:"Acting · Travail Émotionnel",                     slots:["Ven. 11 · 13h–15h","Sam. 12 · 13h–15h","Dim. 13 · 15h30–17h30"] },
    { id:"scene",        seg:"#cf5a54", name:"Donner vie à un texte",            tech:"Acting · Travail de Scène",                       slots:["Ven. 11 · 15h30–17h30","Sam. 12 · 15h30–17h30","Dim. 13 · 13h–15h"] },
    { id:"impro",        seg:"#cf5a54", name:"Inventer dans l'instant",          tech:"Acting · Improvisation",                          slots:["Sam. 12 · 10h–12h"] },
    { id:"amateur",      seg:"#4b4b4b", name:"Oser vous libérer",                 tech:"Acting Amateur",                                  slots:["Ven. 11 · 18h–20h"] },
    { id:"srda",         seg:"#4a6fb5", name:"Écrire & réaliser vos films",      tech:"Scénario, Réalisation & Direction d'acteurs",     slots:["Ven. 11 · 18h–20h","Sam. 12 · 13h–15h","Dim. 13 · 15h30–17h30"] },
    { id:"english",      seg:"#5f7a3a", name:"Jouer vrai, en anglais",           tech:"Acting in English",                               slots:["Sam. 12 · 18h–20h","Dim. 13 · 13h–15h"] },
    { id:"screenwriting",seg:"#5f7a3a", name:"Écrire pour l'écran, en anglais",  tech:"Screenwriting in English",                        slots:["Dim. 13 · 18h–20h"] }
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
})();
