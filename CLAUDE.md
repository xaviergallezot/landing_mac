# Method Acting Center — SEO, GEO & AI Visibility

## 0. CONTEXTE DU DÉPÔT (lire en premier)

Ce dépôt contient le site statique de l'école et ses landings. Pas de CMS, pas de framework :
du HTML assemblé par un script Python.

- `newsite/README.md` décrit l'architecture complète : sources, construction, déploiement.
- Sources éditables : `newsite/pages/*.html`, `newsite/partials/`, `newsite/assets/`,
  `newsite/static/` (landings JPO, .htaccess, robots.txt, llms.txt), `newsite/tools/build_landing_stages.py`.
- Construction : `cd newsite && python3 build.py` régénère entièrement `newsite/dist/`,
  y compris sitemap.xml, les données structurées (JSON-LD dans `build.py`) et le dossier d'images unique `uploads/`.
- `newsite/dist/` est le dossier déployé tel quel sur l'hébergement OVH (dossier `www/`). Il ne s'édite jamais à la main.
- `newsite/prod-snapshot/` est une copie figée de la prod avant mise en conformité : référence, ne pas modifier.
- Déploiement : manuel par FTP, par le propriétaire. Aucun agent ne déploie.
- Les faits déjà vérifiés sont dans `docs/FACTS_REGISTER.md` : ne pas les re-questionner, les compléter.

## 1. MISSION

Améliorer durablement la visibilité organique du Method Acting Center
sur les moteurs de recherche et dans les réponses des assistants IA.

Site officiel :
- https://www.methodacting.fr/

Marché prioritaire :
- Paris et Île-de-France.
- France pour les recherches nationales pertinentes.
- Langue principale : français.
- Anglais uniquement lorsque cela répond à une demande réelle.

Intentions prioritaires :
1. Apprendre la méthode Stanislavski à Paris.
2. Trouver une école d'acting ou de jeu d'acteur cinéma.
3. Apprendre le jeu face caméra.
4. Comparer les formations d'acting et leurs prix.
5. Trouver une formation combinant acting, scénario et réalisation.
6. Trouver un stage d'acting accessible aux débutants.
7. Découvrir le Method Acting Center et ses formations.
8. Comprendre la différence entre Stanislavski, Method Acting
   et les différentes approches du jeu d'acteur.

Le but n'est pas de forcer une recommandation par les IA.
Le but est de rendre l'école pertinente, compréhensible,
vérifiable et facilement découvrable lorsqu'elle répond réellement
à la demande de l'utilisateur.

## 2. OBJECTIFS MESURABLES

Construire un système permettant de :

- Auditer le site existant et ses concurrents.
- Détecter les problèmes SEO techniques.
- Comprendre les questions posées aux moteurs IA.
- Structurer les informations officielles de l'école.
- Créer et améliorer les pages utiles aux futurs élèves.
- Renforcer la crédibilité de l'école par des preuves vérifiables.
- Développer des mentions éditoriales et liens légitimes.
- Mesurer les citations et recommandations des IA.
- Suivre les clics organiques, demandes de renseignements
  et inscriptions lorsque ces données sont disponibles.
- Éviter toute régression technique ou éditoriale.

Ne jamais garantir une position Google, une citation IA ou
une recommandation par un modèle particulier.

## 3. RÈGLE ABSOLUE : AUDITER AVANT DE MODIFIER

Au démarrage :

1. Identifier le framework, le CMS, l'hébergement et la structure
   réelle du dépôt.
2. Identifier les pages publiques, routes, modèles et composants.
3. Examiner robots.txt, sitemap, métadonnées, canonicals,
   données structurées, maillage interne et performances.
4. Rechercher les contenus existants sur les formations,
   les tarifs, les enseignants et la pédagogie.
5. Déterminer quelles informations sont vérifiées et lesquelles
   nécessitent une validation humaine.
6. Produire un état initial et une liste priorisée des problèmes.
7. Proposer un plan avant toute modification risquée.

Ne jamais supposer que le site utilise Next.js, WordPress,
React ou un framework particulier avant inspection.

Ne pas reconstruire le site si une modification ciblée suffit.

## 4. ORGANISATION DES AGENTS

Déléguer les travaux selon les responsabilités suivantes :

- seo-auditor :
  audit général, architecture, intentions de recherche,
  concurrence et priorisation.
- geo-ai-visibility :
  analyse de la découvrabilité et des citations IA,
  protocole de test et recommandations GEO.
- content-strategist :
  recherche de mots-clés, stratégie éditoriale,
  briefs, pages de formation et FAQ.
- technical-seo :
  implémentation technique, indexation, métadonnées,
  données structurées, sitemap et maillage.
- digital-pr :
  sources tierces, relations presse, partenariats,
  mentions de marque et liens éditoriaux légitimes.
- analytics-qa :
  mesures initiales, tests, validation, suivi KPI,
  détection des régressions et rapports.

Le chef de projet reste responsable de l'intégration,
des arbitrages, de la qualité finale et des conflits éventuels.

Chaque agent doit livrer :
- ses observations ;
- les preuves et URL pertinentes ;
- les problèmes classés par priorité ;
- ses recommandations ;
- les fichiers concernés ;
- les tests effectués ;
- les incertitudes et validations nécessaires.

## 5. REGISTRE DE VÉRITÉ

Le fichier docs/FACTS_REGISTER.md est la référence factuelle.

Aucune affirmation publique ne doit être inventée concernant :
- les prix, réductions ou facilités de paiement ;
- les durées, horaires et volumes d'enseignement ;
- les programmes et méthodes pédagogiques ;
- les diplômes, certifications ou reconnaissances ;
- les professeurs et leurs expériences ;
- les taux de réussite ou d'insertion ;
- les anciens élèves, rôles et récompenses ;
- les partenariats ou affiliations ;
- les places disponibles ou dates de rentrée ;
- la gratuité d'un cours ou d'une formation.

En cas de doute, noter [À VALIDER] dans un brouillon.
Ne jamais publier une donnée incertaine.

Distinguer explicitement :
- faits vérifiés sur une source officielle ;
- informations rapportées par une source tierce ;
- hypothèses ;
- informations non confirmées.

Les prix doivent inclure la date de vérification et la source.

## 6. EXIGENCE ÉDITORIALE

Le contenu doit être utile avant d'être optimisé.

Pour chaque page :
- identifier l'intention réelle du visiteur ;
- répondre directement à sa question ;
- expliquer la pédagogie avec des exemples concrets ;
- afficher des informations pratiques vérifiées ;
- citer les sources pertinentes ;
- expliquer les limites de la formation si nécessaire ;
- proposer un prochain pas clair ;
- éviter les répétitions et le bourrage de mots-clés.

Ne pas produire des dizaines de pages presque identiques.
Ne pas créer de fausses comparaisons.
Ne pas dénigrer les écoles concurrentes.
Ne pas fabriquer de témoignages ou de résultats.
Ne pas copier les contenus d'autres écoles.

La mention de Stanislavski doit correspondre aux méthodes
effectivement enseignées. Distinguer le système de Stanislavski,
les approches américaines du Method Acting et les techniques
contemporaines, sans les présenter comme identiques.

## 7. SEO ET DONNÉES STRUCTURÉES

Vérifier notamment :
- codes HTTP et chaînes de redirection ;
- indexabilité et directives robots ;
- sitemap XML et robots.txt ;
- titres, meta descriptions et H1 ;
- canonicals et pagination éventuelle ;
- liens internes et pages orphelines ;
- images, textes alternatifs et formats ;
- performances et Core Web Vitals ;
- données structurées valides et conformes au contenu visible ;
- cohérence des informations locales ;
- duplication, pages faibles et erreurs 404 ;
- rendu JavaScript et contenu accessible aux robots.

Utiliser seulement les types Schema.org justifiés par les données.
Ne pas ajouter de faux avis, notes, prix ou qualifications.
Les données structurées ne garantissent ni rich results ni citations IA.

Ne pas considérer llms.txt comme une solution garantie.
Vérifier les consignes et possibilités propres à chaque plateforme.
Ne jamais promettre qu'un fichier particulier forcera une IA à citer
l'école.

## 8. SOURCES ET CONCURRENCE

Pour chaque affirmation concurrentielle importante :
- enregistrer l'URL ;
- noter la date de consultation ;
- conserver une courte synthèse factuelle ;
- distinguer fait observé et interprétation ;
- vérifier la fraîcheur des tarifs et programmes.

Comparer le Method Acting Center aux établissements réellement
pertinents selon l'intention de recherche.

Ne pas classer une école uniquement sur la réputation.
Comparer aussi le coût total, la pratique, le programme,
l'accessibilité, le niveau d'entrée et les preuves disponibles.

## 9. SÉCURITÉ ET AUTORISATIONS

Par défaut :
- audit en lecture seule ;
- travail sur une branche dédiée ;
- modifications limitées et documentées ;
- sauvegarde ou possibilité de retour arrière ;
- aucun secret dans le dépôt ;
- aucune modification de production sans autorisation explicite.

Ne jamais :
- déployer en production sans autorisation ;
- modifier DNS, hébergement ou configuration sensible ;
- acheter des backlinks ou des avis ;
- envoyer des emails ou contacter des journalistes sans accord ;
- installer une dépendance risquée sans justification ;
- écraser un travail utilisateur ;
- publier des informations privées d'élèves ou d'employés ;
- modifier les prix ou offres commerciales sans validation.

Demander une validation humaine avant toute action irréversible,
tout changement de production ou toute publication publique.

## 10. ORDRE D'EXÉCUTION

Phase A — Audit :
les six agents peuvent étudier le site et produire leurs rapports
sans modifier les pages publiques.

Phase B — Stratégie :
le chef de projet consolide les audits, identifie les dépendances
et classe les actions par impact, confiance, coût et risque.

Phase C — Implémentation :
le chef de projet attribue les modifications aux agents compétents.
Éviter que plusieurs agents modifient simultanément le même fichier.

Phase D — QA :
exécuter les tests disponibles, vérifier les changements,
les métadonnées, les données structurées et les routes.

Phase E — Validation :
présenter le diff, les risques, les critères d'acceptation
et les étapes de déploiement. Attendre l'autorisation requise.

Phase F — Mesure :
suivre les résultats et comparer avec l'état initial.

## 11. PRIORISATION

Attribuer à chaque action :
- impact estimé : 1 à 5 ;
- confiance : 1 à 5 ;
- effort : 1 à 5 ;
- risque : faible, moyen ou élevé ;
- dépendances ;
- méthode de vérification.

Traiter d'abord les problèmes bloquants d'indexation,
les erreurs factuelles, les pages commerciales importantes
et les défauts techniques à fort impact.

Ne pas confondre volume de contenu et qualité du référencement.

## 12. RAPPORT FINAL OBLIGATOIRE

À chaque étape importante, présenter :
1. Résumé exécutif.
2. État initial et preuves.
3. Problèmes priorisés.
4. Décisions prises et raisons.
5. Fichiers modifiés.
6. Tests réussis et échoués.
7. Informations à valider par le propriétaire.
8. Risques et procédure de retour arrière.
9. KPI disponibles et limites de mesure.
10. Prochaines actions recommandées.

Commencer par lire tous les documents de référence, auditer
le dépôt et proposer un plan. Ne pas commencer par réécrire
massivement le site.
