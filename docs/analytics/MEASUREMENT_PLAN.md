# Plan de mesure — recommandé, NON implémenté

Agent : analytics-qa · Date : 2026-10-12 · Statut : **proposition**, aucune
ligne de code ajoutée. Toute mise en œuvre passe par une décision du
propriétaire (§ 6), une branche dédiée, `python3 build.py` et la
`QA_CHECKLIST.md`.

Principe : mesurer ce qui sert une décision (quelles pages et quelles
sources produisent des demandes), avec le minimum de données personnelles
et sans cookie non consenti.

## 1. Point de départ

Voir `BASELINE.md` : aucun outil d'analytics chargé ; formulaires par
email (Web3Forms) ; un seul événement JS (`stage_form_success` sur
`/stages/`) qui n'atteint aucun outil ; aucun bandeau de consentement ni
page de confidentialité dans les sources.

## 2. Ce qui peut être mesuré sans aucun code (dès maintenant)

| Mesure | Comment | Fréquence | Responsable |
|---|---|---|---|
| Demandes par type (contact, cours d'essai, stage, inscription, JPO) | Compter les emails Web3Forms par préfixe de sujet (table dans `BASELINE.md` § 3) | Mensuel | Propriétaire |
| Source déclarée des demandes | Compter le champ « Comment nous a connus » par valeur (Google, Recherche IA, Instagram, bouche-à-oreille…) | Mensuel | Propriétaire |
| Demandes issues des campagnes Ads sur `/stages/` | Champ « Campagne » (gclid / utm) et « Page » dans l'email de la landing stages | Mensuel | Propriétaire |
| Clics, impressions, CTR, position, pages indexées, 404 | Search Console (accès à demander) | Hebdo / mensuel | Chef de projet |
| Appels, itinéraires, clics site, avis | Google Business Profile → Performances | Mensuel | Propriétaire |
| Visibilité IA | Protocole `docs/geo/AI_PROMPT_BENCHMARK.md` (voir § 7) | Mensuel | Chef de projet / propriétaire |

Ces mesures constituent la baseline minimale. Elles ne demandent ni
consentement ni modification du site.

## 3. Événements à mesurer (spécification)

Nomenclature : `snake_case`, un événement par intention, paramètres sans
donnée personnelle (jamais le nom, l'email, le téléphone ni le message).

### 3.1 Soumissions de formulaire réussies

Déclencher **uniquement après la réponse `success: true` de Web3Forms**
(pas au clic sur « Envoyer »), afin de compter les demandes réellement
reçues.

| Événement | Paramètres | Où le déclencher (fichier / fonction) | Page |
|---|---|---|---|
| `form_submit` avec `form_type = "contact"` | `form_type`, `page_path` | `newsite/assets/site.js`, fonction `showOk()` du bloc contact (l. 117), appelée après `d.success` (l. 111) | `/contact` |
| `form_submit` avec `form_type = "cours_essai"` | `form_type`, `page_path`, `item_count` (nombre d'ateliers cochés) | `newsite/assets/site.js`, `bindForm` → `done()` (l. 210) : ajouter un `cfg.event` ou dériver `form_type` de `cfg.id` (`essai-form` → `cours_essai`) | `/cours-essai` |
| `form_submit` avec `form_type = "stage"` | `form_type`, `page_path`, `item_count`, `items` (noms des stages, pas de PII) | Idem `bindForm` → `done()` pour `stages-form` ; sur la landing : `newsite/tools/build_landing_stages.py`, fonction `track(ch)` (l. 478-483), **déjà présente**, à aligner sur la même nomenclature | `/stages.html`, `/stages/` |
| `form_submit` avec `form_type = "inscription"` | `form_type`, `page_path`, `item_count` (programmes + cours ponctuels), `rentree` (valeur du select, non personnelle) | Idem `bindForm` → `done()` pour `inscription-form` | `/inscription` |
| `form_submit` avec `form_type = "jpo"` | `form_type`, `page_path`, `item_count` | `newsite/assets/site.js`, `initJpo` → `done()` (l. 173) ; landings : `showSuccess(ch,f)` dans `newsite/static/jpo/index.html` (≈ l. 1082) et `newsite/static/jposr/index.html` (équivalent) | `/jpo.html`, `/jpo/`, `/jposr/` |
| `form_error` | `form_type`, `page_path` | Les blocs `.catch()` correspondants (site.js l. 112, 178, 215 ; landings) | Toutes |

Recommandation d'implémentation : une seule fonction utilitaire
`track(name, params)` dans `site.js` qui fait `window.dataLayer.push({event: name, ...params})`
et, si `window.gtag` existe, `gtag('event', name, params)`. Les landings
étant autonomes, la même fonction est à dupliquer dans
`static/jpo/index.html`, `static/jposr/index.html` et dans la chaîne JS
de `tools/build_landing_stages.py`. Sans conteneur chargé, ces appels
restent inoffensifs (c'est déjà le cas sur `/stages/`).

### 3.2 Clics de contact direct

| Événement | Paramètres | Sélecteur / emplacement | Fichiers |
|---|---|---|---|
| `contact_click` avec `method = "phone"` | `method`, `page_path`, `placement` (`footer`, `page`, `card`) | `a[href^="tel:"]` | `newsite/partials/footer.html:27`, `pages/contact.html:19`, `pages/cours-essai.html:161`, `pages/inscription.html:156, 288`, `pages/stages.html:209`, landings |
| `contact_click` avec `method = "whatsapp"` | idem | `a[href^="https://wa.me/"]` | `partials/footer.html:28`, `pages/contact.html:20`, landings |
| `contact_click` avec `method = "email"` | idem | `a[href^="mailto:"]` | `partials/footer.html:26`, `pages/contact.html:18`, etc. |

Déclenchement : un écouteur délégué unique dans `site.js`
(`document.addEventListener("click", …)`) sur ces trois sélecteurs.
Sur mobile, un clic `tel:` ne garantit pas l'appel : lire la mesure
comme une « intention d'appel ».

### 3.3 Clics CTA et navigation vers les pages de conversion

| Événement | Paramètres | Sélecteur | Remarque |
|---|---|---|---|
| `cta_click` | `cta_text` (texte du bouton), `cta_target` (`cours-essai`, `inscription`, `stages`, `jpo`, `contact`), `placement` (`header`, `hero`, `section`, `footer`), `page_path` | `a.btn[href*="cours-essai"]`, `a.btn[href*="inscription"]`, `a.btn[href*="stages"]`, `a.btn[href*="jpo"]`, `a.nav-cta` | Le header (`partials/header.html:2, 17, 18, 23`) et le footer (`partials/footer.html:13-22`) contiennent déjà les liens ; les classes `.btn` / `.nav-cta` servent de sélecteurs sans modifier le HTML. |
| `outbound_click` | `link_domain`, `link_type` (`google_reviews`, `trustpilot`, `maps`, `instagram`, `youtube`, `facebook`) | `a[href^="https://share.google"]`, `a[href^="https://maps.app.goo.gl"]`, `a[href*="trustpilot"]`, réseaux | Mesure l'intérêt pour les preuves (avis) : 6 liens `share.google` sur l'accueil. |
| `landing_to_site` | `from` (`/jpo/`, `/jposr/`, `/stages/`), `to` | liens absolus `https://www.methodacting.fr/...` dans les landings | Reconstitue le parcours landing → site, utile si Ads. |
| `stage_prefill` | `stage_key` (`a`, `b`, `scenario`, …) | `newsite/assets/site.js:252-258` (lecture de `?stage=`) et `:259-264` (boutons `[data-stage]`) | Indique quel stage attire ; pas une conversion. |

### 3.4 Pages vues

Standard de l'outil choisi. Points d'attention propres au site :

- agréger `/tarifs` et `/tarifs/` (copie, voir `BASELINE.md` § 5.7) ;
- exclure ou étiqueter les pages vues des 404 (servies par `index.html`, `.htaccess:65`) :
  recommandation technique = vraie page `404.html` avec `noindex` et sans canonical, à faire
  avant d'activer les pages vues ;
- `/jpo/`, `/jposr/`, `/stages/` : landings Ads hors sitemap ; segmenter leur trafic
  (`page_path` commence par `/jpo/`, etc.) pour ne pas mélanger organique et payant ;
- conserver les paramètres `?stage=`, `?programme=`, `gclid`, `utm_*` dans `page_location`.

## 4. Choix de l'outil et consentement (RGPD / CNIL)

Aucun cookie analytique ne doit être déposé sans consentement préalable
(ePrivacy, lignes directrices CNIL). Deux voies compatibles ; le choix
appartient au propriétaire.

### Option A — mesure sans cookie, exemptée de consentement (recommandée pour démarrer)

Outil d'audience sans cookie ni identifiant cross-site, configuré selon
les critères d'exemption CNIL (finalité limitée à la mesure d'audience,
données agrégées, pas de recoupement, pas de suivi cross-site, hébergement
UE ou données non transférées). Candidats habituels : Matomo (auto-hébergé
ou cloud UE) en mode exempté, ou une solution légère hébergée en UE
(Plausible / Umami en cloud UE ou auto-hébergé). Vérifier la conformité
du fournisseur retenu à la date du choix.

- Avantages : pas de bandeau nécessaire pour la mesure d'audience seule, pas de perte de données
  liée au refus, mise en place légère (un `<script>` dans `newsite/partials/head.html` et dans les
  trois landings autonomes).
- Limites : pas de lien natif avec Google Ads ni Search Console, pas de suivi utilisateur
  multi-session (c'est voulu), événements à envoyer via l'API de l'outil (adapter la fonction
  `track`).
- Coût : abonnement ou hébergement, à valider par le propriétaire (aucune dépense sans accord).

### Option B — GA4 + Google Tag Manager + conversions Google Ads (si campagnes Ads actives)

- Nécessite un **bandeau de consentement** (CMP) avant tout dépôt de cookie, le **Consent Mode v2**,
  et une **politique de confidentialité** qui nomme les outils. Aujourd'hui aucun de ces éléments
  n'existe dans les sources.
- Les événements déjà présents sur `/stages/` (`dataLayer.push`, `gtag('event','generate_lead')`)
  sont prévus pour cette voie : il suffirait de coller la balise à l'emplacement commenté
  (`newsite/tools/build_landing_stages.py:33`) — **mais pas avant le consentement**.
- Attendre : une part des visiteurs refusera ; les chiffres de conversion seront partiels. Les emails
  Web3Forms restent la vérité de référence pour le nombre de demandes.
- Les deux options peuvent coexister : A pour l'audience organique, B uniquement sur les landings
  Ads si le propriétaire fait de la publicité.

### Quelle que soit l'option

- Ajouter une page **Mentions légales / Politique de confidentialité** (pages absentes des sources)
  décrivant Web3Forms (sous-traitant des formulaires, hébergement et durée de conservation à
  vérifier), Google Fonts (chargé depuis `fonts.googleapis.com` dans `partials/head.html` : transfert
  d'adresse IP vers Google, à évaluer ; alternative = auto-héberger les polices dans `uploads/`),
  et l'outil de mesure retenu.
- Ne jamais envoyer de données personnelles dans les événements (pas de nom, email, téléphone,
  message, ni le contenu libre du champ « Message »).
- Documenter dans `docs/CHANGELOG.md` la date d'activation : c'est le T0 des séries.

## 5. Plan de déploiement proposé (après décision)

| Étape | Contenu | Fichiers | Validation |
|---|---|---|---|
| 0 | Décisions du § 6 ; obtention des accès (`BASELINE.md` § 4) | — | Propriétaire |
| 1 | Page de confidentialité / mentions légales ; vraie page 404 | `newsite/pages/`, `newsite/build.py` (PAGES), `newsite/static/.htaccess:65` | Contenu validé par le propriétaire |
| 2 | Fonction `track()` commune + événements `form_submit` / `form_error` sur les 5 formulaires du site et les 3 landings | `newsite/assets/site.js`, `static/jpo/index.html`, `static/jposr/index.html`, `tools/build_landing_stages.py` | `QA_CHECKLIST.md` § formulaires (envoi test avec mention « TEST » dans le message) |
| 3 | Chargement de l'outil (option A ou B + CMP) | `newsite/partials/head.html`, landings | Vérifier dans le navigateur que rien n'est envoyé avant consentement (option B) |
| 4 | Clics contact / CTA / sortants | `newsite/assets/site.js` | Console réseau : un hit par clic |
| 5 | Première lecture à J+28, puis mensuelle | `docs/analytics/KPI_DASHBOARD.md` | Chef de projet |

Chaque étape = une branche, un build, un diff relu, une entrée CHANGELOG,
un déploiement manuel par le propriétaire.

## 6. Décisions attendues du propriétaire

1. Existe-t-il déjà une propriété Search Console, GA4, un compte Google Ads actif ? (BASELINE § 4)
2. Choix de l'outil : option A (sans cookie), option B (GA4/GTM + CMP), ou A + B sur les landings.
3. Budget accepté pour l'outil (A) ou la CMP (B) : aucune dépense sans accord écrit.
4. Rédaction / validation de la politique de confidentialité et des mentions légales
   (raison sociale, SIRET, hébergeur, responsable de traitement : informations absentes du dépôt,
   **[À VALIDER]**).
5. Accord pour le comptage mensuel des emails Web3Forms et pour l'usage du champ
   « Comment nous a connus » comme source d'attribution.
6. Date exacte du dernier déploiement de `dist/` (T0).
7. Souhaite-t-il que les 404 affichent une vraie page d'erreur plutôt que l'accueil ?

## 7. Protocole de benchmark IA

Le benchmark de visibilité dans les assistants IA s'exécute **avec le
fichier `docs/geo/AI_PROMPT_BENCHMARK.md`** (rédigé par l'agent
geo-ai-visibility ; ne pas le dupliquer ici). Règles de mesure côté
analytics-qa :

- utiliser exactement les prompts du fichier, dans l'ordre, sans reformulation ;
- pour chaque exécution, enregistrer : date, assistant et version/modèle affichés, langue, mode
  (avec ou sans recherche web), localisation déclarée, session neuve ou non, texte intégral de la
  réponse (sans donnée personnelle) ;
- coder chaque réponse selon trois colonnes distinctes : **mention** du nom (oui/non),
  **recommandation** explicite (oui/non), **citation** d'une source (URL, officielle ou tierce) ;
  relever les **erreurs factuelles** par rapport à `docs/FACTS_REGISTER.md` (prix, dates,
  adresse, méthode) ;
- répéter chaque prompt au moins 3 fois (ou sur 3 jours) avant de calculer un taux ; un essai
  unique ne prouve ni présence ni absence ;
- ne pas automatiser l'interrogation d'un service contrairement à ses conditions d'utilisation ;
- reporter les taux dans `KPI_DASHBOARD.md` (section GEO) avec le nombre de réponses valides en
  dénominateur ;
- un changement de modèle ou de mode entre deux mesures doit être noté : il invalide la
  comparaison directe.

## 8. Ce que ce plan ne promet pas

Aucune position Google, aucune citation IA, aucun volume de demandes.
La mesure sert à constater, pas à garantir. Une hausse de trafic ne
sera attribuée à une modification que si la chronologie, la page
concernée et l'absence d'autre cause (saisonnalité, campagne Ads,
changement de modèle IA) le permettent.
