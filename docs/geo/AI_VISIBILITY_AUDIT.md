# AI Visibility Audit — Method Acting Center

Agent : geo-ai-visibility · Rédigé le 2026-10-12 · Lecture seule : aucun fichier du site modifié.

## 0. Périmètre et méthode

- Audité : les 13 pages HTML de `newsite/dist/` (copie exacte du déploiement), `dist/llms.txt`,
  `dist/robots.txt`, `dist/sitemap.xml`, `dist/.htaccess`, la fonction `jsonld()` et le
  dictionnaire `ORG` de `newsite/build.py`.
- Texte visible et JSON-LD extraits par script (`extract.py`, scratchpad) ; CSS/JS ignorés.
- Sources tierces : voir `docs/geo/CITATION_SOURCES.md` (16 sources, extraits de recherche uniquement).
- **Non vérifié** : le site en production (injoignable depuis l'environnement), les réponses
  réelles des assistants IA (protocole dans `AI_PROMPT_BENCHMARK.md`), les codes HTTP.
- Référence factuelle : `docs/FACTS_REGISTER.md`.

Rappel : aucun des éléments ci-dessous (JSON-LD, llms.txt, robots.txt) ne garantit une
citation par une IA. Ils réduisent l'ambiguïté ; ils ne créent pas de notoriété.

## 1. Carte des entités

### 1.1 L'organisation

| Attribut | Valeur sur le site (dist) | Statut registre | Cohérence externe |
|---|---|---|---|
| Nom officiel | Method Acting Center | Vérifié | identique partout ; variantes vues : « METHODE ACTING CENTER » (avis Google affiché sur inscription.html), « MAC » (scenario-real.html : « production extérieure (ici, MAC) »), « Method Acting Center Paris » (handle YouTube) |
| Type | École d'acteurs, de scénaristes et de réalisateurs ; JSON-LD : `EducationalOrganization` + `LocalBusiness`, `additionalType: School` | Vérifié | L'Etudiant : « école d'art privée hors contrat » (statut non documenté dans le registre) |
| Site | https://www.methodacting.fr/ | Vérifié | cohérent (BnF, Spectable) |
| Adresse | 93 avenue d'Italie, 75013 Paris · M7 Maison Blanche / M5 Place d'Italie | Vérifié | Gowork : 105 B rue de Tolbiac (obsolète) |
| Téléphone | +33 6 07 41 41 25 | Vérifié | Evous (extrait) : 06 07 07 41 25 (à vérifier) |
| Email | contact@methodacting.fr | Vérifié | cohérent |
| Création | « depuis 1999 », « 25+ ans », `foundingDate: 1999` | À confirmer | L'Etudiant : 2009 |
| Fondateur | « David, fondateur du Method Acting Center » (inscription.html, tarifs.html) ; alt-text « Davids Barrouk » (scenario-real.html, jposr) | À confirmer | BnF / Bloomsbury / Emagister : **David Barrouk** |
| Réseaux | Instagram, YouTube, Facebook, Trustpilot (`sameAs`) | Vérifié / Trustpilot à confirmer | Spectable : champs réseaux vides |
| Avis | 4,8/5 · 98 avis Google (texte + `aggregateRating`) ; cartes d'avis Google datées 2018-2026 ; 1 carte Trustpilot 2025 | Vérifié (valeur datée) | extrait Trustpilot : 4,0/5 |
| Horaires | lun-jeu 10h-20h30, ven 11h-19h, sam-dim 11h-17h (JSON-LD et llms.txt uniquement, **pas dans le texte visible**) | Vérifié | — |

### 1.2 Les formations et ateliers (tels que décrits dans `dist/`)

| Entité | Durée / rythme | Prix affiché | Pages | JSON-LD |
|---|---|---|---|---|
| Formation Acting (« Acting Pro ») | jusqu'à 4 années ; 1re-2e : 2 ateliers de 4 h/sem ; 3e : 1 atelier 4 h + 9 samedis ; 4e : 2 ateliers de 3 h | dès 370 €/mois, 9 mensualités, 200 € frais/an, semaine intensive 300 € en option | acting, tarifs, inscription, planning | `Course` (acting) |
| Formation Scénario, Réalisation & Direction d'acteurs | 2 années ; 26 samedis de 8 h puis 24 dimanches de 5 h ; atelier acting hebdo 4 h inclus | dès 350 €/mois, 9 mensualités, 200 € frais/an | scenario-real, tarifs, inscription, planning | `Course` (scenario-real) |
| Acting in English | hebdo, mer. 15h-18h | sur demande | tarifs, cours-essai, inscription, jpo | aucun |
| Screenwriting in English | hebdo, jeu. 19h30-22h30 | sur demande | idem | aucun |
| Acting Amateur | hebdo, loisir | dès 140 €/mois | tarifs, inscription, jpo | aucun |
| Improvisation | hebdo | sur demande | tarifs, inscription, jpo | aucun |
| Acting Caméra | hebdo (ateliers à l'unité) + module 4e année + stage | sur demande | tarifs, acting, stages | `Event` (stage) |
| Marché Professionnel & Stratégie de carrière | 18 sessions (9 intervenants + 9 avec David) | sur demande | tarifs, inscription, acting | aucun |
| Stages week-end A, Scénario, B, Acting Caméra | 2 jours | dès 160 € (A, Scénario, B) ; sur demande (Caméra) | stages, planning, /stages/ | `Event` ×4 |
| Stages intensifs hiver / printemps | 2 j / 3 j | sur demande | stages, planning | `Event` ×2 |
| Journées Portes Ouvertes | 12-13 déc. 2026 ; 19-21 mars 2027 ; 28-30 mai 2027 | gratuit | jpo, planning, /jpo/, /jposr/ | `Event` (déc. seulement) |
| Cours d'essai | 2, gratuits, toute l'année, en semaine | 0 € | cours-essai (+ bandeau sur toutes les pages) | `Offer` |
| Programme ados | « un programme dédié existe aussi pour les ados » (FAQ de /jpo/ uniquement) | — | /jpo/ | aucun |

Incohérence de nommage interne : la landing `/stages/` appelle les stages « Actors Studio A » et
« Actors Studio B », alors que le site principal et le JSON-LD disent « Stage A — Initiation à la
Méthode » et « Stage B — Approche d'une scène ». Pour une IA, « Actors Studio A » peut être lu
comme un cours de l'Actors Studio (New York). À harmoniser.

### 1.3 Méthode enseignée (telle que revendiquée)

- Formulation du site : « la Méthode (Stanislavski / Actors Studio) », « la Méthode Stanislavski
  dont s'est inspiré l'Actors Studio », « Method Acting Center en est le descendant direct en
  France ». Trois temps : déclencher, maîtriser, reproduire (ou « composer » sur acting.html).
- Scénario : « McKee, Truby, Schrader, Packard », « lien unique entre écriture, réalisation et acting ».
- Références externes : livre « Stan ou Le solfège de l'acting » (2017, BnF) et « Stanislavski and
  The Method for the 21st Century Actor » (Bloomsbury 2024) par David Barrouk : **absentes du site**.
- Registre : exercices précis et filiation détaillée « À confirmer ».
- Point d'attention éditorial (CLAUDE.md §6) : le site présente « Stanislavski / Actors Studio »
  comme un bloc. Le système de Stanislavski (Russie, 1900-1938) et la « Method » américaine
  (Strasberg, Adler, Meisner, à partir des années 1930-1950) sont liés mais distincts. La
  formule « descendant direct » n'est pas vérifiable. Voir §4.5 et le plan d'action.
- Affirmation à risque : « La méthode de Marlon Brando, Meryl Streep, Joaquin Phoenix, Leonardo
  DiCaprio, Jack Nicholson… » (acting.html). Plusieurs de ces acteurs ne sont pas formés à
  l'Actors Studio (Meryl Streep : Yale ; DiCaprio : pas de formation Method documentée). Une IA
  peut relever l'approximation. À reformuler (« popularisée par… » ou retirer).

### 1.4 Personnes

| Personne | Mention sur le site | Source externe | Statut |
|---|---|---|---|
| David (Barrouk) | « David, fondateur » ; alt « Davids Barrouk » (coquille probable) | BnF, Bloomsbury, Emagister, Spectable | À confirmer (nom complet, bio autorisée) |
| Rami (Ghorra ?) | cité dans un avis Google (« Rami au top ») | Spectable : « Rami Ghorra » | À confirmer |
| Rafael | cité dans un avis Google (stage comédie) | — | À confirmer |
| Riccardo Monica | « Lines » de Riccardo Monica (affiche, scenario-real) | Spectable | À confirmer |
| Anna Popkin | — | co-autrice du livre Bloomsbury | hors périmètre sauf validation |

Aucune page équipe, aucune bio. Pour une IA, l'école n'a pas de visage identifiable.

### 1.5 Preuves et productions documentées

- Avis Google : 44 cartes affichées sur le site (export propriétaire), note 4,8/5 sur 98.
- « Nos acteurs tournent ! » : 8 affiches (Le Procès Goldman, Les 7 vies de Léa, Quantum of
  Solace, Ni chaînes ni maîtres, Sans répit, Les Invisibles, Dirty Difficult Dangerous, Martyrs).
  Les noms de fichiers (`Quantum-of-Solace-Olga-Kurylenko.jpg`, `Martyrs_Mylene_Jampanoi.jpg`,
  `Sans-repit-Jemima-West.jpg`, `Les-7-vies-de-Lea_Raika_Hazanavicius.jpg`,
  `Les-invisibles_Deborah_Krey.jpg`) laissent entendre quels anciens élèves sont visés, **sans que
  le texte visible ne nomme personne ni ne précise la nature du passage à l'école**. Risque : une
  IA (ou un lecteur) déduit « Olga Kurylenko a été formée au Method Acting Center », affirmation
  non sourcée publiquement. À documenter (preuve + consentement) ou à retirer (CLAUDE.md §5).
- « Nos réalisateurs tournent ! » : « Lines » (Riccardo Monica), « Goodbye Mélodie » et « Cheap
  Thrill » (Davids Barrouk), « Noir, juif et borgne », + 7 affiches « Film réalisé par un ancien du
  programme » sans titre. Deux des films nommés sont du fondateur lui-même, présentés sous
  « films écrits et réalisés par nos anciens élèves » : ambigu.
- Livres du fondateur (BnF 2017, Bloomsbury 2024) : preuve forte, non exploitée.

## 2. Carte des pages auditées

| Fichier dist | URL canonique | Titre | Rôle GEO |
|---|---|---|---|
| index.html | / | Method Acting Center — Devenir Acteur, Scénariste ou Réalisateur à Paris | entité, vue d'ensemble |
| acting.html | /acting | Formation Acting — Devenir Acteur | intentions 1, 2, 3 |
| scenario-real.html | /scenario-real | Scénario, Réalisation & Direction d'acteurs | intention 5 |
| tarifs.html (+ /tarifs/index.html, copie exclue par robots) | /tarifs | Tarifs | intention 4 |
| cours-essai.html | /cours-essai | Cours d'essai gratuit | intentions 6, 7 |
| stages.html | /stages.html | Stages d'acting & de scénario | intention 6 |
| jpo.html | /jpo.html | Journées Portes Ouvertes — 12 & 13 décembre | intention 7 |
| inscription.html | /inscription | Inscription | conversion |
| planning.html | /planning | Planning | dates |
| contact.html | /contact | Contact | NAP |
| jpo/index.html | /jpo/ | landing Ads acteurs | hors menu, indexable |
| jposr/index.html | /jposr/ | landing Ads scénario | hors menu, indexable |
| stages/index.html | **canonical = /jpo/** (!) | landing Ads stages | hors menu, indexable |

Anomalie : `dist/stages/index.html` déclare `<link rel="canonical" href="https://www.methodacting.fr/jpo/">`
et un `og:title` / `og:description` qui parlent des Portes Ouvertes, alors que la page parle des
stages. Pour un moteur ou un crawler IA, `/stages/` se déclare copie de `/jpo/` : son contenu
(stages, prix, dates) risque de ne pas être retenu. Origine probable : `tools/build_landing_stages.py`
génère la landing à partir de `static/jpo/index.html` sans réécrire ces balises. **À transmettre à technical-seo** (P1).

## 3. Évaluation page par page : les 8 questions

Notation : ✅ répond clairement · ◐ partiel / implicite · ❌ absent.

| Page | Qu'est-ce que l'école ? | Où ? | Pour qui ? | Qu'apprend-on ? | Pédagogie ? | Tarifs / durée ? | S'inscrire ? | Preuves ? |
|---|---|---|---|---|---|---|---|---|
| / | ✅ (hero + footer) | ✅ (footer, « Paris 13ᵉ ») | ◐ (acteur / scénariste / réalisateur ; débutants non explicités) | ◐ (2 formations résumées) | ✅ (3 temps, « méthode pas formatage ») | ◐ (lien tarifs ; aucun chiffre) | ✅ (cours d'essai, JPO, S'inscrire) | ◐ (4,8/5, affiches sans noms) |
| /acting | ✅ | ✅ (footer) | ◐ (« tous les rôles » ; débutant ? âge ? non dits) | ✅ (programme année par année, très détaillé) | ✅ (mais filiation à reformuler) | ◐ (« 4 années » ; prix absent de la page, lien tarifs) | ✅ | ◐ (avis, affiches) |
| /scenario-real | ✅ | ✅ (footer) | ◐ (« raconter vos histoires » ; prérequis non dits) | ✅ (2 années détaillées) | ✅ (McKee, Truby…) | ◐ (« 2 années » ; prix absent) | ✅ | ◐ (films, dont ceux du fondateur) |
| /tarifs | ◐ | ✅ | ◐ | ◐ | ◐ | ✅ (meilleure page : prix datés 2026-2027, frais, mensualités, FAQ) | ✅ | ◐ |
| /cours-essai | ◐ | ✅ | ✅ (« où l'on peut entrer en cours d'année ») | ✅ (ateliers testables, créneaux) | ◐ | ✅ (0 €) | ✅ (formulaire) | ◐ (avis) |
| /stages.html | ◐ | ✅ (« Paris 13ᵉ ») | ✅ (« ouverts à tous, débutants compris ») | ✅ | ◐ | ✅ (dès 160 €, « sur demande » pour 3 stages) | ✅ | ◐ |
| /jpo.html | ◐ | ✅ | ◐ (ateliers par public) | ✅ | ◐ | ✅ (gratuit) | ✅ | ◐ |
| /inscription | ◐ | ✅ | ◐ (« entrée directe sur audition ») | ✅ (rythmes par année) | ❌ | ◐ (durées ; prix absent) | ✅ (3 temps) | ◐ |
| /planning | ❌ | ✅ | ❌ | ◐ | ❌ | ✅ (dates, rythmes) | ✅ | ❌ |
| /contact | ◐ | ✅ (seule page avec adresse dans le corps + métro) | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| /jpo/ (landing) | ✅ | ✅ | ✅ (FAQ : débutants, âge, ados) | ◐ | ✅ | ◐ (« 100 € de remise… offre valable jusqu'au 31/08/2026 » : **périmée**) | ✅ | ◐ (« 25+ ans », 4,8/5) |
| /jposr/ (landing) | ✅ | ✅ | ✅ (FAQ) | ◐ | ✅ | ◐ (même offre périmée) | ✅ | ◐ |
| /stages/ (landing) | ✅ | ✅ (adresse répétée par stage) | ✅ | ✅ | ✅ | ✅ | ✅ | ◐ |

### Manques transversaux (ce qu'une IA ne trouvera nulle part sur le site)

1. **Qui dirige / qui enseigne** : pas de page équipe, pas de nom complet du fondateur, pas de bios, pas de références des coachs (« professionnels en activité » sans exemple).
2. **Identité juridique et statut** : pas de mentions légales (raison sociale, SIREN, forme juridique, directeur de publication, hébergeur) ; pas de réponse à « est-ce une école reconnue / diplômante ? ». Les prompts E5 (limites) et F2 (comparaison) feront remonter cette absence. Note : les mentions légales sont une obligation (LCEN) indépendamment du SEO ; à faire valider par le propriétaire.
3. **Pour qui, concrètement** : âge minimum, niveau d'anglais requis (Acting in English), accessibilité débutants, reconversion, formation continue / financement (CPF ? OPCO ? rien n'est dit, donc une IA répondra « non » ou inventera).
4. **Horaires d'ouverture** : uniquement dans le JSON-LD et llms.txt, jamais dans le texte visible. Google demande que les données structurées reflètent le contenu visible.
5. **Historique** : « depuis 1999 » sans aucun élément d'histoire (fondation, évolution, lieux). Contradiction externe 2009 non adressée.
6. **Preuves nominatives** : aucune alumni nommée dans le texte ; aucun lien vers une œuvre, un festival, un prix.
7. **Jeu face caméra** (intention 3) : pas de page dédiée. Le sujet est éclaté entre un module de 4e année, un atelier à l'unité « sur demande » et un stage « tarif sur demande ».
8. **Stanislavski / Method / autres approches** (intention 8) : pas de contenu explicatif ; les termes sont utilisés comme marque, pas expliqués.
9. **Date de mise à jour** : aucune page n'affiche « mis à jour le ». Les tarifs disent « 2026-2027 » (bien) ; les landings affichent une offre expirée au 31/08/2026 (mal).
10. **Version anglaise** : aucune page en anglais alors que deux ateliers sont en anglais et que des avis d'élèves internationaux sont affichés. Les prompts A6/B6/E9 en anglais ne trouveront que du français.

## 4. Données structurées (JSON-LD) : évaluation

Source : `jsonld()` dans `newsite/build.py`, injecté dans les 10 pages du site (pas dans les 3 landings).
Le JSON-LD est **syntaxiquement valide** sur les 10 pages (parsing JSON OK). Structure : `@graph`
avec `Organization`, `WebSite`, `WebPage`, puis objets spécifiques.

### 4.1 Ce qui est bien

- Un seul `@id` d'organisation (`/#organization`) réutilisé partout : cohérence d'entité.
- Adresse, téléphone, email, horaires, `sameAs`, `knowsAbout`, `areaServed` : renseignés et conformes au registre.
- `Course` sur les deux formations avec `provider`, `courseMode`, `inLanguage`, `hasCourseInstance` et un `description` de rythme.
- `Event` pour les stages et les JPO avec dates ISO, lieu, organisateur, offres ; `isAccessibleForFree` pour les JPO.
- `Offer` « Cours d'essai gratuit » à 0 € sur cours-essai.
- `FAQPage` sur /tarifs avec 4 questions dont le texte **correspond exactement** au contenu visible.
- Descriptions sans superlatifs inventés ; aucun faux avis.

### 4.2 Points à corriger ou à décider

| # | Constat | Pourquoi c'est un problème | Recommandation | Priorité |
|---|---|---|---|---|
| J1 | `logo` = photo d'une scène (`scene-a-deux-acteurs…jpg`) | Un logo est attendu (carré, fond uni) ; Google l'utilise pour le panneau de connaissance ; une photo de scène peut être rejetée ou mal rendue | fournir un vrai logo (PNG/SVG ≥ 112×112) dans `assets/img/` et le référencer | P2 |
| J2 | `aggregateRating` 4,8/98 déclaré par l'organisation sur elle-même, sans indiquer la source (Google) | Google exclut les avis « auto-déclarés » (self-serving) des résultats enrichis pour `LocalBusiness` / `Organization` ; valeur non vérifiable par un crawler ; dérive dans le temps (98 au 2026-10-12) | soit retirer `aggregateRating` du JSON-LD et garder la mention visible avec lien vers la fiche Google ; soit la conserver en acceptant qu'elle ne produise rien et en la **mettant à jour à chaque build** (valeur datée dans le registre) | P2 (décision propriétaire) |
| J3 | `Course.offers.price = "370"` / `"350"` avec `description: "Tarif mensuel de base, 9 mensualités par an"` | Un prix nu sans unité de temps peut être lu comme le prix total du cours (370 € pour 4 ans) | utiliser `priceSpecification: {"@type": "UnitPriceSpecification", "price": 370, "priceCurrency": "EUR", "unitText": "mois", "billingDuration"/… }` ou indiquer le coût annuel de base (9 × 370 + 200) en plus ; garder la description | P2 |
| J4 | Aucun `founder`, aucune entité `Person` | L'IA ne peut relier l'école à son fondateur ni à ses livres (BnF, Bloomsbury), qui sont ses meilleures preuves externes | après validation : `founder: {"@type": "Person", "name": "David Barrouk", "sameAs": [data.bnf.fr…]}` et, sur la future page À propos, `Book` × 2 | P2 (dépend de la validation) |
| J5 | Pas d'`alternateName` ni de désambiguïsation | Nom générique (« method acting » + « center ») ; voir §6 | ajouter `alternateName: ["Method Acting Center Paris", "MAC Paris"]` seulement si ces formes sont réellement utilisées ; ajouter `disambiguatingDescription` courte | P3 |
| J6 | `sameAs` sans la fiche Google Business ni Wikidata (inexistant) | lien d'entité local manquant | ajouter l'URL publique de la fiche Google (lien « g.page » ou Maps) au `sameAs` | P3 |
| J7 | Horaires présents en JSON-LD mais absents du texte visible | écart données structurées / contenu visible | afficher les horaires sur /contact (et footer) | P2 |
| J8 | `Event` des stages : `url` pointe vers `/stages.html` pour tous ; `image` identique pour tous ; pas d'`offers` pour les 3 stages « sur demande » (correct, ne pas inventer) | acceptable ; manque de précision par événement | ancres par stage (`/stages.html#stage-a`) dans `url` ; image propre à chaque stage (elles existent déjà dans `uploads/`) | P3 |
| J9 | JPO de mars et mai 2027 visibles sur /planning mais pas en `Event` | incohérence mineure | ajouter les 2 événements (gratuits, dates connues) | P3 |
| J10 | `Course` : pas de `educationalCredentialAwarded`, pas de `occupationalCredentialAwarded` | Les IA demandent « diplôme ? » ; silence = ambiguïté | si aucun diplôme n'est délivré, le dire en clair dans le texte (FAQ) ; ne rien ajouter de faux au JSON-LD | P2 (contenu) |
| J11 | Landings `/jpo/`, `/jposr/`, `/stages/` : aucun JSON-LD | pages indexables, riches (FAQ, événements) mais muettes pour les machines | au minimum `Organization` (@id partagé) + `Event` JPO ; `FAQPage` pour les FAQ existantes des landings | P3 |
| J12 | `WebPage.primaryImageOfPage` en chaîne, `Organization.image` en chaîne | accepté par Google, mais `ImageObject` avec dimensions est plus robuste | optionnel | P4 |

### 4.3 Vérification à faire en production (non faisable ici)

- Passer chaque URL dans le test des résultats enrichis de Google et le validateur Schema.org.
- Vérifier dans Search Console (rapport « Améliorations ») quels types sont détectés et s'il y a des erreurs.

## 5. llms.txt et robots.txt

### 5.1 llms.txt (`newsite/static/llms.txt`, servi en `/llms.txt`)

- Contenu : résumé de l'école, coordonnées, horaires, 10 pages principales avec une phrase et les
  prix « dès », dates clés 2026-2027, ateliers à l'unité. **Conforme au registre** (vérifié ligne à ligne).
- Points forts : factuel, daté implicitement (saison 2026-2027), URLs canoniques correctes (sauf
  `/stages.html` et `/jpo.html`, qui sont bien les canoniques choisies).
- Limites à garder en tête (ne pas survendre) :
  - `llms.txt` est une **proposition** (llmstxt.org, 2024). À la date de rédaction, aucun grand
    fournisseur d'assistant (OpenAI, Anthropic, Google, Perplexity) n'a documenté publiquement
    qu'il lit ce fichier pour construire ses réponses. Son effet est donc **non mesurable** et
    probablement nul aujourd'hui ; il ne coûte rien et ne nuit pas.
  - Le fichier est **maintenu à la main** (`static/`), alors que les prix, dates et notes sont
    aussi dans `build.py`, `pages/*.html` et `tools/build_landing_stages.py`. Risque de dérive
    (ex. : nombre d'avis, prochaine JPO). Recommandation : le générer depuis `build.py` à partir
    des mêmes constantes (P3).
  - Il ne doit pas contenir d'information absente du site (actuellement : les horaires y sont,
    mais pas dans le texte visible → corriger côté site, pas côté llms.txt).

### 5.2 robots.txt

- `User-agent: * / Allow: / / Disallow: /tarifs/` + liste explicite d'agents IA en `Allow`
  (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, anthropic-ai,
  PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, Meta-ExternalAgent,
  Amazonbot, DuckAssistBot, YouBot, MistralAI-User, cohere-ai, CCBot, Bytespider…) et `Sitemap`.
- Évaluation : ouvert, explicite, sans contradiction. Choix assumé d'autoriser l'entraînement
  (`GPTBot`, `Google-Extended`, `CCBot`, `Bytespider`) : c'est une décision du propriétaire,
  cohérente avec l'objectif de visibilité ; elle peut être revue indépendamment de la recherche
  (les agents « search / user » suffisent pour les citations en temps réel).
- Remarques :
  - Les blocs `User-agent: X / Allow: /` sont redondants avec `*` mais inoffensifs ; ils
    **n'héritent pas** du `Disallow: /tarifs/` (un bloc nommé remplace le bloc `*` pour cet
    agent). Donc GPTBot & co **peuvent** crawler `/tarifs/` (copie). Risque faible (canonical
    identique), mais si l'intention est d'exclure la copie pour tous, ajouter `Disallow: /tarifs/`
    dans chaque bloc ou supprimer les blocs nommés (P3, technical-seo).
  - `robots.txt` n'est pas un mécanisme de citation : il autorise l'accès, rien de plus.
- `.htaccess` : `ErrorDocument 404 /index.html` renvoie la page d'accueil (avec code 404) sur
  toute URL inconnue, y compris les anciennes URLs WordPress encore indexées (voir
  `CITATION_SOURCES.md` S16). Section de redirections 301 vide. Un crawler IA qui suit un vieux
  lien tombe sur un contenu « accueil » sous un code 404 : à corriger (technical-seo).

### 5.3 sitemap.xml

- 10 URLs, `lastmod` = date du build (donc toutes identiques, peu informatif), landings absentes
  (choix cohérent avec « hors menu », mais elles restent indexables ; décider si elles doivent
  être `noindex` ou listées). `/stages/` a de toute façon un canonical vers `/jpo/`.

## 6. Risques de confusion d'entités

Aucune organisation portant exactement le nom « Method Acting Center » n'a été trouvée hors
France. Le risque vient de noms **proches** et d'un vocabulaire **générique** :

| Entité | Nature | Pourquoi la confusion est possible | Preuve observée |
|---|---|---|---|
| The Actors Studio (New York) | atelier d'acteurs professionnels, berceau de la « Method » | le site dit « Stanislavski / Actors Studio » dans le titre, la méta-description, le JSON-LD (`knowsAbout`), le footer ; les fiches Emagister titrent « Formation Actors Studio 2017/2018 », « Actors Studio 1ère année » ; la landing /stages/ nomme les stages « Actors Studio A / B » | résultats de recherche mêlant les deux (requêtes « Method Acting Center avis », « …Actors Studio 2017/2018 ») |
| Lee Strasberg Theatre & Film Institute (NY / LA) | école de la Method | « method acting » + « center » ; ressort sur « "Method Acting Center" avis » | WebSearch 2026-10-12 |
| The Sanford Meisner Center (LA), The Acting Center (LA) | écoles américaines | nom générique | WebSearch 2026-10-12 |
| Acting International (Paris, fondé 1980 par Robert Cordier, membre de l'Actors Studio) | école parisienne concurrente revendiquant un lien réel avec l'Actors Studio | une IA interrogée sur « école Actors Studio à Paris » peut citer celle-ci | techno-science.net via WebSearch |
| « Actors Studio Paris » (rue La Fayette, 10e, selon Evous) et « Acting Studio » (maformation.fr) | écoles parisiennes au nom proche | nom | Evous, maformation.fr via WebSearch |
| Bilingual Acting Workshop (Paris, Saint-Germain) | atelier d'acting en anglais, « American Techniques of Acting » | article London Met « method acting masterclass in Paris » ressort sur les requêtes de marque | S15 |
| Studio AZOT (Paris, Chekhov / Meisner) | école parisienne | ressort sur « David Barrouk … Michael Chekhov » | WebSearch 2026-10-12 |
| Playhouse Paris (Meisner, en anglais) | école parisienne anglophone | prompts anglais | WebSearch 2026-10-12 |
| Cours Florent « Acting in English » | programme concurrent dominant sur les requêtes anglaises | monopolise les résultats « acting in English Paris » | WebSearch 2026-10-12 |
| « Method Acting Center éditions » | maison d'édition du livre de 2017 (BnF) | même nom, entité juridique potentiellement distincte | S12 |

Facteurs aggravants côté site :
- Nom composé de deux termes génériques (« method acting », « center ») sans marqueur local dans le nom lui-même.
- Formule « descendant direct » de l'Actors Studio / de la Méthode Stanislavski : non vérifiable, prête à une lecture d'affiliation.
- Pas d'entité `Person` ni de page À propos : rien ne permet à une IA d'ancrer l'école sur un fondateur, une histoire, un lieu précis au-delà de l'adresse.

Facteurs atténuants :
- Adresse, téléphone, email constants sur toutes les pages et dans le JSON-LD.
- Handle YouTube « MethodActingCenterParis ».
- Notice BnF reliant explicitement « Method Acting Center de Paris » et son fondateur.

## 7. Synthèse des constats (priorisés)

| # | Constat | Impact | Confiance | Effort | Risque | Dépend de |
|---|---|---|---|---|---|---|
| 1 | Fiches tierces obsolètes (Emagister 250 €/3 jours d'essai/2017 ; Gowork Tolbiac ; L'Etudiant 2009) | 5 | 4 | 2 | faible | propriétaire (comptes annonceurs, Sirene) |
| 2 | `/stages/` : canonical et OG pointent vers `/jpo/` | 4 | 5 | 1 | faible | technical-seo |
| 3 | Pas de page À propos / équipe / fondateur ; livres du fondateur absents | 4 | 4 | 3 | moyen (validation bios, consentements) | propriétaire |
| 4 | Preuves « Nos acteurs tournent » non nommées, non sourcées | 4 | 4 | 2 | moyen (droit à l'image, exactitude) | propriétaire |
| 5 | Filiation pédagogique présentée comme un bloc (« descendant direct », liste d'acteurs) | 3 | 4 | 2 | faible | content-strategist + propriétaire |
| 6 | Absence de mentions légales / statut / diplôme | 4 | 5 | 1 | faible | propriétaire |
| 7 | Offre « 100 € de remise jusqu'au 31/08/2026 » encore affichée sur /jpo/ et /jposr/ | 3 | 5 | 1 | faible | propriétaire (offre encore valable ?) |
| 8 | Anciennes URLs WordPress : 404 → accueil, pas de 301 | 3 | 3 (codes non vérifiés) | 2 | faible | technical-seo + Search Console |
| 9 | JSON-LD : logo, prix mensuel ambigu, aggregateRating auto-déclaré, horaires invisibles | 3 | 4 | 2 | faible | technical-seo |
| 10 | Pas de page « jeu face caméra », pas de page « Stanislavski expliqué » | 3 | 3 | 3 | faible | content-strategist |
| 11 | Pas de contenu anglais malgré ateliers en anglais | 2 | 3 | 3 | faible | content-strategist |
| 12 | llms.txt maintenu à la main (dérive) ; effet non prouvé | 1 | 4 | 1 | faible | technical-seo |
| 13 | Nommage « Actors Studio A/B » sur /stages/ | 2 | 5 | 1 | faible | propriétaire (nom officiel des stages) |

Les actions correspondantes, avec raison, preuve, mesure et limite, sont dans `GEO_ACTION_PLAN.md`.
