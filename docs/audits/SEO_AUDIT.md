# Audit SEO de surface — Method Acting Center

Agent : seo-auditor · Date : 2026-10-12 · Périmètre : `newsite/dist/` (= https://www.methodacting.fr/), sources `newsite/`, `prod-snapshot/`.
Livrables liés : `URL_INVENTORY.md`, `KEYWORD_MAP.md`, `COMPETITOR_MATRIX.md`.

## 1. Résumé exécutif

Le site est un site statique propre (HTML généré par `build.py`, CSS/JS intégrés, 10 pages + 3 landings Ads). Par rapport à l'ancienne prod (`prod-snapshot/` : aucun canonical, aucun JSON-LD, pas de robots.txt/sitemap, images en base64), la version `dist/` a réglé les fondamentaux. Il reste :

- **3 défauts techniques à fort impact et faible effort** : tous les liens internes pointent vers `page.html` et déclenchent une 301 à chaque clic (P01) ; la landing `/stages/` porte **deux canonicals contradictoires** dont un vers `/jpo/` (P02) ; `aggregateRating` issu de Google Business dans le JSON-LD contrevient aux consignes Google sur les avis (P06).
- **Une architecture qui se concurrence elle-même** : 3 pages JPO indexables (`/jpo.html`, `/jpo/`, `/jposr/`), 2 pages stages (`/stages.html`, `/stages/`), 2 pages tarifs (`/tarifs`, `/tarifs/`), sans `noindex` ni hiérarchie (P03-P05).
- **Un déficit de contenu sur les intentions prioritaires** : aucune page n'explique la Méthode (Stanislavski vs Method Acting), aucune page équipe/coachs, aucune réponse aux questions d'admission, prix total non calculé (P18).
- **Des affirmations non vérifiables** (acteurs célèbres, « descendant direct », affiches de films comme preuve d'anciens) qui fragilisent la crédibilité auprès des IA comme des visiteurs (P17).
- **Des citations tierces périmées** (Emagister, Gowork) qui dominent les requêtes de marque avec d'anciens prix et une ancienne adresse (P19).
- **Aucune mesure** : pas de GA4/GTM, balise Ads absente de la landing, pas d'accès Search Console connu (P20).

Ce qui n'a pas pu être vérifié (site injoignable depuis l'environnement, proxy `403`) : codes HTTP réels et chaînes de redirection, indexation réelle (`site:` sans résultat), Core Web Vitals, logs, Search Console, existence/contenu de la page Trustpilot, URLs WordPress héritées. Ces points sont marqués **[non confirmé]**.

## 2. Barème

Impact 1-5 (effet attendu sur visibilité/conversion) · Confiance 1-5 (certitude du constat et de l'effet) · Effort 1-5 (1 = < 1 h) · Risque faible / moyen / élevé (régression ou décision commerciale).

---

## 3. Problèmes priorisés

### P01 — Tous les liens internes déclenchent une redirection 301

- **Preuve** : `partials/header.html:5,12-14,17-20,23` et `partials/footer.html:6,11-22` utilisent `href="acting.html"`, `href="index.html"`, etc. ; idem dans toutes les `pages/*.html` ; les landings utilisent `https://www.methodacting.fr/acting.html` (`dist/jpo/index.html`, `dist/jposr/index.html`, `dist/stages/index.html`). Or `.htaccess:48-49` redirige `/page.html` → `/page` (R=301) et `:38-39` `/index.html` → `/`. Les canonicals, eux, sont en URL propre (`build.py:65-68`). Seuls `/jpo.html` et `/stages.html` échappent à la règle (`.htaccess:44-45`).
- **Effet** : chaque clic interne = 1 redirection (latence, cohérence du PageRank interne diluée, crawl doublé) ; Search Console signalera « page avec redirection » pour toutes les URLs `.html`. **[Codes réels non confirmés en ligne, mais la règle est explicite.]**
- Impact **4** · Confiance **5** · Effort **2** · Risque **faible**
- **Action** (technical-seo) : dans `build.py`, réécrire après assemblage les `href="X.html"` en `href="/X"` (sauf `jpo.html`, `stages.html`, et `index.html` → `/`), y compris avec `?query#ancre` ; dans `static/jpo/index.html`, `static/jposr/index.html` et `tools/build_landing_stages.py`, remplacer les absolus `.html` par les URLs propres. Garder les règles 301 dans `.htaccess` pour les anciens liens externes.
- **Validation** : après build, `grep -c 'href="[a-z-]*\.html' dist/*.html` = 0 hors exceptions ; après déploiement, `curl -I` sur 5 liens internes → 200 direct ; crawl : 0 redirection interne.

### P02 — `/stages/` : deux canonicals, deux meta robots, deux jeux Open Graph

- **Preuve** : `dist/stages/index.html:8` `<link rel="canonical" href="https://www.methodacting.fr/stages/">` et `:15` `<link rel="canonical" href="https://www.methodacting.fr/jpo/">` ; `:9` et `:16` deux `meta robots` ; `:11-13` et `:20-23` deux séries `og:url/og:title/og:description` (la seconde décrit les Portes Ouvertes). Cause : `tools/build_landing_stages.py:25-34` insère un bloc après la meta description sans retirer le bloc d'origine de `static/jpo/index.html:8-17`.
- **Effet** : Google ignore généralement des canonicals contradictoires, ou choisit l'un des deux ; risque que `/stages/` soit considérée comme un doublon de `/jpo/` (donc jamais classée) et que les partages sociaux affichent le titre JPO.
- Impact **4** · Confiance **5** · Effort **1** · Risque **faible**
- **Action** : dans le générateur, supprimer (regex) les lignes canonical/robots/og d'origine avant d'insérer les nouvelles ; ajouter une assertion `s.count('rel="canonical"') == 1`.
- **Validation** : `grep -c 'rel="canonical"' dist/stages/index.html` = 1 ; inspection d'URL Search Console : « canonical déclarée par l'utilisateur » = `/stages/`.

### P03 — Trois pages « Portes Ouvertes » indexables qui se cannibalisent

- **Preuve** : `/jpo.html` (site, dans le sitemap), `/jpo/` et `/jposr/` (landings Ads, hors sitemap mais `index, follow`, `dist/jpo/index.html:9`, `dist/jposr/index.html:9`) ; `/jpo/` et `/jposr/` partagent 24,9 % de leurs 6-grammes (39,9 % du plus petit) ; `/jpo/` et `/stages/` ont le même H1 « Vous voulez devenir acteur ? ». Titles : 72 et 90 caractères.
- **Effet** : pour « portes ouvertes method acting center », Google doit arbitrer entre 3 URLs ; les landings, non reliées au site, ont peu de signaux et peuvent prendre la place de `/jpo.html` ou l'inverse selon les semaines (fluctuation).
- Impact **3** · Confiance **4** · Effort **2** · Risque **moyen** (décision Ads)
- **Action** : **décision propriétaire**. Recommandation : `<meta name="robots" content="noindex, follow">` sur `/jpo/`, `/jposr/`, `/stages/` (sans effet sur Google Ads, qui n'exige pas l'indexation) ; sinon canonical de `/jpo/` → `/jpo.html`, `/jposr/` → `/scenario-real` est discutable (contenus différents) donc préférer noindex. Différencier les H1.
- **Validation** : Search Console → les 3 landings sortent de l'index en 2-6 semaines ; `/jpo.html` seule classée sur la requête de marque + JPO.

### P04 — `/stages.html` vs `/stages/` : deux pages pour la même intention

- **Preuve** : `/stages/` (landing, orpheline : aucun lien entrant interne, cf. inventaire) a un title mieux ciblé (`Stages d'acting à Paris — Week-end & intensifs · Method Acting Center`, 69 car.) que la page du site (`Stages d'acting & de scénario — week-end et intensifs — Method Acting Center Paris`, 82 car., tronqué). Les deux listent les mêmes 6 stages avec les mêmes dates/prix ; recouvrement 13,5 % du plus petit hors boilerplate.
- Impact **3** · Confiance **4** · Effort **2** · Risque **moyen**
- **Action** : noindex sur `/stages/` (cf. P03) ; reprendre pour `/stages.html` le title de la landing ; H1 contenant « stage d'acting » ; les dates/prix des deux pages doivent venir d'une source unique (`SESSIONS` de `build_landing_stages.py` → à remonter dans `build.py`).
- **Validation** : une seule URL « stages » dans l'index ; position suivie sur « stage acting paris » (Search Console).

### P05 — `/tarifs/` : doublon bloqué par robots.txt et pourtant lié

- **Preuve** : `dist/tarifs/index.html` = copie à 100 % (862 shingles identiques) avec canonical `/tarifs` ; `static/robots.txt:8` `Disallow: /tarifs/` ; les 3 landings lient `https://www.methodacting.fr/tarifs/` (`dist/jpo/index.html`, `dist/jposr/index.html`, `dist/stages/index.html`). L'ancienne prod servait `/tarifs/index.html` **sans canonical** (`prod-snapshot/tarifs/index.html`) : l'URL a pu être indexée et, bloquée aujourd'hui, Google ne peut plus lire la canonical pour la fusionner.
- Impact **2** · Confiance **4** · Effort **1** · Risque **faible** (vérifier qu'aucune URL finale Ads ne pointe vers `/tarifs/`)
- **Action** : supprimer la variante dans `build.py:187-190`, ajouter `RewriteRule ^tarifs/?$ /tarifs [R=301,L]` dans `.htaccess`, retirer le `Disallow`, corriger les liens des landings.
- **Validation** : `curl -I https://www.methodacting.fr/tarifs/` → 301 vers `/tarifs` ; Search Console : `/tarifs/` « page avec redirection ».

### P06 — `aggregateRating` issu de Google Business dans le JSON-LD Organization

- **Preuve** : `build.py:105` `"aggregateRating": {"ratingValue": "4.8", "reviewCount": "98"}` sur l'entité `EducationalOrganization/LocalBusiness`, répété sur les 11 pages ; valeur = note de la fiche Google (FACT-001). Google : « les notes doivent provenir directement des utilisateurs… n'utilisez pas les avis agrégés d'autres sites » et les avis « auto-attribués » sur `LocalBusiness`/`Organization` ne sont pas éligibles aux extraits enrichis.
- **Effet** : aucun rich result possible ; risque d'action manuelle « données structurées trompeuses » (faible probabilité, impact fort). Le badge visible « 4,8/5 – 98 avis Google » avec lien sortant est, lui, légitime.
- Impact **3** · Confiance **4** · Effort **1** · Risque **faible** (retrait)
- **Action** : retirer `aggregateRating` du graphe ; conserver le badge HTML. Même logique pour tout `Review` futur : ne baliser que des avis collectés par le site lui-même.
- **Validation** : test des résultats enrichis Google → aucun avertissement « avis » ; `grep aggregateRating dist/*.html` = 0.

### P07 — Pas de favicon, `logo` d'organisation = photo

- **Preuve** : aucun `rel="icon"` dans `partials/head.html` ; aucun `favicon.*` dans `dist/` ni `prod-snapshot/` ; `build.py:88-89` `logo` = `scene-a-deux-acteurs-method-acting-center.jpg` (photo de scène).
- **Effet** : icône générique dans les SERP mobiles et les onglets ; Google peut ne pas afficher de logo dans le panneau de connaissance ; 404 `/favicon.ico` à chaque session.
- Impact **2** · Confiance **5** · Effort **1** · Risque **faible**
- **Action** : ajouter `favicon.ico` (48×48), `icon.svg`, `apple-touch-icon.png` (180×180) dans `static/` + balises dans `head.html` ; fournir un vrai logo (PNG/SVG fond uni ≥ 112×112) et le référencer dans `logo`.
- **Validation** : `curl -I /favicon.ico` → 200 ; test résultats enrichis « Logo ».

### P08 — Titles trop longs ou sans les termes de recherche

- **Preuve** : longueurs : `/jposr/` 90, `/stages.html` 82, `/` 72, `/jpo.html` 72, `/jpo/` 72, `/scenario-real` 72 (troncature probable > 60-65) ; `/tarifs` 35, `/contact` 36, `/planning` 37, `/inscription` 40 (espace inutilisé). `/` et `/acting` ne contiennent ni « école d'acting », ni « cinéma » ; `/stages.html` ne contient pas « Paris » avant la marque. H1 : « Le talent, ça s'apprend. », « Apprendre à jouer vrai. », « Des tarifs clairs. » — aucun H1 ne porte un mot-clé de requête (sauf `/jpo/`-`/stages/` « devenir acteur »).
- Impact **3** · Confiance **4** · Effort **1** · Risque **faible**
- **Action** (content-strategist + technical-seo, via `PAGES` dans `build.py:41-62`) : propositions à valider — `/` « École d'acting à Paris : acteur, scénariste, réalisateur | Method Acting Center » ; `/acting` « Formation acteur cinéma à Paris — Méthode Stanislavski | Method Acting Center » ; `/stages.html` « Stages d'acting à Paris — week-end & intensifs | Method Acting Center » ; `/tarifs` « Tarifs formation acteur & scénario à Paris | Method Acting Center ». Garder les H1 de marque mais ajouter un sous-titre H2 descriptif en haut de page, ou enrichir le H1.
- **Validation** : longueurs 50-65 ; CTR Search Console avant/après sur 8 semaines.

### P09 — Meta descriptions hors gabarit ou non conformes au contenu

- **Preuve** : `/stages/` 205 car., `/inscription` 194, `/jposr/` 181, `/jpo.html` 179, `/scenario-real` 178 ; `/planning` 86. `/tarifs` promet « offres à la rentrée » (`build.py:53`) alors que la page n'en décrit aucune.
- Impact **1** · Confiance **5** · Effort **1** · Risque **faible**
- **Action** : 120-155 caractères, une promesse vérifiable par page (prix « dès », dates, gratuit).
- **Validation** : script de contrôle dans `build.py` (assert longueur) ; aperçu SERP.

### P10 — Images : alt faibles, pas de dimensions, pas de lazy-loading, formats lourds

- **Preuve** : `pages/acting.html:39,44,49` alt « Déclencher », « Maîtriser », « Reproduire » (le 3e H3 dit « Composer », `:50`) ; `pages/scenario-real.html:138-144` 7 × « Film réalisé par un ancien du programme » avec fichiers `MV5B….jpg` (IMDb) ; landings : 8 à 11 `<img data-img …>` sans attribut `alt` (`dist/jpo/index.html`, `dist/jposr/index.html`, `dist/stages/index.html`) ; **0** attribut `width/height` sur les 14 pages ; `loading="lazy"` sur 5 images seulement (landing stages) ; `uploads/` = 6,9 Mo, hero JPEG 90-340 Ko, 1 seul WebP, aucun `srcset`.
- **Effet** : CLS et LCP probablement dégradés **[non mesuré]** ; images non décrites pour Google Images et les lecteurs d'écran.
- Impact **3** · Confiance **3** · Effort **3** · Risque **faible**
- **Action** : alt descriptifs (sujet + contexte, ≤ 125 car.) ; `width`/`height` générés par `build.py` (PIL est déjà utilisé dans `build_landing_stages.py`) ; `loading="lazy"` hors hero ; variantes WebP + `srcset` ; renommer les fichiers IMDb.
- **Validation** : PageSpeed Insights mobile après déploiement (LCP < 2,5 s, CLS < 0,1) ; `grep -c 'alt=""' ` limité aux doublons `aria-hidden`.

### P11 — Performance : CSS/JS intégrés sur chaque page + Google Fonts bloquante

- **Preuve** : `partials/head.html:21-24` charge Google Fonts (2 familles, 7 graisses) en CSS bloquant ; `build.py:33-38` intègre 46 Ko de CSS et 20 Ko de JS dans chaque page (HTML 77-115 Ko, non cacheable entre pages) ; `.htaccess:81` cache HTML 1 h.
- Impact **2** · Confiance **3** · Effort **2** · Risque **faible**
- **Action** : auto-héberger les polices (woff2, `font-display: swap`, `preload` des 2 fichiers utilisés) ; envisager CSS/JS externes versionnés (`style.abc123.css`) avec cache 1 an — à arbitrer : l'intégration actuelle évite 2 requêtes mais empêche le cache.
- **Validation** : Lighthouse mobile avant/après ; taille HTML < 40 Ko.

### P12 — `ErrorDocument 404 /index.html` : page d'accueil servie en cas d'erreur

- **Preuve** : `static/.htaccess:65`. Apache conserve normalement le statut 404 pour un `ErrorDocument` local, mais l'utilisateur voit l'accueil sans message, et `/acting/` (slash final) ou toute faute d'URL atterrit sur l'accueil. **[Statut réel non confirmé.]**
- Impact **2** · Confiance **3** · Effort **1** · Risque **faible**
- **Action** : page `404.html` dédiée (message + liens) avec `noindex` ; vérifier le statut avec `curl -I /url-inexistante`.
- **Validation** : statut 404 + contenu dédié ; Search Console « soft 404 » = 0.

### P13 — Anciennes URLs WordPress sans plan de redirection

- **Preuve** : `.htaccess:57-61` section « Redirections 301 des anciennes URLs WordPress (à compléter) » vide ; le commentaire `:3` confirme un ancien WordPress ; Emagister/Spectable référencent l'école depuis 2017 (liens entrants probables vers d'anciennes URLs) ; `prod-snapshot/` ne contient plus ces URLs.
- Impact **3** · Confiance **2** (inconnu sans données) · Effort **2** · Risque **faible**
- **Action** : **propriétaire** : exporter Search Console (Pages → « Introuvable (404) » + « Explorée, non indexée »), logs OVH 90 jours, et la liste des backlinks (Search Console → Liens) ; technical-seo écrit les 301 une à une vers la page équivalente (jamais tout vers l'accueil).
- **Validation** : 404 en baisse dans Search Console ; `curl -I` sur chaque ancienne URL → 301 → 200.

### P14 — Canonicalisation d'hôte non forcée (www / non-www)

- **Preuve** : `.htaccess:27-30` ne force que HTTPS ; aucune règle `methodacting.fr` → `www.methodacting.fr`. Les canonicals corrigent côté Google, mais pas côté liens/outils. **[Comportement OVH réel non confirmé.]**
- Impact **2** · Confiance **2** · Effort **1** · Risque **faible**
- **Action** : vérifier `curl -I https://methodacting.fr/` et `http://` ; ajouter la règle si nécessaire.

### P15 — `lastmod` du sitemap = date de build pour toutes les pages

- **Preuve** : `build.py:159-162` `today` pour les 10 URLs.
- **Effet** : Google ignore `lastmod` quand il est systématiquement « aujourd'hui » ; perte d'un signal utile pour les pages datées (planning, stages).
- Impact **1** · Confiance **4** · Effort **2** · Risque **faible**
- **Action** : `git log -1 --format=%cI -- pages/<slug>.html` (et partials) pour calculer la vraie date.

### P16 — Incohérence pédagogique « Composer » vs « Reproduire »

- **Preuve** : `pages/acting.html:50` 3e temps = « Composer » ; `pages/index.html:61` et `pages/tarifs.html:80` « déclencher, maîtriser et reproduire » ; `static/llms.txt:5`, `build.py:47` (meta description de `/acting`), landings `/jpo/` et `/stages/` H3 « Reproduire ».
- **Effet** : les IA et les visiteurs reçoivent deux descriptions de la même méthode ; nuit à la vérifiabilité.
- Impact **2** · Confiance **5** · Effort **1** · Risque **faible** (choix propriétaire)
- **Action** : le propriétaire tranche la formulation officielle (FACTS_REGISTER § Méthodes) ; appliquer partout.

### P17 — Affirmations non vérifiables ou à risque

- **Preuves** :
  - `pages/acting.html:8` « La méthode de Marlon Brando, Meryl Streep, Joaquin Phoenix, Leonardo DiCaprio, Jack Nicholson… » — attribution contestable (formation de ces acteurs hétérogène) et non sourcée.
  - `pages/index.html:87,156`, `pages/acting.html:34` « Method Acting Center en est le descendant direct » (de Stanislavski) — invérifiable.
  - `pages/scenario-real.html:32,37` « quasi inexistant en France », « notion rare en France » ; `pages/jpo.html:80` « ce que presque aucune école ne propose » — affirmations concurrentielles sans source (CLAUDE.md § 6 : ne pas créer de fausses comparaisons).
  - `pages/index.html:206-213`, `pages/acting.html:165-172` : affiches de *Quantum of Solace*, *Martyrs*, *Le Procès Goldman*, *Les 7 vies de Léa*, *Sans répit*, *Les Invisibles*, *Dirty Difficult Dangerous*, *Ni chaînes ni maîtres* sous « Nos anciens jouent dans des films… » : aucun nom d'ancien élève, aucune source ; droits de reproduction des affiches non documentés ; FACTS_REGISTER classe les anciens élèves « À confirmer ».
  - Badge « Avis vérifiés Trustpilot » sur 8 pages + `sameAs` Trustpilot (`build.py:98`) : profil **[non confirmé]**.
- **Effet** : crédibilité (E-E-A-T), risque juridique (droit à l'image des affiches, publicité comparative), et pour les IA : énoncés non recoupables = non repris.
- Impact **3** · Confiance **4** · Effort **2** · Risque **moyen** (éditorial/juridique)
- **Action** : **propriétaire** valide ou retire chaque énoncé ; remplacer le carrousel par une section « anciens élèves » nominative avec consentement et lien vérifiable (IMDb/Unifrance), ou le retirer ; sourcer la filiation (ouvrage du fondateur, formation NY) si validée.
- **Validation** : chaque affirmation publique a une ligne dans FACTS_REGISTER avec statut « Vérifié ».

### P18 — Pages manquantes pour les intentions prioritaires

- **Preuve** : croisement `KEYWORD_MAP.md` : aucune page pour (a) « la Méthode » expliquée (intention 8 ; requêtes « cours stanislavski paris », « différence stanislavski method acting ») ; (b) équipe / coachs / fondateur (le site dit « David, fondateur » ; sources tierces indiquent David Barrouk, auteur chez Bloomsbury — **à valider**) ; (c) FAQ admission (âge, bac, audition, niveau, CPF, débutants) ; (d) jeu face caméra (contenu dispersé sur 3 pages) ; (e) anciens élèves vérifiables ; (f) coût total annuel (`/tarifs` n'additionne pas 370 × 9 + 200).
- Impact **4** · Confiance **3** · Effort **4** · Risque **faible** (contenu validé par le propriétaire)
- **Action** (content-strategist) : briefs pour `/la-methode`, `/equipe` (ou section), FAQ sur `/acting`, `/scenario-real`, `/inscription` (avec `FAQPage` seulement si visible), bloc « Acting caméra » consolidé, section « ils ont étudié ici » nominative ; ajouter le total annuel sur `/tarifs`. Aucun contenu publié sans ligne « Vérifié » au registre.
- **Validation** : chaque nouvelle page a une requête cible, un title unique, ≥ 2 liens entrants, et une entrée sitemap ; suivi impressions Search Console.

### P19 — Citations tierces périmées (NAP et prix)

- **Preuve** : Emagister (`emagister.fr/formation_method_acting_center-cen-97852.htm`) : fiches 2017/2018, « 250 €/mois », « 1 500 € HT », « 3 jours d'essai gratuits » ; Gowork : « 105 B rue de Tolbiac » ; evous : 93 av. d'Italie (OK). Sur la requête « formation direction d'acteurs paris », c'est la fiche Emagister qui ressort, pas le site.
- **Effet** : les IA qui recoupent plusieurs sources voient des prix et adresses contradictoires ; signal local (NAP) incohérent.
- Impact **3** · Confiance **4** · Effort **2** · Risque **faible**
- **Action** (digital-pr, avec accord propriétaire) : mettre à jour ou faire retirer les fiches Emagister/Spectable/Gowork ; créer/mettre à jour les fiches Onisep, L'Étudiant, Diplomeo, maformation (sources qui dominent les SERP) avec les mêmes données que FACTS_REGISTER ; demander l'ajout de l'école dans le guide evous.
- **Validation** : recherche de marque : 0 résultat avec ancienne adresse/prix en page 1.

### P20 — Aucune mesure en place

- **Preuve** : aucune balise GA4/GTM/Ads dans `partials/head.html` ni dans les landings ; `dist/stages/index.html:14` « collez ici votre balise globale » ; le `dataLayer.push` et `gtag('event','generate_lead')` (`build_landing_stages.py:478-484`) ne parlent à rien. Pas d'accès Search Console connu.
- Impact **3** · Confiance **4** · Effort **2** · Risque **faible** (RGPD : bandeau de consentement requis pour GA4)
- **Action** (analytics-qa + propriétaire) : vérifier la propriété Search Console et Bing Webmaster ; installer GTM + GA4 avec consentement (ou solution exemptée CNIL), balise de conversion Ads sur les 4 formulaires ; exporter l'état initial avant toute modification SEO.
- **Validation** : événements `generate_lead` visibles ; rapport Search Console exporté dans `docs/analytics/`.

### P21 — Hiérarchie de titres et H1 dupliqués

- **Preuve** : `pages/contact.html:16,26` H3/H4 directement sous H1 ; `/jpo/` et `/stages/` H1 identique « Vous voulez devenir acteur ? » ; `pages/planning.html:217` H2 de transition sans contenu.
- Impact **1** · Confiance **4** · Effort **1** · Risque **faible**
- **Action** : H2 avant H3 ; H1 distincts par page.

### P22 — Dates codées en dur et événements passés

- **Preuve** : « 17 & 18 octobre » dans `pages/stages.html:5,28`, `pages/tarifs.html:46,188`, `pages/planning.html:57`, landings `/jpo/` (H3 « Prochain stage : 17 & 18 octobre »), `/stages/` (title/desc) ; JSON-LD `Event` du 17-18/10 dans `build.py:141` restera après l'événement ; « Septembre 2026 (en cours) » `pages/inscription.html:194` ; « Vous avez raté les Portes Ouvertes ? » `pages/index.html:30`, `pages/cours-essai.html:11`.
- **Effet** : contenu périmé dès le 19/10/2026 sur 6 pages ; `Event` passés = données structurées non conformes.
- Impact **2** · Confiance **4** · Effort **2** · Risque **faible**
- **Action** : source unique des sessions dans `build.py` (reprendre `SESSIONS`), calcul du « prochain stage » au build, filtrage des `Event` dont `endDate` < aujourd'hui, et copie intemporelle.
- **Validation** : rebuild après une date passée → aucune mention.

### P23 — Points mineurs

| Constat | Preuve | Impact/Conf./Effort | Action |
|---|---|---|---|
| Horaires d'ouverture dans le JSON-LD mais pas dans le HTML | `build.py:100-104` vs `pages/contact.html` | 1 / 4 / 1 | Afficher les horaires sur `/contact` et en footer |
| `FAQPage` sur `/tarifs` : plus d'extrait enrichi pour ce type de site depuis 08/2023 | `build.py:151-155` | 1 / 5 / 0 | Garder (inoffensif), ne pas en attendre de gain |
| Liens « avis Google » vers une recherche Google au lieu de la fiche | `pages/*.html` `google.com/search?q=avis+…` | 1 / 4 / 1 | Lier l'URL de la fiche (Place ID / `g.page`) |
| URLs paramétrées liées en interne (`stages.html?stage=a`, `inscription.html?programme=acting`) | `pages/tarifs.html:40,89,110,189`, `pages/planning.html` | 1 / 4 / 1 | Acceptable (canonical) ; préférer des ancres sans paramètre quand possible |
| Bandeaux « mots-clés » défilants `aria-hidden` | `pages/index.html:42-47` et équivalents | 1 / 3 / 1 | Décoratif ; ne pas y ajouter de termes non présents ailleurs |
| PDF planning indexable sans `noindex` | `/uploads/planning-hebdomadaire.pdf` | 1 / 3 / 1 | `X-Robots-Tag: noindex` sur les PDF si la page `/planning` doit primer |
| Avis Google reproduits avec noms des auteurs | 44 cartes sur le site | 1 / 3 / 1 | Contenu public, mais CLAUDE.md demande consentement : propriétaire à trancher |
| Pas de contenu anglais malgré ateliers « in English » | — | 2 / 2 / 3 | Conditionner à une demande constatée |
| `llms.txt` présent | `static/llms.txt` | — | Maintenir synchronisé ; aucune garantie d'usage |

---

## 4. Points conformes à conserver

- Une URL canonique propre par page, HTTPS forcé, `robots.txt` ouvert aux robots IA, sitemap valide, `lang="fr"`, viewport, 1 H1 par page, Open Graph/Twitter complets, JSON-LD `Organization` complet (adresse, téléphone, horaires, sameAs), `Course` cohérent avec les volumes affichés sur `/inscription`, `Event` cohérents avec `/planning`, `llms.txt` à jour, NAP identique sur toutes les pages, formulaires sans backend exposé (Web3Forms), poids d'images raisonnable pour un site vitrine, contenu réel et détaillé (programmes nommés par atelier) — supérieur à la plupart des concurrents observés.

## 5. Ce qui n'a pas pu être vérifié

| Sujet | Raison | Comment le vérifier |
|---|---|---|
| Codes HTTP, chaînes de redirection, www/non-www, 404 | site injoignable (proxy 403) | `curl -I` sur 20 URLs depuis un poste externe ; crawl complet |
| Indexation réelle, pages héritées WordPress, requêtes, CTR | pas d'accès Search Console ; `site:` vide dans l'outil | propriétaire ajoute un accès Search Console (lecture) |
| Core Web Vitals, LCP/CLS | pas de mesure possible | PageSpeed Insights / CrUX après déploiement |
| Profil Trustpilot (existence, nombre d'avis) | réseau | ouvrir https://fr.trustpilot.com/review/methodacting.fr |
| Sites concurrents officiels (prix 2026-2027) | réseau | revérifier chaque ligne de `COMPETITOR_MATRIX.md` |
| Fiches Onisep/L'Étudiant/Diplomeo de l'école | réseau | recherche directe sur chaque plateforme |
| Fiche Google Business (catégories, attributs, photos, Q&R) | non transmise | export par le propriétaire |

## 6. Décisions qui nécessitent le propriétaire

1. Sort des landings Ads (`noindex` recommandé) et de `/tarifs/` (301) — vérifier les URLs finales des campagnes.
2. Formulation officielle de la Méthode (Composer vs Reproduire) et de sa filiation (Stanislavski / Strasberg / Actors Studio) ; autorisation de citer le fondateur (nom complet, parcours, ouvrages).
3. Maintien ou retrait : liste d'acteurs célèbres, « descendant direct », « quasi inexistant en France », carrousels d'affiches ; liste nominative d'anciens élèves avec consentement.
4. Statut à afficher : certification (aucune ?), financement CPF (non ?), diplôme délivré.
5. Avis Trustpilot : profil réel ? sinon retirer le badge.
6. Accès Search Console, Google Business, Ads ; installation d'une mesure avec consentement.
7. Mise à jour des fiches tierces (Emagister, Gowork, Spectable, Onisep, L'Étudiant).

## 7. Ordre d'exécution recommandé

| Vague | Items | Agent | Pré-requis |
|---|---|---|---|
| 1 (technique, < 1 jour) | P02, P06, P07, P09, P15, P21 ; P01 (build) | technical-seo | aucun |
| 2 (décisions) | P03, P04, P05, P16, P17, P22 | propriétaire → technical-seo / content-strategist | décisions § 6 |
| 3 (contenu) | P08, P18, P10 (alt) | content-strategist, technical-seo | FACTS_REGISTER complété |
| 4 (hors site) | P19, P13 | digital-pr, technical-seo | accès Search Console, accord propriétaire |
| 5 (mesure/perf) | P20, P10 (perf), P11, P12, P14 | analytics-qa, technical-seo | déploiement + accès en ligne |
