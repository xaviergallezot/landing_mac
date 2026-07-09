# Method Acting Center — Landing « Acteur » (v4)

Landing page marketing pour Method Acting Center (Paris) : stages d'été et
formation annuelle à la Méthode (Stanislavski / Actors Studio).

Implémentation de la maquette **Landing Acteur v4** conçue dans Claude Design.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | La landing page complète, autonome (HTML + CSS inline + un seul `<script>` vanilla). Aucune dépendance de build. |
| `uploads/` | Les images (photos de spectacle, affiches de films, visuels de scène). |
| `design/Landing Acteur v4.dc.html` | Le fichier source Claude Design (format `.dc.html`), conservé pour référence. |

## Lancer le site

Aucune étape de build. Servez le dossier avec n'importe quel serveur statique :

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

(Un `file://` direct fonctionne aussi, mais un serveur local évite les
restrictions de certains navigateurs sur les ressources locales.)

## Ce que fait la page

Le format source `.dc.html` est réactif (`sc-for`, `sc-if`, `{{ … }}`, `onClick`,
`style-hover`). Il a été porté en HTML/CSS/JS standard, à l'identique :

- **Barre sticky**, ancres de navigation et défilement fluide (scroll-snap).
- **Hero** avec carrousel automatique (4 visuels, rotation 4,5 s) + puces cliquables.
- **Apparition au défilement** (`data-reveal`) via `IntersectionObserver`.
- **Survol/focus** : les attributs `style-hover` / `style-focus` de la maquette sont
  ré-appliqués par un petit runtime JS (aucune classe CSS générée).
- **Programme sur 4 ans** : onglets d'année qui mettent à jour titre, ateliers et
  livrables (la 4ᵉ année affiche les livrables : scènes filmées, book, bande démo…).
- **Formulaire de contact** : validation native + passage à l'état « Message envoyé ».
  ⚠️ Le formulaire est purement front-end (comme dans la maquette) : branchez-le à
  votre backend / service d'emailing pour l'exploiter réellement.

## Images — à remplacer

Les visuels de la maquette vivent dans le projet Claude Design. **6 images** ont pu
être récupérées intactes. Les **16 autres dépassent la limite de 256 Kio de l'API
de design** et n'ont pas pu être téléchargées en entier ; elles ont été remplacées
par des **placeholders** aux bonnes proportions (fond sombre + mention
« IMAGE À REMPLACER »). Remplacez ces fichiers dans `uploads/` par les originaux
(mêmes noms de fichier) — aucune modification de code n'est nécessaire.

**Images réelles présentes :** `Malcolm_And_Marie_Horizontal00086407_V1.jpg`,
`Les-7-vies-de-Lea_Raika_Hazanavicius.jpg`, `Quantum-of-Solace-Olga-Kurylenko.jpg`,
`affiche-ni-chaines-ni-maitres-66e49d69a884b564930223.jpg`, `Sans-repit-Jemima-West.jpg`,
`Martyrs_Mylene_Jampanoi.jpg`.

**Placeholders à remplacer :**

- Hero : `Kramer_Horizontal00086408_V1.jpg`, `Felure_Horizontal00086406_V1.jpg`,
  `Joseph-Breaking-Bad.jpg`, `King_Horizontal00086407_V1.jpg`
- La Méthode : `METHOD_ACTING_CENTER_..._Ghorra-3.jpg`,
  `V1-0001_Antichrist_Screenshot_Horizontal00087169.jpg`,
  `METHOD_ACTING_CENTER_..._Ghorra-272.jpg`
- Stages / Formation : `..._Ghorra-22.jpg`, `..._Ghorra-98.jpg`, `..._Ghorra-213.jpg`,
  `..._Ghorra-154.jpg`, `..._Ghorra-163.jpg`, `..._Ghorra-269.jpg`
- Affiches : `Le_Proces_Goldman_Affiche.webp`, `Les-invisibles_Deborah_Krey.jpg`,
  `Dirty-Diffficult-Dangerous.jpg`

## Notes

- Polices **Oswald** + **Archivo** chargées depuis Google Fonts ; repli
  Helvetica / sans-serif si hors-ligne.
- `prefers-reduced-motion` désactive scroll-snap et animations.
- Aucune donnée n'est envoyée : les liens d'inscription pointent vers
  `methodacting.fr`, le formulaire reste local.
