# Inventaire des URLs — Method Acting Center

Agent : seo-auditor · Date : 2026-10-12 · Source auditée : `newsite/dist/` (arborescence exacte déployée sur https://www.methodacting.fr/).

**Limite importante** : le site en production n'était pas joignable depuis l'environnement d'audit (le proxy sortant refuse les connexions, `CONNECT 403`, vers methodacting.fr comme vers tout domaine tiers). Les codes HTTP, l'indexation réelle, les Core Web Vitals et les données Search Console n'ont donc **pas** été vérifiés en ligne. Tout ce qui suit est déduit des fichiers de `dist/`, de `static/.htaccess`, de `build.py` et du snapshot `prod-snapshot/`. Un crawl complet (Screaming Frog ou équivalent) reste à faire après déploiement.

## Vue d'ensemble

| Indicateur | Valeur |
|---|---|
| Pages HTML dans `dist/` | 14 (10 pages de site + `/tarifs/index.html` copie + 3 landings Ads) |
| URLs dans `sitemap.xml` | 10 (les 3 landings et `/tarifs/` n'y figurent pas, volontairement) |
| Pages avec `<title>` unique | 13 / 14 (`/tarifs` et `/tarifs/` identiques, attendu) |
| Pages avec canonical | 14 / 14 (mais `/stages/` en a **deux**, contradictoires) |
| Pages avec meta robots `index, follow` | 14 / 14 (aucun `noindex` nulle part, y compris sur les landings Ads) |
| Pages avec JSON-LD | 11 / 14 (aucune sur `/jpo/`, `/jposr/`, `/stages/`) |
| Pages avec un seul H1 | 14 / 14 |
| Favicon / `rel="icon"` | 0 / 14 (aucun fichier favicon dans `dist/`) |
| Liens internes en `page.html` déclenchant une 301 | sur **toutes** les pages (header, footer, corps) |
| Images sans `alt` ou `alt=""` | 8 sur `/`, 8 sur `/acting`, 11 sur `/scenario-real` (doublons de carrousel `aria-hidden`), 8–11 sur chaque landing (`<img data-img>` sans attribut `alt`) |
| Poids HTML (CSS/JS intégrés) | 77–115 Ko par page ; `uploads/` = 6,9 Mo (46 fichiers) |
| Balise de mesure (GA4 / GTM / Ads) | aucune installée (la landing `/stages/` pousse un `dataLayer` mais aucune balise n'est présente, cf. commentaire ligne 14 de `dist/stages/index.html`) |

Comparaison avec `prod-snapshot/` (prod avant mise en conformité) : mêmes titres et mêmes textes, mais **aucun** canonical, aucune meta robots, aucun JSON-LD, pas de `robots.txt`, pas de `sitemap.xml`, images en base64 (24 sur l'accueil). La version `dist/` est donc un net progrès technique ; les problèmes listés ci-dessous sont ceux qui subsistent.

## Convention

- Liens internes entrants : d'après les `href` des 14 pages. Toutes les pages du site (hors landings) se lient mutuellement via le header et le footer ; je n'indique donc que les liens « de corps » notables et les liens depuis les landings.
- Les numéros de ligne renvoient aux **sources** (`newsite/pages/`, `newsite/partials/`, `newsite/build.py`, `newsite/static/`) quand elles existent, sinon à `dist/`.

---

## 1. `/` — Accueil

| Champ | Observation |
|---|---|
| Fichier | `dist/index.html` ← `pages/index.html` + partials |
| Type / intention | Accueil, navigation + découverte (intention 7 « Découvrir le Method Acting Center ») |
| Sujet principal | École d'acteurs, scénaristes, réalisateurs à Paris ; « la Méthode » |
| `<title>` (72 car.) | `Method Acting Center — Devenir Acteur, Scénariste ou Réalisateur à Paris` |
| H1 | `Le talent, ça s'apprend.` (aucun mot-clé thématique) |
| Meta description (135) | `École de cinéma à Paris depuis 1999 : formations Acteur, Scénariste et Réalisateur autour de la Méthode (Stanislavski / Actors Studio).` |
| Canonical | `https://www.methodacting.fr/` ✔ |
| Indexabilité | `index, follow` ; dans le sitemap (prio 1.0) |
| JSON-LD | Organization (EducationalOrganization + LocalBusiness), WebSite, WebPage, Event (JPO 12-13 déc.) |
| Liens entrants | brand header/footer de toutes les pages (`href="index.html"` → **301** vers `/`) ; les 3 landings (`https://www.methodacting.fr/`) |
| Contenu | ~1 140 mots ; 2 cartes formations, 3 piliers, 3 portes d'entrée, 6 avis Google, carrousel d'affiches |
| Fraîcheur | Phrase « Vous avez raté les Portes Ouvertes ? » (`pages/index.html:30`) alors que les prochaines JPO sont dans 2 mois : copie dépendante du calendrier |
| CTA | Cours d'essai gratuit (×3), Découvrir l'école, Voir les stages |
| Problèmes | (1) H1 et title sans « école d'acting / cours de cinéma » ; (2) affirmations non vérifiables : « descendant direct » de Stanislavski (`index.html:87,156`) ; (3) carrousel d'affiches (Quantum of Solace, Martyrs, Le Procès Goldman… `index.html:206-213`) présenté comme preuve « Nos anciens jouent dans… » sans nom d'ancien élève ni source ; (4) 8 `alt=""` (doublon aria-hidden, acceptable) ; (5) `alt` du hero contient `&rsquo;` encodé dans l'attribut (rendu correct, mais à harmoniser). |
| Action | Reformuler title (ex. intégrer « École d'acting à Paris ») et sous-titre ; retirer ou sourcer la phrase « descendant direct » ; documenter les anciens élèves avant de garder le carrousel (cf. FACTS_REGISTER « À confirmer ») ; rendre la phrase JPO indépendante de la date. |

## 2. `/acting` — Formation Acting

| Champ | Observation |
|---|---|
| Fichier | `dist/acting.html` ← `pages/acting.html` |
| Type / intention | Page formation (intentions 1, 2, 3 : Stanislavski Paris, école acteur cinéma, jeu face caméra) |
| `<title>` (62) | `Formation Acting — Devenir Acteur — Method Acting Center Paris` |
| H1 | `Apprendre à jouer vrai.` |
| Meta description (156) | OK en longueur ; cite Stanislavski / Actors Studio et « face caméra » |
| Canonical | `https://www.methodacting.fr/acting` ✔ |
| Indexabilité | index ; sitemap prio 0.9 |
| JSON-LD | + `Course` (prix 370 €/mois, CourseInstance hebdo, « 2 ateliers de 4 h par semaine en 1re et 2e année ») — cohérent avec `/inscription` |
| Liens entrants | nav « Formations › Acting », footer, `/` (carte), `/tarifs` (« Le programme »), `/planning` (×3 « Voir »), landings (`acting.html` absolu → 301) |
| Contenu | ~1 390 mots ; programme 4 ans détaillé (ateliers nommés), cours à l'unité, 6 avis, affiches |
| CTA | JPO, Tester en stage, Voir les tarifs, « Réserver ma place » (JPO) — **aucun CTA direct vers /inscription ni /cours-essai dans le corps** |
| Problèmes | (1) title sans « cinéma » ni « Stanislavski » alors que c'est la page cible de ces requêtes ; (2) `alt` des 3 visuels Méthode = « Déclencher », « Maîtriser », « Reproduire » (`acting.html:39,44,49`) alors que le 3e H3 dit « Composer » (`:50`) — incohérence et alt non descriptifs ; (3) « La méthode de Marlon Brando, Meryl Streep, Joaquin Phoenix, Leonardo DiCaprio, Jack Nicholson… » (`acting.html:8`) : affirmation non sourçable et discutable (plusieurs de ces acteurs n'ont pas été formés à la Méthode Strasberg) ; (4) 8 affiches dupliquées de l'accueil ; (5) pas de FAQ (débutant ? prérequis ? âge ? horaires ?) ; (6) rien sur les coachs (noms, parcours). |
| Action | Title/H1 orientés requête ; corriger alt ; retirer ou reformuler la liste d'acteurs célèbres ; ajouter FAQ et bloc « vos coachs » après validation propriétaire ; ajouter CTA cours d'essai + inscription. |

## 3. `/scenario-real` — Scénario, Réalisation & Direction d'acteurs

| Champ | Observation |
|---|---|
| Fichier | `dist/scenario-real.html` ← `pages/scenario-real.html` |
| Type / intention | Page formation (intention 5 : acting + scénario + réalisation) |
| `<title>` (72) | `Scénario, Réalisation & Direction d'acteurs — Method Acting Center Paris` (pas le mot « formation » ni « Paris » avant la marque) |
| H1 | `Racontez vos propres histoires.` |
| Meta description (178) | trop longue de ~20 car., répétitive (« direction d'acteurs » ×2) |
| Canonical | ✔ `/scenario-real` |
| JSON-LD | + `Course` (350 €/mois ; « 26 samedis de 8 h en 1re année, 24 dimanches de 5 h en 2e année ») — cohérent avec `/inscription` et `/planning` |
| Liens entrants | nav, footer, `/` (carte), `/tarifs`, `/planning` (×2), `/cours-essai` (implicite), landings (301) |
| Contenu | ~1 025 mots ; références McKee, Truby, Schrader, Packard ; programme 2 ans ; option tournage ; 11 affiches ; 3 avis |
| CTA | JPO, Tester en stage, Voir les tarifs, Nous écrire |
| Problèmes | (1) 7 affiches avec `alt="Film réalisé par un ancien du programme"` et noms de fichiers IMDb (`MV5B….jpg`, `95495ae71c-poster.jpg`) : non descriptif, non vérifiable, droits d'image à confirmer ; (2) « quasi inexistant en France », « une notion rare en France » (`scenario-real.html:32,37`) : affirmation concurrentielle non sourcée ; (3) la page ne répond pas à « combien d'heures / quel niveau / quel diplôme » (aucune certification mentionnée — c'est un fait à afficher explicitement) ; (4) description trop longue. |
| Action | Title « Formation Scénario, Réalisation & Direction d'acteurs à Paris » ; alt nommant le film et l'auteur quand autorisé ; préciser statut (pas de titre RNCP) ; FAQ. |

## 4. `/stages.html` — Stages (page du site)

| Champ | Observation |
|---|---|
| Fichier | `dist/stages.html` ← `pages/stages.html` ; URL **avec** extension (exception `.htaccess:44-45`) |
| Type / intention | Page offre (intention 6 : stage d'acting accessible aux débutants) |
| `<title>` (82) | `Stages d'acting & de scénario — week-end et intensifs — Method Acting Center Paris` → tronqué en SERP |
| H1 | `Un week-end pour tester la Méthode, pour de vrai.` |
| Meta description (153) | OK |
| Canonical | ✔ `/stages.html` |
| JSON-LD | + 6 `Event` (3 avec prix 160 €, 3 sans prix) |
| Liens entrants | nav, footer, `/` , `/acting`, `/scenario-real`, `/tarifs`, `/planning` (9 liens dont 6 avec `?stage=…#reservation`), `/cours-essai`, `/inscription`, landings `/jpo/` et `/jposr/` et `/stages/` (absolu) |
| Contenu | ~1 830 mots ; 4 stages week-end détaillés, intensifs, formulaire multi-choix, 6 avis |
| CTA | Réserver (×8), Cours d'essai, JPO, Inscription |
| Problèmes | (1) **Cannibalisation avec `/stages/`** (landing Ads, indexable, title mieux ciblé « Stages d'acting à Paris ») ; (2) title trop long ; (3) H1 sans « stage » ; (4) dates « 17 & 18 octobre » codées en dur à 6 endroits du site (stages, tarifs ×2, planning, landings) → risque de contenu périmé après le 18/10 ; (5) les `Event` passés resteront dans le JSON-LD tant que `build.py` n'est pas édité ; (6) liens internes paramétrés `stages.html?stage=a#reservation` : canonical gère, mais multiplie les URLs crawlées. |
| Action | Décider du sort de `/stages/` (noindex ou canonical) ; raccourcir le title (« Stages d'acting à Paris — week-end & intensifs \| Method Acting Center ») ; centraliser les dates dans `build.py` ; purger automatiquement les Event passés. |

## 5. `/cours-essai` — Cours d'essai gratuit

| Champ | Observation |
|---|---|
| Fichier | `dist/cours-essai.html` ← `pages/cours-essai.html` |
| Type / intention | Conversion (CTA principal du site) ; intention 6/7 |
| `<title>` (50) | `Cours d'essai gratuit — Method Acting Center Paris` ✔ |
| H1 | `Essayez un cours, gratuitement.` |
| Meta description (150) | ✔ |
| Canonical | ✔ |
| JSON-LD | + `Offer` prix 0 |
| Liens entrants | bandeau d'annonce (toutes pages), nav, footer, `/` (×4), `/tarifs` (×4), `/stages.html`, `/inscription`, `/planning`, landings (`cours-essai.html#reservation`) |
| Contenu | ~1 270 mots ; ateliers testables avec créneaux (jours/heures), formulaire, 3 avis |
| Problèmes | (1) « Vous avez raté les Portes Ouvertes ? » (`cours-essai.html:11`) dépendant du calendrier ; (2) créneaux horaires codés en dur (`:76-110`) — source de vérité ? (FACTS : horaires exacts « À confirmer ») ; (3) pas de mention du public (âge minimum ? débutants ?). |
| Action | Rendre la copie intemporelle ; vérifier les créneaux avec le propriétaire ; ajouter 2-3 questions fréquentes. |

## 6. `/jpo.html` — Journées Portes Ouvertes (page du site)

| Champ | Observation |
|---|---|
| Fichier | `dist/jpo.html` ← `pages/jpo.html` ; URL avec extension |
| `<title>` (72) | `Journées Portes Ouvertes — 12 & 13 décembre — Method Acting Center Paris` (sans année) |
| H1 | `Venez vivre la Méthode.` |
| Meta description (179) | trop longue |
| Canonical | ✔ `/jpo.html` |
| JSON-LD | + `Event` JPO (gratuit) |
| Liens entrants | nav « Portes Ouvertes », footer, `/`, `/acting` (×2), `/scenario-real` (×2), `/contact`, `/tarifs`, `/planning` (×2), `/stages.html`, `/cours-essai`, `/inscription`, landing `/stages/` |
| Contenu | ~1 080 mots ; ateliers par public, planning du week-end (sans horaires : « Les horaires détaillés arrivent »), formulaire (liste d'ateliers injectée en JS `site.js:124-132`, mais le contenu équivalent existe en HTML au-dessus), 3 avis dont 1 Trustpilot |
| Problèmes | (1) **3 pages JPO indexables** : `/jpo.html`, `/jpo/`, `/jposr/` (voir § 11-12) ; (2) « ce que presque aucune école ne propose » (`jpo.html:80`) non sourcé ; (3) après le 13/12 la page doit être mise à jour manuellement (dates dans title, texte, JSON-LD). |
| Action | Clarifier la hiérarchie JPO (page site = canonique) ; évergreeniser (« prochaine session » générée depuis `build.py`). |

## 7. `/inscription` — Demande d'inscription

| Champ | Observation |
|---|---|
| Fichier | `dist/inscription.html` ← `pages/inscription.html` |
| `<title>` (40) | `Inscription — Method Acting Center Paris` |
| H1 | `Demandez votre inscription.` |
| Meta description (194) | trop longue |
| Canonical | ✔ |
| JSON-LD | Organization/WebSite/WebPage seulement |
| Liens entrants | CTA header « S'inscrire » (toutes pages), footer, `/tarifs` (×6 dont `?programme=`), `/planning` (×3), `/cours-essai`, `/stages.html`, landings (`inscription.html#formulaire`) |
| Contenu | ~1 345 mots ; **la page la plus précise du site sur les volumes horaires** (2×4 h/sem, 26 samedis de 8 h…), ateliers à l'unité, lien PDF planning hebdo, 3 avis |
| Problèmes | (1) ces informations clés (volumes horaires, année d'entrée sur audition) ne sont pas sur `/acting` et `/scenario-real` où les visiteurs les cherchent ; (2) description trop longue ; (3) « Septembre 2026 (en cours) » dans le select (`:194`) → à faire vivre. |
| Action | Remonter les volumes horaires sur les pages formation ; raccourcir description. |

## 8. `/tarifs` — Tarifs

| Champ | Observation |
|---|---|
| Fichier | `dist/tarifs.html` ← `pages/tarifs.html` |
| Type / intention | Comparaison / prix (intention 4) |
| `<title>` (35) | `Tarifs — Method Acting Center Paris` (court : place pour « formation acteur » ) |
| H1 | `Des tarifs clairs.` |
| Meta description (104) | « offres à la rentrée » : aucune offre n'est décrite sur la page (hors parrainage) → promesse non tenue |
| Canonical | ✔ `/tarifs` |
| JSON-LD | + `FAQPage` (4 Q/R identiques au HTML `details`) |
| Liens entrants | nav, footer, `/`, `/acting`, `/scenario-real`, `/inscription`, `/planning` ; landings → **`/tarifs/`** (copie bloquée par robots.txt), pas `/tarifs` |
| Contenu | ~1 010 mots ; 370 €/mois Acting, 350 €/mois Scénario, 200 € frais, 300 € semaine intensive, 140 €/mois Acting Amateur, stages dès 160 €, parrainage ; 6 ateliers « sur demande » |
| Problèmes | (1) copie `/tarifs/index.html` (§ 14) ; (2) aucune date de validité des tarifs (le kicker dit « 2026–2027 », bien) mais pas de mention « hors options » ; (3) FAQPage : Google n'affiche plus ce rich result pour les sites non gouvernementaux/santé (depuis août 2023) — sans risque, mais sans gain ; (4) pas de coût annuel/total calculé (370 × 9 + 200 = 3 530 €) alors que c'est ce que comparent les visiteurs et les IA. |
| Action | Afficher le total annuel et par cursus ; aligner meta description sur le contenu ; décider du sort de `/tarifs/`. |

## 9. `/planning` — Planning

| Champ | Observation |
|---|---|
| Fichier | `dist/planning.html` ← `pages/planning.html` |
| `<title>` (37) | `Planning — Method Acting Center Paris` |
| H1 | `Les dates à retenir.` |
| Meta description (86) | trop courte |
| Canonical | ✔ |
| JSON-LD | + 7 `Event` (JPO + 6 stages) |
| Liens entrants | nav, footer, `/`, `/inscription`, landings |
| Contenu | ~980 mots ; timeline 2026-2027 (JS masque le passé), tableaux dates, rythmes par formation, PDF planning hebdo |
| Problèmes | (1) H2 « Toutes les dates, en clair » suivi de H2 de même niveau (structure plate, mineur) ; (2) rythme 3e année « 1 atelier de 4h le vendredi + 9 sessions de 3h le samedi » vs `/inscription` « 1 atelier de 4 h par semaine + Stratégie de carrière 9 samedis » : cohérent mais formulé différemment ; (3) PDF non référencé dans le sitemap (acceptable). |
| Action | Allonger la description ; vérifier que le PDF n'est pas indexé à la place de la page (ajouter `X-Robots-Tag: noindex` sur le PDF via `.htaccess` si besoin). |

## 10. `/contact` — Contact

| Champ | Observation |
|---|---|
| Fichier | `dist/contact.html` ← `pages/contact.html` |
| `<title>` (36) | `Contact — Method Acting Center Paris` |
| H1 | `Parlons de votre projet.` ; puis **H3** sans H2 (`contact.html:16`) et un `<h4 class="h-sm">` (`:26`) |
| Meta description (106) | OK |
| Canonical | ✔ ; sitemap prio 0.5 |
| Contenu | ~330 mots ; NAP complet (adresse, tél, WhatsApp, métro) ; formulaire |
| Problèmes | (1) pas de carte intégrée ni d'horaires d'ouverture visibles (ils sont dans le JSON-LD mais pas dans le HTML → données structurées non « conformes au contenu visible ») ; (2) hiérarchie de titres. |
| Action | Afficher les horaires (vérifiés FACT-002) dans la page ; H2. |

## 11. `/jpo/` — Landing Google Ads « Portes Ouvertes · acteurs »

| Champ | Observation |
|---|---|
| Fichier | `dist/jpo/index.html` ← `static/jpo/index.html` (fichier autonome, 115 Ko) |
| `<title>` (72) | `Method Acting Center — Devenez acteur · Journées Portes Ouvertes à Paris` |
| H1 | `Vous voulez devenir acteur ?` — **identique** au H1 de `/stages/` |
| Meta robots | `index, follow, max-image-preview:large` (aucun noindex) |
| Canonical | `/jpo/` (auto-référent) |
| JSON-LD | aucun |
| Liens entrants | `/jposr/` uniquement (+ Google Ads) ; hors sitemap ; non reliée au menu (voulu) |
| Liens sortants | vers le site en `…/acting.html`, `…/inscription.html` etc. (→ 301) et vers `…/tarifs/` (bloqué robots) |
| Contenu | ~1 840 mots : 4 façons de rejoindre, Méthode en 3 temps (Déclencher/Maîtriser/**Reproduire**), programme 4 ans, affiches, avis, FAQ, formulaire |
| Problèmes | (1) indexable → concurrence `/jpo.html` sur « journées portes ouvertes method acting center » ; 24,9 % de 6-grammes communs avec `/jposr/` ; (2) 8 `<img data-img>` sans `alt` (images injectées en JS) ; (3) liens en `.html` ; (4) pas de JSON-LD (acceptable pour une landing). |
| Action | Propriétaire : choisir `noindex` (recommandé, sans effet sur Ads) ou canonical vers `/jpo.html` ; remplacer les liens par URLs propres. |

## 12. `/jposr/` — Landing Google Ads « Portes Ouvertes · scénario / réalisation »

| Champ | Observation |
|---|---|
| Fichier | `dist/jposr/index.html` ← `static/jposr/index.html` |
| `<title>` (90) | `Method Acting Center — Devenez réalisateur & scénariste · Journées Portes Ouvertes à Paris` → très tronqué |
| H1 | `Vous voulez devenir Scénariste Réalisateur ?` |
| Meta robots | index ; Canonical `/jposr/` ; JSON-LD aucun |
| Liens entrants | `/jpo/` et `/stages/` (lien « jposr ») |
| Contenu | ~1 870 mots, structure miroir de `/jpo/` ; 11 images sans alt |
| Problèmes | mêmes que `/jpo/` + title trop long. |
| Action | idem § 11. |

## 13. `/stages/` — Landing Google Ads « Stages »

| Champ | Observation |
|---|---|
| Fichier | `dist/stages/index.html` **généré** par `tools/build_landing_stages.py` à partir de `static/jpo/index.html` |
| `<title>` (69) | `Stages d'acting à Paris — Week-end & intensifs · Method Acting Center` (meilleur ciblage que `/stages.html`) |
| H1 | `Vous voulez devenir acteur ?` (hérité de `/jpo/`, hors sujet « stages ») |
| Meta robots | **deux** balises : `index, follow` (l.9) et `index, follow, max-image-preview:large` (l.16) |
| Canonical | **deux** balises contradictoires : `https://www.methodacting.fr/stages/` (l.8) **et** `https://www.methodacting.fr/jpo/` (l.15) — cause : `build_landing_stages.py:25-34` insère un nouveau bloc après la description sans supprimer le bloc d'origine (`static/jpo/index.html:8-16`) |
| Open Graph | `og:url`, `og:title`, `og:description` dupliqués ; le second jeu pointe vers `/jpo/` et annonce « Journées Portes Ouvertes » → partage social et Google peuvent retenir la mauvaise version |
| Meta description (205) | trop longue |
| JSON-LD | aucun |
| Liens entrants | **aucun** (ni site, ni `/jpo/`, ni `/jposr/`) → page orpheline, dépend de Google Ads |
| Contenu | ~1 960 mots ; même Méthode en 3 temps et mêmes affiches que `/jpo/` (11,2 % Jaccard, 20,5 % du plus petit) ; stages détaillés (dates/prix centralisés dans `SESSIONS`) ; masquage JS des sessions expirées (`data-end`) ; `dataLayer.push` + `gtag` conditionnel mais aucune balise Ads/GA installée |
| Problèmes | (1) **double canonical** : risque que Google canonise `/stages/` vers `/jpo/` ou ignore les deux ; (2) cannibalisation `/stages.html` ; (3) orpheline ; (4) H1 hors sujet ; (5) 8 images sans alt ; (6) `loading="lazy"` sur 5 images seulement. |
| Action | Corriger le générateur (remplacer, pas insérer) ; décider noindex/canonical ; H1 « Stages d'acting à Paris… » ; vérifier la balise de conversion Ads. |

## 14. `/tarifs/` — copie de `/tarifs`

| Champ | Observation |
|---|---|
| Fichier | `dist/tarifs/index.html` (= `tarifs.html` avec liens absolus, `build.py:165-171`) |
| Canonical | `https://www.methodacting.fr/tarifs` ✔ |
| robots.txt | `Disallow: /tarifs/` (`static/robots.txt:8`) → Google **ne peut pas lire** le canonical ; si l'URL a déjà été indexée (ancienne prod sans canonical, `prod-snapshot/tarifs/index.html`), elle peut rester dans l'index « indexée malgré le blocage » |
| Liens entrants | les 3 landings (`https://www.methodacting.fr/tarifs/`) |
| Problèmes | duplication 100 % ; raison d'être = ancien dossier `/tarifs/` sur le serveur (et peut-être une URL finale Google Ads, à confirmer). |
| Action | Si aucune campagne ne pointe vers `/tarifs/` : supprimer la variante, ajouter `RewriteRule ^tarifs/?$ /tarifs [R=301,L]`, retirer le Disallow, faire pointer les landings vers `/tarifs`. Décision propriétaire (Ads). |

## 15. Fichiers non-HTML

| URL | Observation |
|---|---|
| `/robots.txt` | Ouvert à tous les robots (IA incluses), `Disallow: /tarifs/`, sitemap déclaré ✔ |
| `/sitemap.xml` | 10 URLs ; `lastmod` = date du build pour toutes (`build.py:159`) → signal de fraîcheur non fiable |
| `/llms.txt` | Présent, cohérent avec le site (prix, dates, adresse) ; aucune garantie d'usage par les IA |
| `/uploads/planning-hebdomadaire.pdf` | 182 Ko ; lié depuis `/inscription` et `/planning` ; indexable |
| `/favicon.ico` | **absent** → 404 à chaque visite, icône générique dans les SERP mobiles |
| `/.htaccess` | HTTPS forcé via `X-Forwarded-Proto` ; URLs propres ; `ErrorDocument 404 /index.html` (`:65`) ; section redirections WordPress **vide** (`:57-61`) ; pas de redirection non-www → www |

## 16. URLs potentielles non vérifiées

Impossible à confirmer sans accès en ligne / Search Console :
- anciennes URLs WordPress (ex. `/formation-acteur/`, `/?p=…`) encore indexées ou liées depuis des annuaires (Emagister, Spectable, evous, Gowork) ;
- `methodacting.fr` (sans www) et `http://` : comportement réel des redirections OVH ;
- `/index.html`, `/acting.html`, `/acting/` : codes HTTP réels des règles `.htaccess` ;
- `/jpo` et `/stages` sans slash (mod_dir → 301 vers `/jpo/` et `/stages/` attendu) ;
- images `assets/img/…` de l'ancienne prod (dossier à supprimer selon README) : 404 ou 200 selon l'état du serveur.
