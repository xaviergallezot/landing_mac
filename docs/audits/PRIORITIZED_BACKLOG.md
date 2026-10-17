# Backlog priorisé — SEO, GEO, contenu, mesure

Consolidation des six audits du 2026-10-12 (seo-auditor, geo-ai-visibility, content-strategist,
technical-seo, digital-pr, analytics-qa). Rédigé le 2026-10-17 par le chef de projet.
Rapports sources : `docs/audits/SEO_AUDIT.md` (P01–P23), `docs/technical/TECHNICAL_AUDIT.md` (D1–D17),
`docs/geo/GEO_ACTION_PLAN.md` (G1–G20), `docs/content/CONTENT_AUDIT.md` (§ 4 et § 7),
`docs/pr/PR_OPPORTUNITIES.md`, `docs/analytics/BASELINE.md` et `MEASUREMENT_PLAN.md`.

## Méthode de consolidation

- Chaque ligne cite les identifiants des rapports d'origine ; les doublons entre agents ont été fusionnés.
- Barème : impact 1–5, confiance 1–5, effort 1–5 (1 = moins d'une heure), risque faible / moyen / élevé.
- Priorités : P0 critique ou sécurité ; P1 blocage d'indexation ou défaut majeur sur une page clé ;
  P2 amélioration importante ; P3 secondaire ; P4 facultatif.
- Les constats dépendant du site en ligne (codes HTTP, indexation) sont marqués **[non vérifié en ligne]** :
  la logique est établie à la lecture des fichiers, le comportement réel se confirme par `curl` depuis un
  poste externe (commandes dans `docs/analytics/QA_CHECKLIST.md`).
- Aucune recommandation n'a été traitée comme une preuve : chaque ligne renvoie à un fichier ou une URL.

## Contradictions entre agents, et arbitrage

| Sujet | Positions | Arbitrage du chef de projet |
|---|---|---|
| `aggregateRating` (4,8/98) dans le JSON-LD | seo-auditor et technical-seo : retirer (note reprise d'un autre site, non éligible, risque de pénalité) ; geo-ai-visibility : décision propriétaire | Recommander le retrait du JSON-LD, garder le badge visible qui renvoie vers Google. Décision propriétaire car il a demandé cet ajout (B11). |
| Événement `gtag` de la landing `/stages/` | analytics-qa et technical-seo : aucun conteneur chargé, le gtag n'est qu'un commentaire | Confirmé : aucune mesure n'existe sur le site. |
| Année de création | site : 1999 ; Coup de théâtre : 2002 ; L'Étudiant : 2009 | Décision propriétaire avant toute correction externe (B5). |
| Landings Ads indexables | tous : `noindex, follow` recommandé | Décision propriétaire : vérifier d'abord les URL finales des campagnes (B1). |
| Google Fonts | seo-auditor : à envisager ; technical-seo : auto-héberger | Auto-héberger, après le lot images (A12). |

---

## Lot A — Correctifs techniques sans décision commerciale (technical-seo)

Modifications dans les sources (`newsite/build.py`, `partials/`, `static/`, `tools/`), jamais dans `dist/`.
Tous réversibles par `git revert`. Test commun : `cd newsite && python3 build.py` sans assertion,
`git status` propre après build, checklist `docs/analytics/QA_CHECKLIST.md`.

| ID | Priorité | Problème | Preuve | Impact | Conf. | Effort | Risque | Fichiers | Critère d'acceptation | Dépendances |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | **P1** | `/tarifs` redirige vers `/tarifs/`, dossier interdit par robots.txt : page Tarifs probablement non explorable **[non vérifié en ligne]** (D1, P05) | `dist/tarifs/index.html` existe ; `.htaccess:53` `!-d` ; `robots.txt:8` | 5 | 4 | 2 | faible | `build.py` (supprimer `tarifs_folder_variant`), `.htaccess` (301 `^tarifs/$` → `/tarifs`), `robots.txt`, liens `/tarifs/` des 3 landings, README | `curl -I /tarifs` = 200 ; `/tarifs/` = 301 → `/tarifs` | **Propriétaire : supprimer le dossier `www/tarifs/` sur le serveur** (un dépôt FTP par écrasement ne supprime pas les dossiers) |
| A2 | **P1** | 100 % des liens internes en `.html` passent par une 301 (P01, D2) | `dist/index.html` : 8 × `cours-essai.html`, 4 × `stages.html`… ; `.htaccess:48-49` | 4 | 5 | 2 | faible | `build.py` (réécriture `href` après assemblage), `static/jpo`, `static/jposr`, générateur | `grep -c 'href="[a-z-]*\.html' dist/*.html` = 0 hors `jpo.html` et `stages.html` ; crawl local 0 lien cassé | — |
| A3 | **P1** | `/stages/` : deux canonicals, deux meta robots, deux jeux Open Graph, le second décrivant les JPO (P02, G4) | `dist/stages/index.html:8` et `:15` (vérifié par le chef de projet) | 4 | 5 | 1 | faible | `tools/build_landing_stages.py` (retirer le bloc d'origine, assertion `count('rel="canonical"')==1`) | 1 canonical, 1 og:url, 1 og:title | — |
| A4 | P2 | Faute visible « l\'expérience » dans un H2 de `/stages/` (D11) | `dist/stages/index.html` ; générateur l. 68 | 2 | 5 | 1 | nul | `tools/build_landing_stages.py` | `grep "l\\\\'exp" dist/stages/index.html` = 0 | — |
| A5 | P2 | Événements et dates codés en dur : stages du 17-18 oct. restent dans le JSON-LD et sur 6 pages après la date (P22, D16, contenu P3) | `build.py:141`, `pages/stages.html:5,28`, `tarifs.html:46,188`, `planning.html:57`, landings | 3 | 5 | 3 | faible | `build.py` (source unique `SESSIONS`, filtrage `endDate < today`, calcul du « prochain stage »), pages, générateur | Rebuild après une date passée : aucune mention ni `Event` périmé | — |
| A6 | P2 | Meta descriptions hors gabarit (86 à 205 caractères) ; `/tarifs` promet des « offres à la rentrée » absentes de la page (P09, D14) | `build.py:41-62` | 2 | 5 | 1 | faible | `build.py` (`PAGES`, assertion de longueur 120-160), landings | Toutes ≤ 160 car., promesse vérifiable | formulations validées par content-strategist |
| A7 | P2 | `lastmod` du sitemap = date du build pour toutes les URLs (P15, D9) | `build.py:159-162` | 1 | 5 | 1 | nul | `build.py` (date du dernier commit du fichier source) | Deux builds successifs sans modification → sitemap identique | — |
| A8 | P2 | Hiérarchie de titres : H3/H4 sous H1 sur `/contact`, H2 vide sur `/planning`, H1 identique `/jpo/` et `/stages/` (P21) | `pages/contact.html:16,26`, `planning.html:217` | 1 | 4 | 1 | faible | pages, générateur | 1 H1 distinct par page, pas de saut de niveau | — |
| A9 | P2 | `.htaccess` : 404 servie avec l'accueil, hôte www non forcé, pas d'en-têtes de sécurité, bloc 301 WordPress vide (P12, P14, D10, G5) **[non vérifié en ligne]** | `.htaccess:27-30,57-65` | 3 | 3 | 2 | **moyen** (une directive refusée par OVH = erreur 500) | `.htaccess`, nouvelle `pages/404.html` (noindex, hors sitemap), `build.py` | `curl -I /inexistant` = 404 avec page dédiée ; `http://methodacting.fr/` = 301 en un saut ; aucun 500 | Déployer le `.htaccess` seul d'abord, conserver l'ancien pour retour arrière immédiat ; liste des anciennes URL (E2) |
| A10 | P2 | Images : 2,6 à 4,6 Mo par page, 0 `width/height`, 5 `loading="lazy"` sur 150, 1 seul WebP, landings sans `src` (images injectées en JS), 27 `alt=""` sur des affiches (P10, D6, D13) | `TECHNICAL_AUDIT.md` § 5 | 4 | 4 | 3 | faible | `build.py` (dérivés WebP + `srcset` via Pillow, `width/height`, lazy hors hero), pages, landings | Poids au premier affichage < 1 Mo ; PageSpeed mobile LCP < 2,5 s, CLS < 0,1 après déploiement | alt des affiches : titre du film seul tant que B8 n'est pas tranché |
| A11 | P2 | Google Fonts externe, bloquante, 8 graisses (P11, D8) | `partials/head.html:21-24` | 3 | 4 | 2 | faible | `assets/fonts/` (woff2), `style.css` (`@font-face`, `font-display: swap`), `head.html`, `.htaccess` (cache woff2), landings | Aucune requête vers fonts.googleapis.com ; rendu identique (captures) | après A10 |
| A12 | P2 | Accessibilité : labels non associés sur 5 formulaires, cibles de 8-17 px (bandeau, points de carrousel), contrastes 2,9-3,8:1 sur les étiquettes (D12) | `TECHNICAL_AUDIT.md` § 6 | 3 | 5 | 2 | faible | pages (id/for), `style.css` (tailles, couleurs) | Script Playwright : 0 cible < 24 px, 0 contraste < 4,5:1 hors décor | couleurs : rester dans la charte (assombrir, pas changer) |
| A13 | P3 | Open Graph : 5 images portrait, sans `og:image:width/height/alt` (D15) | `build.py` `OG_IMAGES` | 1 | 5 | 1 | nul | `build.py` (recadrage 1200×630 au build), `head.html` | Aperçu de partage non tronqué | — |
| A14 | P3 | CSS/JS inlinés dans chaque page, cache inutile (P11, D17) | `build.py:33-38` | 1 | 5 | 2 | faible | `build.py`, `.htaccess` | HTML < 40 Ko | après A10/A11, non prioritaire |
| A15 | P3 | Horaires d'ouverture et accès dans le JSON-LD mais pas dans le HTML (P23, G16, contenu P3) | `build.py:100-104` vs `pages/contact.html` | 1 | 4 | 1 | nul | `pages/contact.html`, `partials/footer.html` | Horaires visibles sur `/contact` | — |
| A16 | P3 | `Course` incomplet (`courseMode` minuscule, pas de `courseWorkload`/`courseSchedule`), prix 370/350 € déclarés mais invisibles sur `/acting` et `/scenario-real`, `Offer` orphelin, landings sans JSON-LD (D5, G6) | `build.py` `course()` | 3 | 4 | 2 | faible | `build.py`, `pages/acting.html`, `scenario-real.html` (afficher « dès 370 €/mois » + lien tarifs), landings | Rich Results Test sans erreur ; prix visibles | volumes horaires à figer (B13) |
| A17 | P3 | `llms.txt` maintenu à la main : risque de dérive (G9, P23) | `static/llms.txt` | 1 | 4 | 2 | nul | `build.py` (génération depuis `PAGES`, `SESSIONS`, `ORG`) | Diff nul après génération | après A5 |

## Lot B — Décisions du propriétaire (bloquantes pour les lots C et D)

| ID | Décision | Recommandation | Débloque | Rapports |
|---|---|---|---|---|
| B1 | Sort des landings `/jpo/`, `/jposr/`, `/stages/` : indexables ou réservées aux campagnes ? | **Tranché le 2026-10-17 par le propriétaire : aucun changement, les landings restent indexables.** Conséquence : P03/P04/D4 fermés ; la différenciation des titres et H1 entre landings et pages du site passe par C4 ; A3 (canonical unique de `/stages/`) reste nécessaire. | — | SEO P03-P04, D4 |
| B2 | Offre « 100 € de remise, valable jusqu'au 31/08/2026 » encore affichée sur `/jpo/` et `/jposr/` (expirée), et proposée pour janvier 2027 dans la case du formulaire | Retirer, ou fournir les nouvelles conditions écrites (montant, date limite, rentrée concernée) | correction immédiate des landings | contenu P1, G8, I-6 |
| B3 | Rythme de la 4ᵉ année Acting : `planning.html:274` « 1 atelier de 3 h le mardi » contre `inscription.html:67` « 2 ateliers de 3 h par semaine » | Trancher | correction immédiate | contenu P1, I-2 |
| B4 | Formulation officielle du 3ᵉ temps de la Méthode : « Reproduire » (accueil, tarifs, llms.txt, landings) ou « Composer » (`acting.html:50`) | Une seule formulation partout | A5, C1 | SEO P16, I-1 |
| B5 | Année de création : 1999 (site), 2002 (Coup de théâtre), 2009 (L'Étudiant) | Fournir la date et une source (Sirene, statuts) | D1, C3, JSON-LD `foundingDate` | G2, PR § 1.4 |
| B6 | Fondateur : nom complet publiable (« David » sur le site ; « David Barrouk » dans l'alt d'une image et dans la notice BnF du livre *Stan ou Le solfège de l'acting*, 2017), mention des ouvrages | Autoriser une biographie courte sourcée : c'est la preuve d'expertise la plus solide trouvée | C3, C1 | G10, PR, CITATION S12-S13 |
| B7 | Coachs : noms, fonctions, bios, consentement écrit | Page ou section « L'équipe » | C3 | G10, contenu V-2 |
| B8 | Affiches « Nos acteurs tournent ! » (8 films, aucun nom d'ancien élève, droits non documentés ; fichiers nommés d'après des actrices connues) | Fournir, pour chaque film, l'ancien élève, son rôle, son accord et une source vérifiable (IMDb, Unifrance) ; sinon retirer le carrousel | A10 (alt), C9 | SEO P17, G12, contenu P2 |
| B9 | Affirmations non sourcées : « la méthode de Brando, Streep, DiCaprio… » (`acting.html:8`), « descendant direct » de Stanislavski (`index.html:87,156`), « quasi inexistant en France », « ce que presque aucune école ne propose », « 25 ans » du programme scénario (`jposr`) | Retirer ou remplacer par des faits sourcés (filiation réelle du fondateur, cf. B6) | C1, C6 | SEO P17, contenu P2, I-9 |
| B10 | Badge « Avis vérifiés Trustpilot » sur 8 pages et lien `sameAs` : profil non confirmé (extrait de recherche : 4,0/5 sur 3 avis) | Vérifier la page Trustpilot ; retirer le badge si le profil est faible ou absent | A16 | SEO P17, G3, S11 |
| B11 | `aggregateRating` 4,8/98 dans le JSON-LD (voir arbitrage ci-dessus) | Retirer du JSON-LD, garder le badge visible | A16 | P06, D5, G6 |
| B12 | Nom officiel des stages : « Stage A / Stage B » (site) ou « Actors Studio A / B » (landing `/stages/`) : le second crée une confusion avec The Actors Studio de New York | Un seul nom, sans « Actors Studio » | A5 | I-5, G7 |
| B13 | Statut à afficher : école hors contrat ? diplôme ou certificat délivré ? CPF/financements ? volumes horaires annuels par année | Réponses écrites pour la FAQ et `Course` | A16, C2 | D5 (GEO), SEO § 6 |
| B14 | Fichier logo (PNG/SVG fond uni ≥ 112 × 112) et favicon | Fournir le logo | A18 favicon + `logo` JSON-LD | P07, D7 |
| B15 | Outil de mesure et consentement : option A sans cookie exemptée CNIL (recommandée pour démarrer) ou option B GTM + GA4 + conversions Ads avec bandeau de consentement ; mentions légales et politique de confidentialité absentes du site | Choisir ; ajouter mentions légales et confidentialité (obligation légale, indépendante du SEO) | E4 | MEASUREMENT_PLAN § 4-6, D3, P20 |
| B16 | Cours ados/enfants à 100 €/mois annoncé sur Spectable, programme ados mentionné dans `/jpo/` : existe-t-il ? | Confirmer ou faire retirer | D1 | I-7, CITATION S05 |
| B17 | Avis Google reproduits sur le site avec le nom des auteurs (44 cartes) | Contenu public ; CLAUDE.md demande un consentement : trancher (garder, initiales, ou retirer les noms) | — | SEO P23 |
| B18 | Accès à fournir : Search Console (lecture), Google Business Profile, comptes Emagister / Spectable / Pages Jaunes pro / L'Étudiant, Google Ads (si campagnes), logs OVH, export 16 mois Search Console | Indispensable pour E1-E3 et D1 | lots D et E | BASELINE § 4, GEO D9 |
| B19 | Autorisation de tout contact externe (agendas, annuaires, presse, festivals) | Lot D uniquement après accord | lot D | digital-pr § 6 |

## Lot C — Contenus (content-strategist, après validation des faits)

| ID | Priorité | Action | Faits requis | Livrable | Rapports |
|---|---|---|---|---|---|
| C1 | P2 | Page de référence « Stanislavski, Method Acting et la Méthode du Method Acting Center » (intentions 1 et 8, aucune page française équivalente observée) | B4, B6, B9 | brouillon existant `docs/content/drafts/la-methode-stanislavski-method-acting.md` → `pages/la-methode.html` | P18, G11, CONTENT_PLAN |
| C2 | P2 | FAQ transversale (admission, débutants, âge, prix total, durée, horaires, cours d'essai, stages, accès) ; `FAQPage` seulement si visible | B3, B13 | brouillon existant `docs/content/drafts/faq.md` → `pages/faq.html` ou sections | P18, G13 |
| C3 | P2 | Page « L'école » : histoire, fondateur, équipe, statut, adresse, accès | B5, B6, B7, B13 | nouveau brouillon | G10, P18 |
| C4 | P2 | Titles et H1 portant les requêtes (« école d'acting à Paris », « formation acteur cinéma », « stages d'acting à Paris ») sans dépasser 65 caractères ; sous-titres H2 descriptifs | — | propositions dans `build.py` `PAGES`, validation propriétaire | P08, D14 |
| C5 | P2 | Coût annuel total et date de vérification sur `/tarifs` (370 × 9 + 200 = 3 530 €/an acting ; 350 × 9 + 200 = 3 350 €/an scénario, à confirmer) | FACTS_REGISTER | `pages/tarifs.html` | P18, contenu P2 |
| C6 | P3 | Réduire les répétitions : bloc « Ce n'est pas le talent… » (4 fois), carrousel d'affiches (3 fois), grille « 3 portes d'entrée » (5 fois) | B8 | pages | contenu § 5 |
| C7 | P3 | `/contact` : horaires, accès (métro, bus), plan, délai de réponse | — | `pages/contact.html` | contenu P3, A15 |
| C8 | P3 | Bloc « Jeu face caméra » consolidé (contenu aujourd'hui dispersé sur 3 pages) ; page dédiée seulement si la demande se confirme dans Search Console | — | brief | G14, P18 |
| C9 | P3 | Section « Ils ont étudié ici » nominative et sourcée, en remplacement du carrousel d'affiches | B8 | pages | P17, G12 |

## Lot D — Présence externe (digital-pr, après B19)

| ID | Priorité | Action | Rapports |
|---|---|---|---|
| D1 | **P1** (cohérence) | Corriger ou faire retirer les fiches tierces fausses : Emagister (250 €/mois, « 3 jours d'essai », 2017-2018, 26 fiches), Gowork (105 B rue de Tolbiac), L'Étudiant (« créée en 2009 », chant/danse), Pages Jaunes (2 fiches en doublon), evous (téléphone probablement erroné), Spectable (atelier enfants 100 €/mois, « Robert Lewis ») | CITATION § 3, PR § 1, P19, G1 |
| D2 | P2 | Fiche Google Business : catégories, attributs, photos, questions-réponses, posts JPO et stages (source locale principale de Google et Gemini) | G17 |
| D3 | P2 | Agenda « Que Faire à Paris » (gratuit) pour les JPO des 12-13 décembre et les stages | PR § 2.2 |
| D4 | P3 | Festivals ouverts aux films d'élèves (Nikon Film Festival, Éclats d'Écran, Format Court, 48 Hour Film Project) ; médias (Coup de théâtre, podcast ACTe, Troiscouleurs, magazine Treize) | PR § 2.4, EDITORIAL_PITCHES |
| D5 | P3 | Protocole de témoignages authentiques (consentement, retrait, image) | OUTREACH_DRAFTS § 4 |

## Lot E — Mesure (analytics-qa)

| ID | Priorité | Action | Dépend de | Rapports |
|---|---|---|---|---|
| E1 | **P1** | Accès Search Console et Bing Webmaster ; export 16 mois ; vérifier les anciennes URL en 404 (ex. `/portes-ouvertes-septembre-2021/`, `/tarifs/`, `/contact.html` encore dans l'index) | B18 | BASELINE § 4, CITATION S16 |
| E2 | **P1** | Liste des anciennes URL WordPress à rediriger (Search Console → Pages, logs OVH, Wayback) puis 301 ciblées | E1 | P13, D10, G5 |
| E3 | P2 | Baseline : exécuter le benchmark IA (`docs/geo/AI_PROMPT_BENCHMARK.md`, 34 prompts, 3 répétitions, 4 assistants) avant tout changement de contenu ; compter les demandes Web3Forms par type sur 28 jours | propriétaire | G20, MEASUREMENT § 2 et § 7 |
| E4 | P2 | Installer la mesure choisie (B15) sur les 8 formulaires, clics tel/WhatsApp/email, CTA ; remplacer le placeholder gtag de `/stages/` | B15 | MEASUREMENT § 3 et § 5, D3 |
| E5 | P3 | Vérifications en ligne après chaque déploiement : commandes `curl` et checklist | déploiement | QA_CHECKLIST |

## Déjà réalisé depuis l'audit (hors backlog)

- 2026-10-17 — Validation commune des 8 formulaires (prénom, nom, email ou téléphone obligatoires), à la
  demande explicite du propriétaire : voir `docs/CHANGELOG.md` FORMS-001. La landing `/stages/` envoyait
  un formulaire vide (attribut `novalidate`), les autres acceptaient des espaces.

## Ordre d'exécution proposé

1. **Vague 1 (technique, sans décision)** : A1, A2, A3, A4, A7, A8, A6 (descriptions), A13 — moins d'une journée, un seul commit par item, build et checklist à chaque fois. Déploiement par le propriétaire avec suppression manuelle de `www/tarifs/`.
2. **Vague 2 (décisions rapides)** : B2, B3, B4, B11, B12 → corrections immédiates ; B1 → noindex des landings.
3. **Vague 3 (technique lourde)** : A5, A9 (avec procédure de retour arrière), A10, A11, A12, A16, A17.
4. **Vague 4 (contenu)** : C1 à C5 après B5-B9, B13.
5. **Vague 5 (externe et mesure)** : D1 dès B18/B19 ; E1-E3 dès les accès ; E4 après B15.

Rien n'est déployé ni publié par les agents : chaque vague se termine par un diff, des tests et une
demande d'autorisation.
