#!/usr/bin/env python3
# Assemble le site v2 : head + header + <contenu page> + footer -> dist/
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")

def read(*parts): return open(os.path.join(HERE, *parts), encoding="utf-8").read()

HEAD   = read("partials", "head.html")
HEADER = read("partials", "header.html")
FOOTER = read("partials", "footer.html")

# slug, chemin de sortie, prefixe racine, titre, description
PAGES = [
    ("index",       "index.html",             "",     "Method Acting Center — Devenir Acteur, Scénariste ou Réalisateur à Paris",
     "École de cinéma à Paris depuis 1999 : formations Acteur, Scénariste et Réalisateur autour de la Méthode (Stanislavski / Actors Studio)."),
    ("acteur",      "acteur/index.html",      "../",  "Devenir Acteur — Method Acting Center Paris",
     "Formez-vous au jeu d'acteur avec la Méthode. Apprenez à déclencher, maîtriser et reproduire de vraies émotions face caméra."),
    ("scenariste",  "scenariste/index.html",  "../",  "Devenir Scénariste — Method Acting Center Paris",
     "Écrivez pour le cinéma et la série : structure, personnages, dialogues et développement de projets, encadré par des professionnels."),
    ("realisateur", "realisateur/index.html", "../",  "Devenir Réalisateur — Method Acting Center Paris",
     "Passez derrière la caméra : direction d'acteurs, mise en scène, découpage et tournage, de l'écriture au film fini."),
    ("contact",     "contact/index.html",     "../",  "Contact — Method Acting Center Paris",
     "Une question sur nos formations Acteur, Scénariste ou Réalisateur ? Écrivez-nous, on vous répond sous 48h."),
    ("tarifs",      "tarifs/index.html",      "../",  "Tarifs — Method Acting Center Paris",
     "Tarifs des formations et ateliers du Method Acting Center. Facilités de paiement et offres à la rentrée."),
    ("planning",    "planning/index.html",    "../",  "Planning — Method Acting Center Paris",
     "Le calendrier des cours, ateliers et Journées Portes Ouvertes du Method Acting Center."),
]

def build():
    if os.path.isdir(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    # assets
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(DIST, "assets"))
    for slug, out, root, title, desc in PAGES:
        body = read("pages", slug + ".html")
        page = HEAD + HEADER + body + FOOTER
        page = (page.replace("{{ROOT}}", root)
                    .replace("{{TITLE}}", title)
                    .replace("{{DESC}}", desc))
        dest = os.path.join(DIST, out)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(page)
        print("  ", out, "(", len(page)//1024, "KB )")
    # garde-fou : aucun placeholder non résolu
    for _, out, *_ in PAGES:
        c = open(os.path.join(DIST, out), encoding="utf-8").read()
        assert "{{" not in c, "placeholder non résolu dans " + out
    print("OK — site généré dans dist/ (", len(PAGES), "pages )")

if __name__ == "__main__":
    build()
