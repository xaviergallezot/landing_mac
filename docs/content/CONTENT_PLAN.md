# Plan éditorial — Method Acting Center

Agent : content-strategist · Date : 2026-10-12 · Statut : proposition (Phase B)

Fondé sur `docs/content/CONTENT_AUDIT.md`, `docs/FACTS_REGISTER.md` et
`CLAUDE.md`. Règles appliquées :

- enrichir les pages existantes avant d'en créer ;
- une nouvelle page seulement si elle répond à une intention réelle que
  rien ne couvre (pas de pages ville/mot-clé, pas de comparatifs « meilleure
  école ») ;
- aucun fait nouveau publié sans statut **Vérifié** au registre ; tout le
  reste est marqué [À VALIDER] ;
- la charte et la structure du site sont conservées : ce plan décrit des
  contenus (textes, plans de page, FAQ), pas une refonte.

Statuts : **idée** · **brouillon** · **validé** · **publié**.

---

## 0. Architecture cible (résumé)

```
/                      Accueil (enrichir)
/acting                Formation Acting (enrichir) ──┐
/scenario-real         Scénario · Réal · Direction (enrichir)
/stages.html           Stages (enrichir)             │ liens croisés
/cours-essai           Cours d'essai (enrichir)      │
/jpo.html              Portes Ouvertes (enrichir)    │
/inscription           Inscription (enrichir)        │
/tarifs                Tarifs (enrichir)             │
/planning              Planning (corriger)           │
/contact               Contact, accès & horaires (enrichir, absorbe « Accès »)
/la-methode            NOUVEAU — Stanislavski, Method Acting et la Méthode du MAC  [brouillon]
/faq                   NOUVEAU — Questions fréquentes                                 [brouillon]
/ecole                 NOUVEAU — L'école et l'équipe (histoire, fondateur, coachs)    [idée, dépend du propriétaire]
/films-et-projets      NOUVEAU — Films et projets d'élèves                             [idée, dépend des preuves]
(/jeu-face-camera)     Pas de page tant que l'offre n'est pas clarifiée : section dans /acting + stage
/jpo/, /jposr/, /stages/  Landings Ads : corrections seulement, hors navigation
```

Navigation : ajouter « La Méthode » et « FAQ » (menu ou footer) ; « L'école »
dès validation. Ne rien ajouter pour les landings (consigne du brief).

Ordre de réalisation proposé :

1. Corrections factuelles P1/P2 sur pages existantes (voir §1).
2. Page **La Méthode** (brouillon livré) + FAQ (brouillon livré).
3. Enrichissements Tarifs, Acting, Contact.
4. Page École/Équipe et Films & projets, quand les faits sont fournis.

---

## 1. Pages existantes à enrichir

Format allégé (les champs complets sont dans §2 pour les nouvelles pages).

### 1.1 `/acting` — Formation Acting

- **Objectif commercial** : demandes de cours d'essai et d'inscription Acting.
- **Public** : débutants adultes ; acteurs voulant se perfectionner ;
  reconversion.
- **Intention** : « formation acteur cinéma Paris », « école d'acting Paris »,
  « apprendre à jouer vrai ».
- **Question principale** : « Que vais-je apprendre, à quel rythme, pour
  quel coût, et est-ce pour moi ? »
- **Questions secondaires** : faut-il de l'expérience ? quel âge ? combien
  d'heures par semaine ? qui enseigne ? que se passe-t-il à la fin ? peut-on
  entrer en 2ᵉ année ? y a-t-il du travail face caméra ?
- **Modifications proposées** :
  1. Retirer `acting.html:8` (liste d'acteurs célèbres) ou la remplacer par
     une phrase sourcée renvoyant à `/la-methode`.
  2. Remplacer « descendant direct » (`:34`) par la formulation validée issue
     du brouillon Méthode (lignée documentée ou formulation prudente).
  3. Harmoniser le 3ᵉ temps (« Reproduire » / « Composer ») [À VALIDER I-1].
  4. Ajouter un bloc « En pratique » : rythme par année (source Planning,
     après résolution I-2), prix de base + frais (source Tarifs, avec date),
     admission (rendez-vous ; audition pour 2ᵉ/3ᵉ année [À VALIDER]),
     cours d'essai (2, gratuits, toute l'année).
  5. Ajouter une section « Jeu face caméra dans le cursus » (intention 3) :
     ce qui est filmé en 2ᵉ et 3ᵉ année, l'atelier Acting Caméra & Tournages
     de 4ᵉ année, le stage Acting Caméra ; tout chiffre [À VALIDER I-3].
  6. Ajouter 4-5 questions FAQ propres à la page (extraites du brouillon FAQ).
  7. Attribuer les affiches ou retirer le carrousel (voir 2.4).
- **Liens internes** : /la-methode, /tarifs, /cours-essai, /stages.html
  (Stage A, Acting Caméra), /inscription, /faq, /ecole (quand publiée).
- **CTA** : principal = cours d'essai ; secondaire = stage ; tertiaire = JPO
  (daté).
- **Risques** : promesses de production (« on vous tourne… ») et livrables
  non confirmés.
- **Critères de succès** : impressions/clics sur requêtes « formation
  acting Paris », « école acting Paris » (Search Console) ; taux de clic vers
  cours d'essai ; aucune affirmation non sourcée restante.
- **Statut** : idée (corrections listées).

### 1.2 `/tarifs` — Tarifs

- **Objectif** : lever le doute sur le coût, générer des demandes
  d'inscription qualifiées.
- **Question principale** : « Combien ça coûte en tout, et comment payer ? »
- **Modifications** :
  1. Ajouter « Coût annuel indicatif » par formation : Acting 1ʳᵉ année
     9 × 370 € + 200 € = 3 530 € (+ 300 € semaine intensive si elle est
     suivie) ; Scénario 9 × 350 € + 200 € = 3 350 €. Formule [À VALIDER :
     le « dès » signifie-t-il que 370 € est bien le tarif 1ʳᵉ année ?].
  2. Ajouter « Tarifs vérifiés le JJ/MM/AAAA » (exigence CLAUDE.md §5).
  3. Préciser « inclus / non inclus » (semaine intensive : obligatoire ?
     [À VALIDER]).
  4. Clarifier parrainage, paiement trimestriel/annuel, dégressivité : à
     garder tels quels tant qu'ils sont déjà en ligne, mais à inscrire au
     registre [À VALIDER I-10].
  5. Ajouter une question « Financement / CPF / certification » avec la
     réponse validée, même si elle est négative [À VALIDER].
  6. Trancher l'atelier « Acting Caméra » à l'unité [À VALIDER I-4].
  7. Étendre la FAQ (4 → 7 questions) et mettre à jour le `FAQPage` JSON-LD
     en conséquence (technical-seo).
- **Liens** : /acting, /scenario-real, /stages.html, /cours-essai,
  /inscription, /faq.
- **CTA** : inchangés.
- **Risques** : afficher un total que le bureau ne confirme pas → attendre
  validation.
- **Critères** : baisse des questions « combien ça coûte » dans les
  formulaires (champ message) ; clics vers Inscription.
- **Statut** : idée.

### 1.3 `/` — Accueil

- **Modifications** : (a) remplacer « descendant direct » (`index.html:87`,
  `:156`) par la formulation validée ; (b) ajouter un court bloc factuel
  « L'école en bref » (type d'établissement, adresse, depuis 1999 [À
  confirmer], deux formations, cours d'essai, horaires d'ouverture) — utile
  aux lecteurs pressés et aux IA ; (c) résumer le bloc « talent » en 2
  lignes + lien /la-methode ; (d) attribuer ou retirer les affiches ; (e)
  lien vers /faq et /ecole.
- **Statut** : idée.

### 1.4 `/scenario-real`

- **Modifications** : (a) reformuler les comparatifs (`:32`, `:37`, `:55`)
  en faits : « vous dirigez des acteurs de l'école chaque samedi matin
  (3 h) en 1ʳᵉ année » ; (b) ajouter « En pratique » (rythme, prix, cumul
  avec Acting, prérequis [À VALIDER], matériel [À VALIDER]) ; (c) préciser
  comment McKee/Truby/Schrader/Packard sont utilisés [À VALIDER] ; (d)
  titrer les 7 affiches anonymes ou les retirer ; (e) harmoniser les
  livrables avec la landing (`jposr:867`) [À VALIDER] ; (f) FAQ dédiée (3-4
  questions : débutant en écriture ? faut-il un projet ? option tournage :
  tarif ?).
- **Statut** : idée.

### 1.5 `/stages.html`

- **Modifications** : (a) un seul nom par stage (I-5) ; (b) section « Pour
  qui ? » reprenant la nuance de la landing (débutants et expérimentés
  selon le stage) ; (c) horaires d'une journée type, effectif, politique
  d'annulation [À VALIDER] ; (d) bloc « prochain stage » non daté en dur
  (technical-seo) ; (e) FAQ stage (faut-il avoir fait le A avant le B ?
  que préparer ? âge ?).
- **Statut** : idée.

### 1.6 `/cours-essai`

- **Modifications** : (a) écrire la durée d'un essai (4 h d'après les
  créneaux) [À VALIDER] ; (b) confirmer les créneaux du soir 19h–23h
  [À VALIDER] ; (c) 3 questions FAQ (préparer ? âge ? et après ?).
- **Statut** : idée.

### 1.7 `/jpo.html`

- **Modifications** : (a) reprendre la FAQ de la landing après correction
  (retirer « programme ados » et « débouchés » non sourcés) ; (b) retirer
  « ce que presque aucune école ne propose » (`:80`) ; (c) ajouter « Comment
  se déroule une JPO » (4 étapes, déjà rédigées sur la landing) ; (d)
  gérer la date (section « prochaine session » alimentée par le planning).
- **Statut** : idée.

### 1.8 `/inscription`

- **Modifications** : ajouter « Conditions d'admission » : âge minimum
  [À VALIDER], niveau requis (aucun en 1ʳᵉ année ?) [À VALIDER], audition
  pour 2ᵉ/3ᵉ année : format, durée, préparation [À VALIDER], documents
  demandés [À VALIDER], délai de réponse [À VALIDER]. Résoudre I-2 et I-4.
- **Statut** : idée.

### 1.9 `/planning`

- **Modifications** : corriger I-2 ; supprimer « planning détaillé à venir »
  (`:263`) ; ajouter horaires types des stages et des JPO [À VALIDER].
- **Statut** : idée.

### 1.10 `/contact` → « Contact, accès & horaires »

Plutôt qu'une page « Accès » séparée (trop mince, risque de doublon avec
Contact), enrichir la page existante.

- **Question principale** : « Comment venir, quand est-ce ouvert, comment
  joindre quelqu'un ? »
- **Contenu à ajouter** : horaires d'ouverture (vérifiés : lun–jeu
  10h–20h30, ven 11h–19h, sam–dim 11h–17h) ; accès métro (M7 Maison Blanche ;
  Place d'Italie M5/M6/M7) ; bus / tram / vélo / parking [À VALIDER] ;
  accessibilité PMR [À VALIDER] ; repère visuel de l'entrée, étage,
  interphone [À VALIDER] ; carte (lien Maps existant) ; FAQ courte
  (« Peut-on visiter sans rendez-vous ? » [À VALIDER]).
- **Liens** : /cours-essai, /jpo.html, /faq.
- **Risques** : « réponse sous 48 h » à confirmer ou à adoucir (« sous 2
  jours ouvrés en général »).
- **Critères** : visibilité locale (fiche Google ↔ page cohérentes),
  appels/itinéraires depuis la fiche.
- **Statut** : idée.

### 1.11 Landings `/jpo/`, `/jposr/`, `/stages/`

Corrections seulement (aucun ajout de navigation) :

1. Retirer ou redater l'offre « 100 € » (I-6) — **avant toute diffusion
   Ads**.
2. Retirer « programme ados » (I-7) et « HB Studio » (`jpo:877`) sauf preuve.
3. Harmoniser livrables (I-3) et noms de stages (I-5).
4. Remplacer « descendant direct » et « école créée par des pros » par les
   formulations validées.
5. `jposr:234` « 25 ans » pour le programme Scénario : à confirmer ou
   reformuler (« l'école, depuis 1999 »).

---

## 2. Nouvelles pages

### 2.1 `/la-methode` — Stanislavski, Method Acting et la Méthode enseignée au Method Acting Center

- **Objectif commercial** : devenir la page de référence française sur le
  sujet, capter les intentions 1 et 8, rassurer sur le sérieux de la
  pédagogie, alimenter les réponses des IA avec une source claire ; CTA
  doux vers le cours d'essai.
- **Public visé** : futurs élèves curieux de la méthode ; élèves d'autres
  écoles ; lecteurs qui comparent « Stanislavski » et « Method Acting » ;
  journalistes et assistants IA.
- **Intention de recherche** : informationnelle (« méthode Stanislavski »,
  « method acting c'est quoi », « différence Stanislavski Actors Studio »,
  « apprendre la méthode Stanislavski à Paris »).
- **Question principale** : « Qu'est-ce que la méthode Stanislavski, en quoi
  diffère-t-elle du Method Acting américain, et qu'enseigne vraiment le
  Method Acting Center ? »
- **Questions secondaires** : qui était Stanislavski ? qu'est-ce qu'un
  objectif, une action, une circonstance donnée ? qu'est-ce que la mémoire
  affective et pourquoi est-elle discutée ? Strasberg, Adler, Meisner :
  quelles différences ? le method acting est-il dangereux ? faut-il
  « devenir » son personnage ? est-ce adapté au cinéma ? est-ce pour les
  débutants ?
- **Faits officiels nécessaires** : ce que l'école revendique (3 temps :
  déclencher / maîtriser / reproduire — Vérifié sur le site, À confirmer
  en détail) ; noms et contenu des ateliers (Exploration, Backstory,
  Scènes, Composition — sur le site, À confirmer) ; références
  pédagogiques exactes du fondateur et des coachs [À VALIDER] ; filiation
  éventuelle (Actors Studio, Robert Lewis ? mention Spectable) [À VALIDER].
- **Preuves à obtenir** : parcours de formation du fondateur ; ouvrages de
  référence utilisés ; éventuels certificats / stages suivis à l'étranger ;
  autorisation de citer les noms.
- **Plan H1/H2** :
  - H1 : Stanislavski, Method Acting et la Méthode enseignée au Method
    Acting Center
  - H2 : En deux minutes (réponse directe)
  - H2 : Konstantin Stanislavski et le « système » (contexte historique)
  - H2 : Les notions clés du système (H3 : objectifs et actions ; H3 :
    circonstances données et « si magique » ; H3 : écoute et réaction ;
    H3 : mémoire affective et actions physiques)
  - H2 : De Moscou à New York : le Method Acting américain (H3 : Group
    Theatre et Actors Studio ; H3 : Strasberg, Adler, Meisner, trois
    lectures ; H3 : ce que « Method Acting » veut dire aujourd'hui)
  - H2 : Stanislavski ou Method Acting : les différences en un tableau
  - H2 : Ce que le Method Acting Center enseigne (H3 : déclencher,
    maîtriser, reproduire ; H3 : comment cela se traduit dans les ateliers ;
    H3 : ce que nous ne faisons pas)
  - H2 : Questions fréquentes sur la Méthode
  - H2 : Pour aller plus loin (lectures, et comment tester)
- **Liens internes** : /acting, /stages.html (Stage A), /cours-essai, /faq,
  /ecole, /scenario-real (direction d'acteurs).
- **CTA** : « Tester la Méthode lors d'un cours d'essai gratuit » (fin de
  page, non intrusif) ; lien Stage A.
- **Risques** : attribuer au MAC une fidélité à Stanislavski ou à
  l'Actors Studio non prouvée ; erreurs historiques (relire les faits
  tiers) ; ton promotionnel qui nuirait à la crédibilité.
- **Critères de succès** : page indexée et positionnée sur les requêtes
  informationnelles ci-dessus ; citée par les IA comme source sur
  « différence Stanislavski / method acting » (protocole geo-ai-visibility) ;
  temps de lecture ; clics vers cours d'essai.
- **Statut** : **brouillon** →
  `docs/content/drafts/la-methode-stanislavski-method-acting.md`.

### 2.2 `/faq` — Questions fréquentes

- **Objectif** : répondre en un endroit aux questions pratiques (tarifs,
  durée, débutants, essai, stages, admission, horaires, accès) ; réduire
  les emails répétitifs ; fournir des réponses courtes et citables.
- **Public** : tous les futurs élèves ; parents ; assistants IA.
- **Intention** : « method acting center prix », « cours d'essai gratuit
  acting Paris », « école d'acting débutant », « formation acteur horaires
  soir ».
- **Question principale** : « Les réponses rapides aux questions pratiques
  avant de contacter l'école. »
- **Questions secondaires** : voir brouillon (8 rubriques, ~30 questions).
- **Faits nécessaires** : uniquement ceux marqués Vérifié au registre ;
  les autres [À VALIDER].
- **Preuves** : aucune (contenu factuel issu du registre).
- **Plan H1/H2** : H1 « Questions fréquentes » ; H2 par rubrique : Tarifs et
  paiement · Durée et rythme · Débutants et niveau · Cours d'essai · Stages
  · Admission et inscription · Horaires et calendrier · Accès et contact ·
  La Méthode (renvoi) · En anglais.
- **Liens internes** : toutes les pages du site (c'est le hub).
- **CTA** : cours d'essai ; contact.
- **Risques** : réponses qui vieillissent (dates, prix) → prévoir « mis à
  jour le » et une revue trimestrielle ; cohérence avec la FAQ Tarifs
  (éviter deux réponses différentes à la même question : la FAQ Tarifs
  renvoie vers /faq ou reprend mot pour mot).
- **Critères** : apparition en rich results FAQ (non garanti) ; baisse des
  questions récurrentes en formulaire ; citations IA.
- **Statut** : **brouillon** → `docs/content/drafts/faq.md`.

### 2.3 `/ecole` — L'école et l'équipe

- **Objectif** : crédibilité (E-E-A-T) : qui est derrière l'école, depuis
  quand, où, avec qui.
- **Public** : futurs élèves et parents ; presse ; IA.
- **Intention** : « method acting center fondateur », « qui enseigne au
  method acting center », « method acting center avis » (navigationnelle).
- **Question principale** : « Qui enseigne, et pourquoi leur faire
  confiance ? »
- **Questions secondaires** : histoire de l'école ; statut juridique et
  type d'établissement ; locaux (nombre de salles, plateau ?) ; nombre
  d'élèves ; reconnaissance / absence de diplôme d'État ; valeurs
  (« bienveillance et exigence », déjà sur le site).
- **Faits nécessaires** [tous À VALIDER] : nom complet et parcours du
  fondateur « David » ; liste des coachs (nom public, fonction, 3 lignes de
  bio, expériences vérifiables, lien IMDb/Unifrance/agent si existant,
  consentement écrit) ; année de création (1999, à confirmer) ; locaux ;
  statut.
- **Preuves à obtenir** : consentements ; liens vers filmographies
  publiques ; photo de l'équipe autorisée.
- **Plan H1/H2** : H1 « L'école » ; H2 Depuis 1999 à Paris 13ᵉ ; H2 Le
  fondateur ; H2 Les coachs (H3 par personne) ; H2 Les lieux ; H2 Ce que
  l'école est, et n'est pas (statut, diplôme) ; H2 Nos avis (lien fiche
  Google, 4,8/5 sur 98, daté).
- **Liens** : /la-methode, /acting, /scenario-real, /contact, /faq.
- **CTA** : cours d'essai.
- **Risques** : publier des données personnelles sans consentement ;
  bios invérifiables ; coachs qui quittent l'école (prévoir mise à jour).
- **Critères** : page référencée sur la marque ; mention des noms dans les
  réponses IA sur « qui enseigne » ; baisse de la question dans les
  formulaires.
- **Statut** : **idée** (bloquée par les faits du propriétaire). Variante
  minimale possible sans noms : « L'école » (histoire, lieux, statut) puis
  ajout des bios.

### 2.4 `/films-et-projets` — Films et projets d'élèves

- **Objectif** : transformer les carrousels d'affiches en preuves
  vérifiables ; page unique au lieu de 3 répétitions.
- **Public** : futurs élèves ; presse ; IA.
- **Intention** : « method acting center anciens élèves », « films réalisés
  par les élèves ».
- **Question principale** : « Qu'ont fait concrètement les anciens ? »
- **Faits nécessaires** [tous À VALIDER] : pour chaque entrée : titre,
  année, réalisateur/production, nom de l'élève ou ancien, rôle ou fonction,
  années de formation au MAC, lien public (fiche film, bande-annonce),
  consentement de la personne, droit d'usage de l'affiche. Projets
  pédagogiques internes (scènes tournées, courts) : même chose.
- **Plan H1/H2** : H1 « Films et projets » ; H2 Nos anciens à l'écran (liste
  sourcée) ; H2 Films écrits et réalisés par les élèves du programme
  Scénario ; H2 Projets pédagogiques (scènes tournées à l'école) ; H2
  Comment ces projets naissent (lien Acting 4ᵉ année / option réalisation).
- **Liens** : /acting, /scenario-real, /ecole.
- **CTA** : cours d'essai / JPO.
- **Risques** : droits à l'image et sur les affiches ; sur-interprétation
  (« nos anciens » ≠ « formés par nous ») ; si aucune preuve n'est fournie,
  **ne pas créer la page et retirer les carrousels**.
- **Critères** : zéro affiche sans attribution ; citations tierces.
- **Statut** : **idée** (bloquée par les preuves).

### 2.5 Jeu face caméra — page différée

Intention 3 réelle, mais l'offre du MAC est dispersée (4ᵉ année, stage
Acting Caméra, atelier à l'unité non confirmé). Créer une page maintenant
produirait un contenu mince ou inexact. Décision proposée : section dédiée
dans `/acting` + fiche du stage Acting Caméra enrichie ; réévaluer une page
`/jeu-face-camera` quand (a) I-4 est tranché et (b) les contenus filmés
(volume, matériel, conditions) sont validés.

### 2.6 Pages volontairement non créées

- Pages par ville/arrondissement (« cours de théâtre Paris 13 ») : doublons
  sans valeur.
- « Meilleure école d'acting Paris » / comparatif concurrents : interdit
  sans critères et preuves (CLAUDE.md §6, §8) ; un comparatif factuel coûts
  / durées pourra être étudié plus tard par seo-auditor avec sources datées.
- Page « Témoignages » séparée : les avis sont déjà publics et affichés ;
  une page de plus n'apporte rien tant qu'il n'y a pas de témoignages
  longs consentis.
- Version anglaise : pas avant mesure d'une demande (formulaires, Search
  Console).

---

## 3. Dépendances et validations demandées au propriétaire

| # | Donnée à fournir | Bloque |
|---|---|---|
| V-1 | Formulation exacte de la filiation pédagogique (qui a formé le fondateur, où, quand ; lien éventuel avec l'Actors Studio / Robert Lewis) | /la-methode, accueil, acting, landings |
| V-2 | Nom complet et parcours du fondateur ; liste des coachs avec bios et consentements | /ecole |
| V-3 | Liste nominative des films/rôles des anciens + droits des affiches | /films-et-projets, carrousels |
| V-4 | Rythme réel de la 4ᵉ année (I-2) ; livrables (I-3) ; 3ᵉ temps (I-1) | acting, planning, inscription |
| V-5 | Existence de l'atelier Acting Caméra à l'unité (I-4) ; cursus complet en anglais (I-8) ; programme ados (I-7) | tarifs, inscription, landings |
| V-6 | Offre 100 € : retirée ou nouvelles conditions (I-6) | landings |
| V-7 | Parrainage, paiement trimestriel/annuel, dégressivité 3ᵉ année, semaine intensive obligatoire ou non (I-10) ; financement/certification | tarifs, FAQ |
| V-8 | Créneaux du soir (19h–23h), durée d'un cours d'essai, âge minimum, audition 2ᵉ/3ᵉ année, documents | cours-essai, inscription, FAQ |
| V-9 | Horaires des stages et JPO, effectifs, annulation | stages, jpo, FAQ |
| V-10 | Accès : bus/tram, PMR, entrée, « réponse sous 48 h » | contact, FAQ |
| V-11 | Année de création 1999 (confirmation) | partout |

---

## 4. Calendrier de maintenance éditoriale proposé

- Mensuel : dates (prochain stage, prochaine JPO) sur accueil, tarifs,
  stages, jpo, planning, llms.txt, landings.
- Trimestriel : FAQ, tarifs (date de vérification), avis affichés (note et
  nombre), équipe.
- Annuel (juin) : prix de l'année suivante, calendrier, programme.
