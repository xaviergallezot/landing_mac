# État initial — Method Acting Center

Date : 2026-10-12
Branche de travail : `claude/landing-acteur-v4-0c3wmq` (96 commits, arbre propre au démarrage de l'audit)
Site cible : https://www.methodacting.fr/

## 1. Nature du projet (vérifié par inspection)

- Site statique, sans CMS ni framework JavaScript. Pages HTML assemblées par `newsite/build.py`
  (head + header + page + footer, CSS et JS inlinés dans chaque page).
- Sortie : `newsite/dist/`, déposée telle quelle à la racine `www/` d'un hébergement OVH (Apache,
  `.htaccess`). Déploiement manuel par FTP par le propriétaire.
- `newsite/prod-snapshot/` : copie de la production avant la mise en conformité du 2026-10
  (ancienne structure avec 4 dossiers d'images). Référence uniquement.
- Aucun test automatisé hormis les assertions de `build.py` (pas de `{{` résiduel, pas de chemin
  `assets/`, pas de base64, pas de fichier image manquant).

## 2. Pages publiques déployées

| Page | Poids HTML | Dans le sitemap | Remarque |
|---|---|---|---|
| `/` (index.html) | 94 Ko | oui | |
| `/acting` | 94 Ko | oui | URL propre via .htaccess |
| `/scenario-real` | 91 Ko | oui | |
| `/stages.html` | 107 Ko | oui | garde l'extension (le dossier `/stages/` est une landing) |
| `/cours-essai` | 94 Ko | oui | |
| `/jpo.html` | 91 Ko | oui | garde l'extension (le dossier `/jpo/` est une landing) |
| `/inscription` | 95 Ko | oui | |
| `/tarifs` | 89 Ko | oui | |
| `/planning` | 96 Ko | oui | |
| `/contact` | 78 Ko | oui | |
| `/tarifs/` | 89 Ko | non | copie de `/tarifs`, `Disallow` dans robots.txt |
| `/jpo/` | 115 Ko | non | landing Google Ads acteurs, hors navigation |
| `/jposr/` | 115 Ko | non | landing Google Ads scénario/réalisation, hors navigation |
| `/stages/` | 105 Ko | non | landing Google Ads stages, générée par `tools/build_landing_stages.py` |

Fichiers annexes : `robots.txt` (ouvert à tous les robots, y compris IA), `sitemap.xml` (10 URLs),
`llms.txt`, `.htaccess`, `uploads/` (46 fichiers, 6,9 Mo, dont 5 images de plus de 300 Ko).

## 3. Ce qui est déjà en place côté SEO (vérifié dans les sources)

- Balises title, meta description, canonical, robots, Open Graph et Twitter sur toutes les pages
  (`partials/head.html`, valeurs par page dans `build.py`).
- JSON-LD `@graph` : EducationalOrganization + LocalBusiness (adresse, téléphone, horaires, note
  4,8/98, profils sociaux), WebSite, WebPage, Course (acting, scénario), Event (JPO, stages),
  Offer (cours d'essai), FAQPage (tarifs).
- URLs propres, redirection HTTPS, compression et cache dans `.htaccess`.
- Fiche Google Business existante (note 4,8/5 sur 98 avis au 2026-10-12).

## 4. Mesure

- Aucun snippet Google Analytics, Google Tag Manager ou Google Ads n'est chargé dans `dist/`
  (recherche `googletagmanager`, `gtag/js`, `GTM-`, `G-…` : aucun résultat).
- La landing `/stages/` pousse un événement `stage_form_success` dans `dataLayer` et appelle
  `gtag('event','generate_lead')` : sans conteneur chargé, ces événements ne sont envoyés nulle part.
- Formulaires via Web3Forms : réception par email, pas de tableau de bord.
- Accès Search Console, GA4, Google Ads, Bing Webmaster : non disponibles dans cet environnement,
  à demander au propriétaire. Fichier `BingSiteAuth.xml` en cours de dépôt par le propriétaire.

## 5. Accès et limites de l'environnement d'audit

- Le site en production n'est pas joignable depuis l'environnement (proxy sortant refusé sur
  methodacting.fr). Les audits portent sur `newsite/dist/`, copie exacte du déploiement.
  Non vérifiables ici : codes HTTP réels, redirections, indexation effective, temps de réponse,
  Core Web Vitals terrain.
- Recherche web disponible pour la concurrence et les sources tierces.
- Aucun assistant IA tiers interrogeable : le benchmark IA est livré comme protocole à exécuter
  par le propriétaire, sans résultats simulés.

## 6. Modifications récentes susceptibles de fausser les comparaisons

Entre septembre et octobre 2026 (voir `git log`), le site a été entièrement reconstruit :
nouvelles pages, nouvelles URLs propres, dossier d'images unique `/uploads/`, nouvelles données
structurées, nouveau robots.txt, nouveaux landings. Toute comparaison avec les données antérieures
(anciennes URLs WordPress visibles dans `prod-snapshot/`) devra en tenir compte. Les anciennes
URLs WordPress éventuellement indexées sont à surveiller en 404 dans Search Console.

## 7. Autorisations confirmées pour cette phase

- Audit en lecture seule : aucun fichier de `newsite/` n'est modifié.
- Les livrables sont écrits dans `docs/`.
- Aucune implémentation avant approbation explicite du propriétaire.
