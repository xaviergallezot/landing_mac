# AI Prompt Benchmark — Method Acting Center

Agent : geo-ai-visibility · Version 1 · Rédigé le 2026-10-12 · Statut : **protocole prêt à exécuter, aucun résultat enregistré**.

> Aucune réponse d'assistant IA n'a été simulée ni inventée dans ce document.
> L'environnement de travail de l'agent ne permet pas d'interroger ChatGPT, Claude,
> Gemini, Perplexity ni Google (AI Overviews / AI Mode). Le benchmark doit être
> exécuté par le propriétaire (ou une personne mandatée) depuis un navigateur,
> puis les résultats consignés dans le tableau de la section 6.

## 1. Objectif

Mesurer, de façon reproductible, si le Method Acting Center :
1. apparaît dans les réponses des assistants IA pour des demandes auxquelles
   l'école répond réellement ;
2. est décrit avec des informations exactes (adresse, tarifs, durée, méthode,
   cours d'essai, dates) ;
3. est cité avec des sources réelles et accessibles ;
4. n'est pas confondu avec une autre organisation.

Aucun score ne garantit une citation future. Le benchmark sert à constater, pas à promettre.

## 2. Plateformes à tester

Chaque plateforme a ses propres sources et mécanismes. Ne pas comparer un résultat
d'une plateforme à une autre comme s'il s'agissait du même test.

| Plateforme | Mode à tester | Ce qui alimente la réponse (à vérifier à la date du test) | Robots déclarés dans `robots.txt` du site |
|---|---|---|---|
| ChatGPT (OpenAI) | (a) sans recherche web ; (b) avec recherche web activée | (a) connaissances du modèle ; (b) index web OpenAI + pages consultées en direct | `GPTBot`, `OAI-SearchBot`, `ChatGPT-User` |
| Claude (Anthropic) | (a) sans recherche ; (b) avec recherche web | idem | `ClaudeBot`, `Claude-SearchBot`, `Claude-User` |
| Gemini (Google) | réponse standard | index Google, Knowledge Graph, fiche Google Business (requêtes locales) | `Googlebot`, `Google-Extended` |
| Perplexity | mode recherche standard | index propre + pages consultées, citations numérotées | `PerplexityBot`, `Perplexity-User` |
| Google Search | AI Overviews / AI Mode **si disponibles en France à la date du test** | index Google + fiche Google Business + avis | `Googlebot` |
| Bing Copilot (optionnel) | réponse standard | index Bing | `Bingbot` |

Limites connues :
- Les réponses varient d'une session à l'autre, même à prompt identique. Chaque
  prompt doit être posé **2 fois** (deux sessions neuves) ; on note les deux.
- La disponibilité de la recherche web, de la géolocalisation et des versions de
  modèles change dans le temps : noter précisément le modèle et le mode affichés.
- Un compte connecté avec historique peut biaiser les réponses : utiliser une
  session neuve, sans mémoire activée, sans « instructions personnalisées ».

## 3. Procédure d'exécution

1. **Préparation**
   - Navigateur en navigation privée. Se connecter uniquement si la plateforme l'exige.
   - Désactiver la mémoire / personnalisation quand l'option existe.
   - Langue d'interface : français. Localisation : Paris (si la plateforme la demande).
   - Noter la date, l'heure, la plateforme, le modèle affiché, le mode (recherche web on/off).
2. **Exécution**
   - Coller le prompt **à l'identique** (texte exact de la section 4, sans ajout).
   - Ne pas relancer, ne pas reformuler, ne pas « aider » l'assistant.
   - Copier la réponse complète dans un fichier texte daté (`docs/geo/runs/AAAA-MM-JJ/<plateforme>-<ID>.txt`, à créer au premier run).
   - Capturer les sources / citations affichées (URL exactes).
3. **Enregistrement** (une ligne par prompt × plateforme × répétition) dans le tableau de la section 6.
4. **Analyse** (après le run complet)
   - Vérifier chaque URL citée : existe-t-elle ? est-elle accessible ? parle-t-elle vraiment de l'école ?
   - Comparer chaque fait énoncé au `docs/FACTS_REGISTER.md`.
   - Lister les concurrents cités et leur fréquence.
   - Reporter les sources erronées dans `docs/geo/CITATION_SOURCES.md`.
5. **Fréquence** : run complet tous les **3 mois**, plus un run partiel (prompts E1–E8) après chaque modification importante du site ou des fiches tierces. Ne pas comparer deux runs dont le modèle ou le mode diffèrent.

## 4. Les prompts

Langue : français sauf mention. Les prompts anglais (A6, B6, E9) sont justifiés par
l'existence d'ateliers « Acting in English » et « Screenwriting in English » et par les
avis Google d'élèves internationaux affichés sur le site.

### A. Découverte (intentions 2, 3, 6, 7)

| ID | Prompt exact |
|---|---|
| A1 | Quelle école d'acting choisir à Paris pour devenir acteur de cinéma ? |
| A2 | Où apprendre le jeu face caméra à Paris ? |
| A3 | Je suis débutant complet, quelle école d'acteur à Paris accepte les débutants sans audition ? |
| A4 | Quelles écoles de jeu d'acteur à Paris proposent un cours d'essai gratuit ? |
| A5 | Quel stage d'acting d'un week-end faire à Paris cet automne ? |
| A6 | *(EN)* Where can I take method acting classes in English in Paris? |
| A7 | Je veux me reconvertir pour devenir acteur à 35 ans, quelle formation à Paris en cours du soir ? |

### B. Méthode (intentions 1, 8)

| ID | Prompt exact |
|---|---|
| B1 | Où étudier la méthode Stanislavski en France ? |
| B2 | Quelle formation à Paris travaille l'interprétation réaliste et les émotions vraies, dans l'esprit de l'Actors Studio ? |
| B3 | Quelle est la différence entre le système de Stanislavski, le Method Acting de Lee Strasberg et la technique Meisner ? Où apprendre chacune de ces approches à Paris ? |
| B4 | Existe-t-il une école à Paris qui enseigne le Method Acting ? |
| B5 | Qui a écrit un livre en français sur la méthode Stanislavski pour les acteurs ? |
| B6 | *(EN)* Which drama schools in Paris teach Stanislavski-based or Strasberg-based method acting? |

### C. Budget (intention 4)

| ID | Prompt exact |
|---|---|
| C1 | Quelle école d'acting est abordable à Paris ? |
| C2 | Comment comparer les prix des formations d'acteur à Paris ? Donne des exemples de tarifs. |
| C3 | Combien coûte une formation d'acteur à Paris par mois ? |
| C4 | Quelle formation d'acteur à Paris peut-on payer en mensualités, sans payer l'année d'avance ? |

### D. Parcours combinés (intention 5)

| ID | Prompt exact |
|---|---|
| D1 | Où apprendre à la fois l'acting, le scénario et la réalisation à Paris ? |
| D2 | Quelle formation permet d'écrire et de réaliser ses propres courts-métrages tout en apprenant à diriger des acteurs ? |
| D3 | Je veux apprendre la direction d'acteurs à Paris, quelles formations existent ? |
| D4 | Formation scénario le week-end à Paris pour quelqu'un qui travaille en semaine : quelles options ? |

### E. Marque (intention 7)

| ID | Prompt exact |
|---|---|
| E1 | Que propose le Method Acting Center à Paris ? |
| E2 | Quels sont les tarifs du Method Acting Center ? |
| E3 | Quelle méthode pédagogique utilise le Method Acting Center ? |
| E4 | Où se trouve le Method Acting Center et comment s'y inscrire ? |
| E5 | Quels sont les avantages et les limites de la formation du Method Acting Center ? |
| E6 | Le Method Acting Center propose-t-il des cours d'essai gratuits ? |
| E7 | Qui a fondé le Method Acting Center à Paris ? |
| E8 | Le Method Acting Center est-il lié à l'Actors Studio de New York ? |
| E9 | *(EN)* Is the Method Acting Center in Paris a good school for an English speaker? |

### F. Comparaison

| ID | Prompt exact |
|---|---|
| F1 | J'ai un budget de 4 000 € par an pour une formation d'acteur à Paris. Quelles écoles rentrent dans ce budget ? |
| F2 | Compare le Cours Florent, le Method Acting Center et une école d'acting de ton choix à Paris : durée, prix, méthode, accès aux débutants. Ne cite que des informations que tu peux sourcer. |
| F3 | Quelle école à Paris pour apprendre le jeu caméra plutôt que le théâtre classique ? Compare deux ou trois options. |
| F4 | Entre un cursus d'acting sur 4 ans et des stages ponctuels, que me conseilles-tu pour débuter à Paris, et chez qui ? |

Total : **34 prompts** (A : 7, B : 6, C : 4, D : 4, E : 9, F : 4).

## 5. Grille de notation

À remplir pour chaque ligne du tableau. Rester factuel : la note décrit la réponse, pas une opinion.

| Champ | Valeurs autorisées |
|---|---|
| Présence | `oui` (l'école est nommée) / `non` / `confusion` (une autre entité est prise pour l'école, ou l'inverse) |
| Position | rang de mention parmi les écoles citées (1 = première) ; `—` si absente ; `seule` si c'est la seule école citée |
| Exactitude | `exacte` / `partielle` / `erronée` / `n/a` — comparer avec le registre de vérité sur : adresse (93 av. d'Italie, 75013), téléphone, tarifs (dès 370 €/mois Acting, dès 350 €/mois Scénario, 9 mensualités, 200 € de frais), durée (4 ans / 2 ans), cours d'essai (2, gratuits), stages (dès 160 €), fondation (1999), méthode (Stanislavski / Actors Studio) |
| Faits erronés | texte libre : citer l'erreur exacte (ex. « 250 €/mois », « rue de Tolbiac », « 3 jours d'essai », « fondée en 2009 ») |
| Sources citées | URL complètes, ou `aucune` |
| Sources réelles ? | `oui` / `non` / `partiel` — après vérification manuelle de chaque URL |
| Concurrents cités | noms, dans l'ordre |
| Action | voir `GEO_ACTION_PLAN.md` ; ex. « demander correction Emagister », « ajouter page À propos », « rien » |

Indicateurs agrégés à calculer après chaque run (par plateforme et par bloc A–F) :
- taux de présence = lignes `oui` / lignes totales ;
- taux de confusion = lignes `confusion` / lignes totales ;
- taux d'exactitude = lignes `exacte` / lignes `oui` ;
- part des sources citées pointant vers methodacting.fr ;
- part des sources citées pointant vers des fiches tierces obsolètes (voir `CITATION_SOURCES.md`).

## 6. Tableau d'enregistrement (vide)

Une ligne par prompt × plateforme × répétition. Copier le bloc ci-dessous dans
`docs/geo/runs/AAAA-MM-JJ/RESULTS.md` à chaque run (ou l'utiliser comme en-tête CSV).

```
ID;Plateforme;Modèle affiché;Mode (web on/off);Date;Heure;Langue;Contexte (localisation, compte);Répétition (1/2);Présence;Position;Exactitude;Faits erronés;Sources citées;Sources réelles ?;Concurrents cités;Action;Fichier réponse
```

| ID | Plateforme | Modèle | Mode | Date | Lang. | Contexte | Rép. | Présence | Position | Exactitude | Faits erronés | Sources citées | Sources réelles ? | Concurrents | Action | Fichier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | | | | | fr | | 1 | | | | | | | | | |
| A1 | | | | | fr | | 2 | | | | | | | | | |
| A2 | | | | | fr | | 1 | | | | | | | | | |
| A2 | | | | | fr | | 2 | | | | | | | | | |
| A3 | | | | | fr | | 1 | | | | | | | | | |
| A3 | | | | | fr | | 2 | | | | | | | | | |
| A4 | | | | | fr | | 1 | | | | | | | | | |
| A4 | | | | | fr | | 2 | | | | | | | | | |
| A5 | | | | | fr | | 1 | | | | | | | | | |
| A5 | | | | | fr | | 2 | | | | | | | | | |
| A6 | | | | | en | | 1 | | | | | | | | | |
| A6 | | | | | en | | 2 | | | | | | | | | |
| A7 | | | | | fr | | 1 | | | | | | | | | |
| A7 | | | | | fr | | 2 | | | | | | | | | |
| B1 | | | | | fr | | 1 | | | | | | | | | |
| B1 | | | | | fr | | 2 | | | | | | | | | |
| B2 | | | | | fr | | 1 | | | | | | | | | |
| B2 | | | | | fr | | 2 | | | | | | | | | |
| B3 | | | | | fr | | 1 | | | | | | | | | |
| B3 | | | | | fr | | 2 | | | | | | | | | |
| B4 | | | | | fr | | 1 | | | | | | | | | |
| B4 | | | | | fr | | 2 | | | | | | | | | |
| B5 | | | | | fr | | 1 | | | | | | | | | |
| B5 | | | | | fr | | 2 | | | | | | | | | |
| B6 | | | | | en | | 1 | | | | | | | | | |
| B6 | | | | | en | | 2 | | | | | | | | | |
| C1 | | | | | fr | | 1 | | | | | | | | | |
| C1 | | | | | fr | | 2 | | | | | | | | | |
| C2 | | | | | fr | | 1 | | | | | | | | | |
| C2 | | | | | fr | | 2 | | | | | | | | | |
| C3 | | | | | fr | | 1 | | | | | | | | | |
| C3 | | | | | fr | | 2 | | | | | | | | | |
| C4 | | | | | fr | | 1 | | | | | | | | | |
| C4 | | | | | fr | | 2 | | | | | | | | | |
| D1 | | | | | fr | | 1 | | | | | | | | | |
| D1 | | | | | fr | | 2 | | | | | | | | | |
| D2 | | | | | fr | | 1 | | | | | | | | | |
| D2 | | | | | fr | | 2 | | | | | | | | | |
| D3 | | | | | fr | | 1 | | | | | | | | | |
| D3 | | | | | fr | | 2 | | | | | | | | | |
| D4 | | | | | fr | | 1 | | | | | | | | | |
| D4 | | | | | fr | | 2 | | | | | | | | | |
| E1 | | | | | fr | | 1 | | | | | | | | | |
| E1 | | | | | fr | | 2 | | | | | | | | | |
| E2 | | | | | fr | | 1 | | | | | | | | | |
| E2 | | | | | fr | | 2 | | | | | | | | | |
| E3 | | | | | fr | | 1 | | | | | | | | | |
| E3 | | | | | fr | | 2 | | | | | | | | | |
| E4 | | | | | fr | | 1 | | | | | | | | | |
| E4 | | | | | fr | | 2 | | | | | | | | | |
| E5 | | | | | fr | | 1 | | | | | | | | | |
| E5 | | | | | fr | | 2 | | | | | | | | | |
| E6 | | | | | fr | | 1 | | | | | | | | | |
| E6 | | | | | fr | | 2 | | | | | | | | | |
| E7 | | | | | fr | | 1 | | | | | | | | | |
| E7 | | | | | fr | | 2 | | | | | | | | | |
| E8 | | | | | fr | | 1 | | | | | | | | | |
| E8 | | | | | fr | | 2 | | | | | | | | | |
| E9 | | | | | en | | 1 | | | | | | | | | |
| E9 | | | | | en | | 2 | | | | | | | | | |
| F1 | | | | | fr | | 1 | | | | | | | | | |
| F1 | | | | | fr | | 2 | | | | | | | | | |
| F2 | | | | | fr | | 1 | | | | | | | | | |
| F2 | | | | | fr | | 2 | | | | | | | | | |
| F3 | | | | | fr | | 1 | | | | | | | | | |
| F3 | | | | | fr | | 2 | | | | | | | | | |
| F4 | | | | | fr | | 1 | | | | | | | | | |
| F4 | | | | | fr | | 2 | | | | | | | | | |

Le tableau ci-dessus est à dupliquer **par plateforme** (ChatGPT, Claude, Gemini, Perplexity, Google AI si disponible). Soit, pour un run complet : 34 prompts × 2 répétitions × 4 à 5 plateformes = 272 à 340 lignes. Si le temps manque, exécuter en priorité le sous-ensemble **E1, E2, E3, E4, E6, A1, A2, B1, C3, D1** sur ChatGPT (web on) et Perplexity : 10 prompts × 2 × 2 = 40 lignes.

## 7. Points de vigilance pendant l'analyse

Erreurs que l'on s'attend à rencontrer, d'après les sources tierces trouvées (détail dans `CITATION_SOURCES.md`) :

- adresse « 105 bis rue de Tolbiac » (ancienne, relayée par Gowork) au lieu de 93 avenue d'Italie ;
- tarif « 250 €/mois » ou « 1 500 € » ou « 1 620 € » (fiches Emagister 2017-2018) au lieu de « dès 370 €/mois, 9 mensualités » ;
- « 3 jours d'essai gratuits » (Emagister) au lieu de « 2 cours d'essai gratuits » ;
- année de création « 2009 » (L'Etudiant) au lieu de « 1999 » (site) ;
- cours de « chant », « danse », « comédie musicale » (L'Etudiant, Emagister) qui n'apparaissent plus sur le site ;
- cours « ados & enfants 100 €/mois » (Spectable) non documenté sur le site principal ;
- téléphone « 06 07 07 41 25 » (evous, d'après l'extrait de recherche) au lieu de 06 07 41 41 25 ;
- confusion avec « The Actors Studio » (New York), le « Lee Strasberg Theatre & Film Institute », « Acting International », le « Bilingual Acting Workshop » (Paris, cité par London Met pour une masterclass de method acting), ou une « Actors Studio Paris » générique ;
- affirmation que l'école est « affiliée » à l'Actors Studio : le site dit « descendant direct » de la Méthode Stanislavski « dont s'est inspiré l'Actors Studio », pas affiliée (à reformuler, voir audit).

Toute erreur constatée est reportée dans `CITATION_SOURCES.md` (si une source tierce en est l'origine) ou dans `GEO_ACTION_PLAN.md` (si le site lui-même est ambigu).

## 8. Ce que ce benchmark ne mesure pas

- L'impact commercial d'une citation (à croiser avec le champ « Comment avez-vous connu Method Acting Center ? → Recherche IA (ChatGPT, etc.) » déjà présent dans les formulaires du site, et avec les conversions Web3Forms).
- Les réponses des assistants intégrés à des applications tierces (WhatsApp, Instagram, etc.).
- Les variations par pays : le test est fait depuis la France, en français.
