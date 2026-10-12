# Audit de contenu — Method Acting Center

Agent : content-strategist · Date : 2026-10-12 · Phase A (lecture seule)

Périmètre audité : les 10 pages sources `newsite/pages/*.html`, les partials
(`header.html`, `footer.html`), `newsite/build.py` (titres, descriptions,
JSON-LD), `newsite/static/llms.txt`, les landings `newsite/static/jpo/index.html`,
`newsite/static/jposr/index.html` et le générateur
`newsite/tools/build_landing_stages.py` (landing `/stages/`).

Référence factuelle : `docs/FACTS_REGISTER.md`. Toute affirmation qui n'y
figure pas avec le statut **Vérifié** est signalée ci-dessous comme
« non sourcée » ou « à confirmer ». Les références `fichier:ligne` renvoient
aux fichiers sources (pas à `dist/`).

Observation externe (WebSearch, 2026-10-12) : voir section 6.

---

## 1. Résumé exécutif

Le site est court (10 pages + 3 landings), bien écrit, orienté conversion
(cours d'essai, stages, JPO, inscription) et cohérent graphiquement. Les
informations pratiques essentielles (adresse, prix de base, dates, cours
d'essai) sont présentes et conformes au registre de vérité.

Les principales faiblesses de contenu sont :

1. **Aucune page ne répond à l'intention « méthode Stanislavski / Method
   Acting »** (intentions 1 et 8 du brief). Le sujet est traité par trois
   paragraphes identiques répétés sur 4 pages, avec une formule non sourcée
   (« descendant direct de la Méthode Stanislavski ») et un amalgame
   Stanislavski / Actors Studio jamais expliqué.
2. **Aucune page « école » / « équipe »** : qui enseigne, qui a fondé l'école,
   quel statut, quel type de reconnaissance (ou absence de reconnaissance).
   Les coachs ne sont jamais nommés sur le site, alors que des prénoms
   apparaissent dans les avis Google affichés (« Rami », « Rafael »).
3. **Des preuves implicites non sourcées** : les affiches de films (Quantum
   of Solace, Martyrs, Le Procès Goldman…) sous le titre « Nos acteurs
   tournent ! » suggèrent que des acteurs célèbres sont des anciens élèves,
   sans aucune mention nominative ni source. Idem pour la liste d'acteurs
   « Brando, Streep, Phoenix, DiCaprio, Nicholson » présentée comme utilisant
   « la méthode » enseignée.
4. **Incohérences factuelles entre pages** (rythme de 4ᵉ année, livrables de
   fin de cursus, noms des stages, « Reproduire » vs « Composer », atelier
   Acting Caméra à l'unité présent sur Tarifs mais absent d'Inscription).
5. **Contenus périmés ou à durée de vie courte non gérés** sur les landings
   (offre « 100 € de remise valable jusqu'au 31/08/2026 » toujours affichée,
   « planning détaillé à venir » pour une rentrée passée, prochain stage en
   dur dans le hero de `stages.html`).
6. **Pas de FAQ transversale** sur le site principal : les seules FAQ sont
   celles de la page Tarifs (4 questions) et des landings (7 questions,
   non reprises sur `jpo.html`).
7. **Formules comparatives invérifiables** (« quasi inexistant en France »,
   « ce que presque aucune école ne propose », « une notion rare en France »).

Rien de bloquant pour l'indexation côté contenu ; le travail prioritaire est
d'**enrichir et fiabiliser** les pages existantes, puis de créer deux pages
de référence (Méthode, FAQ) et une page École/Équipe dès que le propriétaire
aura validé les faits.

---

## 2. Grille de lecture

Pour chaque page : intention couverte · question principale (répondue ?) ·
faits manquants · répétitions · affirmations non sourcées (fichier:ligne) ·
CTA · lisibilité.

### 2.1 `index.html` — Accueil

- **Intention couverte** : découvrir l'école (intention 7). Partiellement :
  intentions 1, 2, 8 (Stanislavski / école d'acting / différences) ne sont
  qu'effleurées.
- **Question principale** « Qu'est-ce que Method Acting Center et pour qui ? »
  : répondue à moitié. On sait qu'il y a deux formations et une « Méthode »,
  on ne sait pas : qui enseigne, quel statut d'établissement, quel niveau
  d'entrée, combien ça coûte (il faut cliquer), ce que l'école ne fait pas
  (pas de diplôme d'État ? [À VALIDER]).
- **Faits manquants** : type d'établissement (« école d'art dramatique »,
  fiche Google, vérifié) jamais écrit noir sur blanc ; horaires d'ouverture
  (vérifiés) absents du contenu visible (présents seulement dans le JSON-LD) ;
  année de création « 1999 » affichée (À confirmer dans le registre).
- **Répétitions** : bloc « Ce n'est pas le talent… / descendant direct »
  (`index.html:156`) répété sur `acting.html:32-34`, `static/jpo/index.html:359-361`
  et la landing `/stages/` ; carrousel d'affiches (`index.html:194-227`)
  identique à `acting.html:153-186` ; grille « Par où commencer » reprise
  sur 4 pages.
- **Affirmations non sourcées** :
  - `index.html:9` « forme des générations d'acteurs, scénaristes et
    réalisateurs professionnels » — aucun chiffre, aucun nom.
  - `index.html:10` et `:156` « Méthode Stanislavski dont s'est inspiré
    l'Actors Studio » — historiquement défendable mais jamais expliqué ;
    `:87` et `:156` « Method Acting Center en est le descendant direct en
    France » — filiation non documentée (qui a formé le fondateur ? auprès
    de qui ?). À reformuler ou à prouver.
  - `index.html:92` « coachs professionnels toujours sur le terrain » —
    aucun nom, aucune filmographie (registre : À confirmer).
  - `index.html:187` et `contact.html:7` « on vous répond sous 48h » —
    engagement de service non vérifié.
  - `index.html:200-213` « Nos anciens jouent dans des films… La preuve, à
    l'affiche » suivi d'affiches de films avec des têtes d'affiche connues
    (Olga Kurylenko, Mylène Jampanoï, Jemima West…) : la page ne dit pas
    qui, parmi les élèves, a joué dans ces films ni dans quel rôle. Risque
    de lecture trompeuse + droits sur les affiches à vérifier.
- **CTA** : cohérents (cours d'essai en priorité). Bon.
- **Lisibilité** : bonne, phrases courtes. Beaucoup de blocs décoratifs
  (marquee de mots-clés `index.html:41-47`, `aria-hidden`) sans valeur
  informative pour un lecteur ou un robot.

### 2.2 `acting.html` — Formation Acting

- **Intention couverte** : intention 2 (école d'acting / jeu d'acteur
  cinéma) et partiellement 3 (face caméra, seulement en 4ᵉ année et en
  stage). Intention 1 (apprendre Stanislavski) non traitée en tant que telle.
- **Question principale** « Que vais-je apprendre, en combien de temps, et
  pour quel résultat ? » : bien répondue sur le programme (timeline 4 ans).
  Non répondue : prérequis, âge minimum, volume horaire total par an, taille
  des groupes, profil des coachs, modalités d'évaluation/passage d'année,
  ce que l'école ne garantit pas (débouchés, agent).
- **Faits manquants** : prix (il faut aller sur Tarifs ; un rappel « dès
  370 €/mois, 9 mensualités, 200 € de frais » serait utile) ; rythme
  horaire par année (présent sur Planning et Inscription, pas ici) ;
  admission sur audition en 2ᵉ/3ᵉ année (présent sur Tarifs/Inscription,
  pas ici).
- **Incohérences** :
  - `acting.html:50` troisième temps = **« Composer »** alors que
    `index.html`, `llms.txt:5`, `build.py:47`, la landing JPO (`:381`) et le
    registre disent **« Reproduire »**. À harmoniser (ou expliquer que
    Composer = 3ᵉ année).
  - `acting.html:126` livrables de 4ᵉ année « 3 scènes filmées, 1 book
    photo, 1 bande démo, outils de démarchage » vs landing JPO
    `static/jpo/index.html:888` « 3 scènes filmées et montées, 1 book
    photos, 1 CV, 1 bande démo, 1 vidéo de présentation ». Deux listes
    différentes → [À VALIDER].
- **Affirmations non sourcées** :
  - `acting.html:8` « La méthode de Marlon Brando, Meryl Streep, Joaquin
    Phoenix, Leonardo DiCaprio, Jack Nicholson… » — ces acteurs ont des
    formations très différentes (Streep : Yale ; DiCaprio : pas de formation
    « Method » revendiquée) ; la phrase assimile « la Méthode » du MAC à
    celle de ces acteurs. Risque de fausse association. À supprimer ou à
    remplacer par des faits historiques sourcés (voir brouillon Méthode).
  - `acting.html:34` « descendant direct » (cf. 2.1).
  - `acting.html:89` « on vous tourne un monologue », `:103` « on vous tourne
    une scène à deux », `:126` livrables : promesses de production à
    confirmer (registre : À confirmer).
  - `acting.html:145` Marché Professionnel « rencontres avec agents,
    directeurs de casting, réalisateurs et producteurs » — pas de noms, pas
    d'exemples d'intervenants passés.
  - `acting.html:159-172` affiches (cf. 2.1).
- **Répétitions** : bloc « talent » et carrousel (cf. 2.1) ; descriptions
  d'ateliers (Backstory, Scènes 1, Scènes 3…) recopiées sur
  `cours-essai.html:76-79` et `inscription.html:64-67` avec de légères
  variantes.
- **CTA** : JPO en premier (`:10`), alors que l'accueil pousse le cours
  d'essai ; la JPO est datée (12-13 déc.) donc le CTA sera périmé 2 mois
  par an. Suggestion : CTA principal = cours d'essai (permanent), JPO en
  second.
- **Lisibilité** : très bonne (timeline). Les h3 d'ateliers n'ont pas de
  h2 parent explicite par année (structure `tl-year` sans titre de niveau
  2) — à vérifier par technical-seo.

### 2.3 `scenario-real.html` — Scénario, Réalisation & Direction d'acteurs

- **Intention couverte** : intention 5 (acting + scénario + réalisation).
  Bien.
- **Question principale** « Que contient le programme et à qui s'adresse-
  t-il ? » : répondue sur le contenu, pas sur le public (prérequis ? niveau
  d'écriture ? matériel ? âge ?), ni sur le volume horaire (présent sur
  Tarifs/Planning seulement), ni sur les prix.
- **Faits manquants** : rythme (26 samedis de 8 h / 24 dimanches de 5 h),
  prix (dès 350 €/mois), « compatible avec Acting » (mention sur Tarifs
  uniquement), option « réaliser une scène » : tarif ? [À VALIDER].
- **Affirmations non sourcées / comparatives** :
  - `scenario-real.html:32` « lien constant entre l'écriture, la réalisation
    et l'acting, quasi inexistant en France » ; `:37` « Une notion rare en
    France » ; `:55` « une notion très peu abordée ailleurs » ; landing
    `static/jposr/index.html:345-346` « Une approche unique en France ».
    Aucune comparaison documentée. CLAUDE.md §6 interdit les fausses
    comparaisons : reformuler en fait vérifiable (« vous dirigez des acteurs
    de l'école toute l'année, 3 h chaque samedi en 1ʳᵉ année ») plutôt
    qu'en supériorité.
  - `scenario-real.html:32` références « McKee, Truby, Schrader, Packard » :
    acceptable (théoriciens publics), mais préciser *comment* (ouvrages
    étudiés ? outils dérivés ?) [À VALIDER].
  - `scenario-real.html:92` « débloquer des aides » — quelles aides (CNC,
    régions…) ? Non précisé.
  - `scenario-real.html:128-144` « Les films écrits et réalisés par nos
    anciens élèves » : 4 affiches titrées (« Lines », « Goodbye Mélodie »,
    « Cheap Thrill », « Noir, juif et borgne ») et **7 affiches sans titre**
    (fichiers `MV5B…jpg`, `8227-…catalogue.jpg`, `95495ae71c-poster.jpg`,
    alt « Film réalisé par un ancien du programme »). Impossible à vérifier
    pour un lecteur ou une IA. À compléter (titre, auteur, année, lien) ou
    à retirer.
  - `scenario-real.html:110` « production extérieure (ici, MAC) » :
    formulation ambiguë (l'école joue le rôle du producteur).
- **Répétitions** : faible. Le programme 2 ans est aussi dans
  `static/jposr/index.html:859-868` (JS `PROGRAM`) avec des livrables
  supplémentaires (« moodboards, notes d'intentions, découpages ») absents
  de la page site → [À VALIDER] et harmoniser.
- **CTA** : JPO + stage + tarifs. Le CTA final « Nous écrire / Présentez-nous
  votre projet » est pertinent pour ce public.
- **Lisibilité** : bonne.

### 2.4 `tarifs.html` — Tarifs

- **Intention couverte** : intention 4 (comparer et connaître les prix).
  Bonne page, la plus factuelle du site.
- **Question principale** « Combien ça coûte au total ? » : partiellement.
  Les mensualités et frais sont donnés, mais **aucun coût annuel total**
  n'est écrit. Calcul dérivé des faits vérifiés : Acting 1ʳᵉ année =
  9 × 370 € + 200 € = **3 530 €** (+ 300 € si semaine intensive) ;
  Scénario = 9 × 350 € + 200 € = **3 350 €**. Ces totaux sont arithmétiques
  mais le « dès » laisse entendre des variantes → [À VALIDER] avant
  publication. Pas de date de vérification des prix sur la page (exigence
  CLAUDE.md §5).
- **Faits manquants** : prix des ateliers à l'unité (« sur demande » × 5),
  prix des intensifs, financement (CPF ? Qualiopi ? aides ?) — un concurrent
  (École ACT) met en avant sa certification Qualiopi ; le MAC ne dit rien
  → [À VALIDER : y a-t-il une certification, un financement possible ?
  Sinon le dire pour éviter les questions].
- **Affirmations non présentes dans le registre (à confirmer)** :
  - `tarifs.html:120` « Parrainage : un mois de sa formation vous est
    offert » — absent du FACTS_REGISTER.
  - `tarifs.html:84` et `:206` « tarifs dégressifs dès la 3ᵉ année » — montant
    non précisé.
  - `tarifs.html:118` « par trimestre ou en une fois » — modalités absentes
    du registre (qui ne mentionne que les mensualités).
  - `tarifs.html:87` « Semaine intensive de rentrée en supplément : 300 € » —
    est-elle obligatoire ? Le planning (`planning.html:36`) la présente comme
    le lancement de l'année.
  - `tarifs.html:139` atelier à l'unité **« Acting Caméra · Hebdomadaire »**
    : absent de la liste des cours ponctuels de `inscription.html:98-102`
    et du registre (qui ne connaît Acting Caméra que comme stage et comme
    atelier de 4ᵉ année). Incohérence.
- **Répétitions** : blocs cours d'essai / JPO / stages déjà vus 4 fois.
- **CTA** : nombreux mais hiérarchisés. Bon.
- **Lisibilité** : bonne. La FAQ (4 questions, `tarifs.html:203-208`) est
  utile et reprise en JSON-LD `FAQPage` (`build.py:150-155`) — cohérente avec
  le visible.

### 2.5 `planning.html` — Planning

- **Intention couverte** : dates (support des intentions 6 et 7).
- **Question principale** « Quand ça commence, quand sont les stages et
  JPO ? » : bien répondue, toutes les dates concordent avec le registre
  (FACT-005).
- **Incohérence** : `planning.html:274` « Acting — 4ᵉ année : 1 atelier de
  3h le mardi » vs `inscription.html:67` « 4ᵉ année : 2 ateliers de 3 h par
  semaine (Acting Caméra & Tournages, Scènes 4) ». À trancher [À VALIDER].
- **Contenu périmé** : `planning.html:263` « Horaires et jours selon les
  groupes — planning détaillé à venir » pour la semaine intensive du 21-27
  sept. 2026, déjà passée au 2026-10-12.
- **Faits manquants** : durée d'une JPO (journée ? demi-journée ?), horaires
  des stages (début/fin de journée) [À VALIDER].
- **Affirmations à confirmer** : `planning.html:305` « D'autres stages seront
  programmés dans l'année ».
- **Lisibilité** : bonne ; le PDF `planning-hebdomadaire.pdf` est la seule
  source détaillée des créneaux — contenu non indexable facilement et non
  audité ici (à ouvrir par analytics-qa / technical-seo).

### 2.6 `cours-essai.html` — Cours d'essai

- **Intention couverte** : conversion « tester avant de s'engager ». Très
  bonne page, concrète (ateliers accessibles, créneaux, ce qui n'est pas
  ouvert à l'essai).
- **Question principale** « Comment tester gratuitement ? » : répondue.
- **Faits manquants** : durée d'un essai (4 h d'après les créneaux, jamais
  écrit), âge minimum, faut-il préparer quelque chose, tenue, nombre de
  participants.
- **À confirmer** : créneaux du soir « 19h–23h » (`cours-essai.html:76-79`,
  `:169-172`) et « Jeu. 19h30–22h30 » (`:95`) — le registre ne valide que
  « 10h–14h » et « 15h–18h » (FACT-006). Un cours jusqu'à 23 h est inhabituel
  : à faire confirmer.
- **Divergence externe** : la fiche Emagister (tierce, non datée) annonce
  « 3 journées d'essai gratuites » et un « stage initiation Actors Studio à
  150 € » — données périmées en circulation (source : emagister.fr, consultée
  2026-10-12). À signaler à digital-pr pour mise à jour des annuaires.
- **CTA** : formulaire clair. Bon.

### 2.7 `inscription.html` — Inscription

- **Intention couverte** : admission (support des intentions 2, 5).
- **Question principale** « Comment s'inscrire et quelles sont les
  conditions ? » : répondue sur la procédure (rendez-vous), pas sur les
  critères (âge minimum, niveau, audition : contenu ? durée ? préparation ?),
  ni sur les documents, ni sur le calendrier de réponse.
- **Faits à confirmer** : `inscription.html:41` et `:154` « entrée directe
  en 2ᵉ ou 3ᵉ année, sur audition » (registre : non listé) ; `:78`
  « atelier d'acting hebdomadaire optionnel, compris dans le tarif » ;
  `:102` « David, fondateur » (nom complet, bio : À confirmer) ; `:177`
  « beaucoup d'élèves en Scénario suivent aussi l'Acting » (pas de chiffre).
- **Incohérence** : cf. 2.5 (4ᵉ année) et 2.4 (Acting Caméra à l'unité).
- **Lisibilité** : bonne ; le formulaire est long mais logique.

### 2.8 `jpo.html` — Journées Portes Ouvertes

- **Intention couverte** : découverte / conversion événementielle.
- **Question principale** « Que se passe-t-il, quand, et comment réserver ? »
  : répondue, sauf les horaires (`jpo.html:119-120` « Les horaires détaillés
  arrivent ») et la durée d'un atelier.
- **Affirmations non sourcées** : `jpo.html:80` « ce que presque aucune école
  ne propose » (comparatif) ; `:44` « se donner une vraie chance de
  carrière » (promesse implicite).
- **FAQ manquante** : la landing `/jpo/` contient 7 questions utiles
  (`static/jpo/index.html:610-637` : débutants, théâtre déjà pratiqué, âge,
  débouchés, prérequis) **absentes de la page site**. À réutiliser après
  validation (voir 2.11 pour les points à corriger).
- **Doublon de page** : `jpo.html` (canonical `/jpo.html`) et la landing
  `/jpo/` (canonical `/jpo/`, `index, follow`) ciblent la même intention
  avec un titre proche (« Devenez acteur · JPO »). Point à arbitrer avec
  seo-auditor / technical-seo (hors périmètre contenu, mais impact direct).

### 2.9 `stages.html` — Stages

- **Intention couverte** : intention 6 (stage accessible aux débutants).
  Bonne page, programmes détaillés, prix clairs.
- **Question principale** « Quel stage pour moi, quand, combien ? » :
  répondue. Manquent : horaires d'une journée de stage, nombre de
  participants (« places limitées » `stages.html:24`, `:207` sans chiffre),
  âge minimum, niveau de langue, politique d'annulation/remboursement
  [À VALIDER].
- **Contenu à durée de vie courte** : hero `stages.html:5-9` « Prochain stage
  17 & 18 octobre 2026 » en dur ; dans 6 jours la page sera périmée alors que
  la landing `/stages/` gère l'expiration (`data-end`). Idem
  `tarifs.html:46`, `:188`, `index.html:140`. Suggestion : un seul bloc
  « prochain stage » alimenté par une donnée commune (technical-seo).
- **Incohérence de nommage** : `stages.html:97` « Stage A — Initiation à la
  Méthode » vs landing `/stages/` (`build_landing_stages.py:80`) « Actors
  Studio A — Faites vos premiers pas dans la Méthode » ; « Stage B » vs
  « Actors Studio B ». Deux noms pour le même produit sur deux URLs
  indexables.
- **À confirmer** : `stages.html:223` « Stage intensif d'été 2027 (dates à
  venir) » ; intensif d'hiver sur 2 jours (`:185`) alors que l'avis
  `stages.html:289` parle de « 4 jours » pour un stage d'hiver passé — pas
  une erreur, mais à expliquer (format variable ?).
- **Noms de coachs** : les avis affichés citent « rafael » (`stages.html:301`)
  et « Rami » (`:305`) — seuls prénoms d'enseignants visibles sur tout le
  site. Si ces personnes enseignent encore, une page Équipe validée
  donnerait de la substance à ces mentions.

### 2.10 `contact.html` — Contact

- **Intention couverte** : contact + localisation (partiel).
- **Question principale** « Où est l'école et comment la joindre ? » :
  répondue (adresse, métro, téléphone, WhatsApp, email).
- **Faits manquants** pour une vraie page « Accès » : horaires d'ouverture
  (vérifiés, mais présents nulle part dans le texte visible du site),
  lignes de bus / tram, accès PMR, parking / vélo, plan ou photo de
  l'entrée, nom sur l'interphone, étage [À VALIDER].
- **Affirmation à confirmer** : `contact.html:7` « on vous répond sous 48h ».
- **Lisibilité** : page courte, correcte. Pas de h2.

### 2.11 Landings `/jpo/` et `/jposr/` (fichiers autonomes)

Fichiers : `newsite/static/jpo/index.html` (1 167 l.) et
`newsite/static/jposr/index.html` (1 146 l.). Même squelette, textes adaptés.

- **Intention** : acquisition Google Ads « devenir acteur » / « devenir
  scénariste réalisateur » + JPO. Contenu riche, souvent plus complet que le
  site (programme par année en JS, FAQ, déroulé d'une JPO).
- **Problèmes prioritaires** :
  - **Offre commerciale périmée** : `static/jpo/index.html:546-547` et
    `static/jposr/index.html:527-528` « 100 € de remise sur les frais
    d'inscription — offre valable jusqu'au 31/08/2026 » toujours affichée
    au 2026-10-12 ; et la case du formulaire (`jpo:670`, `jposr:653`)
    propose cette remise pour la « rentrée décalée de janvier 2027 ».
    Contradiction + offre non enregistrée au registre. **P1 (prix/offre).**
  - `static/jpo/index.html:620` « Un programme dédié existe aussi pour les
    ados » — n'existe nulle part sur le site principal ; absent de la
    version `/jposr/` (`:607`). [À VALIDER ou retirer.]
  - `static/jpo/index.html:877` « Scènes 2 : un atelier exclusif, partagé
    seulement avec le HB Studio de New York » — affirmation forte, non
    sourcée, absente du site. [À VALIDER avec preuve ou retirer.]
  - `static/jpo/index.html:313` / `jposr:313` « Une école créée par des
    pros » — sans nom ni parcours du fondateur.
  - `static/jposr/index.html:234` « Depuis plus de 25 ans, nous formons des
    scénaristes et des réalisateurs » — l'ancienneté du programme Scénario
    n'est pas établie (le registre ne date que l'école). [À VALIDER.]
  - `static/jpo/index.html:624` débouchés « Nos anciens tournent dans des
    films… » (cf. affiches).
  - `static/jpo/index.html:888` livrables incohérents avec `acting.html:126`
    (cf. 2.2).
- **Points positifs réutilisables** : FAQ (`jpo:610-637`, `jposr:597-621`),
  « Comment se déroule une JPO » (`jpo:503-509`), descriptions d'ateliers.
- **Répétitions** : les deux landings partagent ~70 % de texte entre elles
  et avec le site (bloc talent, 3 temps, arguments 01-03, avis).

### 2.12 Landing `/stages/` (générée par `tools/build_landing_stages.py`)

- Générée à partir de `/jpo/` ; données des sessions dans `SESSIONS`
  (`build_landing_stages.py:79-86`) — **quatrième source de vérité** pour
  les stages après `stages.html`, `planning.html` et `build.py` (JSON-LD
  Events `build.py:139-147`), plus `llms.txt`. Aujourd'hui cohérentes sur
  les dates et prix, mais pas sur les noms (cf. 2.9).
- `build_landing_stages.py:246` « éprouvée depuis plus de 25 ans » ;
  `:165-171` promesses du stage à la une (« Libérer votre expression… ») —
  acceptables mais générales.
- `:280` « accessibles aux débutants comme aux profils expérimentés, selon le
  programme » — bonne nuance, à reprendre sur `stages.html`.
- Titre `<title>` « Stages d'acting à Paris — Week-end & intensifs » et
  canonical `/stages/` : concurrence directe avec `stages.html` (titre
  « Stages d'acting & de scénario — week-end et intensifs »). À arbitrer
  (seo-auditor).

### 2.13 Métadonnées éditoriales (`build.py:41-62`) et `llms.txt`

- Titres `Tarifs — … / Planning — … / Contact — … / Inscription — …` : exacts
  mais pauvres (aucun mot-clé d'intention : « formation acting Paris »,
  « école d'acteur »). Description Tarifs (`build.py:53`) « Facilités de
  paiement et offres à la rentrée » : « offres » laisse attendre une promo
  qui n'existe pas sur la page.
- `llms.txt` : fidèle au registre, bon résumé. Il décrit la Méthode en une
  phrase (`llms.txt:5`) ; il n'a aucune page vers laquelle renvoyer pour
  « Stanislavski » ou « enseignants » — ces manques se verront dans les
  réponses des IA.
- Description ORG (`build.py:90`) : « École d'art dramatique et de cinéma »
  — cohérent avec la fiche Google.

---

## 3. Couverture des intentions prioritaires (CLAUDE.md §1)

| # | Intention | Page(s) actuelle(s) | Couverture | Manque principal |
|---|---|---|---|---|
| 1 | Apprendre la méthode Stanislavski à Paris | index, acting (3 ¶) | Faible | Aucune page dédiée ; pas d'explication des notions ; filiation non sourcée |
| 2 | École d'acting / jeu d'acteur cinéma | index, acting | Moyenne | Enseignants, statut, admission, coût total, ce que l'école n'est pas |
| 3 | Jeu face caméra | acting (4ᵉ année), stages (Acting Caméra), tarifs (atelier) | Faible | Aucune page/section dédiée ; données incohérentes (atelier à l'unité ?) |
| 4 | Comparer formations et prix | tarifs | Bonne | Coût annuel total, date de vérification, financement |
| 5 | Acting + scénario + réalisation | scenario-real, tarifs | Bonne | Prérequis, coût du cumul, preuves (films titrés) |
| 6 | Stage accessible aux débutants | stages, /stages/ | Bonne | Horaires, effectif, annulation ; nommage cohérent |
| 7 | Découvrir le MAC | index | Moyenne | Page École (histoire, fondateur, équipe, locaux) |
| 8 | Stanislavski vs Method Acting vs autres | — | Nulle | Page de référence (brouillon fourni) |

Publics du brief : débutants (bien servis) ; perfectionnement (seulement
« entrée en 2ᵉ/3ᵉ année sur audition », rien sur le contenu) ; reconversion
(aucun contenu : financement, compatibilité avec un emploi — les créneaux
soir/week-end existent mais ne sont pas « vendus » ainsi) ; auteurs-
réalisateurs (bien servis) ; formation courte (bien servis) ; budget limité
(Acting Amateur 140 €/mois, stages 160 € — pas regroupés dans un message).

Anglais : « Acting in English » et « Screenwriting in English » existent, mais
un avis (`acting.html:220`, Lauren Bruls) parle de « formation complète en
anglais » alors que le site ne présente l'anglais que comme atelier à
l'unité → [À VALIDER : existe-t-il un cursus complet en anglais ?]. Pas de
page en anglais ; à n'envisager que si la demande est mesurée.

---

## 4. Incohérences inter-pages à trancher (liste consolidée)

| # | Sujet | Source A | Source B | Action |
|---|---|---|---|---|
| I-1 | 3ᵉ temps de la Méthode | `acting.html:50` « Composer » | `index.html`, `llms.txt:5`, `build.py:47`, `static/jpo/index.html:381` « Reproduire » | Harmoniser (propriétaire) |
| I-2 | Rythme 4ᵉ année Acting | `planning.html:274` « 1 atelier de 3h le mardi » | `inscription.html:67` « 2 ateliers de 3 h / semaine » | Trancher |
| I-3 | Livrables fin de cursus | `acting.html:126` (3 scènes, book, démo, outils) | `static/jpo/index.html:888` (+ CV, vidéo de présentation) | Trancher |
| I-4 | Atelier « Acting Caméra » à l'unité | `tarifs.html:139` (hebdomadaire, sur demande) | `inscription.html:98-102` (absent) ; registre (absent) | Confirmer l'existence |
| I-5 | Noms des stages | `stages.html:97,127` « Stage A / B » | `build_landing_stages.py:80,82` « Actors Studio A / B » | Un seul nom |
| I-6 | Offre 100 € | landings (valable jusqu'au 31/08/2026) | formulaire landings (janvier 2027) ; site : aucune offre | Retirer ou documenter |
| I-7 | Programme ados | `static/jpo/index.html:620` | absent partout ailleurs | Confirmer ou retirer |
| I-8 | Cursus complet en anglais | avis `acting.html:220` | site : atelier à l'unité | Clarifier |
| I-9 | Ancienneté du programme Scénario | `static/jposr/index.html:234` « 25 ans » | non documenté | Confirmer |
| I-10 | Parrainage, paiement trimestriel/annuel, dégressivité | `tarifs.html:84,118,120` | registre : absents | Ajouter au registre après validation |
| I-11 | Cours d'essai « 3 jours » / stage 150 € | Emagister (tiers, périmé) | site : 2 cours, 160 € | Mettre à jour l'annuaire (digital-pr) |

---

## 5. Répétitions et dilution

- Bloc « Ce n'est pas le talent qui fait l'acteur » (3 paragraphes) : 4
  occurrences quasi identiques. Proposition : le garder sur `acting.html`,
  le résumer ailleurs en 1 phrase + lien vers la future page Méthode.
- Carrousel d'affiches « Nos acteurs tournent » : 3 occurrences (+ landing).
  Proposition : une seule page « Films et projets » sourcée, et un extrait
  (3 affiches titrées + lien) ailleurs.
- Grille « 3 portes d'entrée / D'autres façons de nous découvrir » : 5
  occurrences. Acceptable (navigation), mais inutile de la dupliquer sur
  Tarifs ET Inscription ET Cours d'essai ET Stages.
- Avis Google : 6 cartes par page, 10 pages → ~50 cartes. Acceptable si les
  avis diffèrent (c'est le cas). Vérifier qu'aucune carte n'est datée
  « juin 2026 » sur un avis plus ancien (`index.html:242`).
- Descriptions d'ateliers : trois versions (acting / cours-essai /
  inscription / landing JS). Une seule source rédactionnelle par atelier
  serait souhaitable (technical-seo peut proposer un partial ou un
  dictionnaire dans `build.py`).

---

## 6. Observation externe (WebSearch, 2026-10-12)

Objectif : voir quelles questions sont posées et ce que publient les
concurrents. Observations factuelles (pas d'interprétation commerciale).

| Observation | Source (consultée le 2026-10-12) |
|---|---|
| Cours Florent : cursus 3 ans, 16 300 à 18 900 € au total (≈ 5 500–6 700 €/an selon option théâtre / cinéma / théâtre-caméra) ; certificat d'école, non RNCP | https://www.onisep.fr/ressources/structures-enseignement/ile-de-france/paris/cours-florent/formation-de-l-acteur-et-de-l-actrice-ecole-privee-d-art-dramatique |
| École ACT (Paris 20ᵉ) met en avant une certification Qualiopi (éligibilité à des financements) | https://www.letudiant.fr/fiches/etudes/fiche/ecole-act-paris.html |
| Aberratio (Paris 20ᵉ) : 3 ans, 6 840 € listés ; Acteurs Artisans (14ᵉ) 5 400 € listés (annuaires, fraîcheur non garantie) | https://www.maformation.fr/formations/metier_acteur.html |
| Guides grand public : « écoles publiques gratuites mais sélectives, privées autour de 4 000 €/an » | https://diplomeo.com/etablissements-ecoles_d_acteur |
| Stages week-end : Atelier Juliette Moltes 2 jours, 90 € (juin 2026) ; The Lir Dublin « Stanislavski weekend » 300 € | https://www.helloasso.com/associations/atelier-juliette-moltes/evenements/stage-theatre-20-21-juin ; https://www.thelir.ie/courses/stanislavski-weekend-course |
| Jeu face caméra à Paris : offres peu lisibles (Pat Studio stage intensif ; Actoreel 6 jours) ; Lyon CinéFabrique 5 jours 1 150 € | https://www.maformation.fr/detailformation/stage-intensif-face-camera-375229 ; https://cinefabrique.fr/wp-content/uploads/2024/05/LE_JEU_DACTEUR_FACE_CAMERA_CF-2024.pdf |
| Questions récurrentes sur « Stanislavski vs Method » : mémoire affective (Strasberg) vs imagination / circonstances données (Adler) vs répétition / instant présent (Meisner) ; débat sur l'existence même de « techniques » distinctes | https://en.wikipedia.org/wiki/Method_acting ; https://www.backstage.com/magazine/article/thing-meisner-adler-strasberg-hagen-technique-method-4867/ ; https://www.themeisnertechniquestudio.com/method-vs-meisner-whats-the-difference-and-why-does-it-matter/ |
| Présence tierce du MAC : Emagister (« 3 journées d'essai », stage 150 €, périmé) ; Spectable (mention « Robert Lewis, fondateur de l'Actors Studio » dans la description) ; Gowork (2 posts, pas de note) ; article London Met (masterclass method acting à Paris) | https://www.emagister.fr/formation_method_acting_center-cen-97852.htm ; https://www.spectable.com/paris/cours-formations/cinema-video-photo/n_1895-l_40888.php ; https://gowork.fr/method-acting-center-paris ; https://londonmet.ac.uk/news/articles/theatre--performance-students-on-a-trip-to-paris-to-study-method-acting |

Enseignements pour le contenu :

- Le **coût annuel total** est l'information que les annuaires et guides
  affichent ; le MAC ne l'écrit pas, les tiers ne peuvent donc pas le
  reprendre correctement.
- La question « Stanislavski ou Method Acting, quelle différence ? » est
  posée et documentée en anglais, très peu en français : une page de
  référence française, honnête, a une vraie place.
- La mention « Robert Lewis » (Spectable) suggère une filiation précise que
  le site ne raconte pas. Si elle est vraie et documentable, c'est la
  meilleure façon de remplacer « descendant direct » par un fait. Si elle
  n'est pas vérifiable, il faut la faire retirer de l'annuaire. [À VALIDER
  par le propriétaire.]
- L'article London Met (visite d'étudiants pour une masterclass de method
  acting à Paris) est une mention tierce potentiellement exploitable
  (digital-pr) si le MAC en est bien l'hôte — non vérifié ici.

Limites : WebSearch depuis cet environnement est orienté résultats
américains ; les requêtes françaises ont ramené peu de pages concurrentes
directes. Pas de données de volume de recherche (aucun outil connecté).
L'audit des concurrents « réellement pertinents » (CLAUDE.md §8) reste à
compléter par seo-auditor avec des sources datées.

---

## 7. Problèmes priorisés (contenu uniquement)

| Prio | Problème | Fichiers | Impact | Confiance | Effort | Risque |
|---|---|---|---|---|---|---|
| P1 | Offre « 100 € de remise » périmée / contradictoire sur les landings | `static/jpo/index.html:546-547,670` ; `static/jposr/index.html:527-528,653` | 4 | 5 | 1 | faible |
| P1 | Rythme 4ᵉ année contradictoire | `planning.html:274` / `inscription.html:67` | 3 | 5 | 1 | faible |
| P2 | Liste d'acteurs célèbres « la méthode de… » et filiation « descendant direct » non sourcées | `acting.html:8,34` ; `index.html:87,156` ; landings | 4 | 4 | 2 | moyen (image) |
| P2 | Affiches de films sans attribution nominative | `index.html:206-213` ; `acting.html:165-172` ; `scenario-real.html:134-144` ; landings | 4 | 4 | 3 (données à obtenir) | moyen (droits) |
| P2 | Absence de page Méthode / Stanislavski (intentions 1 et 8) | nouveau | 5 | 4 | 3 | faible |
| P2 | Absence de FAQ transversale | nouveau | 4 | 4 | 2 | faible |
| P2 | Absence de page École / Équipe | nouveau (dépend du propriétaire) | 4 | 3 | 3 | moyen (consentements) |
| P2 | Coût annuel total et date de vérification absents de Tarifs | `tarifs.html` | 3 | 5 | 1 | faible |
| P2 | Comparatifs invérifiables (« quasi inexistant en France », etc.) | `scenario-real.html:32,37,55` ; `jpo.html:80` ; `jposr:345` | 3 | 4 | 1 | faible |
| P3 | Livrables / « Composer » / Acting Caméra / noms de stages incohérents | voir §4 | 2 | 5 | 1 | faible |
| P3 | Contenus datés en dur (prochain stage, « planning à venir », « horaires arrivent ») | `stages.html:5`, `tarifs.html:46,188`, `planning.html:263`, `jpo.html:119` | 2 | 5 | 2 (technique) | faible |
| P3 | Page Contact sans infos d'accès complètes ni horaires visibles | `contact.html` | 2 | 5 | 1 | faible |
| P3 | Titres / descriptions génériques (Tarifs, Planning, Contact, Inscription) | `build.py:50-61` | 2 | 4 | 1 | faible (technical-seo) |
| P4 | Marquees de mots-clés décoratifs | toutes pages | 1 | 3 | 1 | faible |

---

## 8. Ce que l'audit n'a pas pu vérifier

- Le PDF `planning-hebdomadaire.pdf` (créneaux détaillés) : non ouvert.
- Les pages de `dist/` : non auditées (copie conforme des sources par
  construction).
- Le site en production (non joignable depuis l'environnement) : aucune
  divergence prod/sources n'a pu être contrôlée.
- Les avis Google (44 cartes) : non recoupés un par un avec l'export xlsx.
- Les droits d'utilisation des affiches de films.
