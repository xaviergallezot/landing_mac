# Baseline — état initial de la mesure

Agent : analytics-qa · Date : 2026-10-12 · Mode : audit en lecture seule
(aucun fichier de `newsite/` modifié).

Périmètre : ce qui est **réellement présent dans le code** du dépôt
(`newsite/` sources et `newsite/dist/` = production), plus les accès et
limites connus. Aucune donnée de trafic, de position ou de conversion
n'est disponible dans cet environnement : **aucune valeur n'est
inventée**, les KPI restent « À mesurer » dans `KPI_DASHBOARD.md`.

## 1. Résumé

| Question | Réponse (vérifiée dans le code) |
|---|---|
| Un outil d'analytics est-il chargé ? | **Non.** Aucun snippet GA4, Google Tag Manager, Google Ads, Matomo, Plausible, Clarity, Hotjar ou pixel Meta dans `newsite/` (hors `prod-snapshot/`) ni dans `newsite/dist/`. |
| Les formulaires sont-ils mesurés ? | **Partiellement, et nulle part.** Tous les formulaires envoient un email via Web3Forms (pas de tableau de bord). Seule la landing `/stages/` pousse un événement `dataLayer` / `gtag` — sans conteneur chargé, il n'est envoyé à aucun outil. |
| Existe-t-il une référence antérieure (trafic, positions) ? | **Inconnue depuis le dépôt.** À demander au propriétaire (Search Console, GA4 éventuel, Google Ads). Si rien n'existe, la mesure démarre à la date ci-dessous. |
| Date de départ de la mesure | **2026-10-12** (date de l'audit). Toute donnée collectée avant cette date, si elle existe, décrit l'ancien site (voir § 6). |
| Site joignable depuis l'environnement ? | **Non.** Codes HTTP, redirections, indexation et Core Web Vitals terrain ne peuvent pas être vérifiés ici. |

## 2. Inventaire des outils de mesure présents dans le code

### 2.1 Recherches effectuées (preuves)

Motifs recherchés dans `newsite/` (sources et `dist/`, hors `prod-snapshot/`) :
`googletagmanager`, `gtag/js`, `G-XXXXXXXX`, `AW-XXXXXXXX`, `GTM-XXXX`, `UA-`,
`dataLayer`, `gtag(`, `matomo`, `_paq`, `plausible`, `clarity`, `hotjar`, `fbq(`, `umami`.

Résultat : les seules occurrences sont dans le générateur de la landing
stages et dans sa sortie. Le snapshot de l'ancienne prod
(`newsite/prod-snapshot/`) ne contient lui non plus aucun identifiant
GA / GTM / Ads : l'ancien site statique (août–octobre 2026) n'était
donc pas mesuré non plus. Pour la période WordPress antérieure à
août 2026, le dépôt ne permet pas de conclure.

### 2.2 Ce qui existe

| Élément | Fichier : ligne | Portée | Où vont les données |
|---|---|---|---|
| Formulaire de contact (`contact-form`) → Web3Forms | `newsite/assets/site.js:83-118` (clé publique ligne 11) ; page `newsite/pages/contact.html:33` | `/contact` | Email au propriétaire. Sujet : « Nouveau message — site Method Acting Center ». |
| Formulaire JPO du site (`jpo-form`) → Web3Forms | `newsite/assets/site.js:134-181` ; page `newsite/pages/jpo.html:174` | `/jpo.html` | Email. Sujet : « Inscription JPO — Prénom Nom ». |
| Formulaire cours d'essai (`essai-form`) → Web3Forms via `bindForm` | `newsite/assets/site.js:184-226` ; page `newsite/pages/cours-essai.html:164` | `/cours-essai` | Email. Sujet : « Cours d'essai — Prénom Nom ». |
| Formulaire stages du site (`stages-form`) → Web3Forms via `bindForm` | `newsite/assets/site.js:227-232` ; page `newsite/pages/stages.html:212` | `/stages.html` | Email. Sujet : « Réservation stage — Prénom Nom ». |
| Formulaire inscription (`inscription-form`) → Web3Forms via `bindForm` | `newsite/assets/site.js:281-286` ; page `newsite/pages/inscription.html:159` | `/inscription` | Email. Sujet : « Demande d'inscription — Prénom Nom ». |
| Landing JPO acteurs (`booking-form`) → Web3Forms | `newsite/static/jpo/index.html:660` (form), `:813` (clé), `:1099-1114` (envoi) | `/jpo/` | Email. Aucun événement de conversion. |
| Landing JPO scénario (`booking-form`) → Web3Forms | `newsite/static/jposr/index.html:643` (form), `:796` (clé), `:1078-1093` (envoi) | `/jposr/` | Email. Aucun événement de conversion. |
| Landing stages (`stages-form`) → Web3Forms **+ `dataLayer.push({event:"stage_form_success", stages, stage_count})` + `gtag("event","generate_lead", …)` si `window.gtag` existe** | Générateur `newsite/tools/build_landing_stages.py:478-483` (fonction `track`), `:490-507` (payload) ; sortie `newsite/dist/stages/index.html:1021-1026` | `/stages/` | Email (avec champs « Campagne » = gclid/gbraid/wbraid/utm_* et « Page » = URL) ; **l'événement JS n'est transmis à aucun outil** car aucun gtag.js / GTM n'est chargé. Un commentaire HTML invite à coller la balise : `newsite/tools/build_landing_stages.py:33` → `newsite/dist/stages/index.html:14`. |
| Champ « Comment nous a connus » (`name="source"`) avec l'option **« Recherche IA (ChatGPT, etc.) »** | `newsite/pages/contact.html:57-79` ; présent aussi dans `cours-essai.html:199`, `inscription.html:220`, `stages.html:238`, `jpo.html:192`, les deux landings JPO et la landing `/stages/` | Tous les formulaires | Email. **Seule source d'attribution existante** (déclarative) : permet de compter les demandes attribuées à Google, aux IA, aux réseaux, au bouche-à-oreille. |
| Honeypot anti-spam `botcheck` | `newsite/assets/site.js:103, 171, 209` ; champ `newsite/pages/contact.html:34` | Tous les formulaires | Filtrage Web3Forms. Pas de captcha. |
| Paramètres d'URL de pré-sélection `?stage=` et `?programme=` | `newsite/assets/site.js:252-258, 267-279` | `/stages.html`, `/inscription` | Pas de mesure, mais ces paramètres identifient la provenance d'un clic (landing → page) si un jour une analytics lit `page_location`. |

### 2.3 Ce qui n'existe pas

- Aucun chargement de `gtag.js`, GTM, GA4, Google Ads (`AW-`), Matomo, Plausible ou autre.
- Aucun bandeau de consentement / gestion des cookies (recherche `cookie`, `consent`, `rgpd`, `gdpr`,
  `confidentialit`, `mentions l` dans `pages/`, `partials/`, `assets/site.js`, landings : **0 résultat**).
  Conséquence : il n'y a **ni page de politique de confidentialité ni mentions légales** dans les
  sources (point à traiter avant tout ajout de mesure, voir `MEASUREMENT_PLAN.md`).
- Aucun suivi des clics `tel:`, `mailto:`, WhatsApp (`https://wa.me/qr/…`), ni des CTA.
  Liens concernés : `newsite/partials/footer.html:26-28`, `newsite/pages/contact.html:18-20`,
  `cours-essai.html:161`, `inscription.html:156, 288`, `stages.html:209`, landings `:778-780` / `:761-763`.
- Aucun suivi des clics sortants (avis Google via `share.google` et `maps.app.goo.gl`, Trustpilot,
  réseaux sociaux).
- Aucun identifiant de conversion Google Ads bien que trois landings (`/jpo/`, `/jposr/`, `/stages/`)
  soient décrites comme landings Google Ads dans `docs/PROJECT_BRIEF.md`. Si des campagnes tournent,
  leurs conversions ne sont pas mesurées côté site (sauf par email + champ « Campagne » sur `/stages/`).
- Aucun test automatisé hormis les assertions de `newsite/build.py:209-222`.
- Aucun journal serveur, aucun export Search Console, GA4 ou Ads dans le dépôt.

## 3. Formulaires : ce que la réception par email permet de mesurer

Web3Forms n'offre pas de tableau de bord dans l'usage actuel. La seule
« base de données » des demandes est la boîte email qui reçoit les
envois. Un comptage manuel mensuel est néanmoins possible dès maintenant,
sans rien modifier, car chaque sujet d'email identifie le type de
formulaire :

| Sujet reçu (préfixe) | Type de demande | Formulaire |
|---|---|---|
| « Nouveau message — site Method Acting Center » | Contact | `/contact` |
| « Cours d'essai — … » | Cours d'essai | `/cours-essai` |
| « Réservation stage — … » (from_name « Stages · Method Acting Center ») | Stage, page du site | `/stages.html` |
| « Réservation stage — … » (from_name « Stages · Method Acting Center (landing) », champ « Campagne », « Page ») | Stage, landing Ads | `/stages/` |
| « Demande d'inscription — … » | Inscription | `/inscription` |
| « Inscription JPO — … » | JPO (page du site) | `/jpo.html` |
| Sujet défini dans les landings JPO (voir `static/jpo/index.html` ≈ l. 1099) | JPO (landings Ads) | `/jpo/`, `/jposr/` |

Chaque email contient le champ « Comment nous a connus » : c'est la
source d'attribution déclarative à exploiter en priorité (voir
`KPI_DASHBOARD.md`, section Conversion).

Limites : doublons et spams non filtrés (honeypot seulement), pas de
distinction nouveau / ancien contact, pas d'horodatage exploitable
autrement que par la date de l'email, aucune mesure des abandons de
formulaire.

## 4. Accès à demander au propriétaire

Aucun mot de passe ne doit être transmis ni enregistré dans le dépôt :
demander un **accès nominatif** (ou un export) sur chaque outil.

| Outil | Pourquoi | État connu | Demande précise |
|---|---|---|---|
| Google Search Console (propriété `https://www.methodacting.fr/` ou domaine `methodacting.fr`) | Clics, impressions, CTR, positions, pages indexées, erreurs 404 des anciennes URLs, validation du sitemap | Inconnu (existence non vérifiable ici) | Accès « Complet » ou export CSV des 16 derniers mois (Performance + Pages + Sitemaps). |
| Google Analytics 4 | Trafic par page, sources, événements | **Aucun identifiant dans le code** : soit la propriété n'existe pas, soit elle n'est pas installée. | Confirmer si une propriété existe ; si oui, son ID (`G-…`) et un accès « Lecteur ». |
| Google Ads | Campagnes sur `/jpo/`, `/jposr/`, `/stages/` ; conversions ; coût par demande | Inconnu | Confirmer si des campagnes tournent ; accès « Lecture seule » ou export mensuel (coût, clics, conversions). |
| Google Business Profile | Vues de la fiche, appels, itinéraires, clics vers le site, avis (98 au 2026-10-12) | Fiche existante (FACTS_REGISTER) | Accès « Gestionnaire » ou export mensuel des statistiques « Performances ». |
| Bing Webmaster Tools | Indexation Bing (utilisée par Copilot / ChatGPT search) | `BingSiteAuth.xml` en cours de dépôt par le propriétaire | Confirmer la vérification ; accès lecture ou export. |
| Boîte email de réception Web3Forms | Comptage des demandes par type et par source déclarée | Existe (clé publique dans le code) | Comptage mensuel fait par le propriétaire, ou transfert vers une boîte dédiée. Pas d'accès direct nécessaire. |
| Compte Web3Forms | Vérifier le quota du plan gratuit et l'historique des envois | Clé `32e0909e-…` (publique, visible dans le HTML) | Confirmer le plan et le volume mensuel autorisé ; savoir si le tableau de bord payant est activé. |
| Hébergement OVH (logs Apache) | Vrais codes HTTP, hits des robots IA, 404 réels | Inconnu | Export des logs d'accès (30 jours) ou activation des statistiques OVH. |

## 5. Limites de la mesure au 2026-10-12

1. **Site inaccessible depuis l'environnement** : impossible de vérifier codes HTTP, redirections
   `.html` → URL propre, comportement réel du 404, temps de réponse, indexation.
2. **Aucune donnée historique dans le dépôt** : la baseline chiffrée (clics, impressions, positions,
   demandes) ne pourra être renseignée qu'après obtention des accès du § 4. Tant que ces accès
   manquent, la date de départ de la mesure est fixée au **2026-10-12** et la première période de
   référence sera **du premier jour de collecte fiable + 28 jours**.
3. **Conversions non instrumentées** : l'événement `stage_form_success` n'est reçu par aucun outil ;
   les autres formulaires n'émettent aucun événement. Les demandes ne sont comptables que par email.
4. **Attribution déclarative uniquement** : « Comment nous a connus » dépend de la réponse du
   visiteur (champ facultatif, valeur « — » si vide).
5. **Page 404 servie par `index.html`** (`newsite/static/.htaccess:65`, `ErrorDocument 404 /index.html`).
   Avec un chemin local, Apache conserve normalement le code 404 tout en affichant la page d'accueil ;
   à **vérifier en prod** (`curl -sI https://www.methodacting.fr/url-inexistante-test | head -1`
   doit renvoyer `404`). Si une analytics est ajoutée, chaque 404 enverra une page vue avec le
   contenu de l'accueil et un `canonical` pointant sur `/` : prévoir soit une vraie page 404
   (`noindex`, sans canonical), soit un filtre dans l'analytics. Si le code renvoyé est 200, c'est
   un « soft 404 » qui pollue aussi l'indexation.
6. **Liens internes en `.html`** : les pages du site se lient entre elles avec `acting.html`,
   `cours-essai.html`, etc. (`newsite/dist/index.html`, 8 liens `cours-essai.html`, 4 `stages.html`…),
   alors que `.htaccess:48-49` redirige en 301 vers l'URL propre. Chaque clic interne passe donc par
   une redirection (sauf `jpo.html` et `stages.html`, conservés). Effet de mesure : un referrer et
   un code 301 par navigation interne ; à prendre en compte dans l'analyse des logs. Correction à
   évaluer par technical-seo.
7. **`/tarifs/` doublon** : copie de `/tarifs` (`newsite/dist/tarifs/index.html`), `Disallow` dans
   `robots.txt` mais canonical vers `/tarifs`. Les clics mesurés sur `/tarifs/` et `/tarifs` devront
   être agrégés.
8. **Benchmark IA** : aucun assistant tiers interrogeable depuis l'environnement. Le protocole
   (`docs/geo/AI_PROMPT_BENCHMARK.md`, rédigé par l'agent geo-ai-visibility) doit être exécuté
   manuellement et daté. Un seul essai ne prouve pas une absence de visibilité.
9. **Playwright non installé** dans l'environnement (module Python absent) ; Node 22 disponible.
   Le rendu mobile est vérifiable après installation (voir `QA_CHECKLIST.md`).

## 6. Modifications récentes susceptibles de fausser les comparaisons

Source : `git log` (96 commits du 2026-08-03 au 2026-10-12) et `newsite/prod-snapshot/`.

| Période | Changement | Impact sur la mesure |
|---|---|---|
| Avant août 2026 | Site sous WordPress (commentaires `newsite/static/.htaccess:3, 58`, `README.md` racine « Livrable WordPress »). Les anciennes URLs WordPress **ne sont pas connues dans le dépôt** (aucune trace `wp-content`, `?p=`, slugs). | Toute donnée Search Console antérieure porte sur des URLs disparues. Les récupérer dans Search Console (rapport Pages → « Introuvable (404) ») pour alimenter le bloc « Redirections 301 des anciennes URLs WordPress (à compléter) » de `.htaccess:57-61`. |
| 2026-08-03 → 2026-08-21 | Premier site statique ; `.htaccess` de production (commit `1ef0b03`), URLs propres (`a615dcd`). | Changement de structure d'URL n° 1. |
| Août → 2026-10-11 (`prod-snapshot/`) | Site statique avec images en base64 dans les pages (index.html de 5,3 Mo, acting.html 4,7 Mo) et 4 dossiers d'images. Liens internes en `.html` (`cours-essai.html#reservation` ×11, `inscription.html` ×5, `stages.html` ×5, `/tarifs/` ×3…). | Poids de page divisé par ~50 après refonte : toute comparaison de vitesse / CWV avant-après n'est pas imputable au SEO. Les URLs `*.html` restent valides via 301. |
| 2026-10-10 | Création de la landing `/stages/` (Google Ads) avec `dataLayer` / `gtag` (`75476ed`). | Nouvelle URL ; conversions non collectées. |
| 2026-10-11 | Dossier d'images unique `/uploads/` ; `dist/` entièrement généré (`2737cb7`). Anciens dossiers `assets/img/`, `jpo/uploads/`, `jposr/uploads/`, `stages/uploads/` à supprimer sur le serveur. | Les anciennes URLs d'images (Google Images, Discover) renverront 404 après suppression : surveiller dans Search Console. |
| 2026-10-12 | `robots.txt` ouvert aux robots IA, `sitemap.xml` (10 URLs), `llms.txt`, canonical / Open Graph / JSON-LD sur toutes les pages (`c477e9f`), note Google 4,8/98 dans le JSON-LD (`2fac08c`), profils sociaux (`fac76ab`), horaires (`63d2a7e`). | Point zéro des données structurées. Les rich results, s'ils apparaissent, ne pourront être datés qu'à partir du déploiement effectif (date à noter par le propriétaire). |
| Date de déploiement de `dist/` actuel | **Inconnue dans le dépôt** (déploiement FTP manuel). | À demander au propriétaire et à inscrire ici : c'est la vraie date « T0 » des comparaisons. |

URLs à surveiller en 404 / redirection dans Search Console et les logs :

- anciennes URLs WordPress (liste à récupérer, non disponible ici) ;
- `/index.html`, `/index` → 301 vers `/` ;
- `/acting.html`, `/scenario-real.html`, `/contact.html`, `/tarifs.html`, `/planning.html`,
  `/cours-essai.html`, `/inscription.html` → 301 vers l'URL propre ;
- `/jpo.html`, `/stages.html` : conservés (pages du site, 200 attendu) ; `/jpo/`, `/jposr/`,
  `/stages/` : landings (200 attendu, hors sitemap) ;
- `/assets/img/*`, `/jpo/uploads/*`, `/jposr/uploads/*`, `/stages/uploads/*` → 404 après nettoyage
  serveur ; `/uploads/*` → 200 ;
- `/tarifs/` : 200, bloqué par robots, canonical `/tarifs`.

## 7. État des contrôles techniques exécutables localement (2026-10-12)

Exécutés sur une copie de `newsite/` dans le scratchpad, sans toucher au dépôt :

- `python3 build.py` : **OK**, 10 pages + landing `/stages/`, 46 fichiers `uploads/`, aucune assertion
  levée ; la sortie est **identique octet pour octet** à `newsite/dist/` commité (`diff -rq`).
- JSON-LD : 1 bloc `@graph` valide (JSON parsable) sur chacune des 11 pages du site (dont `/tarifs/`) ;
  **0 bloc** sur les trois landings `/jpo/`, `/jposr/`, `/stages/` (choix à confirmer par technical-seo).
- 1 seul `<h1>` par page (14 fichiers HTML), `<title>` et `canonical` présents partout, canonical des
  landings = leur propre URL.
- Liens internes relatifs : aucun lien cassé vers un fichier absent dans `dist/` (le seul faux
  positif est un gabarit JS `'+esc(r.link)+'` des cartes d'avis dans les landings).
- `sitemap.xml` : 10 URLs, toutes cohérentes avec les canonicals ; `lastmod` = date du build
  (change à chaque build, sans rapport avec une modification réelle de contenu).

Ces contrôles sont la référence « avant » pour la section Qualité du `KPI_DASHBOARD.md`.
