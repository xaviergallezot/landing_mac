# -*- coding: utf-8 -*-
"""Construit la landing /stages/ à partir de la landing /jpo/ (qui reste intacte)."""
import re, base64, json

import os as _os
HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
SRC = _os.path.join(HERE, "static", "jpo", "index.html")
DST = _os.path.join(HERE, "dist", "stages", "index.html")
IMG = _os.path.join(HERE, "assets", "img") + "/"
SITE = "https://www.methodacting.fr/"

s = open(SRC, encoding="utf-8").read()

def cut(s, start, end):
    a = s.index(start); b = s.index(end, a)
    return s[:a] + s[b:], s[a:b]

def sub1(s, old, new, label=""):
    assert s.count(old) == 1, (label or old[:60], s.count(old))
    return s.replace(old, new)

# ---------- 1. HEAD : SEO ----------
s = sub1(s, "<title>Method Acting Center — Devenez acteur · Journées Portes Ouvertes à Paris</title>",
         "<title>Stages d'acting à Paris — Week-end &amp; intensifs · Method Acting Center</title>")
s = re.sub(r'<meta name="description" content="[^"]*">',
           '<meta name="description" content="Vous voulez devenir acteur ? Découvrez la Méthode (Stanislavski / Actors Studio) lors d\'un stage week-end ou intensif au Method Acting Center, Paris 13ᵉ. Prochain stage d\'initiation : 17 &amp; 18 octobre 2026.">\n'
           '  <link rel="canonical" href="https://www.methodacting.fr/stages/">\n'
           '  <meta name="robots" content="index, follow">\n'
           '  <meta property="og:type" content="website">\n'
           '  <meta property="og:url" content="https://www.methodacting.fr/stages/">\n'
           '  <meta property="og:title" content="Stages d\'acting à Paris — Method Acting Center">\n'
           '  <meta property="og:description" content="Un week-end pour vivre la Méthode. Prochain stage d\'initiation : 17 &amp; 18 octobre 2026, Paris 13ᵉ.">\n'
           '  <!-- Google Ads / Tag Manager : collez ici votre balise globale (gtag.js ou GTM). Les envois de formulaire réussis déclenchent dataLayer.push({event:"stage_form_success"}) et gtag("event","generate_lead") si gtag est présent. -->',
           s, count=1)

# ---------- 2. Bandeau cours d'essai retiré, header conservé (sticky) ----------
s = re.sub(r'  <div class="topbar">\n  <div class="annce">.*?</div>\n', '  <div class="topbar">\n', s, count=1, flags=re.S)
assert 'class="annce"' not in s

# ---------- 3. Navigation ----------
nav_old = re.search(r'      <nav style="display: flex; align-items: center; gap: 26px">.*?</nav>', s, re.S).group(0)
link = lambda href, txt: f'        <a href="{href}" class="nav-link" style="font-family: \'Oswald\', sans-serif; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; color: #6B655C; text-decoration: none" style-hover="color: #14120F">{txt}</a>'
nav_new = ('      <nav style="display: flex; align-items: center; gap: 26px">\n'
           + link("#methode", "La Méthode") + "\n" + link("#stages", "Stages week-end") + "\n" + link("#intensifs", "Intensifs") + "\n" + link("#avis", "Avis") + "\n"
           + '        <a href="#reservation" class="nav-cta">Réserver un stage</a>\n      </nav>')
s = s.replace(nav_old, nav_new)

# ---------- 4. Hero : CTA + mention discrète ----------
m = re.search(r'(<div class="hero-actions"[^>]*>).*?\n          </div>\n        </div>', s, re.S)
assert m
btn = "font-family: 'Oswald', sans-serif; font-size: 16px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; text-decoration: none; padding: 19px 36px; border-radius: 999px; text-align: center; transition: transform .15s ease, background .15s ease, border-color .15s ease"
hero_actions = (m.group(1) + "\n"
    f'          <a href="#stages" style="{btn}; background: #E0261F; color: #FFFFFF" style-hover="background: #14120F; color: #FFFFFF; transform: translateY(-2px)">Découvrir nos stages</a>\n'
    f'          <a href="#methode" style="{btn}; background: transparent; color: #14120F; padding: 18px 36px; border: 1px solid rgba(20,18,15,0.3)" style-hover="border-color: #14120F; color: #14120F; transform: translateY(-2px)">Comprendre la Méthode</a>\n'
    '          <div class="hero-next" style="font-family: \'Oswald\', sans-serif; font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #6B655C; text-align: center; margin-top: 2px">Prochain stage d\'initiation&nbsp;: <strong style="color: #14120F; font-weight: 600">17 &amp; 18 octobre 2026</strong> &middot; Paris 13ᵉ</div>\n'
    '        </div>')
s = s[:m.start()] + hero_actions + s[m.end():]

# ---------- 5. Sections à retirer ----------
s, _ = cut(s, "  <!-- ============ PAR OU COMMENCER ============ -->", "  <!-- ============ TALENT / METHODE ============ -->")
s, _ = cut(s, "  <!-- ============ JOURNEES PORTES OUVERTES (refonte) ============ -->", "  <!-- ============ NOS ACTEURS TOURNENT (carrousel continu) ============ -->")
s, films = cut(s, "  <!-- ============ NOS ACTEURS TOURNENT (carrousel continu) ============ -->", "  <!-- ============ AVIS (carrousel) ============ -->")
s, avis = cut(s, "  <!-- ============ AVIS (carrousel) ============ -->", "  <!-- ============ FAQ ============ -->")
s, _ = cut(s, "  <!-- ============ FAQ ============ -->", "  <!-- ============ FOOTER (identique au site) ============ -->")

# Avis : titre
avis = re.sub(r'<h2 style="([^"]*)">Ils sont venus d&eacute;couvrir la M&eacute;thode\.<br><span style="color: #E0261F">Voici ce qu&rsquo;ils en disent\.</span></h2>',
              r'<h2 style="\1">Ils ont tenté <span style="color: #E0261F">l\'expérience.</span></h2>', avis, count=1)
assert "Ils ont tenté" in avis
avis = avis.replace('padding: 100px 24px 100px;', 'padding: 100px 24px 40px;', 1)
# Films : phrase ajoutée
films = re.sub(r'(<p data-reveal style="font-size: 18px; line-height: 1.7; color: #6B655C; margin: 0; max-width: 74ch">.*?</p>)',
               r'\1\n      <p data-reveal style="font-size: 18px; line-height: 1.7; color: #14120F; margin: 0; max-width: 74ch; font-weight: 500">Retrouvez nos élèves et anciens élèves à l\'affiche de productions cinématographiques et audiovisuelles.</p>', films, count=1, flags=re.S)
assert "Retrouvez nos élèves" in films
films = films.replace('padding: 100px 24px 40px;', 'padding: 40px 24px 40px;', 1)

# ---------- 6. Données des sessions (à mettre à jour ici) ----------
# Chaque session : id, nom, date (texte), data-end (ISO : masquée automatiquement après), durée, tarif, intro courte
SESSIONS = {
 "a":  dict(name="Actors Studio A — Faites vos premiers pas dans la Méthode", short="Actors Studio A", date="17 & 18 octobre 2026", end="2026-10-18", duration="2 jours (week-end)", price="dès 160 €", kind="Stage week-end"),
 "sc": dict(name="Scénario, réalisation & direction d'acteurs", short="Scénario, réalisation & direction d'acteurs", date="7 & 8 novembre 2026", end="2026-11-08", duration="2 jours (week-end)", price="dès 160 €", kind="Stage week-end"),
 "b":  dict(name="Actors Studio B — Approche d'une scène", short="Actors Studio B", date="14 & 15 novembre 2026", end="2026-11-15", duration="2 jours (week-end)", price="dès 160 €", kind="Stage week-end"),
 "cam":dict(name="Acting Caméra", short="Acting Caméra", date="20 & 21 février 2027", end="2027-02-21", duration="2 jours (week-end)", price="Tarif sur demande", kind="Stage week-end"),
 "hiv":dict(name="Stage intensif d'hiver", short="Stage intensif d'hiver", date="9 & 10 janvier 2027", end="2027-01-10", duration="2 jours", price="Tarif sur demande", kind="Stage intensif"),
 "pri":dict(name="Stage intensif de printemps", short="Stage intensif de printemps", date="16, 17 & 18 avril 2027", end="2027-04-18", duration="3 jours", price="Tarif sur demande", kind="Stage intensif"),
}
def value(k):
    d = SESSIONS[k]; return f'{d["name"]} ({d["date"]})'
def esc_attr(t): return t.replace("&", "&amp;").replace('"', "&quot;")
def cta(k, label="Je m'inscris au stage"):
    return f'<a href="#reservation" class="jpo-cta" data-stage="{esc_attr(value(k))}">{label} &rarr;</a>'

def lis(items): return "".join(f"<li>{i}</li>" for i in items)

import io as _io
from PIL import Image as _PILImage
_EMB = {}
def embed(name, width=720, quality=66):
    key = (name, width, quality)
    if key in _EMB: return _EMB[key]
    im = _PILImage.open(IMG + name).convert("RGB")
    if im.width > width: im = im.resize((width, int(im.height * width / im.width)), _PILImage.LANCZOS)
    buf = _io.BytesIO(); im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    _EMB[key] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _EMB[key]
PHOTOS = {"sc": "tournage-equipe-terrasse-acteurs-method-acting-center.jpg", "b": "scene-de-bar-acteur-tournage-method-acting-center.jpg", "cam": "retour-camera-tournage-exterieur-actrices-method-acting-center.jpg", "hiv": "tournage-exterieur-foret-acteurs-method-acting-center.jpg", "pri": "direction-acteurs-stage-scenario-realisation-method-acting-center.jpg"}
def accordion(k, desc, programme, benefits, extra_note=""):
    d = SESSIONS[k]
    photo = f'<div class="stage-photo"><img src="/uploads/{PHOTOS[k]}" alt="{d["name"]} — Method Acting Center" loading="lazy"></div>' if k in PHOTOS else ""
    prog = "".join(f'<div class="jpo-field"><span class="jpo-label">{lab}</span><ul class="stage-list">{lis(items)}</ul></div>' for lab, items in programme)
    ben = f'<div class="jpo-field"><span class="jpo-label">Ce que vous en retirez</span><ul class="stage-list">{lis(benefits)}</ul></div>' if benefits else ""
    note = f'<p class="stage-note">{extra_note}</p>' if extra_note else ""
    return f'''        <!-- session {k} : {d["date"]} — masquée automatiquement après le {d["end"]} ; supprimez le bloc pour la retirer définitivement -->
        <div class="jpo-card stage-card" data-end="{d["end"]}" id="stage-{k}">
          <button class="jpo-head stage-head" type="button" aria-expanded="false">
            <div class="stage-head-main">
              <span class="stage-kind">{d["kind"]}</span>
              <h3 class="stage-title">{d["name"]}</h3>
              <div class="stage-meta"><span>{d["date"]}</span><span>{d["duration"]}</span><span class="stage-price">{d["price"]}</span></div>
              <p class="stage-short">{desc}</p>
            </div>
            <span class="jpo-plus" aria-hidden="true">+</span>
          </button>
          <div class="jpo-panel">
            <div class="jpo-panel-inner">
              {photo}
              {prog}
              {ben}
              <div class="jpo-field"><span class="jpo-label">Informations pratiques</span><p>Method Acting Center, 93 avenue d'Italie, Paris 13ᵉ &middot; {d["duration"]} &middot; {d["price"]}. Les horaires précis et les modalités vous sont confirmés par email après votre demande.</p></div>
              {note}
              {cta(k)}
            </div>
          </div>
        </div>
'''

FEAT_IMG = "/uploads/scene-theatre-tension-acteurs-method-acting-center.jpg"

d = SESSIONS["a"]
SECTIONS = f'''  <!-- ============ STAGES : INTRODUCTION + STAGE À LA UNE ============ -->
  <section id="stages" data-screen-label="Stages" style="background: #F7F4EE; border-radius: 40px 40px 0 0; margin-top: -40px; position: relative">
    <div style="max-width: 1200px; margin: 0 auto; padding: 100px 24px 48px; display: flex; flex-direction: column; gap: 48px">
      <div data-reveal style="display: flex; flex-direction: column; gap: 22px; max-width: 70ch">
        <div style="display: flex; align-items: center; gap: 12px">
          <span style="width: 40px; height: 2px; background: #E0261F; display: inline-block"></span>
          <span style="font-family: 'Oswald', sans-serif; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; color: #6B655C">Nos stages &middot; Paris 13ᵉ</span>
        </div>
        <h2 style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: clamp(40px, 5vw, 76px); text-transform: uppercase; line-height: 0.98; margin: 0">La Méthode ne se comprend pas seulement. <span style="color: #E0261F">Elle se vit.</span></h2>
        <p style="margin: 0; font-size: 19px; line-height: 1.75; color: #3B362F">Découvrez nos stages pratiques. Que vous souhaitiez faire vos premiers pas dans le jeu d'acteur, approfondir votre technique ou explorer l'écriture et la réalisation, chaque stage est une occasion d'expérimenter, de créer et de progresser.</p>
      </div>

      <!-- ======================================================================
           STAGE À LA UNE — bloc autonome.
           Après le {d["end"]} il est masqué automatiquement (data-end). Pour le remplacer :
           changez la session dans SESSIONS (script de génération) ou éditez le bloc ci-dessous
           sans toucher à l'introduction permanente au-dessus.
           ====================================================================== -->
      <article class="feat" data-reveal data-end="{d["end"]}" id="stage-une">
        <div class="feat-media">
          <img src="{FEAT_IMG}" alt="Scène de tension jouée par deux élèves acteurs du Method Acting Center" style="object-position: 50% 45%">
          <span class="feat-date">{d["date"]}</span>
        </div>
        <div class="feat-body">
          <span class="feat-tag">Stage à la une</span>
          <h3>Actors Studio A &mdash; Faites vos premiers pas dans la Méthode.</h3>
          <p class="feat-desc">Deux jours d'immersion pour découvrir les fondamentaux du jeu d'acteur, apprendre à mobiliser vos émotions et explorer votre créativité à travers des exercices pratiques, accompagnés par les coaches du Method Acting Center.</p>
          <ul class="stage-list feat-list">
            <li>Libérer votre expression et dépasser vos appréhensions.</li>
            <li>Découvrir comment accéder à des émotions authentiques.</li>
            <li>Développer votre imagination et votre écoute du partenaire.</li>
          </ul>
          <div class="feat-meta">
            <div><span>Dates</span><strong>{d["date"]}</strong></div>
            <div><span>Lieu</span><strong>Method Acting Center, Paris 13ᵉ</strong></div>
            <div><span>Durée</span><strong>{d["duration"]}</strong></div>
            <div><span>Tarif</span><strong class="feat-price">{d["price"]}</strong></div>
          </div>
          <a href="#reservation" class="feat-cta" data-stage="{esc_attr(value("a"))}">Je m'inscris au stage &rarr;</a>
        </div>
      </article>
      <!-- ====================== fin STAGE À LA UNE ====================== -->
    </div>
  </section>

  <!-- ============ AUTRES STAGES WEEK-END ============ -->
  <section id="weekend" data-screen-label="Stages week-end" style="background: #F7F4EE">
    <div style="max-width: 1200px; margin: 0 auto; padding: 32px 24px 80px; display: flex; flex-direction: column; gap: 32px">
      <div data-reveal style="display: flex; flex-direction: column; gap: 14px; max-width: 64ch">
        <div style="display: flex; align-items: center; gap: 12px">
          <span style="width: 40px; height: 2px; background: #E0261F; display: inline-block"></span>
          <span style="font-family: 'Oswald', sans-serif; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; color: #6B655C">Autres stages week-end</span>
        </div>
        <h2 style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: clamp(32px, 4vw, 56px); text-transform: uppercase; line-height: 1.02; margin: 0">Deux jours, <span style="color: #E0261F">une technique.</span></h2>
        <p style="margin: 0; font-size: 17px; line-height: 1.7; color: #6B655C">Chaque stage est autonome et se réserve indépendamment. Dépliez une carte pour voir le programme détaillé.</p>
      </div>
      <div data-reveal style="display: flex; flex-direction: column; gap: 16px">
{accordion("sc", "Explorez les liens entre écriture, mise en scène et direction d'acteurs, de l'intention à sa concrétisation.",
    [("Scénario", ["Les bases de l'écriture dramaturgique : écrire le comportement humain", "Travailler son inspiration avec des outils concrets", "Construire des personnages complexes et intéressants", "Structurer une intrigue en fonction de ses personnages", "Les bases de la vente d'un scénario"]),
     ("Réalisation & direction d'acteurs", ["Trouver sa vision unique de réalisateur", "Les piliers du langage cinématographique", "Diriger des acteurs pour qu'ils aillent loin dans l'émotion", "Les bases de la gestion de plateau et de l'intelligence sociale de tournage"])],
    ["Des outils pour rendre votre inspiration systématique : dites adieu à la page blanche", "Une introduction aux techniques d'écriture, de réalisation et de direction d'acteurs du Method Acting Center"])}
{accordion("b", "Approfondissez la Méthode et apprenez à la mettre au service d'une scène et de votre partenaire.",
    [("Au programme", ["Comprendre le sous-texte d'une scène", "Donner vie au texte de n'importe quelle scène, sans le réciter", "Infuser ses émotions au sein d'une scène écrite", "Travailler des scènes à deux, avec retours du coach"])],
    ["Rendre un texte naturel et chargé émotionnellement : donner l'illusion qu'il est spontané", "Une version développée de l'atelier « Travail de Scène »"],
    "Complémentaire au stage Actors Studio A : recommandé avant, mais pas obligatoire.")}
{accordion("cam", "Découvrez les exigences du jeu face caméra et adaptez votre interprétation à l'image.",
    [("Au programme", ["Respecter des déplacements et des marquages au sol précis", "Adapter son jeu à la valeur du cadre, du gros plan au plan d'ensemble", "Tourner des scènes dans le désordre, comme sur un vrai plateau", "Respecter des placements par rapport à la lumière"])],
    ["Adapter « l'aléatoire » de vos émotions à des limites techniques très précises", "Une introduction au cours « Acting Caméra & Tournages »"])}
      </div>
    </div>
  </section>

  <!-- ============ STAGES INTENSIFS ============ -->
  <section id="intensifs" data-screen-label="Stages intensifs" style="background: #FFFFFF; border-top: 1px solid #EEE9DF">
    <div style="max-width: 1200px; margin: 0 auto; padding: 90px 24px 90px; display: flex; flex-direction: column; gap: 32px">
      <div data-reveal style="display: flex; flex-direction: column; gap: 18px; max-width: 70ch">
        <div style="display: flex; align-items: center; gap: 12px">
          <span style="width: 40px; height: 2px; background: #E0261F; display: inline-block"></span>
          <span style="font-family: 'Oswald', sans-serif; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; color: #6B655C">Stages intensifs</span>
        </div>
        <h2 style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: clamp(36px, 4.6vw, 68px); text-transform: uppercase; line-height: 1.0; margin: 0">Plus de temps pour explorer.<br><span style="color: #E0261F">Plus de liberté pour jouer.</span></h2>
        <p style="margin: 0; font-size: 18px; line-height: 1.75; color: #3B362F">Profitez des vacances pour vous immerger dans la pratique du jeu d'acteur. Pendant plusieurs jours, approfondissez votre technique, explorez de nouvelles facettes de votre jeu et progressez à votre rythme, accompagnés par les coaches du Method Acting Center.</p>
      </div>
      <div data-reveal style="display: flex; flex-direction: column; gap: 16px">
{accordion("hiv", "Le stage de la rentrée décalée de janvier 2027 : deux jours pour condenser les techniques des stages Actors Studio A et B.",
    [("Au programme", ["Exploration émotionnelle : creuser en soi pour trouver ce qui vous touche, puis alimenter ce travail avec d'autres outils", "Backstory : création des binômes, élaboration des répétitions, passage des scènes préparées, retours du coach et reprises", "Atelier « Mini-Scènes » : des scènes de 4 répliques qui ne veulent rien dire hors contexte — la démonstration la plus directe du sous-texte"])],
    [], "L'ordre et le dosage des ateliers varient selon le planning.")}
{accordion("pri", "Trois jours pendant les vacances de printemps pour approfondir votre technique et explorer de nouvelles facettes de votre jeu.",
    [("Au programme", ["Exploration émotionnelle : creuser en soi pour trouver ce qui vous touche, puis alimenter ce travail avec d'autres outils", "Backstory : création des binômes, élaboration des répétitions, passage des scènes préparées, retours du coach et reprises", "Atelier « Mini-Scènes » : des scènes de 4 répliques qui ne veulent rien dire hors contexte — la démonstration la plus directe du sous-texte"])],
    [], "L'ordre et le dosage des ateliers varient selon le planning.")}
      </div>
    </div>
  </section>

  <!-- ============ POURQUOI LE METHOD ACTING CENTER ============ -->
  <section id="pourquoi" data-screen-label="Pourquoi" style="background: #F7F4EE">
    <div style="max-width: 1200px; margin: 0 auto; padding: 100px 24px 100px; display: flex; flex-direction: column; gap: 40px">
      <div data-reveal style="display: flex; flex-direction: column; gap: 18px; max-width: 70ch">
        <div style="display: flex; align-items: center; gap: 12px">
          <span style="width: 40px; height: 2px; background: #E0261F; display: inline-block"></span>
          <span style="font-family: 'Oswald', sans-serif; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; color: #6B655C">Pourquoi le Method Acting Center&nbsp;?</span>
        </div>
        <h2 style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: clamp(36px, 4.6vw, 68px); text-transform: uppercase; line-height: 1.0; margin: 0">Une Méthode exigeante.<br><span style="color: #E0261F">Un cadre pour oser.</span></h2>
        <p style="margin: 0; font-size: 18px; line-height: 1.75; color: #3B362F">Au Method Acting Center, apprendre à jouer, c'est aussi apprendre à explorer, à expérimenter et à prendre des risques. Nos coaches vous accompagnent dans un environnement à la fois bienveillant et exigeant, où chacun peut progresser à son rythme.</p>
      </div>
      <div class="why-grid">
        <div class="why-card" data-reveal><span class="why-num">01</span><div><h3>Une Méthode concrète, éprouvée depuis plus de 25 ans</h3><p>Inspirée de Stanislavski et de l'Actors Studio, la Méthode vous apprend à ressentir et à jouer vrai grâce à des outils précis, enrichis au fil des années pour répondre aux exigences du métier d'acteur d'aujourd'hui.</p></div></div>
        <div class="why-card" data-reveal><span class="why-num">02</span><div><h3>Des coaches en activité</h3><p>Acteurs et professionnels toujours présents sur les plateaux, aux castings et sur les tournages, ils transmettent un savoir-faire ancré dans les réalités du métier.</p></div></div>
        <div class="why-card" data-reveal><span class="why-num">03</span><div><h3>Un cadre bienveillant et exigeant</h3><p>Un environnement où vous pouvez expérimenter, vous tromper et recommencer, avec des retours constructifs pour progresser et développer votre singularité.</p></div></div>
        <div class="why-card" data-reveal><span class="why-num">04</span><div><h3>Une véritable communauté de création</h3><p>Acteurs, scénaristes et réalisateurs se rencontrent, échangent et collaborent autour de projets communs. Une dynamique qui se prolonge au-delà des cours.</p></div></div>
      </div>
    </div>
  </section>

'''

def pick(k):
    d = SESSIONS[k]
    return (f'            <!-- session {k} — masquée automatiquement après le {d["end"]} -->\n'
            f'            <label class="stage-pick" data-end="{d["end"]}"><input type="checkbox" name="stage" value="{esc_attr(value(k))}" data-date="{d["date"]}" data-price="{d["price"]}">'
            f'<span><strong>{d["name"]}</strong><small>{d["kind"]} &middot; {d["date"]} &middot; {d["price"]}</small></span></label>\n')

input_css = "font-family: 'Archivo', sans-serif; font-size: 16px; background: #F7F4EE; border: 1px solid #EEE9DF; border-radius: 12px; color: #14120F; padding: 14px 16px; outline: none; box-sizing: border-box; width: 100%"
lab = "display: flex; flex-direction: column; gap: 8px; font-family: 'Oswald', sans-serif; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; color: #6B655C"
source_select = re.search(r'<select name="source"[^>]*>.*?</select>', s, re.S)
source_select = source_select.group(0) if source_select else ''
if not source_select:
    source_select = re.search(r'<select name="source"[^>]*>.*?</select>', open(SRC, encoding="utf-8").read(), re.S).group(0)

FORM = f'''  <!-- ============ RÉSERVATION ============ -->
  <section id="reservation" data-screen-label="Reservation" style="background: #F7F4EE; color: #14120F; border-radius: 40px 40px 0 0; border-top: 1px solid #EEE9DF">
    <div style="max-width: 1200px; margin: 0 auto; padding: 100px 24px 100px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 56px; align-items: start">
      <div data-reveal style="display: flex; flex-direction: column; gap: 24px">
        <div style="display: flex; align-items: center; gap: 12px">
          <span style="width: 40px; height: 2px; background: #E0261F; display: inline-block"></span>
          <span style="font-family: 'Oswald', sans-serif; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; color: #6B655C">À vous de jouer</span>
        </div>
        <h2 style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: clamp(42px, 5.5vw, 72px); text-transform: uppercase; line-height: 0.98; margin: 0">Réservez votre <span style="color: #E0261F">stage.</span></h2>
        <p style="font-size: 18px; line-height: 1.7; color: #6B655C; margin: 0; max-width: 48ch">Choisissez le stage qui vous correspond et envoyez votre demande de réservation. L'équipe du Method Acting Center vous confirmera votre place et les modalités pratiques par email.</p>
        <ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 14px; font-size: 16px; color: #14120F">
          <li style="display: flex; gap: 12px; align-items: baseline"><span style="color: #E0261F; font-weight: 700">&#10003;</span><span>Stages accessibles aux débutants comme aux profils expérimentés, selon le programme.</span></li>
          <li style="display: flex; gap: 12px; align-items: baseline"><span style="color: #E0261F; font-weight: 700">&#10003;</span><span>Des coaches en activité pour vous accompagner.</span></li>
          <li style="display: flex; gap: 12px; align-items: baseline"><span style="color: #E0261F; font-weight: 700">&#10003;</span><span>Des exercices pratiques pour progresser à votre rythme.</span></li>
        </ul>
        <div style="font-size: 15px; line-height: 1.7; color: #6B655C">Une question avant de réserver&nbsp;? <a href="tel:+33607414125" style="color: #14120F; text-decoration: none; font-weight: 600">+33 6 07 41 41 25</a> &middot; <a href="mailto:contact@methodacting.fr" style="color: #14120F; text-decoration: none; font-weight: 600">contact@methodacting.fr</a> &middot; <a href="https://wa.me/qr/TPPR3BYKF55FD1" target="_blank" rel="noopener" style="color: #14120F; text-decoration: none; font-weight: 600">WhatsApp</a></div>
        <div style="width: 100%; aspect-ratio: 16 / 9; border-radius: 20px; overflow: hidden; margin-top: 12px"><img data-img="contact_scene" alt="Deux acteurs en travail de scène, noir et blanc" style="width: 100%; height: 100%; object-fit: cover; display: block"></div>
      </div>
      <div data-reveal>
        <form id="stages-form" novalidate style="background: #FFFFFF; border: 1px solid #EEE9DF; border-radius: 28px; padding: clamp(28px, 4vw, 48px); display: flex; flex-direction: column; gap: 22px">
          <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true" style="position: absolute; left: -9999px; width: 0; height: 0; opacity: 0">
          <div style="display: flex; flex-direction: column; gap: 12px">
            <span style="font-family: 'Oswald', sans-serif; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; color: #6B655C">Les stages qui m'intéressent <span style="text-transform: none; letter-spacing: 0; color: #6B655C">(un ou plusieurs)</span></span>
            <div id="stage-list" style="display: flex; flex-direction: column; gap: 10px">
{pick("a")}{pick("sc")}{pick("b")}{pick("cam")}{pick("hiv")}{pick("pri")}            </div>
            <div id="stages-recap" class="book-recap">Aucun stage sélectionné pour l'instant.</div>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 22px">
            <label style="{lab}">Prénom<input name="prenom" type="text" required placeholder="Votre prénom" style="{input_css}"></label>
            <label style="{lab}">Nom<input name="nom" type="text" required placeholder="Votre nom" style="{input_css}"></label>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 22px">
            <label style="{lab}">Email<input name="email" type="email" autocomplete="email" placeholder="vous@exemple.fr" style="{input_css}"></label>
            <label style="{lab}">Téléphone<input name="telephone" type="tel" autocomplete="tel" placeholder="06 12 34 56 78" style="{input_css}"></label>
          </div>
          <label style="{lab}">Message <span style="text-transform: none; letter-spacing: 0; color: #6B655C">(facultatif)</span><textarea name="message" rows="3" placeholder="Votre expérience, une question…" style="{input_css}; resize: vertical"></textarea></label>
          <label style="{lab}">Comment avez-vous connu Method Acting Center&nbsp;?
            {source_select}
          </label>
          <button type="submit" style="font-family: 'Oswald', sans-serif; font-size: 17px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; background: #E0261F; color: #FFFFFF; border: none; cursor: pointer; padding: 19px 0; border-radius: 999px; transition: background .15s ease, transform .15s ease" style-hover="background: #14120F; transform: translateY(-2px)">Réserver mon stage</button>
          <p style="margin: 0; font-size: 13px; color: #6B655C; line-height: 1.5">En envoyant ce formulaire, vous acceptez d’être recontacté(e) par Method Acting Center. Vos données ne seront jamais partagées.</p>
        </form>
        <div id="stages-success" style="display:none">
          <div style="background: #FFFFFF; border: 1px solid #E0261F; border-radius: 28px; padding: 64px 48px; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center">
            <span style="font-family: 'Oswald', sans-serif; font-size: 56px; color: #E0261F; line-height: 1">&#10003;</span>
            <h3 style="font-family: 'Oswald', sans-serif; font-size: 28px; text-transform: uppercase; margin: 0">Demande envoyée&nbsp;!</h3>
            <p id="stages-success-recap" style="margin: 0; font-size: 16px; color: #6B655C; max-width: 42ch; line-height: 1.6">Merci&nbsp;! L'équipe du Method Acting Center vous confirme votre place et les modalités pratiques par email.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ COURS D'ESSAI GRATUIT ============ -->
  <section id="essai" data-screen-label="Cours d'essai" style="background: #0B0A0A; color: #F4F1EC">
    <div style="max-width: 1000px; margin: 0 auto; padding: 100px 24px 120px; display: flex; flex-direction: column; align-items: center; gap: 26px; width: 100%; text-align: center">
      <div data-reveal style="display: flex; align-items: center; gap: 12px">
        <span style="width: 40px; height: 2px; background: #E0261F; display: inline-block"></span>
        <span style="font-family: 'Oswald', sans-serif; font-size: 14px; letter-spacing: 3px; text-transform: uppercase; color: #B7B0A6">Une autre façon de commencer</span>
      </div>
      <h2 data-reveal style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: clamp(38px, 5.2vw, 76px); text-transform: uppercase; line-height: 1.0; margin: 0">Pas encore prêt<br>à réserver <span style="color: transparent; -webkit-text-stroke: 1.5px #E0261F">un stage&nbsp;?</span></h2>
      <p data-reveal style="margin: 0; font-size: 19px; line-height: 1.7; color: #B7B0A6; max-width: 56ch">Commencez par un cours d'essai gratuit. Intégrez un atelier aux côtés des élèves du Method Acting Center, découvrez la Méthode en conditions réelles et faites-vous votre propre idée, sans engagement.</p>
      <div data-reveal style="display: flex; gap: 14px 28px; flex-wrap: wrap; justify-content: center; font-family: 'Oswald', sans-serif; font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase; color: #F4F1EC">
        <span>&#10003; Gratuit</span><span>&#10003; Sans engagement</span><span>&#10003; 2 cours d'essai offerts</span>
      </div>
      <a data-reveal href="{SITE}cours-essai.html#reservation" style="font-family: 'Oswald', sans-serif; font-size: 17px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; background: #E0261F; color: #FFFFFF; text-decoration: none; padding: 21px 44px; border-radius: 999px; display: inline-block; margin-top: 8px; transition: transform .15s ease, background .15s ease" style-hover="background: #F4F1EC; color: #0B0A0A; transform: translateY(-2px)">Réserver mon cours d'essai</a>
    </div>
  </section>

'''

# Assemblage : … Méthode | SECTIONS | avis | films | FORM | footer
footer_marker = "  <!-- ============ FOOTER (identique au site) ============ -->"
s = s.replace(footer_marker, SECTIONS + avis + films + FORM + footer_marker, 1)

# ---------- 7. CSS ----------
CSS = '''
  /* ===== Landing stages ===== */
  #mac-landing .hero-next { max-width: 34ch; }
  #mac-landing .stage-list { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:9px; }
  #mac-landing .stage-list li { position:relative; padding-left:24px; font-size:15.5px; line-height:1.55; color:#3B362F; }
  #mac-landing .stage-list li::before { content:"\\2713"; position:absolute; left:0; top:0; color:#E0261F; font-weight:700; }
  /* stage à la une */
  #mac-landing .feat { display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); background:#FFFFFF; border:1px solid rgba(224,38,31,0.45); border-radius:28px; overflow:hidden; box-shadow:0 30px 60px rgba(224,38,31,0.10); }
  #mac-landing .feat-media { position:relative; min-height:360px; background:#14120F; }
  #mac-landing .feat-media img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block; }
  #mac-landing .feat-date { position:absolute; top:22px; left:22px; background:#E0261F; color:#FFFFFF; font-family:'Oswald',sans-serif; font-size:13px; letter-spacing:1.5px; text-transform:uppercase; font-weight:600; padding:10px 16px; border-radius:999px; box-shadow:0 10px 24px rgba(20,18,15,0.18); }
  #mac-landing .feat-body { padding:clamp(28px,4vw,52px); display:flex; flex-direction:column; gap:20px; }
  #mac-landing .feat-tag { align-self:flex-start; font-family:'Oswald',sans-serif; font-size:11px; letter-spacing:1.5px; text-transform:uppercase; font-weight:600; color:#E0261F; background:rgba(224,38,31,0.08); padding:7px 12px; border-radius:999px; }
  #mac-landing .feat-body h3 { font-family:'Oswald',sans-serif; font-weight:700; font-size:clamp(26px,2.8vw,38px); text-transform:uppercase; line-height:1.04; margin:0; }
  #mac-landing .feat-desc { margin:0; font-size:17px; line-height:1.7; color:#3B362F; }
  #mac-landing .feat-meta { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr)); gap:14px 24px; padding:18px 0; border-top:1px solid #EEE9DF; border-bottom:1px solid #EEE9DF; }
  #mac-landing .feat-meta div { display:flex; flex-direction:column; gap:4px; }
  #mac-landing .feat-meta span { font-family:'Oswald',sans-serif; font-size:11px; letter-spacing:1.5px; text-transform:uppercase; color:#6B655C; }
  #mac-landing .feat-meta strong { font-size:15px; color:#14120F; font-weight:600; line-height:1.3; }
  #mac-landing .feat-meta .feat-price { font-family:'Oswald',sans-serif; font-size:24px; color:#E0261F; font-weight:700; }
  #mac-landing .feat-cta { align-self:flex-start; font-family:'Oswald',sans-serif; font-size:16px; letter-spacing:2px; text-transform:uppercase; font-weight:600; background:#E0261F; color:#FFFFFF; text-decoration:none; padding:18px 34px; border-radius:999px; transition:background .15s ease, transform .15s ease; }
  #mac-landing .feat-cta:hover { background:#14120F; color:#FFFFFF; transform:translateY(-2px); }
  /* accordéons stages */
  #mac-landing .stage-head { align-items:flex-start; padding:28px 32px; }
  #mac-landing .stage-head-main { flex:1; display:flex; flex-direction:column; gap:8px; min-width:0; }
  #mac-landing .stage-kind { font-family:'Oswald',sans-serif; font-size:11px; letter-spacing:1.5px; text-transform:uppercase; font-weight:600; color:#E0261F; }
  #mac-landing .stage-title { font-family:'Oswald',sans-serif; font-size:clamp(20px,2.2vw,27px); text-transform:uppercase; font-weight:600; color:#14120F; margin:0; line-height:1.12; }
  #mac-landing .stage-meta { display:flex; flex-wrap:wrap; gap:6px 18px; font-family:'Oswald',sans-serif; font-size:13px; letter-spacing:1.2px; text-transform:uppercase; color:#6B655C; }
  #mac-landing .stage-price { color:#E0261F; font-weight:700; }
  #mac-landing .stage-short { margin:2px 0 0; font-size:15.5px; line-height:1.6; color:#6B655C; max-width:70ch; }
  #mac-landing .stage-card.open .jpo-panel { max-height:2200px; }
  #mac-landing .stage-photo { aspect-ratio:16/8; border-radius:16px; overflow:hidden; background:#14120F; }
  #mac-landing .stage-photo img { width:100%; height:100%; object-fit:cover; display:block; }
  #mac-landing .stage-note { margin:0; font-size:14px; line-height:1.5; color:#6B655C; font-style:italic; }
  #mac-landing .stage-card .jpo-panel-inner { padding:0 32px 34px; gap:22px; }
  #mac-landing .stage-card .jpo-field p { max-width:70ch; }
  #mac-landing [data-end].is-expired { display:none !important; }
  /* pourquoi */
  #mac-landing .why-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:20px; }
  #mac-landing .why-card { background:#FFFFFF; border:1px solid #EEE9DF; border-radius:20px; padding:30px 32px; display:grid; grid-template-columns:clamp(48px,4.5vw,64px) 1fr; gap:20px; align-items:start; transition:transform .2s ease, box-shadow .2s ease, border-color .2s ease; }
  #mac-landing .why-card:hover { transform:translateY(-4px); box-shadow:0 20px 40px rgba(20,18,15,0.08); border-color:rgba(224,38,31,0.3); }
  #mac-landing .why-num { font-family:'Oswald',sans-serif; font-size:clamp(34px,3.4vw,48px); font-weight:700; color:transparent; -webkit-text-stroke:1.5px #E0261F; line-height:1; }
  #mac-landing .why-card h3 { font-family:'Oswald',sans-serif; font-size:21px; text-transform:uppercase; margin:0 0 8px; line-height:1.15; }
  #mac-landing .why-card p { margin:0; font-size:15.5px; line-height:1.65; color:#6B655C; }
  /* formulaire : cases à cocher stages */
  #mac-landing .stage-pick { display:flex; align-items:flex-start; gap:12px; cursor:pointer; background:#F7F4EE; border:1px solid #EEE9DF; border-left:3px solid #E0261F; border-radius:12px; padding:12px 14px; transition:background .15s ease, box-shadow .15s ease; }
  #mac-landing .stage-pick:hover { background:#FFFFFF; }
  #mac-landing .stage-pick input { margin:3px 0 0; width:18px; height:18px; accent-color:#E0261F; flex:0 0 auto; }
  #mac-landing .stage-pick > span { display:flex; flex-direction:column; gap:2px; min-width:0; }
  #mac-landing .stage-pick strong { font-family:'Oswald',sans-serif; font-size:15px; letter-spacing:.3px; color:#14120F; font-weight:600; line-height:1.25; }
  #mac-landing .stage-pick small { font-size:12.5px; color:#6B655C; line-height:1.4; }
  #mac-landing .stage-pick:has(input:checked) { background:#FFFFFF; box-shadow:0 0 0 2px #E0261F; }
  #mac-landing .stage-pick.is-prefilled { box-shadow:0 0 0 3px rgba(224,38,31,0.35); }
  @media (max-width:860px){ #mac-landing .feat { grid-template-columns:1fr; } #mac-landing .feat-media { min-height:0; aspect-ratio:16/9; } }
  @media (max-width:640px){ #mac-landing .stage-head { padding:22px 20px; } #mac-landing .stage-card .jpo-panel-inner { padding:0 20px 26px; } #mac-landing .hero-next { max-width:none; } }
'''
s = s.replace("\n</style>", CSS + "</style>", 1)

# ---------- 8. JS : avis, données JPO retirées, formulaire stages ----------
reviews = [
 {"quote": "Après deux premiers stages (exploration et scenes) chez Method Acting Center en 2023, je me suis de nouveau inscrit cette année pour le stage d’hiver. Encore une fois cette année j’ai été très satisfait des cours dispensés. Les profs sont vraiment investis et passionés, les ateliers sont instructifs et organisés autour d’une méthode précise qui me semble maintenant indispensable pour mon jeu. Je sens que j’ai progressé pendant ces 4 jours et je compte me réinscrire dès que possible à un stage / classe d’été / etc. Encore merci à l’équipe pédagogique et merci aux autres comédiens qui étaient là pendant ce stage. Note : Si vous pouviez monter une antenne à Barcelone ou y organiser des stages comme celui-ci ce serait top :) Bonne continuation !", "name": "Antoine Ppr", "date": "2024", "link": "https://share.google/Yygbq9L4y0KN0ncDx"},
 {"quote": "Ecole de formation qui prend tous les participants de là où ils en sont pour les faire progresser dans la bienveillance. L'écoute est mutuelle et la qualité des stages donne envie de poursuivre. J'ai pu faire plusieurs stages week-end avec plaisir. L'école semble en pleine évolution en proposant des nouveautés, à suivre !", "name": "Anne-Sophie Cotroneo", "date": "2018", "link": "https://share.google/2PnWeEdpYnzOIe3rJ"},
 {"quote": "J'ai participé à plusieurs stages pour découvrir la \"méthode\" et cela m'a beaucoup apporté. Je recommande ces stages de weekend à tous ceux, tous niveaux confondus, qui auraient envie de dépasser leurs limites et faire une nouvelle expérience ! Très bonne ambiance instaurée par des coachs vraiment bienveillants et exigeants. Et une équipe administrative à l'écoute et réactive. Je m'y suis tellement bien sentie, qu'après avoir participé ponctuellement aux stages, j'ai suivi des cours à l'année.", "name": "Celine Larmoyer", "date": "2020", "link": "https://share.google/rQzMyyBFP2Y4O1Voz"},
]
js_rev = "  var REVIEWS = [\n" + ",\n".join("    " + json.dumps(r, ensure_ascii=False) for r in reviews) + "\n  ];"
s, n = re.subn(r"  var REVIEWS = \[\n.*?\n  \];", lambda m: js_rev, s, count=1, flags=re.S); assert n == 1
s, n = re.subn(r"  var JPO_DAYS = .*?\n  var ATELIERS = \[\n.*?\n  \];\n", "", s, count=1, flags=re.S); assert n == 1
s, n = re.subn(r"  var PROGRAM = \[\n.*?\n  \];\n", "", s, count=1, flags=re.S); assert n == 1
s = sub1(s, "initProgram(); initJpo(); initReviews(); initBooking(); initAnchors(); initMobileCta(); }",
            "initExpired(); initJpo(); initReviews(); initStagesForm(); initAnchors(); }", "init line")

JS = r'''
  /* ============================================================
     SESSIONS EXPIRÉES — tout élément [data-end="AAAA-MM-JJ"] (stage à la une,
     carte dépliable, case du formulaire) est masqué automatiquement une fois
     la date passée. Supprimez le bloc HTML pour le retirer définitivement.
     ============================================================ */
  function initExpired(){
    var today=new Date(); today.setHours(0,0,0,0);
    ROOT.querySelectorAll("[data-end]").forEach(function(el){
      var d=new Date(el.getAttribute("data-end")+"T23:59:59");
      if(d<today) el.classList.add("is-expired");
    });
  }

  /* ============================================================
     FORMULAIRE STAGES — sélection multiple, récapitulatif, pré-cochage
     depuis les boutons « Je m'inscris au stage », envoi Web3Forms,
     conversion Google Ads (dataLayer / gtag).
     ============================================================ */
  function initStagesForm(){
    var form=document.getElementById("stages-form"), ok=document.getElementById("stages-success"),
        recap=document.getElementById("stages-recap"), successRecap=document.getElementById("stages-success-recap");
    if(!form) return;
    var boxes=[].slice.call(form.querySelectorAll('input[name="stage"]'));
    function available(){ return boxes.filter(function(b){ var row=b.closest("[data-end]"); return !(row&&row.classList.contains("is-expired")); }); }
    function chosen(){ return available().filter(function(b){return b.checked;}).map(function(b){ return {name:b.value.replace(/\s*\([^)]*\)\s*$/,""), date:b.getAttribute("data-date")||"", price:b.getAttribute("data-price")||""}; }); }
    function updateRecap(){
      var ch=chosen();
      if(!ch.length){ recap.className="book-recap"; recap.textContent="Aucun stage sélectionné pour l’instant."; return; }
      recap.className="book-recap active";
      recap.innerHTML=ch.length+" stage"+(ch.length>1?"s":"")+" : "+ch.map(function(c){ return "<strong>"+esc(c.name)+"</strong> ("+esc(c.date)+(c.price?" · "+esc(c.price):"")+")"; }).join(" · ");
    }
    boxes.forEach(function(b){ b.addEventListener("change",updateRecap); });
    updateRecap();

    /* pré-cochage : boutons [data-stage] (sans décocher les autres) + ?stage=a,sc,b,cam,hiv,pri à l'arrivée */
    var tmp=document.createElement("textarea");
    function norm(t){ tmp.innerHTML=t; return tmp.value.replace(/\s+/g," ").trim(); }
    function tick(box, ms){
      if(!box) return;
      box.checked=true; updateRecap();
      var row=box.closest(".stage-pick"); if(row){ row.classList.add("is-prefilled"); setTimeout(function(){ row.classList.remove("is-prefilled"); }, ms||2500); }
    }
    ROOT.querySelectorAll("[data-stage]").forEach(function(btn){
      btn.addEventListener("click",function(){
        var want=norm(btn.getAttribute("data-stage"));
        tick(boxes.filter(function(b){ return norm(b.value)===want; })[0]);
      });
    });
    try{
      var q=new URLSearchParams(location.search).get("stage");
      if(q){ q.toLowerCase().split(",").forEach(function(key){ var row=document.getElementById("stage-"+key.trim()); var kw=row?row.querySelector(".stage-title").textContent:""; if(kw) tick(boxes.filter(function(b){ return norm(b.value).indexOf(norm(kw))===0; })[0],4000); }); }
    }catch(e){}


    /* ---- champs obligatoires communs : prénom + nom, et email ou téléphone ---- */
    function checkIdentity(form){
      function el(n){ return form.querySelector('[name="'+n+'"]'); }
      function val(n){ var e=el(n); return e?String(e.value||"").trim():""; }
      var bad=[], msgs=[];
      var miss=[];
      if(!val("prenom")){ bad.push(el("prenom")); miss.push("votre prénom"); }
      if(!val("nom")){ bad.push(el("nom")); miss.push("votre nom"); }
      if(miss.length) msgs.push(miss.join(" et "));
      var email=val("email"), tel=val("telephone");
      if(!email && !tel){ bad.push(el("email"), el("telephone")); msgs.push("un email ou un numéro de téléphone"); }
      else {
        if(email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)){ bad.push(el("email")); msgs.push("un email valide"); }
        if(tel && tel.replace(/\D/g,"").length<9){ bad.push(el("telephone")); msgs.push("un numéro de téléphone valide"); }
      }
      var warn=form.querySelector(".field-warn");
      if(!warn){
        warn=document.createElement("div"); warn.className="field-warn"; warn.style.cssText="font-size:14px;line-height:1.5;color:#14120F;padding:12px 14px;border:1px solid #E0261F;border-radius:12px;background:rgba(224,38,31,.10)"; warn.setAttribute("role","alert");
        var telEl=el("telephone"), row=telEl&&(telEl.closest(".field-2")||telEl.parentNode.parentNode);
        if(row&&row.parentNode) row.parentNode.insertBefore(warn,row.nextSibling); else form.insertBefore(warn,form.firstChild);
      }
      [].slice.call(form.querySelectorAll(".is-invalid")).forEach(function(i){ i.classList.remove("is-invalid"); i.removeAttribute("aria-invalid"); i.style.borderColor="#EEE9DF"; });
      if(!bad.length){ warn.style.display="none"; return true; }
      bad.forEach(function(i){ if(!i) return; i.classList.add("is-invalid"); i.setAttribute("aria-invalid","true"); i.style.borderColor="#E0261F";
        i.addEventListener("input",function h(){ i.classList.remove("is-invalid"); i.removeAttribute("aria-invalid"); i.style.borderColor="#EEE9DF"; i.removeEventListener("input",h); }); });
      warn.textContent="Pour vous recontacter, merci d’indiquer "+msgs.join(", ")+".";
      warn.style.display="";
      warn.scrollIntoView({behavior:"smooth",block:"center"});
      var first=bad.filter(Boolean)[0]; if(first) try{ first.focus({preventScroll:true}); }catch(e){ first.focus(); }
      return false;
    }
    function field(n){ var el=form.querySelector('[name="'+n+'"]'); return el?String(el.value||"").trim():""; }
    function campaign(){
      try{
        var p=new URLSearchParams(location.search), keys=["gclid","gbraid","wbraid","utm_source","utm_medium","utm_campaign","utm_term","utm_content"], out=[];
        keys.forEach(function(k){ if(p.get(k)) out.push(k+"="+p.get(k)); });
        return out.length?out.join(" | "):"";
      }catch(e){ return ""; }
    }
    function track(ch){
      try{
        window.dataLayer=window.dataLayer||[];
        window.dataLayer.push({event:"stage_form_success", stages:ch.map(function(c){return c.name;}), stage_count:ch.length});
        if(typeof window.gtag==="function"){ window.gtag("event","generate_lead",{event_category:"stages",event_label:ch.map(function(c){return c.name;}).join(" | "),value:ch.length}); }
      }catch(e){}
    }
    function showSuccess(ch){
      if(successRecap){ successRecap.innerHTML="Merci&nbsp;! Nous avons bien reçu votre demande pour "+ch.length+" stage"+(ch.length>1?"s":"")+" : "+ch.map(function(c){return "<strong>"+esc(c.name)+"</strong>";}).join(", ")+". L’équipe du Method Acting Center vous confirme votre place et les modalités pratiques par email."; }
      form.style.display="none"; ok.style.display=""; ok.scrollIntoView({behavior:"smooth",block:"center"});
      track(ch);
    }
    form.addEventListener("submit",function(e){
      e.preventDefault();
      var ch=chosen();
      if(!ch.length){ recap.className="book-recap warn"; recap.textContent="Cochez au moins un stage avant d’envoyer."; recap.scrollIntoView({behavior:"smooth",block:"center"}); return; }
      if(!checkIdentity(form)) return;
      var btn=form.querySelector('button[type="submit"]'), btnLabel=btn?btn.innerHTML:"";
      var name=(field("prenom")+" "+field("nom")).trim()||"sans nom";
      var payload={
        access_key: WEB3FORMS_KEY,
        subject: "Réservation stage — "+name,
        from_name: "Stages · Method Acting Center (landing)",
        "Prénom": field("prenom"), "Nom": field("nom"), "Email": field("email"), "Téléphone": field("telephone")||"—",
        "Stages": ch.map(function(c){ return "• "+c.name+" — "+c.date+(c.price?" — "+c.price:""); }).join("\n"),
        "Message": field("message")||"—",
        "Comment nous a connus": field("source")||"—",
        "Campagne": campaign()||"—",
        "Page": location.href,
        botcheck: (function(){ var b=form.querySelector('[name="botcheck"]'); return b?b.checked:false; })()
      };
      if(!WEB3FORMS_KEY){ if(window.console)console.warn("Web3Forms: clé manquante, aucun email envoyé."); showSuccess(ch); return; }
      if(btn){ btn.disabled=true; btn.innerHTML="Envoi en cours…"; }
      fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(payload)})
        .then(function(r){return r.json();}).then(function(d){ if(d&&d.success){ showSuccess(ch); } else { throw new Error((d&&d.message)||"echec"); } })
        .catch(function(){ if(btn){ btn.disabled=false; btn.innerHTML=btnLabel; } recap.className="book-recap warn"; recap.textContent="L’envoi a échoué. Vérifiez votre connexion et réessayez dans un instant."; recap.scrollIntoView({behavior:"smooth",block:"center"}); });
    });
  }

  /* in-page anchor smooth scroll */'''
s = sub1(s, "\n  /* in-page anchor smooth scroll */", JS, "js insert")

# Fonctions JPO devenues inutiles (programme 4 ans, formulaire ateliers, CTA mobile)
for fn in ("initProgram","initBooking","initMobileCta"):
    s, n = re.subn(r"  /\*[^\n]*\*/\n  function "+fn+r"\(\)\{.*?\n  \}\n", "", s, count=1, flags=re.S)
    assert n == 1, fn
assert "function initBooking" not in s and "function initProgram" not in s

# Footer : le lien Portes Ouvertes pointe vers la landing JPO (pas d'ancre locale)
s = sub1(s, '<a href="#jpo">Journ&eacute;es Portes Ouvertes</a>', '<a href="https://www.methodacting.fr/jpo.html">Journ&eacute;es Portes Ouvertes</a>', "footer jpo")

# Images : la source (static/jpo) est déjà en /uploads/ absolu ; blocs Méthode et visuels du hero
assert 'url: "/uploads/' in s and 'url: "uploads/' not in s and "data:image" not in s
s = sub1(s, 'var HERO_KEYS = ["hero_scene"];', 'var HERO_KEYS = ["hero_scene","hero_foret","hero_portrait"];', "hero keys")
s = sub1(s, "    methode_1: { url:", '    hero_foret: { url: "/uploads/tournage-exterieur-foret-acteurs-method-acting-center.jpg", label: "Tournage en extérieur · deux acteurs face caméra" },\n    hero_portrait: { url: "/uploads/portrait-acteur-costume-lumiere-bleue-method-acting-center.jpg", label: "Acteur en costume sous une lumière bleue" },\n    methode_1: { url:', "hero slides")

# Ancre [id] : marge sous le header fixe (bandeau retiré)
s = s.replace("  #mac-landing [id] { scroll-margin-top:130px; }", "  #mac-landing [id] { scroll-margin-top:96px; }", 1)

_os.makedirs(_os.path.dirname(DST), exist_ok=True)
open(DST, "w", encoding="utf-8").write(s)
assert "data:image" not in s and 'src="uploads/' not in s and 'url: "uploads/' not in s
print("landing écrite :", DST, len(s)//1024, "Ko")
# contrôles
for must in ["Vous voulez devenir", "Commencez par apprendre", "Ce n&rsquo;est pas<br>le talent", "Elle se vit.", "Stage à la une", "Plus de temps pour explorer", "Une Méthode exigeante", "Ils ont tenté", "Retrouvez nos élèves", "À vous de jouer", "Pas encore prêt", "jposr"]:
    assert must in s, must
for mustnot in ["Journ&eacute;es Portes Ouvertes</span></h2>", 'id="jpo"', 'id="formation"', 'id="faq"', "booking-form", "Cours d&rsquo;essai gratuit</a>\n      </nav>", "class=\"annce\""]:
    assert mustnot not in s, mustnot
print("contrôles ok")
