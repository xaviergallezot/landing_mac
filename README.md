# Method Acting Center — Landing « Acteur » (v4)

Landing page marketing pour Method Acting Center (Paris) : stages d'été et
formation annuelle à la Méthode (Stanislavski / Actors Studio).

Implémentation de la maquette **Landing Acteur v4** conçue dans Claude Design.

## Fichiers

| Fichier | Rôle |
|---|---|
| **`landing-mac.html`** | ⭐ **Le livrable WordPress** : bloc HTML autonome (fonts + CSS + JS) à coller dans un bloc « HTML personnalisé ». Toutes les URLs d'images sont centralisées dans l'objet `IMAGES` (voir plus bas). |
| `index.html` | Version « document complet » pour prévisualiser en local (double-clic) avec les images du dossier `uploads/`. |
| `uploads/` | Images de prévisualisation. 6 sont réelles ; 16 sont des **placeholders** (voir plus bas) — sur WordPress, elles sont remplacées par la Médiathèque, pas par ces fichiers. |
| `design/Landing Acteur v4.dc.html` | Le fichier source Claude Design (`.dc.html`), conservé pour référence. |

## Intégration dans WordPress

1. Crée une page (idéalement avec un gabarit **pleine largeur / vierge**, sans
   la sidebar du thème).
2. Ajoute un bloc **« HTML personnalisé »** (Gutenberg) ou un **widget HTML**
   (Elementor / Divi / WPBakery).
3. Colle tout le contenu de **`landing-mac.html`**.
4. Publie les photos (voir ci-dessous), puis renseigne leurs URLs dans l'objet
   `IMAGES` en bas du bloc.

Le bloc est **sans effet sur le thème** : tous les styles sont limités à
`#mac-landing`, il n'y a pas de `scroll-snap` global qui détournerait le
défilement, et l'en-tête / pied de page du thème restent intacts.

## Publier les photos (process WordPress)

Tant qu'une URL n'est pas renseignée (ou invalide), un **cadre étiqueté**
s'affiche à la place — la page n'est jamais « cassée ». Pour chaque visuel :

1. **Médias → Ajouter** : téléverse la photo.
2. Ouvre-la, copie son **« URL du fichier »**
   (ex. `https://votre-site.fr/wp-content/uploads/2026/07/photo.jpg`).
3. Dans `landing-mac.html`, colle cette URL dans le champ `url` de la clé
   correspondante de l'objet `IMAGES`.

### Correspondance des images

| Clé `IMAGES` | Emplacement sur la page | Format conseillé |
|---|---|---|
| `hero_kramer` / `hero_felure` / `hero_joseph` / `hero_king` | Carrousel du **hero** (4 visuels) | paysage large (~1600×1000) |
| `methode_1` / `methode_2` / `methode_3` | Cartes **Déclencher / Maîtriser / Reproduire** | paysage 16:10 |
| `stage_1` / `stage_2` / `stage_3` | Galerie **Stages d'été** | portrait 3:4 |
| `formation_1` / `formation_2` / `formation_3` | Galerie **Formation annuelle** | portrait 3:4 |
| `film_proces_goldman`, `film_7_vies_lea`, `film_quantum_solace`, `film_ni_chaines`, `film_sans_repit`, `film_les_invisibles`, `film_dirty_difficult`, `film_martyrs` | Carrousel **« Nos acteurs tournent »** | affiche 2:3 |
| `contact_scene` | Section **Contact** | paysage 16:9 |

L'étiquette affichée dans chaque cadre placeholder indique aussi de quel visuel
il s'agit, directement dans la page.

## Ce que fait la page

Le format source `.dc.html` est réactif (`sc-for`, `sc-if`, `{{ … }}`, `onClick`,
`style-hover`). Il a été porté en HTML/CSS/JS standard, à l'identique :

- **Barre sticky**, navigation par ancres avec défilement fluide.
- **Hero** : carrousel automatique (4 visuels, rotation 4,5 s) + puces cliquables.
- **Apparition au défilement** (`data-reveal`) via `IntersectionObserver`.
- **Survol / focus** : les attributs `style-hover` / `style-focus` de la maquette
  sont ré-appliqués par un petit runtime JS.
- **Programme sur 4 ans** : onglets d'année qui mettent à jour titre, ateliers et
  livrables (la 4ᵉ année affiche : scènes filmées, book, bande démo…).
- **Formulaire de contact** : validation native + passage à l'état
  « Message envoyé ». ⚠️ Purement front-end (comme la maquette) — sur WordPress,
  branche-le à ton plugin de formulaire / emailing pour le rendre fonctionnel
  (Contact Form 7, WPForms…), ou garde-le décoratif.

## Le dossier `uploads/` (prévisualisation locale)

6 images ont pu être récupérées intactes depuis le projet Claude Design. Les 16
autres **dépassaient la limite de 256 Kio de l'API de design** et ont été
remplacées par des placeholders aux bonnes proportions, uniquement pour que
`index.html` s'affiche joliment en local. **Sur WordPress, tout passe par la
Médiathèque** — ces fichiers ne sont donc pas utilisés en production.

Placeholders (à fournir via la Médiathèque) : les 4 visuels hero
(`Kramer`, `Felure`, `Joseph`, `King`), les 9 photos de plateau `…Ghorra-…`
+ `Antichrist`, et 3 affiches (`Le Procès Goldman`, `Les Invisibles`,
`Dirty Difficult Dangerous`).

## Notes

- Polices **Oswald** + **Archivo** (Google Fonts) ; repli Helvetica / sans-serif.
- `prefers-reduced-motion` désactive les animations.
- Liens d'inscription → `methodacting.fr`. Aucune donnée n'est envoyée par la page.
