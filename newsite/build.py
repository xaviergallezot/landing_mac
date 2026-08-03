#!/usr/bin/env python3
# Assemble le site v2 en pages AUTONOMES : head + header + <contenu> + footer,
# avec CSS, JS et images INTÉGRÉS dans chaque fichier (aucun dossier assets requis).
import os, re, shutil, base64

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
IMGDIR = os.path.join(HERE, "assets", "img")

def read(*parts): return open(os.path.join(HERE, *parts), encoding="utf-8").read()

HEAD   = read("partials", "head.html")
HEADER = read("partials", "header.html")
FOOTER = read("partials", "footer.html")
CSS    = read("assets", "style.css")
JS     = read("assets", "site.js")

MIME = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}

def img_data_uri(name):
    path = os.path.join(IMGDIR, name)
    ext = name.rsplit(".", 1)[-1].lower()
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    return "data:%s;base64,%s" % (MIME[ext], b64)

def inline(page):
    # CSS externe -> <style> intégré
    page = re.sub(r'<link rel="stylesheet" href="[^"]*assets/style\.css">',
                  "<style>\n" + CSS + "\n</style>", page)
    # JS externe -> <script> intégré
    page = re.sub(r'<script src="[^"]*assets/site\.js"></script>',
                  "<script>\n" + JS + "\n</script>", page)
    # images -> data URI base64
    def repl(m):
        name = m.group(1)
        return 'src="' + img_data_uri(name) + '"'
    page = re.sub(r'src="[^"]*assets/img/([^"]+)"', repl, page)
    return page

# slug, fichier de sortie (PLAT, un seul dossier), titre, description
PAGES = [
    ("index",       "index.html",       "Method Acting Center — Devenir Acteur, Scénariste ou Réalisateur à Paris",
     "École de cinéma à Paris depuis 1999 : formations Acteur, Scénariste et Réalisateur autour de la Méthode (Stanislavski / Actors Studio)."),
    ("acteur",      "acteur.html",      "Devenir Acteur — Method Acting Center Paris",
     "Formez-vous au jeu d'acteur avec la Méthode. Apprenez à déclencher, maîtriser et reproduire de vraies émotions face caméra."),
    ("scenariste",  "scenariste.html",  "Devenir Scénariste — Method Acting Center Paris",
     "Écrivez pour le cinéma et la série : structure, personnages, dialogues et développement de projets, encadré par des professionnels."),
    ("realisateur", "realisateur.html", "Devenir Réalisateur — Method Acting Center Paris",
     "Passez derrière la caméra : direction d'acteurs, mise en scène, découpage et tournage, de l'écriture au film fini."),
    ("contact",     "contact.html",     "Contact — Method Acting Center Paris",
     "Une question sur nos formations Acteur, Scénariste ou Réalisateur ? Écrivez-nous, on vous répond sous 48h."),
    ("tarifs",      "tarifs.html",      "Tarifs — Method Acting Center Paris",
     "Tarifs des formations et ateliers du Method Acting Center. Facilités de paiement et offres à la rentrée."),
    ("planning",    "planning.html",    "Planning — Method Acting Center Paris",
     "Le calendrier des cours, ateliers et Journées Portes Ouvertes du Method Acting Center."),
    ("avis",        "avis.html",        "Avis Google — Method Acting Center Paris",
     "Les avis Google des élèves du Method Acting Center : acteurs, scénaristes et réalisateurs. Note 4,8/5."),
]

def build():
    if os.path.isdir(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    for slug, out, title, desc in PAGES:
        body = read("pages", slug + ".html")
        page = HEAD + HEADER + body + FOOTER
        page = (page.replace("{{ROOT}}", "")   # fichiers plats : pas de préfixe
                    .replace("{{TITLE}}", title)
                    .replace("{{DESC}}", desc))
        page = inline(page)
        dest = os.path.join(DIST, out)
        open(dest, "w", encoding="utf-8").write(page)
        print("  ", out, "(", len(page)//1024, "KB )")
    # garde-fous
    for _, out, *_ in PAGES:
        c = open(os.path.join(DIST, out), encoding="utf-8").read()
        assert "{{" not in c, "placeholder non résolu dans " + out
        assert "assets/style.css" not in c, "CSS non intégré dans " + out
        assert "assets/img/" not in c, "image non intégrée dans " + out
    print("OK — site autonome généré dans dist/ (", len(PAGES), "pages, CSS+JS+images intégrés )")

if __name__ == "__main__":
    build()
