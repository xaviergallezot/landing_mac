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

Les entrées doivent être ajoutées au fur et à mesure.
Ne pas réécrire l'historique pour donner une impression de succès.
