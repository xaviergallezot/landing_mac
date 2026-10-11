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
import os, re, shutil, subprocess, sys

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
        page = page.replace("{{ROOT}}", "").replace("{{TITLE}}", title).replace("{{DESC}}", desc)
        page = inline(page)
        open(os.path.join(DIST, out), "w", encoding="utf-8").write(page)
        print("  %-20s %5d Ko" % (out, len(page) // 1024))

    # 2) variante /tarifs/
    os.makedirs(os.path.join(DIST, "tarifs"))
    open(os.path.join(DIST, "tarifs", "index.html"), "w", encoding="utf-8").write(
        tarifs_folder_variant(open(os.path.join(DIST, "tarifs.html"), encoding="utf-8").read()))

    # 3) fichiers statiques (.htaccess, landings jpo / jposr, PDF)
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
