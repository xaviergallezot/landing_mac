#!/usr/bin/env python3
"""
Construit le dossier de déploiement `dist/` — copie conforme de ce qui doit être en ligne.

    dist/
      .htaccess                 ← static/.htaccess
      index.html, acting.html…  ← partials + pages (CSS et JS intégrés, images en /uploads/)
      tarifs/index.html         ← variante de tarifs.html avec liens absolus (dossier /tarifs/ sur le serveur)
      jpo/index.html            ← static/jpo/index.html   (landing Portes Ouvertes · acteurs)
      jposr/index.html          ← static/jposr/index.html (landing Portes Ouvertes · scénario / réalisation)
      stages/index.html         ← généré par tools/build_landing_stages.py à partir de static/jpo
      uploads/                  ← LE SEUL dossier d'images du site : assets/img/* + static/uploads/*

Règle : toute image du site, quelle que soit la page, est référencée en absolu `/uploads/<fichier>`.
"""
import os, re, shutil, subprocess, sys, json, datetime

SITE = "https://www.methodacting.fr"

HERE   = os.path.dirname(os.path.abspath(__file__))
DIST   = os.path.join(HERE, "dist")
IMGDIR = os.path.join(HERE, "assets", "img")
STATIC = os.path.join(HERE, "static")

def read(*parts): return open(os.path.join(HERE, *parts), encoding="utf-8").read()

HEAD   = read("partials", "head.html")
HEADER = read("partials", "header.html")
FOOTER = read("partials", "footer.html")
CSS    = read("assets", "style.css")
JS     = read("assets", "site.js")

def inline(page):
    # CSS et JS intégrés (une seule requête par page) ; images -> /uploads/ (dossier unique)
    page = re.sub(r'<link rel="stylesheet" href="[^"]*assets/style\.css">', lambda m: "<style>\n" + CSS + "\n</style>", page)
    page = re.sub(r'<script src="[^"]*assets/site\.js"></script>', lambda m: "<script>\n" + JS + "\n</script>", page)
    page = re.sub(r'src="[^"]*assets/img/([^"]+)"', lambda m: 'src="/uploads/' + m.group(1) + '"', page)
    return page

# slug, fichier de sortie, titre, description
PAGES = [
    ("index",       "index.html",       "Method Acting Center — Devenir Acteur, Scénariste ou Réalisateur à Paris",
     "École de cinéma à Paris depuis 1999 : formations Acteur, Scénariste et Réalisateur autour de la Méthode (Stanislavski / Actors Studio)."),
    ("jpo",         "jpo.html",         "Journées Portes Ouvertes — 12 & 13 décembre — Method Acting Center Paris",
     "Journées Portes Ouvertes gratuites les 12 & 13 décembre à Paris, pour la rentrée de janvier : ateliers immersifs d'acting, scénario et réalisation. Réservez vos ateliers en ligne."),
    ("acting",        "acting.html",        "Formation Acting — Devenir Acteur — Method Acting Center Paris",
     "Formation Acting : apprenez à jouer vrai avec la Méthode (Stanislavski / Actors Studio). Déclencher, maîtriser et reproduire de vraies émotions face caméra."),
    ("scenario-real", "scenario-real.html", "Scénario, Réalisation & Direction d'acteurs — Method Acting Center Paris",
     "Formation Scénario, Réalisation & Direction d'acteurs : écriture, réalisation et direction d'acteurs. Des outils concrets, un lien unique entre écriture, mise en scène et acting."),
    ("contact",     "contact.html",     "Contact — Method Acting Center Paris",
     "Une question sur nos formations Acteur, Scénariste ou Réalisateur ? Écrivez-nous, on vous répond sous 48h."),
    ("tarifs",      "tarifs.html",      "Tarifs — Method Acting Center Paris",
     "Tarifs des formations et ateliers du Method Acting Center. Facilités de paiement et offres à la rentrée."),
    ("planning",    "planning.html",    "Planning — Method Acting Center Paris",
     "Le calendrier des cours, ateliers et Journées Portes Ouvertes du Method Acting Center."),
    ("cours-essai", "cours-essai.html", "Cours d'essai gratuit — Method Acting Center Paris",
     "Testez gratuitement un vrai atelier d'acting, de scénario ou en anglais au Method Acting Center, Paris 13ᵉ : 2 cours d'essai offerts, sans engagement."),
    ("stages",      "stages.html",      "Stages d'acting & de scénario — week-end et intensifs — Method Acting Center Paris",
     "Stages week-end (Initiation à la Méthode, Approche d'une scène, Scénario & Réalisation, Acting Caméra) et stages intensifs pendant les vacances, à Paris."),
    ("inscription", "inscription.html", "Inscription — Method Acting Center Paris",
     "Demandez votre rendez-vous d'inscription : formations Acting (4 ans), Scénario · Réalisation & Direction d'acteurs (2 ans) et cours ponctuels. Rentrée de septembre ou rentrée décalée en janvier."),
]

# URL publique de chaque page : URLs propres, sauf jpo.html et stages.html (dossiers homonymes = landings)
def canonical(slug, out):
    if slug == "index": return SITE + "/"
    if slug in ("jpo", "stages"): return SITE + "/" + out
    return SITE + "/" + slug

OG_IMAGES = {
    "index": "scene-a-deux-acteurs-method-acting-center.jpg",
    "acting": "methode-declencher.jpg",
    "scenario-real": "tournage-equipe-terrasse-acteurs-method-acting-center.jpg",
    "stages": "scene-theatre-tension-acteurs-method-acting-center.jpg",
    "cours-essai": "cours-acting-groupe-method-acting-center.jpg",
    "jpo": "actrice-emotion-stage-initiation-method-acting-center.jpg",
    "inscription": "portrait-acteur-method-acting-center.jpg",
    "tarifs": "methode-maitriser.jpg",
    "planning": "methode-reproduire.jpg",
    "contact": "scene-a-deux-acteurs-method-acting-center.jpg",
}

ORG = {
    "@type": ["EducationalOrganization", "LocalBusiness"],
    "@id": SITE + "/#organization",
    "name": "Method Acting Center",
    "url": SITE + "/",
    "logo": SITE + "/uploads/scene-a-deux-acteurs-method-acting-center.jpg",
    "image": SITE + "/uploads/scene-a-deux-acteurs-method-acting-center.jpg",
    "description": "École d'art dramatique et de cinéma à Paris depuis 1999 : formations d'acteur, de scénariste et de réalisateur fondées sur la Méthode (Stanislavski / Actors Studio). Note Google 4,8/5 sur 98 avis.",
    "foundingDate": "1999",
    "telephone": "+33607414125",
    "email": "contact@methodacting.fr",
    "address": {"@type": "PostalAddress", "streetAddress": "93 avenue d'Italie", "postalCode": "75013", "addressLocality": "Paris", "addressCountry": "FR"},
    "areaServed": "Paris, France",
    "knowsAbout": ["Méthode Stanislavski", "Actors Studio", "formation d'acteur", "écriture de scénario", "réalisation", "direction d'acteurs"],
    "sameAs": ["https://fr.trustpilot.com/review/methodacting.fr"],
    "additionalType": "https://schema.org/School",
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "bestRating": "5", "reviewCount": "98"},
}

def event(name, start, end, url, desc, price=None, location_name="Method Acting Center"):
    ev = {"@type": "Event", "name": name, "startDate": start, "endDate": end, "url": url, "description": desc,
          "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled",
          "location": {"@type": "Place", "name": location_name, "address": ORG["address"]},
          "organizer": {"@id": ORG["@id"]}, "image": SITE + "/uploads/" + OG_IMAGES["stages"]}
    if price is None:
        ev["isAccessibleForFree"] = True
        ev["offers"] = {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": url}
    else:
        ev["offers"] = {"@type": "Offer", "price": str(price), "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": url}
    return ev

def course(name, desc, url, price_month, duration_text):
    return {"@type": "Course", "name": name, "description": desc, "url": url, "provider": {"@id": ORG["@id"]},
            "courseMode": "onsite", "inLanguage": "fr",
            "offers": {"@type": "Offer", "category": "Paid", "price": str(price_month), "priceCurrency": "EUR", "description": "Tarif mensuel de base, 9 mensualités par an"},
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "onsite", "courseSchedule": {"@type": "Schedule", "repeatFrequency": "Weekly", "scheduleTimezone": "Europe/Paris"}, "location": {"@type": "Place", "name": "Method Acting Center", "address": ORG["address"]}, "description": duration_text}}

def jsonld(slug, out, title, desc):
    url = canonical(slug, out)
    graph = [ORG,
             {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Method Acting Center", "publisher": {"@id": ORG["@id"]}, "inLanguage": "fr"},
             {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG["@id"]}, "inLanguage": "fr",
              "primaryImageOfPage": SITE + "/uploads/" + OG_IMAGES[slug]}]
    stages_url = SITE + "/stages.html"
    if slug == "acting":
        graph.append(course("Formation Acting — devenir acteur", "Programme complet d'acteur fondé sur la Méthode (Stanislavski / Actors Studio), jusqu'à 4 années, ateliers hebdomadaires matin ou soir.", url, 370, "2 ateliers de 4 h par semaine en 1re et 2e année"))
    if slug == "scenario-real":
        graph.append(course("Formation Scénario, Réalisation & Direction d'acteurs", "Programme sur 2 années : écriture, réalisation et direction d'acteurs, sessions le week-end, atelier d'acting hebdomadaire inclus.", url, 350, "26 samedis de 8 h en 1re année, 24 dimanches de 5 h en 2e année"))
    if slug in ("jpo", "index", "planning"):
        graph.append(event("Journées Portes Ouvertes — Method Acting Center", "2026-12-12", "2026-12-13", SITE + "/jpo.html", "Un week-end d'ateliers gratuits d'acting, de scénario et de réalisation pour vivre la Méthode en conditions réelles, avant la rentrée décalée de janvier 2027."))
    if slug in ("stages", "planning"):
        graph += [
            event("Stage A — Initiation à la Méthode", "2026-10-17", "2026-10-18", stages_url, "Deux jours pour découvrir les bases du travail émotionnel avec les outils de la Méthode Stanislavski.", 160),
            event("Stage Scénario, Réalisation & Direction d'acteurs", "2026-11-07", "2026-11-08", stages_url, "Introduction aux techniques d'écriture, de réalisation et de direction d'acteurs du Method Acting Center.", 160),
            event("Stage B — Approche d'une scène", "2026-11-14", "2026-11-15", stages_url, "Donner vie à un texte sans le réciter et infuser ses émotions dans une scène écrite.", 160),
            {"@type": "Event", "name": "Stage intensif d'hiver", "startDate": "2027-01-09", "endDate": "2027-01-10", "url": stages_url, "description": "Stage de la rentrée décalée : exploration émotionnelle, backstory et mini-scènes. Tarif sur demande.", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "location": {"@type": "Place", "name": "Method Acting Center", "address": ORG["address"]}, "organizer": {"@id": ORG["@id"]}, "image": SITE + "/uploads/" + OG_IMAGES["stages"]},
            {"@type": "Event", "name": "Stage Acting Caméra", "startDate": "2027-02-20", "endDate": "2027-02-21", "url": stages_url, "description": "Adapter son jeu aux contraintes techniques d'un tournage. Tarif sur demande.", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "location": {"@type": "Place", "name": "Method Acting Center", "address": ORG["address"]}, "organizer": {"@id": ORG["@id"]}, "image": SITE + "/uploads/" + OG_IMAGES["stages"]},
            {"@type": "Event", "name": "Stage intensif de printemps", "startDate": "2027-04-16", "endDate": "2027-04-18", "url": stages_url, "description": "Trois jours pour condenser les techniques des stages A et B. Tarif sur demande.", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "location": {"@type": "Place", "name": "Method Acting Center", "address": ORG["address"]}, "organizer": {"@id": ORG["@id"]}, "image": SITE + "/uploads/" + OG_IMAGES["stages"]},
        ]
    if slug == "cours-essai":
        graph.append({"@type": "Offer", "name": "Cours d'essai gratuit", "description": "2 cours d'essai offerts, toute l'année, dans les ateliers du Method Acting Center, sans engagement.", "price": "0", "priceCurrency": "EUR", "url": url, "offeredBy": {"@id": ORG["@id"]}, "availability": "https://schema.org/InStock"})
    if slug == "tarifs":
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": "Comment se passe le paiement ?", "acceptedAnswer": {"@type": "Answer", "text": "Aucun paiement en ligne. Après votre demande d'inscription, le bureau vous rappelle pour fixer un rendez-vous, puis tout se règle avec l'école : 9 mensualités par an sans surcoût, par trimestre ou en une fois."}},
            {"@type": "Question", "name": "Le tarif exact dépend-il de mon programme ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. Les tarifs « dès » correspondent au programme de base. Ateliers à l'unité, année avancée ou cumul Acting + Scénario : un devis précis est établi ensemble."}},
            {"@type": "Question", "name": "Puis-je entrer directement en 2e ou 3e année ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui, sur audition, selon votre expérience. Les tarifs sont dégressifs à partir de la 3e année d'Acting."}},
            {"@type": "Question", "name": "Et si je ne suis pas sûr(e) ?", "acceptedAnswer": {"@type": "Answer", "text": "Commencez par un cours d'essai gratuit ou un stage d'un week-end. Rien ne vous engage avant la demande d'inscription."}}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

def sitemap():
    today = datetime.date.today().isoformat()
    prio = {"index": "1.0", "acting": "0.9", "scenario-real": "0.9", "stages": "0.9", "cours-essai": "0.9", "jpo": "0.8", "inscription": "0.8", "tarifs": "0.8", "planning": "0.6", "contact": "0.5"}
    rows = "".join("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n" % (
        canonical(s, o), today, "weekly" if s in ("index", "stages", "planning", "jpo") else "monthly", prio[s]) for s, o, *_ in PAGES)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n"

def tarifs_folder_variant(html):
    """/tarifs/index.html : la page est servie depuis un dossier, les liens deviennent absolus."""
    html = html.replace('href="index.html"', 'href="/"')
    for slug, out, *_ in PAGES:
        if slug in ("index", "tarifs"): continue
        html = html.replace('href="' + out, 'href="/' + out)
    return html.replace('href="tarifs.html', 'href="/tarifs/')

def build():
    if os.path.isdir(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)

    # 1) pages du site
    for slug, out, title, desc in PAGES:
        page = (HEAD + HEADER + read("pages", slug + ".html") + FOOTER)
        page = (page.replace("{{ROOT}}", "").replace("{{TITLE}}", title).replace("{{DESC}}", desc)
                    .replace("{{CANON}}", canonical(slug, out)).replace("{{OGIMG}}", SITE + "/uploads/" + OG_IMAGES[slug])
                    .replace("{{JSONLD}}", jsonld(slug, out, title, desc)))
        page = inline(page)
        open(os.path.join(DIST, out), "w", encoding="utf-8").write(page)
        print("  %-20s %5d Ko" % (out, len(page) // 1024))

    # 2) variante /tarifs/
    os.makedirs(os.path.join(DIST, "tarifs"))
    open(os.path.join(DIST, "tarifs", "index.html"), "w", encoding="utf-8").write(
        tarifs_folder_variant(open(os.path.join(DIST, "tarifs.html"), encoding="utf-8").read()))

    # 2b) sitemap
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(sitemap())

    # 3) fichiers statiques (.htaccess, landings jpo / jposr, PDF, robots.txt, llms.txt)
    for root, dirs, files in os.walk(STATIC):
        rel = os.path.relpath(root, STATIC)
        dest = DIST if rel == "." else os.path.join(DIST, rel)
        os.makedirs(dest, exist_ok=True)
        for f in files: shutil.copy2(os.path.join(root, f), os.path.join(dest, f))

    # 4) le dossier d'images unique
    for f in sorted(os.listdir(IMGDIR)):
        shutil.copy2(os.path.join(IMGDIR, f), os.path.join(DIST, "uploads", f))

    # 5) landing stages (générée à partir de static/jpo/index.html)
    subprocess.run([sys.executable, os.path.join(HERE, "tools", "build_landing_stages.py")], check=True)

    # 6) garde-fous : aucun placeholder, aucune image en relatif ou en base64, aucun fichier manquant
    uploads = set(os.listdir(os.path.join(DIST, "uploads")))
    missing = []
    for root, dirs, files in os.walk(DIST):
        for f in files:
            if not f.endswith(".html"): continue
            c = open(os.path.join(root, f), encoding="utf-8").read()
            assert "{{" not in c, "placeholder non résolu dans " + f
            assert "assets/" not in c, "référence assets/ restante dans " + f
            assert "data:image" not in c, "image base64 restante dans " + f
            assert 'src="uploads/' not in c and 'url: "uploads/' not in c, "chemin relatif restant dans " + f
            for ref in set(re.findall(r'/uploads/([^"\')\s]+)', c)):
                if ref not in uploads: missing.append((f, ref))
    assert not missing, "fichiers manquants dans uploads/ : %r" % missing
    print("OK — dist/ généré : %d pages, uploads/ = %d fichiers, aucune image manquante" % (len(PAGES), len(uploads)))

if __name__ == "__main__":
    build()
