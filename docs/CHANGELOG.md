# Changelog — SEO & GEO

## Format d'entrée

### YYYY-MM-DD — [ID du changement]

- Catégorie :
- Problème initial :
- URL ou fichier concerné :
- Modification :
- Justification :
- Source ou preuve :
- Auteur / agent :
- Validation humaine :
- Tests effectués :
- Résultats :
- Risques :
- Procédure de retour arrière :
- Date de suivi :
- Résultats observés après suivi :

## Historique

### 2026-10-12 — [SETUP-001]

- Catégorie : organisation
- Problème initial : absence de cadre de travail pour les agents SEO / GEO.
- URL ou fichier concerné : `CLAUDE.md`, `.claude/agents/*.md`, `docs/`
- Modification : installation du système d'agents et des documents de
  pilotage ; pré-remplissage de `docs/FACTS_REGISTER.md` avec les faits
  déjà vérifiés.
- Justification : spécification fournie par le propriétaire.
- Source ou preuve : message du propriétaire du 2026-10-12.
- Auteur / agent : chef de projet (session Claude Code).
- Validation humaine : à faire par le propriétaire.
- Tests effectués : aucun (documentation uniquement, aucune page modifiée).
- Résultats : structure en place.
- Risques : aucun sur le site.
- Procédure de retour arrière : supprimer les fichiers créés.
- Date de suivi : —
- Résultats observés après suivi : —

### 2026-10-12 → 2026-10-17 — [AUDIT-001]

- Catégorie : audit (lecture seule)
- Problème initial : aucun état des lieux SEO / GEO / contenu / technique / mesure.
- URL ou fichier concerné : `docs/audits/`, `docs/geo/`, `docs/content/`, `docs/technical/`,
  `docs/pr/`, `docs/analytics/`.
- Modification : six audits parallèles (seo-auditor, geo-ai-visibility, content-strategist,
  technical-seo, digital-pr, analytics-qa), consolidés dans `docs/audits/PRIORITIZED_BACKLOG.md` ;
  registre de vérité complété (FACT-008 à FACT-018, contradictions X-1 à X-7).
- Justification : phase A de CLAUDE.md § 10.
- Source ou preuve : chaque rapport cite fichier:ligne ou URL datée.
- Auteur / agent : chef de projet et six agents.
- Validation humaine : décisions B1 à B19 du backlog en attente.
- Tests effectués : build de contrôle identique au `dist/` commité ; crawl local des 14 pages ;
  Playwright mobile 390 px ; JSON-LD valide sur 11 pages.
- Résultats : 17 correctifs techniques, 19 décisions, 9 contenus, 5 actions externes, 5 actions de mesure.
- Risques : aucun (aucune page modifiée par l'audit).
- Procédure de retour arrière : sans objet.
- Date de suivi : à la validation du propriétaire.
- Résultats observés après suivi : —

Limite : le site en production n'était pas joignable depuis l'environnement ; les codes HTTP,
l'indexation réelle et les performances terrain restent à confirmer (commandes dans
`docs/analytics/QA_CHECKLIST.md`). L'agent seo-auditor s'est interrompu sur une limite de session
après avoir écrit ses quatre livrables ; ils sont complets.

### 2026-10-17 — [FORMS-001]

- Catégorie : conversion / qualité des leads
- Problème initial : un formulaire pouvait être envoyé sans nom, prénom, email ni téléphone. La
  landing `/stages/` désactivait la validation (`novalidate="false"`, attribut présent donc actif) ;
  sur les autres formulaires, des espaces suffisaient à passer le contrôle natif `required`.
- URL ou fichier concerné : `newsite/assets/site.js`, `newsite/assets/style.css`,
  `newsite/pages/{contact,cours-essai,inscription,jpo,stages}.html`, `newsite/static/jpo/index.html`,
  `newsite/static/jposr/index.html`, `newsite/tools/build_landing_stages.py` ; `newsite/dist/` régénéré.
- Modification : fonction `checkIdentity()` commune : prénom et nom non vides, au moins un email valide
  ou un téléphone valide (9 chiffres minimum), message d'erreur sous les champs, champs en rouge,
  focus sur le premier champ fautif ; email et téléphone ne sont plus exigés individuellement
  (mention « (ou téléphone) / (ou email) » sur les étiquettes) ; `novalidate` sur les 8 formulaires
  pour une expérience identique partout.
- Justification : demande explicite du propriétaire le 2026-10-17.
- Source ou preuve : reproduction du défaut avec Playwright avant correction.
- Auteur / agent : chef de projet.
- Validation humaine : demande du propriétaire ; déploiement de `dist/` par ses soins.
- Tests effectués : 56 scénarios Playwright (7 cas × 8 formulaires) : vide, espaces, nom + téléphone,
  nom + email, email invalide, téléphone invalide, sans nom ; aucune erreur JavaScript ; build sans
  assertion.
- Résultats : 56 / 56 conformes.
- Risques : faible ; un visiteur sans email ni téléphone ne peut plus envoyer (comportement voulu).
- Procédure de retour arrière : `git revert` des commits « Formulaires : … » puis rebuild.
- Date de suivi : 28 jours après déploiement (volume de demandes Web3Forms par type).
- Résultats observés après suivi : —

### 2026-10-17 — [JPO-001]

- Catégorie : contenu / conversion
- Problème initial : la page `/jpo.html` annonçait « les horaires détaillés arrivent » et proposait
  Screenwriting in English, qui n'est plus au programme ; la photo du hero ne convenait pas.
- URL ou fichier concerné : `newsite/pages/jpo.html`, `newsite/assets/site.js` (liste des ateliers du
  formulaire), `newsite/build.py` (image Open Graph de la page), nouvelle image
  `newsite/assets/img/etreinte-emotion-scene-a-deux-method-acting-center.jpg`.
- Modification : planning horaire du samedi et du dimanche ; bloc « Avant le week-end : intégrez un cours
  de la semaine » (Acting Amateur mer. 9 déc., Improvisation ven. 11 déc.) ; mention correspondante sur
  les cartes Improvisation et Acting Amateur ; retrait de Screenwriting in English ; formulaire avec les
  créneaux exacts ; photo du hero et image de partage remplacées par la photo fournie.
- Justification : planning transmis par le propriétaire.
- Source ou preuve : message du propriétaire du 2026-10-17 (FACTS_REGISTER, JPO décembre · horaires).
- Auteur / agent : chef de projet.
- Validation humaine : demande du propriétaire.
- Tests effectués : build sans assertion ; Playwright desktop et mobile (aucun débordement, aucune erreur
  JS) ; envoi simulé du formulaire : les créneaux choisis arrivent dans l'email.
- Résultats : conformes.
- Risques : les landings `/jpo/` et `/jposr/` ont leur propre liste d'ateliers, non modifiée.
- Procédure de retour arrière : `git revert` du commit, rebuild.
- Date de suivi : après les JPO (nombre de réservations par atelier).
- Résultats observés après suivi : —

### 2026-10-17 — [JPO-002]

- Catégorie : conversion
- Modification : sur les landings `/jpo/` et `/jposr/`, premier bouton du haut de page « Réserver les
  Portes Ouvertes » (rouge) vers `https://www.methodacting.fr/jpo.html#inscription` ; le bouton cours
  d'essai passe en noir pour garder un seul bouton rouge ; « Tester en stage » inchangé.
- Fichiers : `newsite/static/jpo/index.html`, `newsite/static/jposr/index.html` ; `dist/` régénéré.
  La landing `/stages/` n'est pas concernée (son haut de page est réécrit par le générateur).
- Justification : demande du propriétaire du 2026-10-17.
- Tests : build sans assertion ; Playwright desktop et mobile sur les deux landings (bouton en premier,
  lien correct, aucun débordement, aucune erreur JS).
- Retour arrière : `git revert` du commit, rebuild.

### 2026-10-26 — [DATES-001]

- Catégorie : contenu / conversion
- Problème initial : le stage A des 17 & 18 octobre 2026, passé, restait mis en avant sur la page Stages,
  la page Tarifs, les landings `/jpo/` et `/stages/`, dans `llms.txt` et dans les données structurées ;
  les landings JPO affichaient encore « horaires communiqués prochainement » et Screenwriting in English ;
  l'accueil et la page Cours d'essai disaient « Vous avez raté les Portes Ouvertes ? ».
- Modification : mise en avant des stages des 7 & 8 novembre (Scénario) et 14 & 15 novembre (Stage B) ;
  stage A présenté en « prochaine session à venir », réservable pour être prévenu ; planning horaire de
  décembre et cours de la semaine sur `/jpo/` ; atelier du samedi 12 décembre 18h–20h sur `/jposr/` ;
  Screenwriting in English retiré des landings ; mention des Portes Ouvertes des 12 & 13 décembre sur
  l'accueil et la page Cours d'essai ; bouton « Réserver » masqué sur les événements passés du planning ;
  `build.py` retire automatiquement des données structurées les événements terminés ; le préremplissage
  `?stage=` de la landing `/stages/` ne dépend plus de l'ordre des cartes.
- Fichiers : `newsite/pages/{stages,tarifs,index,cours-essai}.html`, `newsite/assets/style.css`,
  `newsite/static/{llms.txt,jpo/index.html,jposr/index.html}`, `newsite/tools/build_landing_stages.py`,
  `newsite/build.py` ; `dist/` régénéré.
- Justification : demande du propriétaire du 2026-10-26 ; dates issues du registre de vérité.
- Tests : build sans assertion ; plus aucune mention du 17-18 octobre hors tableau annuel brut du planning ;
  Playwright : captures desktop, aucun débordement ni erreur JS, réservations simulées sur `/stages.html`,
  `/stages/`, `/jpo/` et `/jposr/` avec les bons créneaux, préremplissage `?stage=` vérifié.
- Retour arrière : `git revert` du commit, rebuild.
- Suivi : après le 15 novembre, le prochain rendez-vous à mettre en avant sera l'intensif d'hiver
  (9 & 10 janvier) et les Portes Ouvertes (12 & 13 décembre).

### 2026-10-31 — [PLANNING-001]

- Catégorie : contenu / exactitude
- Source : planning officiel 2026-2027 V3 (PDF transmis par le propriétaire le 2026-10-31).
- Écarts trouvés avec le planning publié jusque-là : cours du matin 9h30–13h30 devenus 10h–14h ;
  Acting in English passé du mercredi 15h30–18h30 au vendredi 15h–18h ; Improvisation passée du jeudi
  15h30–18h30 au vendredi 10h–13h ; Scènes 4 (mardi 15h30–18h30) retiré ; intervenants des cours du soir
  désormais nommés dans le PDF.
- Modification : `static/uploads/planning-hebdomadaire.pdf` remplacé par le nouveau PDF (même nom, les liens
  ne changent pas) ; page Cours d'essai : Acting in English le vendredi 15h–18h (carte et formulaire) ;
  page Planning et page Inscription : 4e année = 1 atelier de 3 h, le lundi 15h30–18h30 ; `llms.txt` :
  section « Planning hebdomadaire 2026-2027 » ; registre de vérité complété et contradiction X-2 tranchée.
- Non modifié : descriptions pédagogiques qui citent Scènes 4 (page Acting, programme de la landing `/jpo/`),
  en attente de confirmation du propriétaire ; noms des coachs (décision B7 du backlog).
- Tests : build sans assertion ; pages Cours d'essai, Inscription et Planning chargées en mobile sans
  erreur ni débordement ; PDF servi correctement.
- Retour arrière : `git revert` du commit, rebuild.

### 2026-11-09 — [STAGES-LP-002]

- Catégorie : landing Google Ads `/stages/`
- Source : brief « Mise à jour landing page stages » du propriétaire, textes intégrés sans reformulation.
- Fichier : `newsite/tools/build_landing_stages.py` (seul fichier modifié) ; `dist/stages/index.html` régénéré.
  Aucune autre page du site n'est modifiée.
- Modifications : encart « Stage à la une » dans le hero (données `HERO_EVENT`) ; rubrique Stages fusionnée
  (sur-titre « Nos stages · Paris 13ᵉ et en ligne ») ; grande carte Scénario avec encadré participation en
  ligne et photo réduite ; accordéons Actors Studio B et Acting Caméra (nouvelle UX) ; carte et option
  Actors Studio A supprimées ; intensifs en cartes sombres ; « Pourquoi » en grille 2 × 2 avec nouveaux
  textes ; bandeau animé déplacé sous « Pourquoi », sans séparateurs ; formulaire dans l'ordre demandé avec
  choix obligatoire présentiel / à distance pour le stage d'écriture, transmis dans l'email et le récapitulatif ;
  liens du footer gris clair, rouges au survol, focus visible.
- Corrections techniques sur la même page : une seule balise canonical et un seul jeu Open Graph (le second
  pointait vers `/jpo/`) ; titre « Ils ont tenté l'expérience » sans barre oblique parasite ; liens du footer
  qui s'affichaient tous en rouge ; zones tactiles des points de carrousel agrandies ; accordéons sans saut de
  page à l'ouverture.
- Point d'attention : le stage d'écriture des 7 & 8 novembre 2026 est passé à la date de la livraison
  (2026-11-09). L'encart du hero, la grande carte et l'option du formulaire sont donc masqués automatiquement
  en ligne. Les tests ont été faits avec une date simulée au 4 novembre.
- Tests (Playwright) : desktop 1280 et mobile 390 sans débordement ni erreur JS ; 7 ancres vérifiées sous le
  header fixe ; 4 accordéons ouverts et fermés sans décalage ; réservation simple, multiple, stage d'écriture
  sans format (refusée), en présentiel et à distance ; préremplissage cumulatif par les CTA ; conversion
  `stage_form_success` uniquement après envoi réussi ; couleurs du footer au repos et au survol.
- Retour arrière : `git revert` du commit, rebuild.

### 2026-11-09 — [STAGES-B-001]

- Catégorie : contenu / conversion
- Demande du propriétaire : le stage Scénario des 7 & 8 novembre étant passé, mettre le stage B au premier plan.
- Landing `/stages/` (`tools/build_landing_stages.py`) : encart du hero et grande carte « Stage à la une »
  consacrés à Actors Studio B (textes du brief du propriétaire) ; carte à la une rendue générique
  (variable `FEATURED`, textes dans `SESSIONS`) ; les stages week-end passés sont retirés au build ;
  sur-titre « Nos stages · Paris 13ᵉ » sans « et en ligne » tant qu'aucun stage en ligne n'est à venir.
  Les textes du stage d'écriture restent dans `SESSIONS["sc"]`, prêts pour une prochaine session.
- Page Stages du site : « Prochain stage · 14 & 15 novembre » ; bloc Prochainement = stage B puis
  intensif d'hiver ; stage B en première offre ; stage Scénario en « prochaine session à venir »
  (bouton « Me prévenir des dates ») ; formulaire mis à jour. Page Tarifs : « Prochain stage les 14 & 15 novembre ».
- Tests : à la date du 2026-11-09, desktop et mobile sans débordement ni erreur JS ; encart et carte
  visibles ; boutons qui cochent le stage B et l'intensif d'hiver ; envois simulés corrects.
- Non modifié : landing `/jposr/` (carte « Prochain stage : 7 & 8 novembre ») et `llms.txt`.
- Retour arrière : `git revert` du commit, rebuild.

Les entrées doivent être ajoutées au fur et à mesure.
Ne pas réécrire l'historique pour donner une impression de succès.
