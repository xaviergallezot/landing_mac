# Implementation Plan

## Phase 0 — Préparation

- [ ] Vérifier le dépôt et le site cible.
- [ ] Lire CLAUDE.md et les fichiers docs/.
- [ ] Identifier le CMS, le framework et les environnements.
- [ ] Identifier les accès réellement disponibles.
- [ ] Vérifier la présence d'une branche de travail.
- [ ] Confirmer le périmètre des autorisations.
- [ ] Créer un état initial.
- [ ] Vérifier les modifications déjà présentes dans le dépôt.

Livrable : docs/audits/INITIAL_STATE.md

Rappel : site statique construit par `cd newsite && python3 build.py`,
sortie `newsite/dist/`, déploiement manuel par le propriétaire.

## Phase 1 — Audits parallèles

- [ ] SEO audit.
- [ ] GEO et benchmark IA.
- [ ] Audit des contenus.
- [ ] Audit technique.
- [ ] Recherche d'opportunités éditoriales.
- [ ] Inventaire des outils de mesure.

Tous les audits sont en lecture seule.

Livrable : rapports consolidés et registre des risques.

## Phase 2 — Priorisation

Pour chaque action, enregistrer :
- problème ;
- preuve ;
- URL concernée ;
- impact estimé ;
- confiance ;
- effort ;
- risque ;
- dépendances ;
- responsable ;
- critère d'acceptation.

Priorité :
P0 : risque critique, problème de sécurité ou site inaccessible.
P1 : blocage d'indexation ou défaut majeur affectant une page clé.
P2 : amélioration importante de contenu, architecture ou conversion.
P3 : amélioration secondaire.
P4 : expérimentation facultative.

Ne pas attribuer P0 à un problème SEO mineur.

Livrable : docs/audits/PRIORITIZED_BACKLOG.md

## Phase 3 — Contenus et preuves

- [ ] Compléter le registre de vérité.
- [ ] Identifier les informations manquantes.
- [ ] Valider les programmes et les tarifs.
- [ ] Préparer les briefs.
- [ ] Rédiger les brouillons.
- [ ] Vérifier les sources.
- [ ] Faire relire les affirmations pédagogiques.
- [ ] Obtenir les validations commerciales.

Aucune publication automatique.

## Phase 4 — Corrections techniques

- [ ] Résoudre les défauts prioritaires approuvés.
- [ ] Corriger les métadonnées.
- [ ] Améliorer le maillage interne.
- [ ] Vérifier les canonicals.
- [ ] Corriger les erreurs de sitemap.
- [ ] Valider les données structurées.
- [ ] Préserver les URLs performantes.
- [ ] Vérifier le rendu mobile.
- [ ] Exécuter les tests et le build.

Ne modifier que ce qui est justifié par l'audit.
Modifier les sources (`newsite/pages`, `newsite/partials`,
`newsite/assets`, `newsite/static`, `newsite/build.py`), jamais
`newsite/dist/` directement.

## Phase 5 — Présence externe

- [ ] Valider les angles éditoriaux.
- [ ] Identifier les médias et partenaires.
- [ ] Préparer les propositions de collaboration.
- [ ] Vérifier les coûts et les conditions.
- [ ] Faire approuver les contacts et publications.
- [ ] Documenter les résultats.

Tout contact externe exige une autorisation.

## Phase 6 — Validation

- [ ] Revue humaine des contenus.
- [ ] Revue du diff technique.
- [ ] Tests automatisés disponibles.
- [ ] Contrôle des liens.
- [ ] Contrôle des données structurées.
- [ ] Vérification des faits et des prix.
- [ ] Vérification des risques de régression.
- [ ] Préparation du retour arrière.
- [ ] Autorisation explicite de déploiement.

## Phase 7 — Mesure

- [ ] Enregistrer les KPI initiaux.
- [ ] Vérifier les données de Search Console.
- [ ] Vérifier les conversions disponibles.
- [ ] Répéter le benchmark IA.
- [ ] Comparer les périodes équivalentes.
- [ ] Documenter les modifications intervenues.
- [ ] Évaluer les effets et les limites de l'analyse.
- [ ] Réviser le backlog.

Ne pas attribuer automatiquement une variation à une seule action.

## Rapport de clôture

Le rapport doit indiquer :
- actions réalisées ;
- actions non réalisées ;
- raisons des blocages ;
- fichiers modifiés ;
- tests effectués ;
- résultats observés ;
- validations encore nécessaires ;
- risques résiduels ;
- prochaines actions.
