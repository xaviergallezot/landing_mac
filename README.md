# Method Acting Center — Landing « Acteur » (v5 · Journées Portes Ouvertes)

Landing page marketing pour Method Acting Center (Paris), optimisée **CRO** pour
les campagnes **Google Ads Search** (« devenir acteur », « école de théâtre »…).

Objectif de conversion : **maximiser les inscriptions aux Journées Portes
Ouvertes (JPO)** immersives — la porte d'entrée naturelle vers la formation.
Le parcours raconte une histoire : « Je veux devenir acteur » → « Je vais
commencer par vivre une Journée Portes Ouvertes ». Tous les CTA principaux
convergent vers la réservation d'une JPO.

## Fichiers

| Fichier | Rôle |
|---|---|
| **`landing-mac.html`** | ⭐ **Livrable WordPress** : bloc HTML autonome à coller dans un bloc « HTML personnalisé ». URLs d'images centralisées dans l'objet `IMAGES`. |
| `maquette-ordinateur.html` / `maquette-telephone.html` | Maquettes de relecture **autonomes** (photos embarquées en base64), même base responsive. |
| `index.html` | Aperçu local (double-clic) utilisant le dossier `uploads/`. |
| `src/` | **Source unique** qui génère les 4 fichiers ci-dessus (voir plus bas). |
| `uploads/` | Images de prévisualisation (6 réelles + 16 placeholders étiquetés). |
| `design/Landing Acteur v4.dc.html` | Fichier source Claude Design d'origine. |

## Source unique & régénération (`src/`)

Pour éviter que les 4 fichiers ne divergent, ils sont **générés** à partir d'un
seul jeu de sources :

- `src/content.html` — le HTML de toutes les sections (images via `data-img`).
- `src/style.css` — les styles (limités à `#mac-landing`).
- `src/script.js` — le runtime JS (carrousels, accordéon JPO, formulaire…).
- `src/build_all.py` — assemble et écrit `index.html`, `landing-mac.html` et les
  2 maquettes.

Régénérer après modification :

```bash
cd src && python3 build_all.py
```

## Contenus éditables sans toucher au design

Dans `src/script.js` (et donc en haut du `<script>` des fichiers générés) :

- **`IMAGES`** — les visuels. Sur WordPress : téléversez chaque photo dans la
  Médiathèque et collez son URL. Tant qu'une URL manque, un cadre étiqueté
  s'affiche (la page n'est jamais cassée).
- **`REVIEWS`** — les avis Google. ⚠️ N'utilisez que de **vrais avis** de la
  fiche Google. Ajoutez-en autant que voulu : le carrousel s'adapte
  automatiquement (flèches, points, défilement auto).
- **`PROGRAM`** — le détail des 4 années de formation.

## Ce que fait la page

- **Barre sticky** + **CTA fixe mobile** « Je réserve ma JPO » (apparaît après le
  hero, se masque au niveau du formulaire).
- **Hero** : carrousel automatique.
- **Section JPO** (le cœur de la conversion) : 4 grandes cartes en **accordéon**
  (Vous vous reconnaissez si… / Vous allez vivre… / Vous repartirez avec…), un
  **déroulé en 4 étapes**, et un CTA immersif.
- **Formation** : onglets par année (programme Acting Pro), présentée comme la
  suite naturelle de la JPO.
- **Avis** : véritable **carrousel** (grandes cartes, avatars, flèches, points,
  défilement auto) — uniquement de vrais avis Google, note 4,8/5.
- **FAQ**, **formulaire** de réservation JPO (validation + état « Demande
  envoyée »), apparitions au scroll, survols.

⚠️ Le formulaire est front-end (comme la maquette). Sur WordPress, branchez-le à
Contact Form 7 / WPForms pour l'exploiter réellement.

## Intégration WordPress (rappel)

1. Page en gabarit pleine largeur.
2. Bloc « HTML personnalisé » → coller `landing-mac.html`.
3. Téléverser les photos dans la Médiathèque et renseigner l'objet `IMAGES`.

Le bloc est **sans effet sur le thème** (styles limités à `#mac-landing`,
pas de scroll-snap global).

## Le dossier `uploads/`

6 images réelles ont pu être récupérées ; les 16 autres dépassaient la limite de
256 Kio de l'API de design et sont des **placeholders** aux bonnes proportions,
pour l'aperçu local uniquement. En production, tout passe par la Médiathèque.

## Notes

- Polices **Oswald** + **Archivo** (Google Fonts) ; repli Helvetica / sans-serif.
- Charte inchangée : cream `#F7F4EE`, noir `#14120F` / `#0B0A0A`, rouge `#E0261F`.
- `prefers-reduced-motion` désactive les animations.
