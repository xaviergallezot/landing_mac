(function () {
  "use strict";

  /* ============================================================
     IMAGES — collez ici les URL de la Médiathèque WordPress.
     Tant qu'une url est vide ou invalide, un cadre étiqueté s'affiche.
     ============================================================ */
  var IMAGES = {
__IMAGES__
  };

  /* ============================================================
     AVIS GOOGLE — uniquement de VRAIS avis de la fiche Google.
     Ajoutez-en autant que vous voulez : le carrousel s'adapte.
     ============================================================ */
  var REVIEWS = [
    { quote: "Quelle école incroyable ! Formation et formateurs au top !", name: "Quentin B." },
    { quote: "The best experience ever! The best school in Paris…", name: "Jake F." },
    { quote: "Excellente école :) rien à dire, je recommande vivement !!", name: "Alix A." }
  ];

  var HERO_KEYS = ["hero_kramer", "hero_felure", "hero_joseph", "hero_king"];

  var PROGRAM = [
    { label: "1ère année", title: "Les bases de la Méthode", ateliers: [
      { name: "Exploration 1", tagline: "Le training de fond de l’acting", desc: "Faire surgir vos émotions, enrichir votre imaginaire, vous débarrasser du trac, aiguiser votre concentration et votre écoute." },
      { name: "Backstory", tagline: "Vivre réellement des situations imaginaires", desc: "La première approche des scènes à deux : de l’improvisation vers la scène écrite, jusqu’aux scènes tirées de pièces et de scénarios." },
      { name: "Scènes 1", tagline: "Sculpter le silence", desc: "Le travail de fond du sous-texte : construire une scène seul, sans texte ni mime, portée par le langage du corps et des émotions." }
    ] },
    { label: "2ème année", title: "Faire de la Méthode sa méthode", ateliers: [
      { name: "Exploration 2", tagline: "Approfondir corps, imaginaire et émotions", desc: "Le training aborde des thématiques spécifiques : l’horreur, la séduction, la comédie…" },
      { name: "Scènes 2", tagline: "La science du jeu", desc: "Un atelier exclusif, partagé seulement avec le HB Studio de New York : de nouveaux outils pour enrichir vos performances." },
      { name: "Scènes 3", tagline: "De la scène à la caméra", desc: "Apprendre à structurer vos performances dans des scènes tirées de pièces et de films, début du jeu face caméra." }
    ] },
    { label: "3ème année", title: "Maîtriser la composition de personnages", ateliers: [
      { name: "Composition A & Exploration 3", tagline: "L’art de la métamorphose", desc: "Enquête minutieuse et exploration profonde de votre personnage. L’ultime stade de l’acting : devenir quelqu’un d’autre." },
      { name: "Composition B", tagline: "L’incarnation de votre personnage", desc: "Composer votre personnage scène après scène, dans la perspective du rôle tout entier." },
      { name: "Suivi de carrière & développement personnel", tagline: "Aborder les marchés professionnels", desc: "Comprendre les marchés, s’outiller (book photos, bande démo) et trouver les ressources pour donner le meilleur de vous-même en casting." }
    ] },
    { label: "4ème année", title: "La touche finale : vous aiguisez vos performances, nous produisons vos outils pour démarcher", ateliers: [
      { name: "Acting Caméra & Tournages", tagline: "Gérer les impératifs du cinéma dans votre jeu", desc: "Un atelier de scènes tournées dans les conditions réelles d’un plateau : les réflexes qui manquent trop souvent aux acteurs débutants." },
      { name: "Scènes 4", tagline: "Le plus haut niveau d’exigence", desc: "Un approfondissement de tous les outils vus les années précédentes avec une exigence encore plus élevée." }
    ], deliverables: ["3 scènes filmées et montées", "1 book photos", "1 CV", "1 bande démo", "1 vidéo de présentation"] }
  ];

  var ROOT = document.getElementById("mac-landing");
  if (!ROOT) return;

  function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
  function conf(key){ return IMAGES[key] || {}; }
  function placeholder(label){
    var d = document.createElement("div");
    d.className = "mac-ph"; d.setAttribute("role","img");
    d.setAttribute("aria-label", label || "Visuel à ajouter");
    d.textContent = label || "Visuel à ajouter";
    return d;
  }

  function applyImages(){
    ROOT.querySelectorAll("img[data-img]").forEach(function(img){
      var c = conf(img.getAttribute("data-img"));
      var label = c.label || img.getAttribute("alt") || "Visuel à ajouter";
      if (!c.url){ img.replaceWith(placeholder(label)); return; }
      img.onerror = function(){ if (img.parentNode) img.replaceWith(placeholder(label)); };
      img.src = c.url;
    });
  }

  /* hover / focus */
  function parseDecl(s){
    return (s||"").split(";").map(function(x){return x.trim();}).filter(Boolean).map(function(x){
      var i=x.indexOf(":"); return [x.slice(0,i).trim(), x.slice(i+1).trim()];
    });
  }
  function bindState(attr,on,off){
    ROOT.querySelectorAll("["+attr+"]").forEach(function(el){
      var d=parseDecl(el.getAttribute(attr));
      el.addEventListener(on,function(){ el.__p={}; d.forEach(function(p){ el.__p[p[0]]=el.style.getPropertyValue(p[0]); el.style.setProperty(p[0],p[1]); }); });
      el.addEventListener(off,function(){ if(el.__p) d.forEach(function(p){ el.style.setProperty(p[0], el.__p[p[0]]||""); }); });
    });
  }

  /* reveal on scroll */
  function initReveal(){
    var r = ROOT.querySelectorAll("[data-reveal]");
    r.forEach(function(el){ el.style.opacity="0"; el.style.transform="translateY(24px)"; el.style.transition="opacity .55s ease, transform .55s ease"; });
    if(!("IntersectionObserver" in window)){ r.forEach(function(el){ el.style.opacity="1"; el.style.transform="none"; }); return; }
    var io=new IntersectionObserver(function(en){ en.forEach(function(e){ if(e.isIntersecting){ e.target.querySelectorAll("[data-reveal]").forEach(function(el){ el.style.opacity="1"; el.style.transform="translateY(0)"; }); io.unobserve(e.target); } }); },{threshold:0.08});
    ROOT.querySelectorAll("section[data-screen-label]").forEach(function(s){ io.observe(s); });
  }

  /* hero carousel */
  function initHero(){
    var wrap=document.getElementById("hero-slides"), dotsEl=document.getElementById("hero-dots");
    if(!wrap||!dotsEl) return;
    var idx=0,timer=null,slides=[],dots=[];
    HERO_KEYS.forEach(function(key,i){
      var c=conf(key), s=document.createElement("div");
      s.style.cssText="position:absolute;inset:0;width:100%;height:100%;opacity:"+(i===0?"1":"0")+";transition:opacity 1s ease;";
      if(c.url){ var im=document.createElement("img"); im.alt=c.label||""; im.style.cssText="width:100%;height:100%;object-fit:cover;display:block;"; im.onerror=function(){ s.innerHTML=""; s.appendChild(placeholder(c.label)); }; im.src=c.url; s.appendChild(im); }
      else { s.appendChild(placeholder(c.label)); }
      wrap.appendChild(s); slides.push(s);
      var b=document.createElement("button"); b.type="button"; b.setAttribute("aria-label","Voir : "+(c.label||("visuel "+(i+1))));
      b.addEventListener("click",function(){ go(i); restart(); }); dotsEl.appendChild(b); dots.push(b);
    });
    function paint(){
      slides.forEach(function(s,i){ s.style.opacity=i===idx?"1":"0"; });
      dots.forEach(function(b,i){ b.style.cssText="width:"+(i===idx?"26px":"8px")+";height:8px;border-radius:999px;border:none;cursor:pointer;padding:0;background:"+(i===idx?"#E0261F":"rgba(255,255,255,0.65)")+";transition:all .3s ease;"; });
    }
    function go(i){ idx=(i+slides.length)%slides.length; paint(); }
    function restart(){ if(timer) clearInterval(timer); timer=setInterval(function(){ go(idx+1); },4500); }
    paint(); restart();
  }

  /* program (4-year tabs) */
  function initProgram(){
    var tabsEl=document.getElementById("program-tabs"), titleEl=document.getElementById("program-title"),
        atEl=document.getElementById("program-ateliers"), delEl=document.getElementById("program-deliverables");
    if(!tabsEl||!titleEl||!atEl||!delEl) return;
    var active=0, tabs=[];
    function tabStyle(on){ return "font-family:'Oswald',sans-serif;font-size:14px;letter-spacing:2px;text-transform:uppercase;font-weight:600;padding:12px 20px;border-radius:999px;cursor:pointer;transition:all .2s ease;border:1px solid "+(on?"#E0261F":"rgba(20,18,15,0.2)")+";background:"+(on?"#E0261F":"transparent")+";color:"+(on?"#FFFFFF":"#6B655C")+";"; }
    PROGRAM.forEach(function(y,i){ var b=document.createElement("button"); b.type="button"; b.textContent=y.label; b.style.cssText=tabStyle(i===0); b.addEventListener("click",function(){ active=i; render(); }); tabsEl.appendChild(b); tabs.push(b); });
    function render(){
      var y=PROGRAM[active];
      tabs.forEach(function(b,i){ b.style.cssText=tabStyle(i===active); });
      titleEl.textContent=y.title;
      atEl.innerHTML=y.ateliers.map(function(a){
        return '<div style="display:flex;flex-direction:column;gap:10px;border-top:2px solid #E0261F;padding-top:18px">'+
          '<h4 style="font-family:\'Oswald\',sans-serif;font-size:20px;text-transform:uppercase;margin:0">'+esc(a.name)+'</h4>'+
          '<p style="margin:0;font-size:14px;font-style:italic;color:#E0261F">'+esc(a.tagline)+'</p>'+
          '<p style="margin:0;font-size:15px;line-height:1.65;color:#6B655C">'+esc(a.desc)+'</p></div>';
      }).join("");
      if(y.deliverables&&y.deliverables.length){
        delEl.style.display="";
        delEl.innerHTML='<div style="display:flex;flex-direction:column;gap:14px;border-top:1px solid #EEE9DF;padding-top:24px">'+
          '<p style="margin:0;font-size:15px;font-weight:600;color:#14120F">À la sortie de cet atelier, vous repartez avec&nbsp;:</p>'+
          '<div style="display:flex;gap:10px;flex-wrap:wrap">'+
          y.deliverables.map(function(d){ return '<span style="font-family:\'Oswald\',sans-serif;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;background:#F7F4EE;color:#14120F;padding:10px 16px;border-radius:999px">'+esc(d)+'</span>'; }).join("")+
          '</div></div>';
      } else { delEl.style.display="none"; delEl.innerHTML=""; }
    }
    render();
  }

  /* JPO accordion (one open at a time) */
  function initJpo(){
    var cards=[].slice.call(ROOT.querySelectorAll(".jpo-card"));
    cards.forEach(function(card){
      var head=card.querySelector(".jpo-head");
      head.addEventListener("click",function(){
        var isOpen=card.classList.contains("open");
        cards.forEach(function(c){ c.classList.remove("open"); var h=c.querySelector(".jpo-head"); if(h) h.setAttribute("aria-expanded","false"); });
        if(!isOpen){ card.classList.add("open"); head.setAttribute("aria-expanded","true"); }
      });
    });
  }

  /* reviews carousel */
  function initReviews(){
    var track=document.getElementById("rev-track"), dotsEl=document.getElementById("rev-dots"),
        prev=document.getElementById("rev-prev"), next=document.getElementById("rev-next");
    if(!track) return;
    if(!REVIEWS.length){ var c=track.closest(".rev-carousel"); if(c) c.style.display="none"; return; }
    track.innerHTML = REVIEWS.map(function(r){
      var initial = (r.name||"?").trim().charAt(0).toUpperCase();
      return '<div class="rev-slide"><div class="rev-card">'+
        '<span class="rev-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'+
        '<p class="rev-quote">&laquo;&nbsp;'+esc(r.quote)+'&nbsp;&raquo;</p>'+
        '<div class="rev-author"><span class="rev-avatar">'+esc(initial)+'</span>'+
        '<span><span class="rev-name">'+esc(r.name)+'</span><br><span class="rev-src">avis Google</span></span></div>'+
        '</div></div>';
    }).join("");
    var slides=[].slice.call(track.children);
    var idx=0, perView=1, maxIdx=0, timer=null;
    function computePer(){ var w=ROOT.clientWidth||window.innerWidth; return w>=760 ? Math.min(2, slides.length) : 1; }
    function layout(){
      perView=computePer(); maxIdx=Math.max(0, slides.length-perView);
      slides.forEach(function(s){ s.style.flexBasis=(100/perView)+"%"; });
      if(idx>maxIdx) idx=maxIdx;
      var hasNav = slides.length>perView;
      [prev,next].forEach(function(b){ if(b) b.style.display=hasNav?"":"none"; });
      buildDots(hasNav); paint();
    }
    function buildDots(show){
      dotsEl.innerHTML="";
      if(!show){ return; }
      for(var i=0;i<=maxIdx;i++){ (function(i){ var b=document.createElement("button"); b.type="button"; b.className="rev-dot"+(i===idx?" active":""); b.setAttribute("aria-label","Avis "+(i+1)); b.addEventListener("click",function(){ idx=i; paint(); restart(); }); dotsEl.appendChild(b); })(i); }
    }
    function paint(){
      track.style.transform="translateX(-"+(idx*(100/perView))+"%)";
      [].slice.call(dotsEl.children).forEach(function(d,i){ d.className="rev-dot"+(i===idx?" active":""); });
    }
    function go(d){ idx=(idx+d); if(idx<0) idx=maxIdx; if(idx>maxIdx) idx=0; paint(); }
    function restart(){ if(timer) clearInterval(timer); if(slides.length>perView) timer=setInterval(function(){ go(1); },5000); }
    if(prev) prev.addEventListener("click",function(){ go(-1); restart(); });
    if(next) next.addEventListener("click",function(){ go(1); restart(); });
    var rt; window.addEventListener("resize",function(){ clearTimeout(rt); rt=setTimeout(function(){ layout(); restart(); },150); });
    layout(); restart();
  }

  /* contact form */
  function initForm(){
    var form=document.getElementById("contact-form"), ok=document.getElementById("contact-success");
    if(!form||!ok) return;
    form.addEventListener("submit",function(e){ e.preventDefault(); form.style.display="none"; ok.style.display=""; ok.scrollIntoView({behavior:"smooth",block:"center"}); });
  }

  /* in-page anchor smooth scroll */
  function initAnchors(){
    ROOT.querySelectorAll('a[href^="#"]').forEach(function(a){
      a.addEventListener("click",function(e){
        var id=a.getAttribute("href").slice(1); if(!id) return;
        var t=document.getElementById(id); if(!t) return;
        e.preventDefault(); t.scrollIntoView({behavior:"smooth",block:"start"});
      });
    });
  }

  /* sticky mobile CTA: mobile only, appears after hero, hidden over the form */
  function initMobileCta(){
    var cta=document.getElementById("mobile-cta"); if(!cta) return;
    var contact=document.getElementById("contact");
    var overContact=false;
    if("IntersectionObserver" in window && contact){
      new IntersectionObserver(function(en){ overContact=en[0].isIntersecting; update(); },{threshold:0.05}).observe(contact);
    }
    function update(){
      var mobile=window.matchMedia("(max-width:760px)").matches;
      var scrolled=window.scrollY>window.innerHeight*0.6;
      if(mobile && scrolled && !overContact){ cta.style.display="block"; cta.style.opacity="1"; cta.style.transform="translateY(0)"; }
      else { cta.style.opacity="0"; cta.style.transform="translateY(120%)"; setTimeout(function(){ if(cta.style.opacity==="0") cta.style.display="none"; },300); }
    }
    window.addEventListener("scroll",update,{passive:true});
    window.addEventListener("resize",update);
    update();
  }

  function init(){ applyImages(); bindState("style-hover","mouseenter","mouseleave"); bindState("style-focus","focus","blur"); initReveal(); initHero(); initProgram(); initJpo(); initReviews(); initForm(); initAnchors(); initMobileCta(); }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init); else init();
})();
