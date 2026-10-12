# GEO Action Plan — Method Acting Center

Agent : geo-ai-visibility · Rédigé le 2026-10-12 · À arbitrer par le chef de projet.

Chaque action indique : raison, priorité (échelle `docs/IMPLEMENTATION_PLAN.md` : P1 blocage
ou erreur factuelle sur page clé → P4 expérimentation), preuve (où le constat a été fait),
méthode de mesure, limite connue, responsable pressenti, validation humaine requise.

Scores (CLAUDE.md §11) : impact 1-5 · confiance 1-5 · effort 1-5 · risque faible / moyen / élevé.

Rappels :
- Aucune action ne garantit une citation par une IA.
- Aucune modification du site sans passage par les sources (`newsite/pages`, `partials`,
  `static`, `build.py`) puis `python3 build.py`, puis validation, puis déploiement par le propriétaire.
- Aucune affirmation nouvelle (fondateur, anciens élèves, filiation) sans validation écrite et
  inscription dans `docs/FACTS_REGISTER.md`.

---

## Lot 1 — Corriger les sources que les IA citent déjà (hors site)

### G1. Mettre à jour ou neutraliser les fiches tierces obsolètes
- **Raison** : les requêtes tarifaires et « avis » renvoient en premier Emagister (250 €/mois, 3 jours d'essai, fiches 2017-2018), Gowork (105 B rue de Tolbiac) et L'Etudiant (créée en 2009, chant/danse). Ce sont les faits faux les plus probables dans une réponse IA.
- **Priorité** : P1 · impact 5 · confiance 4 · effort 2 · risque faible.
- **Preuve** : `CITATION_SOURCES.md` S01, S02, S03, S04, S06 (extraits de recherche du 2026-10-12).
- **Actions** (propriétaire, dans cet ordre) :
  1. Vérifier l'adresse du siège dans Sirene / INPI (annuaire-entreprises.data.gouv.fr). Si « rue de Tolbiac » y figure encore, déclarer le transfert : les agrégateurs (Gowork, Pappers, Societe.com…) se resynchronisent dessus.
  2. Emagister : se connecter au compte annonceur ; mettre à jour prix (dès 370 €/mois, 9 mensualités, 200 € de frais), durée (jusqu'à 4 ans), essai (2 cours gratuits), supprimer chant/danse/comédie musicale si non proposés ; sinon demander la suppression du centre.
  3. L'Etudiant : demander la correction de l'année (après avoir tranché 1999 vs 2009) et de la liste des formations.
  4. Gowork : revendiquer la fiche et corriger l'adresse.
  5. Evous : ouvrir la page, vérifier le numéro de téléphone ; si faux, demander correction par email à la rédaction.
  6. Spectable : confirmer ou retirer « Ados & enfants 100 €/mois » ; remplir les liens réseaux.
- **Mesure** : (a) re-lecture des fiches à J+30 ; (b) benchmark prompts C3, E2, E4, E6 : disparition des valeurs fausses (« 250 € », « Tolbiac », « 3 jours ») dans les réponses à J+90.
- **Limite** : délais de recrawl inconnus (semaines à mois) ; certaines plateformes ne corrigent pas ; les modèles sans recherche web conservent d'anciennes données tant qu'ils ne sont pas ré-entraînés.
- **Validation** : propriétaire (comptes, démarches administratives).

### G2. Trancher et documenter la date de création
- **Raison** : 1999 (site, JSON-LD, « 25+ ans ») contre 2009 (L'Etudiant). Une IA qui compare relèvera la contradiction ; le registre classe 1999 « À confirmer ».
- **Priorité** : P1 (erreur factuelle potentielle sur toutes les pages) · impact 3 · confiance 5 · effort 1 · risque faible.
- **Preuve** : `FACTS_REGISTER.md` (FACT-007, confiance moyenne) ; S01.
- **Action** : le propriétaire fournit la date réelle (ex. : date de création de la structure juridique vs date de début d'activité) ; si l'activité a commencé en 1999 sous une autre forme, l'écrire explicitement sur la future page À propos (« ateliers depuis 1999, société créée en 20XX »).
- **Mesure** : registre mis à jour ; prompt E1/E7 : date restituée correctement.
- **Limite** : aucune.

### G3. Vérifier le profil Trustpilot avant de le promouvoir
- **Raison** : le site affiche « Avis vérifiés Trustpilot » sur toutes les pages et l'URL est dans le `sameAs` ; l'extrait de recherche indique « 4,0/5, petit nombre d'avis ». Un écart 4,8 (Google) / 4,0 (Trustpilot) est un angle de réponse pour un prompt « limites » (E5).
- **Priorité** : P2 · impact 2 · confiance 2 (non vérifié) · effort 1 · risque faible.
- **Preuve** : S11 ; `ORG.sameAs` dans `build.py`.
- **Action** : ouvrir fr.trustpilot.com/review/methodacting.fr ; noter note, nombre, statut revendiqué ; décider de garder le lien partout, de le limiter, ou de solliciter des avis authentiques (jamais d'avis fabriqués ni achetés, CLAUDE.md §9).
- **Mesure** : registre complété (note Trustpilot datée).
- **Limite** : les notes évoluent ; ne jamais inscrire une note dans le JSON-LD sans la maintenir.

---

## Lot 2 — Corrections techniques à fort effet (site)

### G4. Corriger le canonical et les balises OG de `/stages/`
- **Raison** : `dist/stages/index.html` déclare `canonical = https://www.methodacting.fr/jpo/` et des `og:title` / `og:description` qui parlent des Portes Ouvertes. Les moteurs et crawlers IA traiteront la page stages comme un doublon de la landing JPO ; son contenu (stages, prix, dates) risque de ne pas être retenu.
- **Priorité** : P1 · impact 4 · confiance 5 · effort 1 · risque faible.
- **Preuve** : `AI_VISIBILITY_AUDIT.md` §2 ; extraction META de `dist/stages/index.html`.
- **Action** (technical-seo) : dans `tools/build_landing_stages.py`, réécrire `canonical` (→ `/stages/`), `og:title`, `og:description`, `og:url` ; rebuild ; vérifier.
- **Mesure** : après déploiement, `curl -s https://www.methodacting.fr/stages/ | grep canonical` ; Search Console → page indexée avec sa propre canonique.
- **Limite** : décider en parallèle si les landings Ads doivent rester indexables (si non : `noindex` et le problème disparaît autrement).

### G5. Redirections 301 des anciennes URLs et page 404 réelle
- **Raison** : des URLs de l'ancien site (`/portes-ouvertes-septembre-2021/`, `/contact.html`, `/tarifs/`) sont encore dans les index. `.htaccess` : section 301 vide, `ErrorDocument 404 /index.html` (accueil servie sous 404). Un assistant qui suit un vieux lien voit la page d'accueil avec un statut d'erreur, ou un contenu 2021.
- **Priorité** : P2 · impact 3 · confiance 3 (codes HTTP non vérifiés depuis l'environnement) · effort 2 · risque faible.
- **Preuve** : S16 ; `newsite/static/.htaccess`.
- **Action** (technical-seo + propriétaire) : exporter les URLs indexées (Search Console, « Pages ») ; définir une table ancienne → nouvelle ; ajouter les `RewriteRule … [R=301,L]` ; créer une vraie page 404 légère (ou garder l'accueil mais vérifier que le code reste 404 et non 200).
- **Mesure** : `curl -I` sur chaque ancienne URL → 301 vers la bonne page ; Search Console : disparition des anciennes URLs.
- **Limite** : la liste complète des anciennes URLs n'est pas connue sans Search Console ; `prod-snapshot/` ne contient pas l'ancien WordPress.

### G6. JSON-LD : logo, prix mensuel, horaires visibles, aggregateRating
- **Raison** : (a) `logo` est une photo de scène ; (b) `Course.offers.price = 370` sans unité de temps peut être lu comme prix total ; (c) horaires présents en JSON-LD mais absents du texte ; (d) `aggregateRating` auto-déclaré non éligible aux résultats enrichis et sujet à dérive.
- **Priorité** : P2 · impact 3 · confiance 4 · effort 2 · risque faible.
- **Preuve** : `AI_VISIBILITY_AUDIT.md` §4.2 J1, J2, J3, J7.
- **Action** (technical-seo) : fournir un logo (propriétaire) ; `UnitPriceSpecification` (unitText « mois ») + mention du coût annuel de base ; afficher les horaires sur /contact et dans le footer ; décision propriétaire sur `aggregateRating` (retirer, ou maintenir avec mise à jour à chaque build via une constante datée).
- **Mesure** : validateur Schema.org / test des résultats enrichis sans erreur ; prompts E2/C3 : prix restitué « par mois ».
- **Limite** : les données structurées n'influencent pas directement les modèles sans recherche web ; effet sur Google uniquement probable.

### G7. Harmoniser le nommage des stages
- **Raison** : « Actors Studio A / B » sur `/stages/` vs « Stage A — Initiation à la Méthode / Stage B — Approche d'une scène » partout ailleurs (y compris JSON-LD). « Actors Studio A » peut être lu comme un cours de l'Actors Studio (New York).
- **Priorité** : P2 · impact 2 · confiance 5 · effort 1 · risque faible.
- **Preuve** : `dist/stages/index.html` (H3 « Actors Studio A — … ») vs `dist/stages.html`.
- **Action** : le propriétaire choisit le nom officiel ; mise à jour de `SESSIONS` dans `tools/build_landing_stages.py`.
- **Mesure** : grep « Actors Studio A » dans `dist/` = 0 occurrence après rebuild (si ce nom est abandonné).
- **Limite** : si « Actors Studio A » est le nom commercial historique, le garder mais l'expliciter (« Stage A (dit « Actors Studio A ») »).

### G8. Retirer ou actualiser l'offre expirée des landings
- **Raison** : `/jpo/` et `/jposr/` affichent « 100 € de remise sur les frais d'inscription… offre valable jusqu'au 31/08/2026 » (date dépassée au 2026-10-12) et une case à cocher « rentrée décalée de janvier 2027, 100 € de remise ». Une IA peut citer une offre caduque ; risque commercial.
- **Priorité** : P1 (offre commerciale potentiellement fausse) · impact 3 · confiance 5 · effort 1 · risque faible.
- **Preuve** : extraction texte de `dist/jpo/index.html` et `dist/jposr/index.html`.
- **Action** : propriétaire : l'offre est-elle prolongée pour janvier 2027 ? Si oui, nouvelle date ; sinon retrait (CLAUDE.md §9 : pas de modification d'offre sans validation).
- **Mesure** : grep « 31/08/2026 » dans `dist/` = 0.
- **Limite** : aucune.

### G9. Générer `llms.txt` depuis `build.py`
- **Raison** : fichier maintenu à la main alors que prix, dates, note et JPO vivent dans `build.py`, `pages/` et `build_landing_stages.py` → dérive certaine à la prochaine saison. Effet du fichier sur les IA non démontré : la seule chose qui compte est qu'il ne dise jamais rien de faux.
- **Priorité** : P3 · impact 1 · confiance 4 · effort 2 · risque faible.
- **Preuve** : `AI_VISIBILITY_AUDIT.md` §5.1.
- **Action** (technical-seo) : constantes partagées (tarifs, dates, note datée) ; `llms.txt` écrit par `build()`.
- **Mesure** : diff entre `llms.txt` et pages = 0 écart à chaque build.
- **Limite** : ne pas présenter ce fichier comme un levier de citation.

---

## Lot 3 — Contenus qui répondent aux questions que les IA posent (site)

### G10. Page « L'école » (À propos) : histoire, fondateur, équipe, statut
- **Raison** : aucune page ne dit qui dirige, qui enseigne, depuis quand exactement, sous quel statut. Les meilleures preuves externes de l'école (livre « Stan ou Le solfège de l'acting », BnF 2017 ; « Stanislavski and The Method for the 21st Century Actor », Bloomsbury 2024, par David Barrouk) ne sont citées nulle part. Les prompts E1, E5, E7, E8, B5 n'ont aujourd'hui aucune réponse sur le site.
- **Priorité** : P2 · impact 4 · confiance 4 · effort 3 · risque moyen (bios, droit à l'image, exactitude).
- **Preuve** : `AI_VISIBILITY_AUDIT.md` §1.4, §3 ; S12, S13.
- **Action** (content-strategist rédige le brouillon dans `docs/content/drafts/` ; propriétaire valide) :
  - histoire datée (1999 / 2009, voir G2), lieux successifs (Tolbiac → avenue d'Italie, avec dates : cela neutralise aussi l'ancienne adresse) ;
  - fondateur : nom complet, parcours **vérifié et autorisé** (le registre note « À confirmer ») ; ses deux livres avec ISBN et lien BnF ;
  - équipe : noms, fonction, 2-3 lignes **avec consentement** ; sinon ne pas nommer ;
  - statut : établissement privé (hors contrat ?), diplôme délivré ou non, pas de financement CPF (si c'est le cas) : dire les limites plutôt que les laisser deviner ;
  - JSON-LD : `founder` (`Person`, `sameAs` data.bnf.fr), `Book` × 2 (`author` = fondateur, `publisher`, `isbn`).
- **Mesure** : prompts E7, E8, B5 : nom du fondateur et titres des livres restitués, avec source = methodacting.fr ou BnF.
- **Limite** : dépend entièrement des validations ; sans elles, publier seulement le statut et l'histoire institutionnelle.

### G11. Clarifier la filiation pédagogique (Stanislavski / Method / approches actuelles)
- **Raison** : le site présente « Stanislavski / Actors Studio » comme un bloc, se dit « descendant direct », et liste des acteurs (Meryl Streep, DiCaprio…) dont le lien avec la Method est discutable. CLAUDE.md §6 impose de distinguer le système de Stanislavski, les approches américaines et les techniques contemporaines. Une IA bien informée relèvera l'approximation ; une IA mal informée amplifiera l'affiliation supposée à l'Actors Studio (prompt E8).
- **Priorité** : P2 · impact 3 · confiance 4 · effort 2 · risque faible.
- **Preuve** : `dist/acting.html`, `dist/index.html` (texte « descendant direct », liste d'acteurs) ; §6 de l'audit.
- **Action** (content-strategist + propriétaire) : reformuler sur index, acting, landings : « pédagogie fondée sur le système de Stanislavski et sur ses développements américains (la « Méthode » de l'Actors Studio), adaptée au jeu caméra » ; retirer « descendant direct » ou le justifier (qui a formé le fondateur, où) ; retirer ou nuancer la liste d'acteurs ; ajouter une courte page ou section « La Méthode expliquée » (intention 8) : ce que l'école enseigne concrètement (3 temps, exercices nommés : backstory, moment à moment, composition, mini-scènes) et ce qu'elle n'enseigne pas (Meisner, Chekhov… sauf si vrai).
- **Mesure** : prompt B3 / E3 / E8 : la réponse distingue correctement et ne parle plus d'affiliation.
- **Limite** : la version exacte des exercices est « À confirmer » dans le registre ; ne publier que ce que le fondateur valide.

### G12. Documenter ou retirer les preuves « Nos acteurs tournent ! »
- **Raison** : 8 affiches sans nom ni lien ; les noms de fichiers désignent des actrices connues (Olga Kurylenko, Mylène Jampanoï, Jemima West…). Sans texte, c'est invérifiable et, si une IA l'extrapole (« formée au Method Acting Center »), c'est potentiellement faux ou non consenti.
- **Priorité** : P1 (preuve non sourcée sur pages clés) · impact 4 · confiance 4 · effort 2 · risque moyen.
- **Preuve** : `dist/index.html`, `dist/acting.html` (alt « Affiche · … »), `dist/uploads/` (noms de fichiers).
- **Action** (propriétaire) : pour chaque affiche, fournir : nom de l'ancien élève, période / atelier suivi, preuve (crédit, interview, autorisation écrite). Publier une légende sobre (« X, élève de 20XX à 20XX ») uniquement avec consentement ; sinon retirer l'affiche. Idem pour « Nos réalisateurs tournent ! » : distinguer les films du fondateur de ceux des anciens élèves.
- **Mesure** : registre « Témoignages et résultats » complété ; 0 affiche sans légende validée.
- **Limite** : la plupart des affiches partiront probablement ; c'est préférable à une preuve inexploitable.

### G13. FAQ « questions que l'on pose à une IA » sur les pages clés
- **Raison** : les assistants restituent bien les paires question/réponse courtes et sourcées. Les questions récurrentes sans réponse sur le site : débutant accepté ? âge minimum ? diplôme ? financement ? durée minimale d'engagement ? niveau d'anglais pour Acting in English ? cours ados ? horaires d'ouverture ? « reconnu par l'État » ?
- **Priorité** : P2 · impact 3 · confiance 4 · effort 2 · risque faible (si réponses validées).
- **Preuve** : `AI_VISIBILITY_AUDIT.md` §3 (manques 2, 3, 4) ; la FAQ existante de /tarifs est le bon modèle (texte visible = JSON-LD).
- **Action** (content-strategist rédige, propriétaire valide) : 5-8 Q/R sur /acting, /scenario-real, /cours-essai, /stages.html ; `FAQPage` correspondant dans `jsonld()`. Réponses honnêtes y compris négatives (« pas de diplôme d'État », « pas éligible CPF ») si c'est le cas.
- **Mesure** : prompts A3, A7, E5, E9 : réponses alignées sur la FAQ ; Search Console : impressions sur requêtes-questions.
- **Limite** : Google n'affiche plus les FAQ enrichies pour la plupart des sites ; l'intérêt est le contenu lisible, pas le rich result.

### G14. Page dédiée « Jeu face caméra à Paris »
- **Raison** : intention prioritaire n° 3 ; aujourd'hui le sujet est dispersé (module 4e année, atelier « sur demande », stage « tarif sur demande »). Le prompt A2 n'a pas de page cible.
- **Priorité** : P2 · impact 3 · confiance 3 · effort 3 · risque faible.
- **Preuve** : audit §3 (manque 7) ; `dist/stages.html` (stage Acting Caméra), `dist/acting.html` (4e année).
- **Action** (content-strategist) : une page qui explique ce qui est enseigné face caméra (marques, valeur de cadre, continuité, tournage dans le désordre : contenu déjà présent sur le stage), à quel moment du cursus, dans quel atelier, à quel prix (quand il est connu), avec les scènes filmées / bande démo comme livrables. Pas de duplication des pages existantes : les relier.
- **Mesure** : prompts A2, F3 ; impressions Search Console « jeu face caméra Paris ».
- **Limite** : ne pas créer une page par mot-clé (CLAUDE.md §6) ; une seule page, utile.

### G15. Version anglaise minimale
- **Raison** : ateliers « Acting in English » et « Screenwriting in English », avis d'élèves internationaux, prompts anglais plausibles (A6, B6, E9) ; aucun contenu anglais sur le site ; Cours Florent occupe seul ce terrain dans les résultats.
- **Priorité** : P3 · impact 2 · confiance 3 · effort 3 · risque faible.
- **Preuve** : audit §3 (manque 10) ; WebSearch « acting in English Paris » (Cours Florent, BAW, Playhouse).
- **Action** : une page `/en/` (ou `/acting-in-english`) décrivant les deux ateliers, horaires, niveau requis, prix (quand connu), cours d'essai ; `hreflang` ; `inLanguage: en`.
- **Mesure** : prompts A6, B6, E9 ; trafic organique EN.
- **Limite** : demande réelle à confirmer avec le propriétaire (nombre d'élèves anglophones).

### G16. Afficher les dates de mise à jour et des informations pratiques visibles
- **Raison** : les assistants privilégient les contenus datés et cohérents ; horaires d'ouverture absents du texte ; aucune page n'indique sa date de mise à jour.
- **Priorité** : P3 · impact 2 · confiance 3 · effort 1 · risque faible.
- **Action** : « Tarifs 2026-2027, mis à jour le JJ/MM/AAAA » sur /tarifs et /planning ; horaires sur /contact et footer ; `dateModified` réel dans `WebPage` (généré au build par page, pas la date globale du build).
- **Mesure** : présence dans `dist/` ; aucun KPI direct.
- **Limite** : `lastmod` du sitemap est aujourd'hui la date du build pour toutes les pages, ce qui le rend peu fiable ; corriger en même temps.

---

## Lot 4 — Présence externe et graphe de connaissances

### G17. Fiche Google Business : la source locale des IA
- **Raison** : Gemini et les fonctionnalités IA de Google s'appuient sur la fiche (catégorie, description, horaires, services, Q&R, posts). C'est aussi l'origine de la note 4,8/5. Non auditable depuis ici.
- **Priorité** : P2 · impact 4 · confiance 3 · effort 1 · risque faible.
- **Action** (propriétaire) : vérifier catégorie principale (« École d'art dramatique ») et secondaires (école de cinéma, cours de théâtre), description (reprendre le résumé de llms.txt), site web = `https://www.methodacting.fr/`, horaires = registre, services (formations, stages, cours d'essai gratuit), publier les JPO et stages en « Événements », répondre aux Q&R avec les mêmes faits que le site ; vérifier qu'aucune ancienne fiche « rue de Tolbiac » ne subsiste (doublon à fusionner / fermer).
- **Mesure** : prompts A1, A4, E4 sur Gemini ; vues et actions de la fiche (Insights).
- **Limite** : pas d'accès agent ; dépend des outils Google.

### G18. Mentions éditoriales fraîches et datées (JPO, stages, livre)
- **Raison** : les sources positives trouvées datent de 2018-2025 (Que Faire à Paris, Paris Étudiant, Sortiraparis, ProfilCulture). Rien de récent pour 2026-2027. Les IA avec recherche web citent les pages fraîches.
- **Priorité** : P2 · impact 3 · confiance 3 · effort 2 · risque faible.
- **Preuve** : S07-S10.
- **Action** (digital-pr, **après accord du propriétaire pour tout contact**) : déposer les JPO des 12-13 déc. 2026 et les stages sur Que Faire à Paris, Paris Étudiant, ProfilCulture, Sortiraparis ; proposer un angle « le fondateur publie chez Bloomsbury un guide Stanislavski/Method » à la presse spécialisée (si G10 validé). Aucun achat de lien, aucun avis sollicité contre avantage.
- **Mesure** : nombre de mentions datées 2026-2027 ; sources citées par les IA dans le benchmark (part des sources tierces récentes).
- **Limite** : les agendas ne font pas autorité sur les prix ; ils renforcent la fraîcheur et les dates, pas la crédibilité pédagogique.

### G19. Entrée Wikidata / Wikipédia : ne pas forcer
- **Raison** : aucune entrée trouvée. Les graphes de connaissances aident à désambiguïser, mais une création auto-promotionnelle sans sources secondaires indépendantes serait supprimée et nuirait à la réputation.
- **Priorité** : P4 · impact 2 · confiance 2 · effort 2 · risque moyen.
- **Action** : attendre d'avoir ≥ 2-3 sources secondaires indépendantes (presse, ouvrage tiers). Le livre Bloomsbury du fondateur peut justifier une entrée **sur l'auteur** (notoriété par publication), pas nécessairement sur l'école.
- **Mesure** : n/a.
- **Limite** : critères de notoriété ; ne jamais rédiger soi-même un article Wikipédia sur son organisation.

---

## Lot 5 — Mesure

### G20. Baseline et suivi
- **Raison** : sans état initial, impossible d'attribuer un changement.
- **Priorité** : P2 · impact 3 · confiance 5 · effort 2 · risque faible.
- **Actions** :
  1. Exécuter le benchmark complet (`AI_PROMPT_BENCHMARK.md`) **avant** toute modification du site : c'est la baseline. Stocker dans `docs/geo/runs/2026-MM-JJ/`.
  2. Exploiter le champ existant des formulaires « Comment avez-vous connu Method Acting Center ? → Recherche IA (ChatGPT, etc.) » : demander à analytics-qa d'extraire mensuellement le nombre de demandes par source (Web3Forms).
  3. Demander à l'hébergeur (OVH) l'accès aux logs serveur : compter les hits de `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`, `Google-Extended` par page et par mois (preuve que les pages sont lues par les assistants).
  4. Search Console : requêtes de marque, requêtes-questions, impressions des pages clés.
- **Mesure** : taux de présence / exactitude / confusion par bloc A-F et par plateforme (définis dans le benchmark), suivi trimestriel ; nombre de demandes « Recherche IA » ; hits de robots IA.
- **Limite** : corrélation seulement ; les plateformes changent de modèle entre deux runs ; les logs n'indiquent pas si une page a été citée.

---

## Décisions nécessitant le propriétaire (récapitulatif)

| # | Décision | Bloque |
|---|---|---|
| D1 | Date de création réelle (1999 / 2009) et formulation autorisée | G2, G10, G1 |
| D2 | Nom complet et biographie publiable du fondateur ; mention de ses livres | G10, J4 |
| D3 | Noms et bios des coachs (consentement) | G10 |
| D4 | Preuves et consentements pour chaque affiche « Nos acteurs / réalisateurs tournent » | G12 |
| D5 | Statut de l'école (hors contrat ?), diplôme délivré ou non, financements acceptés | G10, G13 |
| D6 | Sort de l'offre « 100 € de remise » expirée | G8 |
| D7 | Nom officiel des stages (« Stage A » vs « Actors Studio A ») | G7 |
| D8 | Maintien de `aggregateRating` dans le JSON-LD et du lien Trustpilot | G6, G3 |
| D9 | Accès : comptes Emagister / L'Etudiant / Gowork / Google Business, Search Console, logs OVH | G1, G17, G20 |
| D10 | Autorisation de tout contact externe (agendas, presse) | G18 |
| D11 | Existence et prix du cours ados/enfants | G1 (Spectable), G13 |
| D12 | Adresse du siège dans Sirene / INPI | G1 |

## Ordre d'exécution proposé

1. Baseline benchmark (G20.1) — propriétaire, avant tout changement.
2. G4, G8 (correctifs immédiats, faible risque) — technical-seo, propriétaire.
3. G1, G2, G12, D1-D5 (vérité factuelle, hors site et sur site) — propriétaire.
4. G6, G7, G5, G17 — technical-seo, propriétaire.
5. G10, G11, G13, G14 — content-strategist (brouillons), validation, build, QA.
6. G18, G15, G16, G9 — digital-pr, content, technical.
7. Re-run benchmark à J+90 après déploiement ; comparer à la baseline ; réviser ce plan.
