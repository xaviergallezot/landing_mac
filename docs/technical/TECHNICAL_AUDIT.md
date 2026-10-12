# Audit SEO technique — Method Acting Center (newsite/dist)

Agent : technical-seo · Date : 2026-10-12 · Phase A (audit en lecture seule, aucun fichier de `newsite/` modifié).
Périmètre : les 14 pages HTML de `newsite/dist/` (copie exacte de ce qui est déployé sur https://www.methodacting.fr/), `.htaccess`, `robots.txt`, `sitemap.xml`, `llms.txt`, `build.py`, partials et générateur de la landing `/stages/`.

---

## 1. Méthode et limites

### Ce qui a été testé localement

| Contrôle | Outil | Résultat brut |
|---|---|---|
| Build reproductible | `python3 build.py` dans une copie temporaire du dossier `newsite/` (scratchpad), puis `diff -rq` avec `newsite/dist/` | Build OK en 0,1 s, `dist/` strictement identique, `git status` propre sur `newsite/` |
| Crawl des 14 pages | Script Python (`html.parser`, stdlib) : titres, meta, canonical, OG, JSON-LD (parsing + types), H1-H6, liens internes/externes, images, `alt`, `loading`, `width/height`, références `/uploads/` (HTML + JS + CSS), poids brut et gzip | Voir § 2 |
| Images | Pillow : dimensions, format, poids des 46 fichiers de `dist/uploads/` | Voir § 5 |
| Rendu mobile | Playwright + Chromium, viewport 390×844, `isMobile`, DPR 2, requêtes externes bloquées (pas de réseau sortant) : débordements horizontaux, cibles tactiles, contraste approximatif, erreurs console, LCP/CLS locaux, captures | Voir § 6 |
| `.htaccess` | Analyse à la lecture, règle par règle (mod_rewrite, mod_dir, ErrorDocument, cache) | Voir § 4.4 |
| JSON-LD | Validation syntaxique (JSON), cohérence avec le texte visible (grep des prix, dates, note, FAQ), comparaison aux exigences Google (Course, Event, LocalBusiness, FAQPage) | Voir § 3 |

### Ce qui n'a PAS pu être vérifié (site en ligne injoignable depuis l'environnement)

- Codes HTTP réels, chaînes de redirection, en-têtes (`Location`, `Cache-Control`, `Content-Encoding`), HSTS.
- Comportement effectif d'Apache OVH : `X-Forwarded-Proto`, `DirectorySlash`, `AllowOverride` (une directive refusée en `.htaccess` = erreur 500).
- TTFB, Core Web Vitals terrain (CrUX), Lighthouse en conditions réseau réelles, chargement des Google Fonts.
- État d'indexation (Search Console), anciennes URLs WordPress à rediriger, fichiers obsolètes encore présents sur le serveur (`assets/img/`, `jpo/uploads/`…).
- Les valeurs LCP/CLS mesurées localement (fichiers servis instantanément, polices bloquées) ne sont **pas** représentatives et ne sont citées qu'à titre indicatif.

Méthode de vérification en ligne proposée (à exécuter par le propriétaire ou un agent disposant du réseau) :

```bash
for u in / /acting /acting.html /tarifs /tarifs/ /tarifs.html /jpo /jpo.html /jpo/ /stages /stages.html /stages/ /index.html /inexistant /favicon.ico; do
  printf "%-18s " "$u"; curl -s -o /dev/null -w "%{http_code} -> %{redirect_url}\n" "https://www.methodacting.fr$u"; done
curl -sI http://methodacting.fr/ | grep -i "^HTTP\|^location"     # non-www / http
curl -sI https://www.methodacting.fr/ | grep -i "content-encoding\|cache-control\|strict-transport"
curl -s https://www.methodacting.fr/robots.txt ; curl -s https://www.methodacting.fr/sitemap.xml | head
# PageSpeed Insights (mobile) sur /, /acting, /stages.html, /stages/ ; Rich Results Test sur /acting, /stages.html, /tarifs.
```

---

## 2. Résultats du crawl local

Toutes les pages : `lang="fr"`, viewport correct, un seul `<h1>`, canonical et OG présents, JSON-LD syntaxiquement valide, **aucun lien interne cassé** sur disque, **aucune image manquante** dans `/uploads/`. Aucune page ne déclare de favicon. Aucune balise analytics n'est présente (voir D3).

| Page (dist) | Titre | L. | Meta description (début) | L. | H1 | H1 | Canonical | OG image | Types JSON-LD | Liens int. | Img | Img alt vide | HTML brut / gzip |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| /index.html | Method Acting Center — Devenir Acteur, Scénariste ou Réalisateur à Paris | 72 | École de cinéma à Paris depuis 1999 : formations Acteur… | 135 | Le talent, ça s'apprend. | 1 | / | scene-a-deux-acteurs… (1100×733) | Organization+LocalBusiness, WebSite, WebPage, Event | 10 | 24 | 8 | 94 / 21 Ko |
| /acting.html | Formation Acting — Devenir Acteur — Method Acting Center Paris | 62 | Formation Acting : apprenez à jouer vrai avec la Méthode… | 156 | Apprendre à jouer vrai. | 1 | /acting | methode-declencher.jpg (900×1125, portrait) | + Course | 11 | 20 | 8 | 94 / 22 Ko |
| /scenario-real.html | Scénario, Réalisation & Direction d'acteurs — Method Acting Center Paris | 72 | Formation Scénario, Réalisation & Direction d'acteurs… | 178 | Racontez vos propres histoires. | 1 | /scenario-real | tournage-equipe-terrasse… (1600×1064) | + Course | 11 | 24 | 11 | 91 / 21 Ko |
| /contact.html | Contact — Method Acting Center Paris | 36 | Une question sur nos formations… | 106 | Parlons de votre projet. | 1 | /contact | scene-a-deux-acteurs… | Org, WebSite, WebPage | 10 | 0 | 0 | 78 / 18 Ko |
| /tarifs.html | Tarifs — Method Acting Center Paris | 35 | Tarifs des formations et ateliers… | 104 | Des tarifs clairs. | 1 | /tarifs | methode-maitriser.jpg (portrait) | + FAQPage | 15 | 12 | 0 | 89 / 20 Ko |
| /planning.html | Planning — Method Acting Center Paris | 37 | Le calendrier des cours, ateliers et JPO… | 86 | Les dates à retenir. | 1 | /planning | methode-reproduire.jpg (portrait) | + Event ×7 | 19 | 1 | 0 | 96 / 20 Ko |
| /cours-essai.html | Cours d'essai gratuit — Method Acting Center Paris | 50 | Testez gratuitement un vrai atelier… | 150 | Essayez un cours, gratuitement. | 1 | /cours-essai | cours-acting-groupe… (1100×880) | + Offer (orphelin) | 10 | 1 | 0 | 94 / 21 Ko |
| /stages.html | Stages d'acting & de scénario — week-end et intensifs — Method Acting Center Paris | 82 | Stages week-end (Initiation à la Méthode…) | 153 | Un week-end pour tester la Méthode, pour de vrai. | 1 | /stages.html | scene-theatre-tension… (1333×2000, portrait) | + Event ×6 | 10 | 5 | 0 | 107 / 24 Ko |
| /inscription.html | Inscription — Method Acting Center Paris | 40 | Demandez votre rendez-vous d'inscription… | 194 | Demandez votre inscription. | 1 | /inscription | portrait-acteur… (880×1100, portrait) | Org, WebSite, WebPage | 11 | 1 | 0 | 95 / 22 Ko |
| /jpo.html | Journées Portes Ouvertes — 12 & 13 décembre — Method Acting Center Paris | 72 | Journées Portes Ouvertes gratuites les 12 & 13 décembre… | 179 | Venez vivre la Méthode. | 1 | /jpo.html | actrice-emotion-stage… (1333×2000, portrait) | + Event | 10 | 1 | 0 | 91 / 21 Ko |
| /tarifs/index.html | *(copie de tarifs.html)* | 35 | *(idem)* | 104 | Des tarifs clairs. | 1 | /tarifs | methode-maitriser.jpg | + FAQPage | 15 | 12 | 0 | 89 / 20 Ko |
| /jpo/index.html (landing) | Method Acting Center — Devenez acteur · Journées Portes Ouvertes à Paris | 72 | Vous voulez devenir acteur ? Venez vivre la Méthode… | 171 | Vous voulez devenir acteur ? | 1 | /jpo/ | actrice-emotion-stage… | **aucun** | 14 | 27 (via JS) | 8 | 115 / 24 Ko |
| /jposr/index.html (landing) | Method Acting Center — Devenez réalisateur & scénariste · Journées Portes Ouvertes à Paris | 90 | Vous voulez devenir scénariste réalisateur ?… | 181 | Vous voulez devenir Scénariste Réalisateur ? | 1 | /jposr/ | tournage-equipe-terrasse… | **aucun** | 14 | 33 (via JS) | 11 | 115 / 24 Ko |
| /stages/index.html (landing générée) | Stages d'acting à Paris — Week-end & intensifs · Method Acting Center | 69 | Vous voulez devenir acteur ? Découvrez la Méthode… | 205 | Vous voulez devenir acteur ? | 1 | /stages/ | actrice-emotion-stage… | **aucun** | 12 | 26 (5 lazy) | 8 | 105 / 22 Ko |

Observations transversales :

- **Titres** : 7 titres sur 14 dépassent 65 caractères (jusqu'à 90 pour `/jposr/`), donc tronqués en SERP ; le suffixe « — Method Acting Center Paris » est bien placé en fin.
- **Meta descriptions** : 5 pages > 160 caractères (inscription 194, `/stages/` 205, jposr 181, jpo.html 179, scenario-real 178) ; planning est courte (86) et générique.
- **H1** : uniques et pertinents ; mais `/jpo/` et `/stages/` partagent exactement le même H1 (« Vous voulez devenir acteur ? »), avec des descriptions qui commencent à l'identique.
- **Liens internes** : chaque page du site relie les 9 autres (nav + footer) : pas de page orpheline parmi les 10 pages du site. En revanche les trois landings `/jpo/`, `/jposr/`, `/stages/` ne reçoivent **aucun lien** depuis le site (seulement entre elles et depuis le footer de `/stages/` → `/jposr/`) : orphelines du point de vue du maillage, absentes du sitemap.
- **Forme des liens** : 100 % des liens internes sont écrits `acting.html`, `tarifs.html`… (ou `/acting.html` sur les landings et `/tarifs/`). Or `.htaccess` redirige `/page.html` → `/page` en 301 : **chaque clic interne passe par une redirection** (voir D2).
- **Images sans `alt` renseigné** : 27 occurrences (`alt=""`) concentrées sur les affiches de films de la section « Nos acteurs tournent » (index, acting : 8 ; scenario-real : 11 ; landings idem). Ces affiches portent une information (films où jouent des anciens élèves) ; elles ne sont pas décoratives. Aucun `alt` absent par ailleurs : bon point.
- **Attributs image** : 0 `width`/`height` sur 150 balises `<img>` ; `loading="lazy"` sur 5 images seulement (toutes sur `/stages/`) ; aucun `srcset`, aucun `fetchpriority`, aucun `preload`.
- **Scripts** : tout est inline ; aucun script tiers ; les formulaires appellent `api.web3forms.com` (clé publique visible dans le JS, comportement normal de Web3Forms).
- **Mots** : 330 (contact) à 1 960 (`/stages/`) mots par page ; aucune page « vide ».

---

## 3. Données structurées

### 3.1 Validité et cohérence avec le contenu visible

| Nœud (build.py) | Pages | Validité | Cohérence visible | Remarques |
|---|---|---|---|---|
| `EducationalOrganization` + `LocalBusiness` `#organization` | les 10 pages du site (+ `/tarifs/`) | JSON valide | Adresse, téléphone, email, horaires, réseaux : cohérents avec `FACTS_REGISTER` | **`logo` = photo de scène** (`scene-a-deux-acteurs…jpg`), pas un logo : Google exige une image de logo ; `image` identique. `description` embarque « Note Google 4,8/5 sur 98 avis » : vieillira. `additionalType: School` acceptable. Manquent `priceRange`, `geo`, `hasMap` (recommandés LocalBusiness). |
| `aggregateRating` 4,8 / 98 | idem | valide | Le badge « 4,8/5 · 98 avis » est visible sur chaque page (1 à 2 occurrences) | **Avis « auto-déclarés »** : Google n'affiche pas d'étoiles pour une note placée par l'entité sur son propre site (règle « self-serving reviews »). Pas une infraction, mais aucun résultat enrichi à attendre ; risque de décalage avec la fiche Google au fil du temps (valeur datée du 2026-10-12). |
| `WebSite`, `WebPage` | toutes | valide | — | `primaryImageOfPage` passé comme chaîne URL (toléré). |
| `Course` « Formation Acting » (370 €/mois) | /acting | valide | Le prix **370 € n'est pas visible sur /acting** (seulement sur /tarifs) ; « 2 ateliers de 4 h par semaine » visible sur /acting et /inscription | Exigences Google « Course info » non remplies : `courseMode` attendu `Onsite` (ici `onsite`), `courseWorkload` absent, `courseSchedule` sans `repeatCount` ni `duration`. Le volume horaire est placé dans `CourseInstance.description`. Ne génère pas de résultat enrichi en l'état. |
| `Course` « Scénario, Réalisation… » (350 €/mois) | /scenario-real | valide | Prix non visible sur la page ; « 26 samedis de 8 h » visible | Idem ; `repeatFrequency: Weekly` est faux pour un programme de 26 samedis + 24 dimanches. |
| `Event` JPO 12-13 déc. 2026 (gratuit, `isAccessibleForFree`) | /, /jpo.html, /planning | valide | Dates visibles sur les 3 pages | Pas d'heure ni de fuseau (recommandé) ; `image` = visuel des stages ; `offers.url` → `/jpo.html` OK. |
| `Event` ×6 stages (160 € ou sans offre) | /stages.html, /planning | valide | Dates et « dès 160 € » visibles ; intensifs « tarif sur demande » sans `offers` : conforme au registre | `url` → `/stages.html` et non vers l'ancre du stage ; pas d'heure. Les stages passés (après le 18/10/2026) resteront déclarés `EventScheduled` tant que `build.py` n'est pas édité : prévoir un retrait automatique par date. |
| `Offer` « Cours d'essai gratuit » | /cours-essai | valide | Visible | Nœud orphelin (non rattaché à un `Product`/`Service`/`Course`) : ignoré par Google ; inoffensif. |
| `FAQPage` (4 questions) | /tarifs | valide | Les 4 questions/réponses sont présentes mot pour mot dans la page | Depuis août 2023 Google ne montre les FAQ enrichies que pour des sites gouvernementaux/santé : aucun gain SERP, reste utile aux IA. |
| Landings `/jpo/`, `/jposr/`, `/stages/` | — | **aucun JSON-LD** | — | Pas même `Organization` ni `Event` alors que ces pages portent les dates des JPO et stages. |

### 3.2 Propriétés discutables ou à décider

1. `aggregateRating` : conserver uniquement si une procédure de rafraîchissement (date + valeur) existe ; sinon retirer du JSON-LD (le badge visible peut rester).
2. `logo` : remplacer par un vrai fichier logo (PNG/SVG ≥ 112×112) — **[À VALIDER] : fichier logo à fournir par le propriétaire**.
3. `Course.offers.price` : soit afficher le prix mensuel sur /acting et /scenario-real (renvoi vers /tarifs), soit retirer `offers` des `Course` (le JSON-LD ne doit pas dire plus que la page).
4. `courseSchedule` : aligner sur les faits (`repeatCount`, `duration` en ISO 8601 : `PT4H`, `PT8H`, `PT5H`) — valeurs présentes sur /inscription, mais **[À VALIDER]** par le propriétaire avant de les figer dans le balisage.
5. Les `Event` dupliqués sur 2-3 pages sont acceptables (même entité) ; ajouter `@id` stables (`…/stages.html#stage-a`) pour éviter des doublons côté Google.

---

## 4. Indexation

### 4.1 Sitemap vs pages réelles

- `sitemap.xml` (généré par `build.py`) : 10 URL, toutes canoniques et cohérentes avec les balises `canonical` des pages. Bon.
- Absentes : `/jpo/`, `/jposr/`, `/stages/` (landings) — elles sont pourtant **indexables** (`index, follow`, canonical sur elles-mêmes) : incohérence (soit on les veut indexées et on les ajoute, soit on les passe en `noindex`).
- `lastmod` = date du build pour les 10 URL (`datetime.date.today()`), même sans modification : signal faux ; Google ignore un `lastmod` non fiable.
- Mélange d'URL propres (`/acting`) et d'URL `.html` (`/jpo.html`, `/stages.html`) : fonctionnel, documenté dans `.htaccess`, mais peu lisible.

### 4.2 robots.txt

- `Allow: /` + `Disallow: /tarifs/` + `Sitemap:` : syntaxe correcte, ouvert aux crawlers IA (choix stratégique assumé dans `CLAUDE.md`).
- **Problème** : `Disallow: /tarifs/` bloque le crawl de l'URL vers laquelle `/tarifs` redirige probablement (voir 4.4). Un `Disallow` ne désindexe pas et empêche surtout Google de lire la canonical de `/tarifs/index.html`.
- Les landings contiennent des liens vers `/tarifs/` (footer), donc vers une URL bloquée.

### 4.3 Canonicals et duplication

| Doublon | Canonical | Évaluation |
|---|---|---|
| `/tarifs.html` ↔ `/tarifs` ↔ `/tarifs/index.html` | tous → `/tarifs` | voir D1 : la cible canonique n'est probablement pas servable en 200 |
| `/stages.html` (page site) ↔ `/stages/` (landing) | chacune sur elle-même | **deux pages indexables sur la même intention** « stages d'acting Paris », titres proches, mêmes 6 stages, même formulaire : cannibalisation |
| `/jpo.html` ↔ `/jpo/` | chacune sur elle-même | idem pour « journées portes ouvertes » ; `/jpo/` et `/stages/` ont le même H1 |
| `/index.html` ↔ `/` | `.htaccess` 301 | correct |
| `/jpo/index.html`, `/stages/index.html` | canonical → dossier | correct (pas de redirection mais canonical) |

### 4.4 `.htaccess` (analyse à la lecture, non exécutée)

Ordre : HTTPS → TRACE → `/index.html`→`/` → exception `jpo.html|stages.html` → `/page.html`→`/page` (301) → réécriture interne `/page`→`page.html` → `ErrorDocument 404 /index.html` → gzip → Expires.

1. **`/tarifs` est un dossier sur le serveur** (`dist/tarifs/index.html`). La réécriture interne exige `RewriteCond %{REQUEST_FILENAME} !-d` : elle est donc **ignorée** pour `/tarifs`, et `mod_dir` (DirectorySlash, actif par défaut) renvoie **301 `/tarifs` → `/tarifs/`**. Conséquences probables : la canonical `/tarifs` (sitemap, balises, llms.txt) répond 301 ; la page réellement servie `/tarifs/` est **interdite par robots.txt** ; le lien interne `tarifs.html` produit une chaîne **301 → 301 → URL bloquée**. La page Tarifs — commerciale, intention n° 4 — est vraisemblablement mal ou pas indexée. Confiance 4/5 : à confirmer par `curl -sI https://www.methodacting.fr/tarifs`.
2. Redirection `.html` → URL propre : correcte (THE_REQUEST évite les boucles ; la query string est conservée automatiquement). Mais elle transforme tous les liens internes en 301 (D2).
3. `/jpo` et `/stages` (sans extension) servent les landings via `mod_dir` ; `/jpo.html` et `/stages.html` sont protégées de la règle 3 : conforme à l'intention.
4. **HTTPS** : conditionné à `X-Forwarded-Proto` (comportement OVH mutualisé derrière proxy). Si le header manquait, la règle bouclerait (301 infini). Non vérifiable ici ; à tester avec `curl -I http://www.methodacting.fr/`.
5. **Aucune canonicalisation d'hôte** : `methodacting.fr` → `www.methodacting.fr` n'est pas forcée (seule la balise canonical corrige). À vérifier en ligne ; ajouter la règle si OVH ne le fait pas.
6. **`ErrorDocument 404 /index.html`** : avec un chemin local, Apache conserve le statut **404** (pas de soft-404 côté code) mais sert le HTML de l'accueil, avec `canonical` = `/`, titre de l'accueil et aucun message d'erreur : expérience trompeuse, signaux contradictoires. Si le test en ligne renvoie 200 (certaines configurations OVH), c'est un soft-404 généralisé à corriger en priorité.
7. Cache : HTML 1 h, images 1 an (sans versionnement : remplacer une photo sous le même nom = cache obsolète 1 an), **pas de règle pour `font/woff2`** (utile si polices auto-hébergées), PDF 1 mois. Le commentaire « images en base64 » est obsolète.
8. Aucun en-tête de sécurité (`Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`). Sans impact direct SEO, mais attendu.
9. Bloc « Redirections 301 des anciennes URLs WordPress » **vide**. Le dépôt (`prod-snapshot/`) ne contient ni ancien sitemap, ni robots, ni .htaccess : la liste des anciennes URL est inconnue → **[À VALIDER]** export Search Console (pages avec impressions) + Wayback Machine avant d'écrire les 301.
10. `Options -Indexes`, `LimitRequestBody`, `<Files .htaccess>` : nécessitent `AllowOverride` suffisant ; si OVH refuse l'une d'elles, tout le site répond 500. À confirmer que la prod actuelle répond bien (elle utilise déjà ce fichier).

### 4.5 llms.txt

Cohérent avec le registre des faits et les canonicals (`/stages.html`, `/jpo.html`). Il reprend la note Google (à dater). Aucune garantie d'usage par les IA : fichier à considérer comme un complément, pas une solution.

---

## 5. Performance

### 5.1 Poids des pages

- HTML : 78 à 115 Ko brut, **18 à 24 Ko gzip** (`mod_deflate` déclaré). CSS (45 Ko / 9 Ko gzip) et JS (19 Ko / 5 Ko gzip) sont inlinés dans chaque page : ~14 Ko gzip retéléchargés à chaque page, non mis en cache entre pages. Acceptable pour un site de 10 pages ; pas prioritaire.
- Images référencées par page (HTML + JS) : accueil **2,6 Mo** (17 fichiers, toutes chargées en eager), acting 2,0 Mo, scenario-real 1,9 Mo, tarifs 1,5 Mo, landings **3,0 à 4,6 Mo** (`/stages/` : 26 fichiers). Sur mobile 4G, c'est le premier poste de coût.
- Dossier `uploads/` : 46 fichiers, 6,9 Mo, un seul WebP.

### 5.2 Images les plus lourdes

| Fichier | Poids | Dimensions | Usage | Commentaire |
|---|---|---|---|---|
| hero-tournage-exterieur.jpg | 332 Ko | 1600×1066 | hero landings (JS) | pas de variante mobile |
| Le_Proces_Goldman_Affiche.webp | 332 Ko | 1200×1600 | affiche carrousel | affichée ~300 px de large |
| Dirty-Diffficult-Dangerous.jpg | 310 Ko | 1400×2000 | affiche carrousel | idem |
| Les-invisibles_Deborah_Krey.jpg | 303 Ko | 1448×2048 | affiche carrousel | idem |
| scene-theatre-tension-acteurs… | 296 Ko | 1333×2000 | OG + stage à la une | portrait 2000 px |
| portrait-acteur-costume-lumiere-bleue… | 289 Ko | 1333×2000 | hero `/stages/` | |
| tournage-equipe-terrasse-acteurs… | 254 Ko | 1600×1064 | OG scenario-real, photos | |
| scene-de-bar-acteur-tournage… | 239 Ko | 1600×1066 | accordéon `/stages/` | lazy OK |
| actrice-emotion-stage-initiation… | 238 Ko | 1333×2000 | OG jpo, hero landing | |
| retour-camera-tournage-exterieur… | 232 Ko | 1600×1066 | accordéon `/stages/` | lazy OK |
| Cheap-Thrill_…-min.png | 230 Ko | 441×741 | affiche | **PNG photo** : 5× trop lourd pour sa taille |
| 22Goodbye-Melodie22…-min.png | 172 Ko | 580×820 | affiche | PNG photo |

Treize fichiers dépassent 200 Ko ou 1600 px. Les affiches IMDb (`MV5B…@._V1_.jpg`) ont des noms de fichier illisibles.

### 5.3 Attributs et chargement

- 0 `width`/`height` → ratio non réservé par le navigateur ; la plupart des conteneurs ont un `aspect-ratio` CSS, ce qui limite le CLS (mesuré 0 en local, **non vérifié en ligne**).
- 145 images sur 150 sans `loading="lazy"` ; aucun `decoding="async"` ; aucun `srcset`/`sizes` ; une seule image WebP.
- **Landings** : les images sont injectées par JavaScript (`<img data-img="…">` → `img.src = IMAGES[key].url`). Sans JS (lecteurs non-navigateur, certains crawlers IA, aperçus), **aucune image n'existe** ; le LCP (hero) attend l'exécution du script ; pas de `<noscript>`.
- Polices : Google Fonts externe, **render-blocking**, 8 fontes (Oswald ×4, Archivo ×4) ; `preconnect` présent ; aucune police auto-hébergée, pas de `font-display` maîtrisé (`display=swap` dans l'URL seulement). Dépendance tierce RGPD (fonts.gstatic.com).
- Pas de `preload`/`fetchpriority="high"` sur l'image hero de l'accueil (`scene-a-deux-acteurs…`, 100 Ko).
- Aucun `<link rel="icon">` : chaque visite provoque une requête `/favicon.ico` → 404 (servie avec… la page d'accueil, cf. `ErrorDocument`, soit ~20 Ko gzip inutiles par visite).

### 5.4 Propositions (détaillées en § 7)

Pipeline images dans `build.py` (Pillow déjà utilisé par le générateur) : variantes 480/960/1600 px + WebP, `srcset`/`sizes`, `width`/`height` lus à la construction, `loading="lazy"` hors hero, `preload` du hero ; conversion PNG → JPEG/WebP ; auto-hébergement des polices réduites à 4 fontes ; favicon ; règle Expires `font/woff2`.

---

## 6. Mobile et accessibilité (Playwright, 390×844, réseau externe coupé)

| Constat | Pages | Détail |
|---|---|---|
| Débordement horizontal | aucune (scrollWidth = 390 sur 13/14 ; tarifs 392 px, imperceptible) | Les éléments signalés « hors cadre » sont les bandeaux défilants (`kw-track`, `marquee-track`) masqués par `overflow:hidden` : volontaire. Le tableau du planning (560 px) est dans `.table-wrap{overflow-x:auto}` : scrollable, correct. |
| Menu mobile | OK | ouverture/fermeture, `aria-expanded` mis à jour, liens larges (342×34 px). Capture vérifiée. |
| Cibles tactiles < 24×24 px (WCAG 2.5.8) | toutes | lien du bandeau rouge « Réservez → » : **93×14 px** ; points de carrousel des landings **8×8 px** ; liens email/téléphone/adresse 16-17 px de haut (contact, cours-essai, stages, inscription) ; cases à cocher 18×18 px. |
| Cibles 24-43 px | toutes | 18 à 44 éléments par page (liens de footer 34 px, boutons « Réserver → » 26 px sur planning). Recommandation Google : 48 px, min. 24 px. |
| Contraste < 4,5:1 (texte normal) | 1 à 10 cas par page | étiquettes colorées : `#C88A3E` sur fond clair (2,9:1), `#CF5A54` (3,65:1), `#8A8A8A` « Vacances » (3,45:1), `#4A6FB5` 11 px (3,77:1), rouge `#E0261F` sur fond `#F7F4EE` (4,28:1, très proche), étoiles jaunes (1,85:1, décoratives). Mesure approximative (fond calculé sur l'ancêtre le plus proche). |
| Taille de texte minimale | 11 px | étiquettes « tags » en 11 px uppercase : lisibilité mobile faible. |
| Formulaires | contact, cours-essai, inscription, jpo.html, stages.html | `<label>Prénom</label><input name="prenom">` : **labels non associés** (ni `for`/`id`, ni imbrication) → champs sans nom accessible (lecteurs d'écran, Lighthouse a11y). Les landings utilisent des labels imbriqués : correctes. |
| Structure | contact (h1 → h3), landings (h2 → h4), landings sans `<main>` | sauts de niveaux ; pas de lien d'évitement. |
| Erreurs console | aucune propre au site | seule erreur : chargement de Google Fonts bloqué par l'environnement de test (attendu). Aucune erreur JS, aucune ressource locale manquante. |
| LCP / CLS locaux | LCP 60-720 ms, CLS 0 | **non représentatifs** (disque local, polices absentes) ; à mesurer en ligne. |

---

## 7. Liste priorisée des défauts

Barème : impact 1-5, confiance 1-5, effort 1-5 (1 = < 1 h), risque faible / moyen / élevé. Les fichiers indiqués sont les **sources** (`newsite/…`), jamais `dist/`.

### D1 — La page Tarifs canonique redirige vers un dossier bloqué par robots.txt
- Preuve : `dist/tarifs/index.html` existe → `/tarifs` est un dossier ; `.htaccess` ne réécrit pas un dossier (`!-d`) → `mod_dir` 301 `/tarifs/` ; `robots.txt` : `Disallow: /tarifs/` ; liens internes `tarifs.html` → 301 → 301 → bloqué ; landings → `/tarifs/` bloqué.
- Impact 5 · Confiance 4 (non vérifié en ligne) · Effort 2 · Risque faible · Dépendance : suppression manuelle du dossier `www/tarifs/` sur le serveur au déploiement (un dépôt par écrasement ne supprime pas les dossiers).
- Fichiers : `newsite/build.py` (étape « 2) variante /tarifs/ » et fonction `tarifs_folder_variant`), `newsite/static/.htaccess`, `newsite/static/robots.txt`, `newsite/README.md`, footers des landings (`static/jpo/index.html`, `static/jposr/index.html`, `tools/build_landing_stages.py` via la source jpo).
- Patch :
  ```
  build.py      : supprimer la génération de dist/tarifs/index.html (et tarifs_folder_variant)
  .htaccess     : avant la réécriture interne, ajouter
                  RewriteRule ^tarifs/$ /tarifs [R=301,L]
  robots.txt    : retirer "Disallow: /tarifs/"
  landings      : href="/tarifs/" -> href="/tarifs"
  ```
- Test : build OK ; `curl -sI …/tarifs` = 200 ; `…/tarifs/` = 301 → `/tarifs` ; `…/tarifs.html` = 301 → `/tarifs` (un seul saut) ; inspection d'URL Search Console sur `/tarifs`.

### D2 — Tous les liens internes passent par une redirection 301
- Preuve : `header.html`, `footer.html`, `pages/*.html` écrivent `href="acting.html"` ; `.htaccess` règle 3 redirige `/acting.html` → `/acting` ; landings : `/acting.html`, `/cours-essai.html`… (seuls `jpo.html`/`stages.html` sont exemptés).
- Impact 4 · Confiance 5 · Effort 2 · Risque faible.
- Fichiers : `newsite/build.py` (fonction `inline()`), `newsite/static/jpo/index.html`, `newsite/static/jposr/index.html` (le générateur `/stages/` hérite de jpo).
- Patch (dans `inline()`, après le remplacement des images) :
  ```python
  CLEAN = ("acting","scenario-real","contact","tarifs","planning","cours-essai","inscription")
  page = re.sub(r'href="/?(' + "|".join(CLEAN) + r')\.html', r'href="/\1', page)
  page = page.replace('href="index.html"', 'href="/"')
  ```
  et, dans les deux landings statiques, remplacer `/acting.html` etc. par `/acting` (sed), en conservant `/jpo.html` et `/stages.html`.
- Test : `grep -c 'href="[a-z-]*\.html' dist/*.html` → seuls `jpo.html` et `stages.html` subsistent ; crawl local sans lien cassé ; en ligne, les liens de nav répondent 200 directement.

### D3 — Aucune balise de mesure (GA4 / GTM) sur aucune page
- Preuve : `grep googletagmanager|gtag/js` sur `dist/` → aucun résultat ; `/stages/` ne contient qu'un **commentaire placeholder** (« collez ici votre balise globale ») et des appels `window.gtag` conditionnels. Contrairement à l'hypothèse de départ, il n'y a donc de tag sur aucune page.
- Impact 4 (aucun KPI de conversion mesurable, Phase F impossible) · Confiance 5 · Effort 2 · Risque moyen (RGPD : consentement ou configuration exemptée CNIL).
- Fichiers : `newsite/partials/head.html`, `newsite/static/jpo/index.html`, `newsite/static/jposr/index.html`, `newsite/tools/build_landing_stages.py` (remplacer le placeholder).
- Patch : insertion d'un snippet GTM (ou GA4 en mode consent) juste après `<meta name="robots">` ; événements déjà émis par le JS (`stage_form_success`, `generate_lead`) à exploiter. Coordination avec analytics-qa (plan de mesure) ; **[À VALIDER]** : identifiant de propriété et choix CMP par le propriétaire.
- Test : Tag Assistant / DebugView ; événement reçu après envoi d'un formulaire de test.

### D4 — Doublons d'intention entre pages du site et landings (`/stages.html` vs `/stages/`, `/jpo.html` vs `/jpo/`)
- Preuve : les deux couples sont `index, follow` avec canonical sur eux-mêmes ; mêmes stages, mêmes dates, même formulaire ; `/jpo/` et `/stages/` partagent le H1 ; landings absentes du sitemap et sans lien entrant depuis le site.
- Impact 3 · Confiance 4 · Effort 1 · Risque faible · Décision éditoriale requise (chef de projet / propriétaire) : les landings servent-elles uniquement aux campagnes ?
- Fichiers : `newsite/static/jpo/index.html`, `newsite/static/jposr/index.html`, `newsite/tools/build_landing_stages.py` (ligne `<meta name="robots" content="index, follow">`).
- Patch recommandé (landings = campagnes) : `<meta name="robots" content="noindex, follow">` sur les trois landings ; sinon, variante : `<link rel="canonical" href="https://www.methodacting.fr/stages.html">` sur `/stages/` et `/jpo.html` sur `/jpo/`, et retrait de `/jposr/` ou ajout au sitemap avec contenu différencié.
- Test : `grep -o '<meta name="robots"[^>]*>' dist/*/index.html` ; Search Console → couverture.

### D5 — Données structurées : logo incorrect, Course incomplet, prix non visibles, note auto-déclarée
- Preuve : § 3. `logo` = photo ; `courseMode: "onsite"` ; pas de `courseWorkload` ; `Course.offers.price` 370/350 € absents des pages /acting et /scenario-real ; `aggregateRating` self-serving ; `Offer` orphelin ; landings sans JSON-LD.
- Impact 3 · Confiance 4 · Effort 2 · Risque faible.
- Fichiers : `newsite/build.py` (`ORG`, `course()`, `jsonld()`), `newsite/pages/acting.html` et `scenario-real.html` (afficher « dès 370 €/mois » avec lien tarifs, ou retirer `offers`), landings (ajouter `Organization` + `Event`).
- Patch minimal :
  ```python
  "logo": SITE + "/uploads/logo-method-acting-center.png",   # [À VALIDER] fichier logo
  "courseMode": "Onsite", "courseWorkload": "PT8H"            # [À VALIDER] par année
  "courseSchedule": {"@type":"Schedule","repeatFrequency":"Weekly","repeatCount":30,"duration":"PT4H",…}
  ```
  retirer `aggregateRating` si aucun rafraîchissement n'est planifié ; ajouter `priceRange`, `geo` (coordonnées **[À VALIDER]**), `hasMap` (lien Maps déjà en footer).
- Test : Rich Results Test / Schema Markup Validator sur /acting, /stages.html, /tarifs ; aucune erreur, avertissements documentés.

### D6 — Images : poids, formats, attributs manquants, injection JS sur les landings
- Preuve : § 5. 2,6 Mo d'images eager sur l'accueil, 4,6 Mo sur `/stages/` ; 0 `width/height` ; 5 `loading="lazy"` sur 150 ; PNG photographiques ; aucune variante responsive ; landings sans `src`.
- Impact 4 (CWV mobile, intention « formation acting Paris » majoritairement mobile) · Confiance 4 · Effort 3 · Risque faible (pipeline au build, sources inchangées).
- Fichiers : `newsite/build.py` (nouvelle étape de dérivation d'images avec Pillow : `assets/img/*` → `uploads/{nom}-480.webp|960|1600` ; injection `width`, `height`, `srcset`, `sizes`, `loading="lazy"`, `decoding="async"`), `newsite/pages/*.html` (hero : `fetchpriority="high"` + `<link rel="preload">` dans `head.html` via un placeholder `{{PRELOAD}}`), `newsite/static/jpo/index.html` et `jposr` (remplacer `data-img` par `src` réel + `noscript`), `assets/img/*.png` → JPEG/WebP.
- Test : `build.py` garde-fous OK ; poids total par page < 1 Mo au premier affichage ; PageSpeed Insights mobile avant/après (LCP < 2,5 s, CLS < 0,1).

### D7 — Favicon et icônes absents
- Preuve : aucun `<link rel="icon">`, aucun fichier `favicon.ico` dans `dist/` ; 404 servie avec la page d'accueil (cf. D10).
- Impact 2 (icône générique dans les SERP mobiles, marque) · Confiance 5 · Effort 1 · Risque nul.
- Fichiers : `newsite/static/favicon.ico`, `newsite/static/icon.svg`, `newsite/static/apple-touch-icon.png` (à créer **[À VALIDER]** : logo fourni par le propriétaire), `newsite/partials/head.html` + têtes des landings : `<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" href="/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">`.
- Test : `curl -sI …/favicon.ico` = 200 `image/x-icon` ; icône visible dans l'onglet.

### D8 — Polices Google externes, render-blocking, 8 fontes
- Preuve : `head.html` ligne 23 ; aucune police locale ; aucune règle de cache `woff2`.
- Impact 3 (FCP/LCP, RGPD) · Confiance 4 · Effort 2 · Risque faible.
- Fichiers : `newsite/assets/fonts/` (nouveau, 4 fichiers woff2 : Oswald 500/700, Archivo 400/600 — ou le sous-ensemble réellement utilisé dans `style.css`), `newsite/assets/style.css` (`@font-face` + `font-display: swap`), `newsite/partials/head.html` (retirer Google Fonts, `preload` des 2 fontes du hero), `newsite/build.py` (copier `assets/fonts` → `dist/fonts`), `newsite/static/.htaccess` (`ExpiresByType font/woff2 "access plus 1 year"`), landings (même changement).
- Test : aucune requête vers `fonts.googleapis.com` ; rendu identique (capture avant/après) ; Lighthouse « Eliminate render-blocking resources » disparu.

### D9 — Sitemap : `lastmod` factice, landings absentes
- Preuve : `build.py` `sitemap()` utilise `date.today()` ; 10 URL.
- Impact 2 · Confiance 5 · Effort 1 · Risque nul.
- Fichier : `newsite/build.py`.
- Patch : `lastmod` = date du dernier commit touchant `pages/<slug>.html` (`git log -1 --format=%cs -- pages/slug.html`, repli sur la date de modification du fichier) ; ajouter les landings **si** D4 conclut à leur indexation ; sinon les laisser hors sitemap.
- Test : deux builds successifs sans modification produisent le même `sitemap.xml`.

### D10 — `.htaccess` : page 404 = accueil, pas de www forcé, pas d'en-têtes de sécurité, anciennes URL non redirigées
- Preuve : § 4.4 ; bloc WordPress vide ; `ErrorDocument 404 /index.html`.
- Impact 3 · Confiance 3 (non vérifié en ligne) · Effort 2 · Risque **moyen** (une directive refusée = 500 ; déployer d'abord le `.htaccess` seul, tester, garder l'ancien fichier pour retour arrière immédiat).
- Fichiers : `newsite/static/.htaccess`, `newsite/pages/404.html` (nouvelle page, hors sitemap, `noindex`), `newsite/build.py` (générer `404.html`, l'exclure du sitemap).
- Patch :
  ```apache
  # hôte canonique (à placer après la règle HTTPS)
  RewriteCond %{HTTP_HOST} ^methodacting\.fr$ [NC]
  RewriteRule ^(.*)$ https://www.methodacting.fr/$1 [R=301,L]
  ErrorDocument 404 /404.html
  <IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
  </IfModule>
  ExpiresByType font/woff2 "access plus 1 year"
  ```
  + 301 des anciennes URL une fois la liste obtenue (**[À VALIDER]** export Search Console / Wayback).
- Test : `curl -sI …/inexistant` = 404 avec le contenu de `404.html` ; `curl -sI http://methodacting.fr/` = 301 → `https://www.…` en un saut ; aucun 500.

### D11 — Faute visible « l\'expérience » sur la landing `/stages/`
- Preuve : `dist/stages/index.html` : `<h2 …>Ils ont tenté <span …>l\'expérience.</span></h2>` ; cause : `re.sub` avec chaîne brute `r'…l\'expérience…'` dans `tools/build_landing_stages.py` ligne 68 (le `\'` survit au remplacement).
- Impact 2 (titre H2 visible, crédibilité) · Confiance 5 · Effort 1 · Risque nul.
- Patch : remplacer `l\'expérience` par `l’expérience` (apostrophe typographique, comme dans `"Ils ont tenté"` du contrôle ligne 69) ou passer le remplacement par `lambda m: …`.
- Test : `grep -c "l\\\\'exp" dist/stages/index.html` = 0 ; contrôle `assert "Ils ont tenté" in s` toujours vert.

### D12 — Accessibilité : labels non associés, cibles tactiles, contrastes, hiérarchie des titres
- Preuve : § 6.
- Impact 2-3 · Confiance 5 (labels, tailles) / 4 (contraste, mesure approximative) · Effort 2 · Risque faible.
- Fichiers : `newsite/pages/contact.html`, `cours-essai.html`, `inscription.html`, `jpo.html`, `stages.html` (ajouter `id` aux champs et `for` aux labels, ou imbriquer) ; `newsite/assets/style.css` (`.annce a{padding:6px 0; display:inline-block}` → ≥ 24 px ; `.footer-grid a`, liens contact : `padding:4px 0` ; points de carrousel ≥ 24 px avec zone cliquable ; assombrir `#C88A3E` → `#8E5F1E`, `#CF5A54` → `#B8463F`, `#8A8A8A` → `#6B655C` ; taille mini des tags 12 px) ; `pages/contact.html` (h3 → h2) ; landings (`<main>`).
- Test : relance du script Playwright (0 cible < 24 px, 0 contraste < 4,5:1 hors étoiles) ; Lighthouse Accessibilité ≥ 95.

### D13 — Alt vides et noms de fichiers illisibles sur les affiches de films
- Preuve : 27 `alt=""` sur des affiches ; fichiers `MV5B…@._V1_.jpg`, `8227-…-catalogue.jpg`, `95495ae71c-poster.jpg`.
- Impact 2 · Confiance 5 · Effort 1-2 · Risque faible (renommer = changer les URL d'images, sans enjeu de classement).
- Fichiers : `newsite/pages/index.html`, `acting.html`, `scenario-real.html`, landings ; `newsite/assets/img/` (renommage).
- Patch : `alt="Affiche du film Les Invisibles"` (titre seul ; toute mention « avec [ancien élève] » reste **[À VALIDER]** — le registre n'a aucun ancien élève vérifié) ; renommer en `affiche-les-invisibles.jpg`, etc.
- Test : garde-fou `build.py` (aucune image manquante) ; crawl : 0 alt vide hors images décoratives.

### D14 — Titres et meta descriptions trop longs
- Preuve : § 2 (7 titres > 65 car., 5 descriptions > 160 car.).
- Impact 2 · Confiance 4 · Effort 1 · Risque faible (dépend de content-strategist pour la formulation).
- Fichiers : `newsite/build.py` (`PAGES`), `newsite/static/jpo/index.html`, `jposr`, `tools/build_landing_stages.py`.
- Patch : ex. `/stages.html` → « Stages d'acting à Paris : week-end et intensifs — Method Acting Center » (64 car.) ; `/jposr/` → « Portes Ouvertes Scénario & Réalisation — Method Acting Center Paris » ; descriptions ramenées à 150-160 car. en gardant date/prix vérifiés.
- Test : crawl : titres ≤ 65, descriptions ≤ 160.

### D15 — Open Graph : images portrait et sans dimensions
- Preuve : 5 OG images portrait (acting, tarifs, planning, inscription, jpo, stages) ; pas de `og:image:width/height/alt`.
- Impact 1 · Confiance 5 · Effort 1.
- Fichiers : `newsite/build.py` (`OG_IMAGES`, recadrage 1200×630 à générer au build via Pillow), `partials/head.html` (`og:image:width`, `og:image:height`, `og:image:alt`).
- Test : débogueurs de partage (Facebook, LinkedIn) — aperçu non tronqué.

### D16 — Événements expirés restants dans le JSON-LD et sur les pages
- Preuve : stages du 17-18 oct. 2026 codés en dur dans `build.py` et `pages/stages.html` ; seul le JS masque les cartes (`data-end`) ; le JSON-LD continuera d'annoncer des `Event` passés.
- Impact 2 · Confiance 5 · Effort 2 · Risque faible.
- Fichiers : `newsite/build.py` (filtrer les `event()` dont `endDate < today` au build, ou passer `eventStatus`), `tools/build_landing_stages.py` (même logique sur `SESSIONS`).
- Test : build après la date → l'événement disparaît du JSON-LD et de la landing.

### D17 — CSS/JS inlinés dans chaque page (cache)
- Preuve : ~14 Ko gzip de CSS+JS répétés par page ; `.htaccess` prévoit un cache 1 mois pour CSS/JS qui ne sert à rien.
- Impact 1 · Confiance 5 · Effort 2 · Risque faible. À ne traiter qu'après D6/D8 : externaliser `style.[hash].css` / `site.[hash].js` ou conserver l'inline en minifiant. Non prioritaire.

---

## 8. Résumé

**Dix défauts prioritaires** (ordre de traitement proposé) :
1. D1 — `/tarifs` → 301 vers `/tarifs/`, dossier interdit par robots.txt : la page Tarifs est vraisemblablement non indexable (à confirmer par `curl`).
2. D2 — 100 % des liens internes en `.html` passent par une 301 (navigation, footer, landings).
3. D3 — Aucun tag de mesure sur aucune page (le « gtag » de `/stages/` n'est qu'un commentaire) : aucun KPI possible.
4. D6 — Images : 2,6 à 4,6 Mo par page, pas de lazy loading ni de dimensions, landings sans `src` (images injectées en JS).
5. D4 — `/stages/` vs `/stages.html` et `/jpo/` vs `/jpo.html` indexables en parallèle : cannibalisation, landings orphelines.
6. D5 — JSON-LD : logo = photo, `Course` non conforme aux exigences Google, prix déclarés mais invisibles sur /acting et /scenario-real, note auto-déclarée.
7. D10 — `.htaccess` : 404 servie avec la page d'accueil, pas de www forcé, pas d'en-têtes de sécurité, aucune 301 des anciennes URL WordPress (liste inconnue).
8. D8 — Google Fonts render-blocking (8 fontes, domaine tiers).
9. D7 — Aucun favicon (404 à chaque visite, icône générique en SERP).
10. D12 — Accessibilité : labels de formulaire non associés sur 5 pages, cibles tactiles de 8-17 px, contrastes insuffisants sur les étiquettes.

Puis D11 (faute « l\'expérience » : correction d'une ligne), D9, D13, D14, D15, D16, D17.

**Non vérifié en ligne** (site injoignable depuis l'environnement) : codes HTTP et chaînes de redirection réelles (D1, D2, D10), comportement OVH (`X-Forwarded-Proto`, `DirectorySlash`, `AllowOverride`), statut exact de la 404, TTFB et Core Web Vitals terrain, état d'indexation Search Console, liste des anciennes URL. La commande `curl` du § 1 permet de lever ces incertitudes en quelques minutes.

**Validations propriétaire nécessaires** : fichier logo, identifiant GA4/GTM et politique de consentement, destin des landings (indexables ou non), volumes horaires à figer dans `Course`, coordonnées GPS, titres des films et mentions d'anciens élèves, export Search Console des anciennes URL.

**État du dépôt** : `git status` ne montre que les livrables des agents dans `docs/` (fichiers non suivis) ; **aucun fichier de `newsite/` n'a été modifié**, le build de contrôle a été exécuté dans une copie temporaire et a produit un `dist/` strictement identique.
