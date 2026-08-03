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
})();
