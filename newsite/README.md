# Site Method Acting Center — architecture

## Règle unique pour les images

Toutes les images du site vivent dans **un seul dossier** : `/uploads/` à la racine du serveur.
Chaque page, où qu'elle soit dans l'arborescence (`/`, `/jpo/`, `/jposr/`, `/stages/`, `/tarifs/`),
référence ses images en absolu : `/uploads/nom-du-fichier.jpg`.

Les anciens dossiers `assets/img/`, `jpo/uploads/`, `jposr/uploads/` et `stages/uploads/` ne servent plus
et peuvent être supprimés du serveur.

## Sources (ce que l'on édite)

| Dossier / fichier | Rôle |
|---|---|
| `pages/*.html` | contenu de chaque page du site (sans header ni footer) |
| `partials/head.html`, `header.html`, `footer.html` | parties communes |
| `assets/style.css`, `assets/site.js` | styles et scripts du site, intégrés dans chaque page à la construction |
| `assets/img/` | **toutes** les photos et affiches, copiées telles quelles dans `dist/uploads/` |
| `static/.htaccess` | règles serveur (HTTPS, URLs propres, cache) |
| `static/jpo/index.html` | landing Portes Ouvertes · acteurs (fichier autonome) |
| `static/jposr/index.html` | landing Portes Ouvertes · scénario / réalisation (fichier autonome) |
| `static/uploads/` | fichiers non-image à publier dans `/uploads/` (planning PDF) |
| `tools/build_landing_stages.py` | génère la landing `/stages/` à partir de `static/jpo/index.html` ; sessions, dates et tarifs se règlent dans `SESSIONS` |
| `prod-snapshot/` | copie conforme de la prod telle qu'elle était avant la mise en conformité (référence, non utilisée) |

## Construction

```bash
cd newsite
python3 build.py
```

`build.py` vide et régénère `dist/` en entier :

```
dist/
  .htaccess
  index.html  acting.html  scenario-real.html  contact.html  tarifs.html
  planning.html  cours-essai.html  stages.html  inscription.html  jpo.html
  tarifs/index.html        (variante de tarifs.html pour le dossier /tarifs/)
  jpo/index.html
  jposr/index.html
  stages/index.html        (générée)
  uploads/                 (le dossier d'images unique + planning PDF)
```

Le script refuse de terminer si une page référence un fichier absent de `uploads/`,
contient encore une image en base64 ou un chemin relatif.

## Mise en ligne

Déposer le contenu de `dist/` à la racine du site (dossier `www/`), en écrasant l'existant.
Après le premier déploiement de cette architecture, supprimer sur le serveur :
`assets/img/`, `jpo/uploads/`, `jposr/uploads/`, `stages/uploads/`.

## Ajouter ou remplacer une photo

Choix des photos (consigne du propriétaire, 2026-10-17) : privilégier des photos **actives, explosives
en jeu d'acteur**, où le **visage est bien visible** (de face ou de trois-quarts face). Éviter les dos,
les profils perdus et les plans statiques. Les affiches du carrousel de films ne changent pas.

1. Déposer le fichier dans `assets/img/` avec un nom explicite (minuscules, tirets, sans accents).
2. Le référencer dans la page source avec `{{ROOT}}assets/img/nom.jpg` (pages du site)
   ou `/uploads/nom.jpg` (landings et générateur).
3. Relancer `python3 build.py` puis déposer `dist/`.
