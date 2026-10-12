# KPI Dashboard — Method Acting Center

## Règles de mesure

Aucune valeur ne doit être inventée.
Chaque indicateur doit avoir une source, une période et une définition.

## SEO

| KPI | Baseline | Actuel | Période | Source |
|---|---|---|---|---|
| Clics organiques | À mesurer | — | — | Search Console |
| Impressions organiques | À mesurer | — | — | Search Console |
| CTR organique | À mesurer | — | — | Search Console |
| Position moyenne | À mesurer | — | — | Search Console |
| Pages indexées | À mesurer | — | — | Search Console |
| Requêtes pertinentes | À mesurer | — | — | Search Console |
| Erreurs techniques | À mesurer | — | — | Crawl / outils |

## GEO / visibilité IA

| KPI | Baseline | Actuel | Période | Source |
|---|---|---|---|---|
| Prompts testés | À définir | — | — | Benchmark IA |
| Prompts mentionnant l'école | À mesurer | — | — | Tests datés |
| Taux de mention | À calculer | — | — | Benchmark |
| Citations du site officiel | À mesurer | — | — | Réponses observées |
| Sources tierces citées | À mesurer | — | — | Réponses observées |
| Exactitude factuelle | À mesurer | — | — | Contrôle manuel |
| Erreurs de description | À mesurer | — | — | Contrôle manuel |

Taux de mention =
nombre de réponses mentionnant l'école / nombre de réponses valides
pour le même ensemble de prompts et de conditions.

Distinguer la présence du nom, une recommandation réelle et une
citation de source. Ce sont trois indicateurs différents.

## Conversion

| KPI | Baseline | Actuel | Source |
|---|---|---|---|
| Demandes de renseignements | À mesurer | — | Analytics / CRM |
| Formulaires terminés | À mesurer | — | Analytics |
| Clics d'inscription | À mesurer | — | Analytics |
| Inscriptions confirmées | À mesurer | — | Système métier |
| Taux de conversion | À calculer | — | Sources validées |

Ne pas collecter de données personnelles superflues.

Outils de mesure connus dans le dépôt (2026-10-12) : formulaires
Web3Forms (réception par email, pas de tableau de bord) ; événement
`stage_form_success` poussé dans `dataLayer` et `gtag` `generate_lead`
sur la landing `/stages/` uniquement. Aucun identifiant Google Analytics
ou Google Ads n'est présent dans les sources : à vérifier côté
propriétaire.

## Rythme de suivi

- Technique : après chaque lot de changements.
- Search Console : suivi hebdomadaire ou mensuel selon le volume.
- Conversions : mensuel.
- Benchmark IA : mensuel au départ, puis ajusté selon les résultats.
- Revue stratégique : chaque mois.

## Interprétation

Documenter les changements du site, la saisonnalité, les campagnes,
les changements de modèle IA et les limites de chaque source.

Une hausse de visibilité n'est pas nécessairement une hausse des
inscriptions. Une hausse des mentions IA n'est pas nécessairement
une hausse du trafic.

Chaque rapport doit distinguer observations, hypothèses et conclusions.
