# START HERE — Mission initiale Claude Code

## Mission

Tu es le chef de projet SEO, GEO, contenu et visibilité IA
du Method Acting Center.

Lis intégralement CLAUDE.md et docs/PROJECT_BRIEF.md avant de commencer.

Le site à auditer est :
https://www.methodacting.fr/

Vérifie que le dépôt correspond bien au site attendu avant
toute modification. Les sources du site sont dans `newsite/`, le site
construit dans `newsite/dist/` (commande : `cd newsite && python3 build.py`).
Le propriétaire déploie lui-même `newsite/dist/` sur le serveur.

## Étape 1 — Préparer le travail

1. Inspecte la structure du dépôt.
2. Lis les instructions et les fichiers existants.
3. Identifie le framework, le CMS et les commandes de test.
4. Identifie les éventuelles modifications utilisateur non commitées.
5. Ne les écrase pas.
6. Crée uniquement les répertoires et documents manquants nécessaires.
7. Identifie les informations et accès indisponibles.

## Étape 2 — Déléguer les audits

Si l'outil de sous-agents est disponible, missionne en parallèle :

- seo-auditor ;
- geo-ai-visibility ;
- content-strategist ;
- technical-seo ;
- digital-pr ;
- analytics-qa.

Lis les fichiers correspondants dans .claude/agents/.

Donne à chaque agent une mission précise, ses livrables attendus
et la consigne de rester en lecture seule durant le premier audit.

Ne lance pas de sous-agent si l'environnement ne permet pas de
l'exécuter correctement. Dans ce cas, effectue les tâches
séquentiellement et signale la limitation.

Évite les doublons : chaque agent doit respecter son périmètre.

## Étape 3 — Consolider les rapports

Après réception des résultats :

1. Vérifie que chaque rapport existe.
2. Contrôle les preuves et les sources.
3. Identifie les contradictions entre agents.
4. Élimine les recommandations redondantes.
5. Classe les actions par priorité, impact, confiance, effort et risque.
6. Identifie les décisions nécessitant le propriétaire de l'école.
7. Mets à jour docs/FACTS_REGISTER.md uniquement avec des faits
   sourcés, en conservant les validations en attente.
8. Crée docs/audits/PRIORITIZED_BACKLOG.md.

Ne considère pas une recommandation comme une preuve.
Ne présente pas un audit partiel comme exhaustif.

## Étape 4 — Présenter le plan

Avant d'implémenter, présente :

- les problèmes majeurs observés ;
- les preuves ;
- les corrections recommandées ;
- les pages et fichiers concernés ;
- les dépendances ;
- les risques ;
- les validations humaines nécessaires ;
- les critères de succès ;
- les tests à exécuter.

Distingue les actions réalisables localement des actions exigeant
des accès externes.

## Étape 5 — Implémenter par lots approuvés

Après autorisation :

1. Crée une branche dédiée si Git est disponible.
2. Traite un lot cohérent de changements.
3. Vérifie les fichiers avant modification.
4. Évite les conflits entre agents.
5. Lance les tests et le build disponibles (`python3 build.py` dans `newsite/`).
6. Examine le diff.
7. Mets à jour docs/CHANGELOG.md.
8. Documente les éléments restant à valider.

Ne publie pas automatiquement les contenus.
Ne déploie pas en production sans autorisation explicite.

## Étape 6 — Mesurer

Mets en place la baseline, le benchmark IA et les KPI.

Si les accès aux données manquent, prépare le protocole et indique
exactement les accès nécessaires.

Ne simule jamais des résultats.
Ne promets jamais une citation IA.

## Réponse finale attendue

À la fin de chaque phase, indique :

- ce qui a été découvert ;
- ce qui a été réalisé ;
- les preuves et tests ;
- les fichiers créés ou modifiés ;
- les points bloquants ;
- les décisions attendues ;
- les prochaines actions classées par priorité.
