# Project Brief — Method Acting Center

## Identité du projet

Nom utilisé : Method Acting Center
Site à examiner : https://www.methodacting.fr/
Marché initial : Paris et Île-de-France
Langue principale : français
Objectif : améliorer la découvrabilité organique et la visibilité
dans les réponses des assistants IA.

Les informations ci-dessus constituent le périmètre initial.
Elles ne remplacent pas la vérification des informations officielles.

## Contexte du dépôt

- Site statique, sans CMS : sources dans `newsite/` (pages, partials,
  assets), construction par `cd newsite && python3 build.py`, sortie
  dans `newsite/dist/` (arborescence exacte déposée sur le serveur OVH).
- Déploiement manuel par le propriétaire (FileZilla). Aucun agent ne
  déploie.
- `newsite/prod-snapshot/` : copie figée de la production avant la mise
  en conformité (référence, non utilisée par le build).
- Landings Google Ads non reliées au menu : `/jpo/`, `/jposr/`,
  `/stages/`. Elles ne doivent pas être ajoutées à la navigation.
- Formulaires : Web3Forms (pas de backend). Suivi des conversions :
  `dataLayer` / `gtag` sur la landing `/stages/` uniquement.

## Objectifs métier

Aider les personnes intéressées par :
- le jeu d'acteur au cinéma ;
- la méthode Stanislavski ;
- les approches de Method Acting ;
- le jeu face caméra ;
- les formations d'acting ;
- l'écriture de scénario ;
- la réalisation ;
- la direction d'acteurs ;
- les stages et ateliers.

Faciliter une décision éclairée grâce à des informations exactes
sur les programmes, les tarifs, les professeurs et les modalités
d'admission.

## Publics à étudier

Ne pas considérer ces segments comme confirmés avant recherche :
- débutants souhaitant apprendre à jouer ;
- acteurs souhaitant se perfectionner ;
- personnes préparant une reconversion ;
- auteurs et réalisateurs ;
- personnes recherchant une formation courte ;
- personnes ayant un budget limité.

Pour chaque segment, déterminer les besoins et les intentions
à partir des données et des sources disponibles.

## Positionnement

Ne pas inventer un positionnement commercial.

Examiner si l'école peut légitimement se différencier par :
- sa pédagogie ;
- ses méthodes de travail ;
- la pratique devant caméra ;
- ses ateliers ;
- la combinaison éventuelle de plusieurs disciplines ;
- son accessibilité financière ;
- ses enseignants et leurs expériences ;
- les projets effectivement réalisés.

Toute différenciation retenue doit être documentée.

## Périmètre

Inclus :
- audit SEO et GEO ;
- recherche de requêtes ;
- architecture éditoriale ;
- rédaction de brouillons ;
- amélioration technique ;
- données structurées ;
- présence éditoriale externe ;
- mesure et QA.

Exclus sans autorisation :
- refonte complète ;
- migration de CMS ;
- modification DNS ;
- achat média ;
- dépenses ;
- envoi de communications externes ;
- publication en production ;
- modification de prix ou d'offres.

## Contraintes

- Préserver le site existant et sa charte graphique.
- Ne pas casser les URLs performantes.
- Ne pas inventer de preuves.
- Ne pas publier de faux avis.
- Respecter les droits d'auteur et la vie privée.
- Préserver les données personnelles.
- Respecter les conditions d'utilisation des plateformes.
- Garder une possibilité de retour arrière.
- Ne pas modifier `newsite/dist/` à la main : toute modification passe
  par les sources puis par `build.py`.

## Critères de réussite

Le projet est réussi si :
1. Les problèmes prioritaires sont documentés et corrigés.
2. Les pages importantes présentent des informations exactes.
3. Les informations officielles sont cohérentes entre les pages.
4. Les performances SEO sont mesurées.
5. La visibilité IA est évaluée avec un protocole reproductible.
6. Les conversions sont suivies lorsqu'un système de mesure existe.
7. Les changements sont testés, documentés et réversibles.

Ne pas déclarer le projet réussi sur la seule base du nombre d'articles.
