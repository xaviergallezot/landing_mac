# KPI Dashboard — Method Acting Center

## Règles de mesure

Aucune valeur ne doit être inventée.
Chaque indicateur doit avoir une source, une période et une définition.

Date de départ de la mesure : **2026-10-12** (voir `BASELINE.md`). Aucune
donnée historique n'est disponible dans le dépôt ; les accès à demander
sont listés dans `BASELINE.md` § 4. Période de référence proposée : les
28 premiers jours de collecte fiable, puis comparaison mois par mois et,
dès qu'elle existe, année sur année (saisonnalité des rentrées de
septembre et janvier).

Échelle de qualité des données utilisée dans les tableaux :
**A** = mesure directe par l'outil source ; **B** = mesure directe mais
partielle (échantillonnage, consentement, agrégation) ; **C** =
déclaratif ou comptage manuel ; **D** = non mesurable aujourd'hui.

## SEO

| KPI | Baseline | Actuel | Période | Source | Formule | Dénominateur / unité | Objectif | Qualité |
|---|---|---|---|---|---|---|---|---|
| Clics organiques | À mesurer | — | — | Search Console → Performances (Web) | Somme des clics sur la période, filtre pays = France | Par 28 jours ; ventiler par page et par requête | À définir | A (données SC lissées, requêtes anonymisées partiellement) |
| Impressions organiques | À mesurer | — | — | Search Console | Somme des impressions | Par 28 jours | À définir | A |
| CTR organique | À mesurer | — | — | Search Console | clics ÷ impressions × 100 | Impressions de la même période et du même filtre | À définir | A (dépend de la position : lire avec elle) |
| Position moyenne | À mesurer | — | — | Search Console | Moyenne pondérée fournie par SC | Impressions ; à lire par requête cible, pas globalement | À définir | B (moyenne trompeuse si le mix de requêtes change) |
| Pages indexées | À mesurer | — | — | Search Console → Pages ; `site:methodacting.fr` en contrôle | Nombre d'URLs « Indexées » ; cible = 10 URLs du sitemap + 3 landings | Sur les 10 URLs du sitemap (`newsite/dist/sitemap.xml`) | 10 / 10 indexées ; 0 ancienne URL indexée | A |
| Requêtes pertinentes | À mesurer | — | — | Search Console | Nombre de requêtes avec impressions > 0 appartenant à la liste d'intentions (CLAUDE.md § 1 : Stanislavski Paris, école acting, jeu face caméra, prix formation acting, acting + scénario + réalisation, stage acting débutant, Method Acting Center) | Liste de requêtes cibles maintenue par content-strategist | À définir | B (liste à constituer ; SC masque les requêtes rares) |
| Erreurs techniques | À mesurer | — | — | Search Console → Pages / Paramètres ; checklist locale | Nombre d'URLs en 404, soft 404, redirection, « explorée non indexée », erreurs JSON-LD | URLs explorées | 0 sur les URLs du sitemap | A (SC) / C (contrôle local `QA_CHECKLIST.md`) |
| Anciennes URLs en 404 | À mesurer | — | — | Search Console → Pages → Introuvable (404) ; logs OVH | Nombre d'URLs 404 recevant des impressions ou des hits (anciennes URLs WordPress, `/assets/img/`, `/jpo/uploads/`…) | URLs 404 listées par SC | 0 URL 404 avec trafic (via 301 dans `.htaccess`) | A |
| Résultats enrichis | À mesurer | — | — | Search Console → Améliorations (FAQ, Événements, Avis) | Nombre d'éléments valides / avec avertissement / erreurs par type | Pages portant le type (`build.py` : Course, Event, FAQPage, Offer, AggregateRating) | 0 erreur | A |
| Performances terrain (CWV) | À mesurer | — | — | PageSpeed Insights / CrUX | LCP, INP, CLS mobile par page clé (`/`, `/acting`, `/stages.html`) | Par page, 28 jours CrUX si volume suffisant | « Bon » sur les 3 métriques | B (CrUX absent si trafic faible : lire le labo) |

## GEO / visibilité IA

Protocole : `docs/geo/AI_PROMPT_BENCHMARK.md` (agent geo-ai-visibility),
règles d'exécution dans `MEASUREMENT_PLAN.md` § 7. Une « réponse
valide » est une réponse complète obtenue dans les conditions
enregistrées (date, assistant, modèle, langue, mode recherche web
oui/non, session neuve). Chaque prompt est répété au moins 3 fois.

| KPI | Baseline | Actuel | Période | Source | Formule | Dénominateur / unité | Objectif | Qualité |
|---|---|---|---|---|---|---|---|---|
| Prompts testés | À définir | — | — | `AI_PROMPT_BENCHMARK.md` | Nombre de prompts distincts du protocole | — (liste fixe par vague) | Liste stable d'une vague à l'autre | A |
| Réponses valides | À mesurer | — | — | Tests datés | prompts × répétitions × assistants, moins les réponses invalides (erreur, refus, hors-sujet) | — | ≥ 3 par prompt et par assistant | C (manuel) |
| Prompts mentionnant l'école | À mesurer | — | — | Tests datés | Nombre de prompts pour lesquels au moins une réponse valide contient « Method Acting Center » | Prompts testés | À définir | C |
| Taux de mention | À calculer | — | — | Benchmark | réponses mentionnant l'école ÷ réponses valides × 100, par assistant et au global | Réponses valides du même ensemble de prompts et de conditions | À définir | C (variance élevée : ne comparer que des vagues de même protocole) |
| Taux de recommandation | À calculer | — | — | Benchmark | réponses où l'école est explicitement recommandée (pas seulement nommée) ÷ réponses valides × 100 | Réponses valides | À définir | C |
| Citations du site officiel | À mesurer | — | — | Réponses observées | Nombre de réponses citant une URL `methodacting.fr` ; détailler les pages citées | Réponses valides (taux = ÷ réponses valides) | À définir | C (dépend du mode « recherche web ») |
| Sources tierces citées | À mesurer | — | — | Réponses observées | Nombre de réponses citant une source tierce parlant de l'école ; liste des domaines (alimente digital-pr) | Réponses valides | À définir | C |
| Exactitude factuelle | À mesurer | — | — | Contrôle manuel vs `docs/FACTS_REGISTER.md` | affirmations exactes ÷ affirmations vérifiables sur l'école (prix, adresse, durée, méthode, dates) × 100 | Affirmations vérifiables contenues dans les réponses qui mentionnent l'école | 100 % | C |
| Erreurs de description | À mesurer | — | — | Contrôle manuel | Nombre d'erreurs distinctes (ex. mauvais prix, mauvaise ville, confusion avec une autre école), avec leur fréquence | Réponses mentionnant l'école | 0 erreur récurrente | C |
| Concurrents cités | À mesurer | — | — | Réponses observées | Pour chaque prompt, liste et fréquence des écoles citées à la place ou à côté | Réponses valides | Information, pas d'objectif | C |
| Demandes « Recherche IA » | À mesurer | — | — | Emails Web3Forms, champ « Comment nous a connus » | Nombre de demandes dont la source déclarée = « Recherche IA (ChatGPT, etc.) » | Demandes avec source renseignée (hors « — ») | À définir | C (déclaratif ; seul signal de trafic IA disponible, les referrers IA n'étant pas mesurés) |

Taux de mention =
nombre de réponses mentionnant l'école / nombre de réponses valides
pour le même ensemble de prompts et de conditions.

Distinguer la présence du nom, une recommandation réelle et une
citation de source. Ce sont trois indicateurs différents.

Limites : variabilité des réponses entre deux exécutions identiques,
changements de modèle non annoncés, localisation et historique de
l'utilisateur. Un seul essai ne prouve ni présence ni absence. Ne pas
automatiser l'interrogation d'un service contre ses conditions
d'utilisation.

## Conversion

| KPI | Baseline | Actuel | Période | Source | Formule | Dénominateur / unité | Objectif | Qualité |
|---|---|---|---|---|---|---|---|---|
| Demandes de renseignements (total) | À mesurer | — | — | Emails Web3Forms (comptage manuel) ; plus tard événement `form_submit` | Nombre d'emails reçus sur la période, hors spam et doublons, tous formulaires | Par mois | À définir | C aujourd'hui (comptage manuel) → A/B après instrumentation (`MEASUREMENT_PLAN.md` § 3.1) |
| Demandes par type | À mesurer | — | — | Préfixe du sujet des emails (`BASELINE.md` § 3) | Comptage par type : contact, cours d'essai, stage (site), stage (landing), inscription, JPO (site), JPO (landings) | Par mois ; part = type ÷ total × 100 | À définir | C → A/B |
| Demandes par source déclarée | À mesurer | — | — | Champ « Comment nous a connus » | Comptage par valeur (Recherche Google, Recherche IA, Instagram, TikTok, Facebook, Bouche à oreille, Ancien élève, Eventbrite, Newsletter, Autre…) | Demandes avec source renseignée (hors « — ») ; indiquer aussi le taux de non-réponse | À définir | C (déclaratif, champ facultatif) |
| Demandes attribuées à Google Ads | À mesurer | — | — | Champ « Campagne » (gclid / utm) de la landing `/stages/` ; Google Ads si accès | Nombre d'emails de la landing stages avec « Campagne » ≠ « — » ; plus tard conversions Ads | Demandes de la landing `/stages/` | À définir | C (uniquement `/stages/` ; `/jpo/` et `/jposr/` n'enregistrent pas la campagne) |
| Formulaires terminés (taux) | À mesurer | — | — | Analytics (après instrumentation) | `form_submit` ÷ sessions ayant affiché la page du formulaire × 100 | Sessions sur la page du formulaire, par formulaire | À définir | D aujourd'hui ; B après instrumentation (consentement) |
| Erreurs d'envoi | À mesurer | — | — | Événement `form_error` (après instrumentation) | `form_error` ÷ (`form_submit` + `form_error`) × 100 | Tentatives d'envoi | < 2 % | D → B |
| Clics d'inscription (CTA) | À mesurer | — | — | Événement `cta_click` avec `cta_target = inscription` (après instrumentation) | Nombre de clics ; taux = clics ÷ pages vues de la page d'origine | Pages vues de la page portant le CTA | À définir | D → B |
| Clics tel / WhatsApp / email | À mesurer | — | — | Événement `contact_click` (après instrumentation) ; Google Business Profile pour les appels depuis la fiche | Nombre de clics par méthode | Pages vues ; par placement (footer, page) | À définir | D → B (clic ≠ appel abouti) |
| Clics vers les avis (preuves) | À mesurer | — | — | Événement `outbound_click` (`google_reviews`, `trustpilot`) | Nombre de clics sortants vers les avis | Pages vues | Information | D → B |
| Inscriptions confirmées | À mesurer | — | — | Registre de l'école (système métier, hors dépôt) | Nombre d'inscriptions signées sur la période, par programme | Par rentrée (septembre, janvier) | À définir | C (dépend du propriétaire ; ne jamais publier) |
| Taux de conversion demande → inscription | À calculer | — | — | Inscriptions confirmées ÷ demandes d'inscription | inscriptions ÷ demandes « inscription » × 100 | Demandes « inscription » de la même fenêtre (délai de décision à définir) | À définir | C |
| Taux de conversion visite → demande | À calculer | — | — | Analytics + emails | demandes ÷ sessions × 100 | Sessions (option sans cookie : visites) de la période | À définir | B (sessions partielles selon l'outil / consentement) |
| Coût par demande (si Ads) | À calculer | — | — | Google Ads (accès à demander) + demandes attribuées | dépenses Ads ÷ demandes attribuées Ads | Demandes attribuées à la campagne | À définir | B/C (attribution incomplète hors `/stages/`) |

Ne pas collecter de données personnelles superflues. Aucune valeur de
ce tableau ne doit être publiée sur le site.

Outils de mesure connus dans le dépôt (2026-10-12, détail et preuves
dans `BASELINE.md` § 2) : formulaires Web3Forms (réception par email,
pas de tableau de bord) ; événement `stage_form_success` poussé dans
`dataLayer` et `gtag` `generate_lead` sur la landing `/stages/`
uniquement, **sans aucun conteneur GA4 / GTM / Ads chargé : ces
événements ne sont envoyés nulle part**. Aucun identifiant Google
Analytics ou Google Ads n'est présent dans les sources ni dans
`prod-snapshot/` : à vérifier côté propriétaire.

## Qualité

Contrôles locaux de `QA_CHECKLIST.md`, exécutables sans accès externe.
Baseline relevée le 2026-10-12 sur `newsite/dist/` (voir `BASELINE.md` § 7).

| KPI | Baseline (2026-10-12) | Actuel | Période | Source | Formule | Dénominateur / unité | Objectif | Qualité |
|---|---|---|---|---|---|---|---|---|
| Build réussi | OK (0 assertion) | — | Chaque lot | `python3 build.py` | Réussite / échec | Par build | 100 % | A |
| dist/ reproductible | OK (identique au commit) | — | Chaque lot | `diff -rq` build ↔ `dist/` commité | Identique / différent (hors `sitemap.xml` lastmod) | Par build | Identique | A |
| Liens internes cassés | 0 | — | Chaque lot | Script `QA_CHECKLIST.md` § 4 | Nombre de `href` relatifs ou absolus sans cible dans `dist/` | 14 fichiers HTML | 0 | A |
| Liens internes en `.html` (301 interne) | 210 liens (dont 42 `cours-essai.html`, 34 `inscription.html`, 25 `acting.html`) | — | Chaque lot | grep | Nombre de liens `href="page.html"` vers des pages à URL propre | 14 fichiers HTML | Décision technical-seo | A |
| Pages avec title / description / H1 uniques | 14 / 14 | — | Chaque lot | Script § 3 | Pages conformes ÷ pages | 14 fichiers HTML | 14 / 14 | A |
| Canonicals cohérents avec le sitemap | 10 / 10 | — | Chaque lot | § 3 et § 5 | URLs du sitemap dont le canonical de la page = `<loc>` | 10 URLs | 10 / 10 | A |
| Blocs JSON-LD valides | 11 / 11 pages du site (0 sur les 3 landings) | — | Chaque lot | Script § 6 | Blocs parsables ÷ blocs ; types justifiés par le contenu | Pages avec JSON-LD | 100 % valides, 0 erreur dans les validateurs Google / Schema.org | A (syntaxe) / C (conformité au contenu, relecture) |
| Faits non validés publiés | 0 connu (FACTS_REGISTER « Vérifié » pour prix et dates) | — | Chaque lot | Relecture § 7 vs `FACTS_REGISTER.md` | Nombre d'affirmations publiques sans statut « Vérifié » | Affirmations sensibles (prix, dates, durées, promesses) | 0 | C (relecture humaine) |
| Erreurs JS au chargement | À mesurer (Playwright non installé dans l'environnement d'audit) | — | Chaque lot | Script § 8 | Nombre de `pageerror` sur les 13 URLs | 13 URLs × 2 viewports | 0 | A |
| Débordement horizontal mobile | À mesurer | — | Chaque lot | Script § 8 | Pages avec `scrollWidth > clientWidth` à 390 px | 13 URLs | 0 | A |
| Formulaires fonctionnels | À mesurer (8 formulaires : 5 pages + 3 landings) | — | Chaque lot | Script § 9 | Formulaires dont l'envoi intercepté et l'écran de succès sont OK ÷ formulaires | 8 formulaires | 8 / 8 | A |
| Poids HTML des pages | 78–118 Ko (`BASELINE.md`), vs 0,07–5,3 Mo avant refonte | — | Chaque lot | `ls -la newsite/dist` | Taille du HTML par page | Par page | Pas de régression > 10 % sans justification | A |
| Images > 300 Ko dans `uploads/` | 4 (`find -size +300k`, soit > 300 Kio) ; 5 selon INITIAL_STATE.md (seuil 300 000 octets) | — | Chaque lot | `find newsite/dist/uploads -size +300k` | Nombre de fichiers | 46 fichiers | Décision technical-seo | A |
| Codes HTTP en prod | Non testé (site injoignable depuis l'environnement) | — | Après chaque dépôt | `QA_CHECKLIST.md` § 10 (propriétaire) | URLs conformes ÷ URLs testées ; 404 réel sur URL inexistante | Liste § 10 | 100 % ; 404 = `404` | A quand exécuté |

## Rythme de suivi

- Technique : après chaque lot de changements.
- Search Console : suivi hebdomadaire ou mensuel selon le volume.
- Conversions : mensuel.
- Benchmark IA : mensuel au départ, puis ajusté selon les résultats.
- Revue stratégique : chaque mois.

## Interprétation

Documenter les changements du site, la saisonnalité, les campagnes,
les changements de modèle IA et les limites de chaque source.

Journal des événements à tenir en regard des courbes (à compléter) :

| Date | Événement | Impact attendu sur la mesure |
|---|---|---|
| Avant 2026-08 | Site WordPress (URLs inconnues dans le dépôt) | Données SC antérieures non comparables |
| 2026-08-03 → 2026-08-21 | Premier site statique, `.htaccess`, URLs propres | Changement d'URLs n° 1 |
| 2026-10-10 → 2026-10-12 | Refonte : `/uploads/` unique, landing `/stages/`, robots, sitemap, llms.txt, JSON-LD (voir `BASELINE.md` § 6) | Point zéro SEO / GEO ; poids des pages ÷ ~50 |
| À renseigner | Date du dépôt FTP de `dist/` actuel | T0 réel |
| À renseigner | Activation de l'outil de mesure (`MEASUREMENT_PLAN.md`) | Début des séries conversion |
| 2026-10-17/18, 11-07/08, 11-14/15 ; 2026-12-12/13 | Stages et JPO (FACTS_REGISTER) | Pics attendus de demandes « stage » et « JPO », indépendants du SEO |
| 2027-01-04 | Rentrée décalée | Pic « inscription » |

Une hausse de visibilité n'est pas nécessairement une hausse des
inscriptions. Une hausse des mentions IA n'est pas nécessairement
une hausse du trafic.

Chaque rapport doit distinguer observations, hypothèses et conclusions.
