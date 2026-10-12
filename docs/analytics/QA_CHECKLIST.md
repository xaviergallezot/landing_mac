# QA Checklist — Method Acting Center (site statique, build.py)

Agent : analytics-qa · Version : 2026-10-12.

À dérouler **avant chaque validation de lot** (phase D) et avant de
remettre `newsite/dist/` au propriétaire pour dépôt FTP. Toutes les
commandes se lancent depuis la racine du dépôt (`/home/user/landing_mac`
dans l'environnement d'audit ; adapter le chemin ailleurs). Les contrôles
marqués **[prod]** exigent l'accès au site en ligne et sont à exécuter par
le propriétaire ou depuis un poste ayant accès à Internet.

Règle : on modifie les sources (`newsite/pages`, `partials`, `assets`,
`static`, `build.py`, `tools/`), jamais `newsite/dist/` à la main.

## 0. Avant de commencer

```bash
git status --short            # arbre propre ou seulement les fichiers du lot
git branch --show-current     # jamais la branche principale pour un lot
git diff --stat               # périmètre du lot
```

- [ ] Le lot ne touche que les fichiers annoncés.
- [ ] Aucun fichier de `newsite/prod-snapshot/` n'est modifié.
- [ ] Aucun secret ajouté (la clé Web3Forms est publique par conception, elle ne compte pas).

## 1. Construction

```bash
cd newsite && python3 build.py ; echo "exit=$?" ; cd ..
```

- [ ] Sortie terminée par `OK — dist/ généré : 10 pages, uploads/ = N fichiers, aucune image manquante`
      et `exit=0`. Toute `AssertionError` (placeholder `{{`, référence `assets/`, base64,
      chemin relatif `uploads/`, fichier manquant) bloque le lot.
- [ ] La landing stages s'écrit (`landing écrite : …/dist/stages/index.html` et `contrôles ok`).

```bash
git status --short newsite/dist | grep -v sitemap.xml
```

- [ ] Après build, seuls les fichiers de `dist/` correspondant au lot ont changé.
      `dist/sitemap.xml` change à chaque build (`lastmod` = date du jour) : c'est attendu.
- [ ] Rebuild idempotent : lancer `python3 build.py` une seconde fois, `git status` ne doit rien
      ajouter.

## 2. Garde-fous sur le contenu généré

```bash
grep -rl "assets/" newsite/dist --include=*.html ; echo "(attendu : rien)"
grep -rl "data:image" newsite/dist --include=*.html ; echo "(attendu : rien)"
grep -rl "{{" newsite/dist --include=*.html ; echo "(attendu : rien)"
grep -rn 'src="uploads/' newsite/dist --include=*.html ; echo "(attendu : rien)"
```

- [ ] Quatre résultats vides.

```bash
# toutes les images référencées existent dans dist/uploads/
cd newsite/dist && grep -rhoE '/uploads/[^"'"'"')[:space:]]+' --include=*.html . | sort -u \
  | while read -r u; do [ -f ".$u" ] || echo "MANQUANT $u"; done ; cd ../..
```

- [ ] Aucune ligne `MANQUANT`.

## 3. Titres, descriptions, H1, canonicals, robots

```bash
cd newsite/dist && for f in *.html */index.html; do
  printf '%-22s title=%s | canon=%s | h1=%s | desc=%s\n' "$f" \
    "$(grep -c '<title>' "$f")" "$(grep -o 'rel="canonical" href="[^"]*"' "$f" | head -1)" \
    "$(grep -c '<h1' "$f")" "$(grep -c 'name="description"' "$f")"
done ; cd ../..
```

- [ ] `title=1`, `desc=1`, `h1=1` pour chaque fichier (14 fichiers).
- [ ] Canonical = URL propre (`https://www.methodacting.fr/acting`…), sauf `jpo.html` et
      `stages.html` qui gardent l'extension, `tarifs/index.html` → `/tarifs`, landings → leur
      propre dossier (`/jpo/`, `/jposr/`, `/stages/`).
- [ ] Titres et descriptions définis dans `newsite/build.py` (liste `PAGES`) : uniques, ≤ ~60 / ~155
      caractères, cohérents avec le contenu visible.

```bash
grep -rho 'name="robots" content="[^"]*"' newsite/dist --include=*.html | sort | uniq -c
```

- [ ] Aucun `noindex` sur une page du sitemap. (`newsite/maintenance/index.html` est `noindex`
      et ne doit jamais être copié dans `dist/`.)

## 4. Liens internes et externes

```bash
cd newsite/dist && python3 -I - <<'EOF'
import re, os, glob
files = sorted(glob.glob("*.html") + glob.glob("*/index.html"))
for f in files:
    c = open(f, encoding="utf-8").read()
    hrefs = re.findall(r'href="([^"#?]+)', c)
    rel = {h for h in hrefs if not h.startswith(("http", "mailto:", "tel:", "/", "'"))
           and not os.path.exists(os.path.join(os.path.dirname(f), h))}
    ab = {h for h in hrefs if h.startswith("/") and not h.startswith("/uploads/")
          and not any(os.path.exists(p) for p in ("."+h, "."+h+".html", "."+h.rstrip("/")+"/index.html"))}
    print(f"{f:22s} cassés relatifs={sorted(rel)} cassés absolus={sorted(ab)}")
EOF
cd ../..
```

- [ ] Aucun lien cassé (le gabarit JS `'+esc(r.link)+'` des landings est un faux positif connu).
- [ ] **[prod]** Liens externes (Google avis, Trustpilot, Maps, Instagram, YouTube, Facebook,
      WhatsApp `wa.me/qr/…`, PDF `/uploads/planning-hebdomadaire.pdf`) : ouvrir chacun une fois.

```bash
# liens internes en .html qui passeront par une 301 (information, pas un blocage)
grep -rhoE 'href="(acting|scenario-real|contact|tarifs|planning|cours-essai|inscription|index)\.html' \
  newsite/dist --include=*.html | sort | uniq -c
```

- [ ] Noter le nombre ; une décision technical-seo est attendue sur le passage aux URLs propres
      dans les liens internes. Vérifier qu'aucun nouveau lien ne crée de chaîne (A → B → C).

## 5. Sitemap et robots

```bash
python3 -I -c "import xml.dom.minidom,sys; xml.dom.minidom.parse('newsite/dist/sitemap.xml'); print('sitemap XML valide')"
grep -c "<loc>" newsite/dist/sitemap.xml          # attendu : 10
grep -o "<loc>[^<]*" newsite/dist/sitemap.xml | sed 's/<loc>//'
cat newsite/dist/robots.txt | head -10
```

- [ ] Sitemap valide, 10 URLs, chacune égale au canonical de sa page, aucune landing, pas de
      `/tarifs/`.
- [ ] `robots.txt` : `Allow: /`, `Disallow: /tarifs/`, `Sitemap:` en HTTPS www.
- [ ] Une nouvelle page = une entrée dans `PAGES` (`build.py`) → elle apparaît automatiquement dans
      le sitemap et reçoit son JSON-LD ; vérifier `OG_IMAGES` et `prio` complétés (sinon `KeyError`).
- [ ] **[prod]** `curl -s https://www.methodacting.fr/sitemap.xml | head -5` et
      `curl -s https://www.methodacting.fr/robots.txt` identiques à `dist/`.

## 6. Données structurées (JSON-LD)

```bash
cd newsite/dist && python3 -I - <<'EOF'
import re, json, glob
for f in sorted(glob.glob("*.html") + glob.glob("*/index.html")):
    c = open(f, encoding="utf-8").read()
    for i, b in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.S)):
        try:
            d = json.loads(b); g = d.get("@graph", [d])
            print(f"{f:22s} bloc {i}: OK  types={[x.get('@type') for x in g]}")
        except Exception as e:
            print(f"{f:22s} bloc {i}: INVALIDE {e}")
    if "ld+json" not in c: print(f"{f:22s} aucun JSON-LD")
EOF
cd ../..
```

- [ ] Tous les blocs sont parsables.
- [ ] Les valeurs JSON-LD correspondent au contenu visible **et** à `docs/FACTS_REGISTER.md` :
      prix des `Course` (370 / 350 € par mois), prix des `Event` stages (160 € ; « sur demande » =
      pas d'`offers` avec prix), dates des stages et JPO, horaires, adresse, téléphone, note
      `aggregateRating` (4,8 / 98 au 2026-10-12 : valeur datée à rafraîchir).
- [ ] Aucun type non justifié (pas de `Review` inventé, pas d'`AggregateRating` sans source).
- [ ] **[prod]** Tester 1 page de chaque type dans le test de résultats enrichis Google
      (`https://search.google.com/test/rich-results`) et le validateur Schema.org
      (`https://validator.schema.org/`) ; conserver la capture et la date dans `docs/technical/`.

## 7. Faits, prix, dates, CTA

```bash
# prix affichés dans les sources (à comparer au FACTS_REGISTER)
grep -rnoE '[0-9]{2,4}[  ]?€' newsite/pages newsite/static/jpo/index.html newsite/static/jposr/index.html newsite/tools/build_landing_stages.py newsite/static/llms.txt | sort | uniq -c | sort -rn
# dates 2026/2027 affichées
grep -rnoE '[0-9]{1,2}(,| &amp;| &| et) [0-9]{1,2} (octobre|novembre|décembre|janvier|février|mars|avril|mai|juin|juillet) 20[0-9]{2}|[0-9]{1,2} (au|-) [0-9]{1,2} [a-zéû]+ 20[0-9]{2}' newsite/pages newsite/static newsite/tools | sort -u
```

- [ ] Chaque prix et chaque date figure dans `docs/FACTS_REGISTER.md` avec le statut **Vérifié** ;
      sinon [À VALIDER] et retrait du lot.
- [ ] Les mêmes valeurs sont identiques entre `pages/*.html`, `build.py` (JSON-LD),
      `static/llms.txt`, `tools/build_landing_stages.py` (`SESSIONS`) et les landings.
- [ ] Aucune nouvelle promesse (gratuité, taux de réussite, diplôme, partenariat) sans source.
- [ ] CTA : chaque bouton mène à la page attendue (`cours-essai`, `inscription`, `stages.html`,
      `jpo.html`, `contact`) ; les paramètres `?stage=` et `?programme=` pré-cochent bien les cases
      (voir § 9).

## 8. Rendu mobile et desktop (Playwright)

Installation (une fois ; non présent dans l'environnement d'audit) :

```bash
pip install playwright && python3 -m playwright install chromium
```

Servir `dist/` localement puis capturer :

```bash
(cd newsite/dist && python3 -m http.server 8080 >/dev/null 2>&1 &) ; sleep 1
mkdir -p /tmp/qa-shots && python3 -I - <<'EOF'
from playwright.sync_api import sync_playwright
pages = ["", "acting", "scenario-real", "stages.html", "cours-essai", "jpo.html", "inscription", "tarifs", "planning", "contact", "jpo/", "jposr/", "stages/"]
with sync_playwright() as p:
    b = p.chromium.launch()
    for vp, name in (({"width": 390, "height": 844}, "mobile"), ({"width": 1366, "height": 900}, "desktop")):
        ctx = b.new_context(viewport=vp, device_scale_factor=1)
        pg = ctx.new_page(); errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        for path in pages:
            url = "http://localhost:8080/" + (path if path.endswith((".html", "/")) or path == "" else path + ".html")
            pg.goto(url, wait_until="networkidle")
            overflow = pg.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
            pg.screenshot(path=f"/tmp/qa-shots/{name}-{path.replace('/','_') or 'index'}.png", full_page=True)
            print(f"{name:7s} {url:45s} overflow_horizontal={overflow} erreurs_js={len(errors)}")
        ctx.close()
    b.close()
EOF
pkill -f "http.server 8080"
```

- [ ] `overflow_horizontal=False` partout (pas de défilement latéral sur mobile).
- [ ] `erreurs_js=0`.
- [ ] Relire les captures : menu mobile, bandeau sticky, formulaires lisibles, images non déformées,
      polices Oswald / Archivo chargées (connexion Internet requise pour Google Fonts ; sinon
      fallback attendu).
- [ ] **[prod]** PageSpeed Insights sur `/`, `/acting`, `/stages.html` (mobile) : relever LCP, CLS,
      INP et le poids de page dans `KPI_DASHBOARD.md` (Qualité). Images > 300 Ko dans `uploads/`
      à signaler.

## 9. Formulaires (sans spammer la boîte du propriétaire)

En local, les envois partent réellement vers Web3Forms (clé publique) :
**limiter à un envoi test par formulaire modifié**, avec « TEST QA — à ignorer » dans le message,
et prévenir le propriétaire. Pour tester la logique sans envoyer, intercepter la requête :

```bash
(cd newsite/dist && python3 -m http.server 8080 >/dev/null 2>&1 &) ; sleep 1
python3 -I - <<'EOF'
from playwright.sync_api import sync_playwright
tests = [  # (url, id du form, champs à remplir, cases à cocher)
  ("contact.html", "contact-form", {"prenom":"Test","nom":"QA","email":"qa@example.com","message":"TEST QA"}, []),
  ("cours-essai.html", "essai-form", {"prenom":"Test","nom":"QA","email":"qa@example.com"}, ["atelier"]),
  ("stages.html?stage=a", "stages-form", {"prenom":"Test","nom":"QA","email":"qa@example.com"}, []),
  ("inscription.html?programme=acting", "inscription-form", {"prenom":"Test","nom":"QA","email":"qa@example.com"}, []),
  ("jpo.html", "jpo-form", {"prenom":"Test","nom":"QA","email":"qa@example.com"}, []),
]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":390,"height":844})
    captured = []
    pg.route("https://api.web3forms.com/submit", lambda r: (captured.append(r.request.post_data), r.fulfill(status=200, content_type="application/json", body='{"success":true}')))
    for url, fid, fields, boxes in tests:
        pg.goto("http://localhost:8080/" + url, wait_until="networkidle")
        for n, v in fields.items(): pg.fill(f"#{fid} [name={n}]", v)
        for n in boxes: pg.check(f"#{fid} input[name={n}] >> nth=0")
        if fid == "jpo-form": pg.select_option("#jpo-list select >> nth=0", index=1)
        before = len(captured)
        pg.click(f"#{fid} button[type=submit]"); pg.wait_for_timeout(800)
        ok = pg.is_visible(f"#{fid.replace('-form','')}-success")
        print(f"{url:35s} envoi intercepté={len(captured)>before} succès affiché={ok} payload_contient_PII={'qa@example.com' in (captured[-1] or '') if captured else None}")
    b.close()
EOF
pkill -f "http.server 8080"
```

- [ ] Chaque formulaire : `envoi intercepté=True`, `succès affiché=True`.
- [ ] Validation : sans case cochée, le message d'avertissement s'affiche et rien n'est envoyé.
- [ ] `?stage=a` pré-coche « Stage A » ; `?programme=acting` pré-coche le programme Acting.
- [ ] Landings `/jpo/`, `/jposr/`, `/stages/` : même test en adaptant `booking-form` /
      `stages-form` ; sur `/stages/`, vérifier dans la console que `window.dataLayer` contient
      `stage_form_success` après succès.
- [ ] Si un événement analytics a été ajouté (voir `MEASUREMENT_PLAN.md`) : il ne contient **aucune
      donnée personnelle** (vérifier le payload réseau), il part **après** `success:true`, et, en
      option B, **rien ne part avant consentement**.
- [ ] Le sujet et le `from_name` du payload identifient toujours le type de formulaire (base du
      comptage par email, `BASELINE.md` § 3).

## 10. Serveur et URLs [prod]

À exécuter par le propriétaire après dépôt FTP (ou depuis un poste connecté) :

```bash
for u in / /acting /acting.html /index.html /jpo.html /stages.html /jpo/ /jposr/ /stages/ /tarifs /tarifs/ \
         /sitemap.xml /robots.txt /llms.txt /uploads/planning-hebdomadaire.pdf /url-inexistante-test-qa; do
  printf '%-45s ' "$u"; curl -s -o /dev/null -w '%{http_code} -> %{redirect_url}\n' "https://www.methodacting.fr$u"
done
curl -s -o /dev/null -w '%{http_code} -> %{redirect_url}\n' "http://methodacting.fr/acting"
```

- [ ] `/` , `/acting`, `/jpo.html`, `/stages.html`, landings, `/tarifs`, `/tarifs/`, sitemap,
      robots, llms.txt, PDF : `200`.
- [ ] `/acting.html` → `301` vers `/acting` ; `/index.html` → `301` vers `/` ; `http://` → `301`
      vers `https://www.` en **une seule** redirection (pas de chaîne http → https → www).
- [ ] `/url-inexistante-test-qa` → **`404`** (et non `200`). S'il renvoie `200`, c'est un soft 404 à
      corriger (`.htaccess:65`). Dans les deux cas, le corps est aujourd'hui la page d'accueil.
- [ ] Anciennes URLs d'images (`/assets/img/…`, `/jpo/uploads/…`) : `404` attendu après nettoyage
      serveur ; les nouvelles `/uploads/…` : `200`.
- [ ] Après dépôt : « Vérifier l'URL en direct » dans Search Console sur une page modifiée.

## 11. Diff, documentation, retour arrière

```bash
git diff --stat ; git diff newsite/pages newsite/partials newsite/assets newsite/static newsite/build.py newsite/tools
```

- [ ] Diff relu ligne à ligne ; aucune modification hors périmètre.
- [ ] Entrée ajoutée dans `docs/CHANGELOG.md` (format imposé) avec tests effectués et procédure de
      retour arrière (`git revert <commit>` puis `python3 build.py` puis redépôt de `dist/`).
- [ ] `docs/FACTS_REGISTER.md` mis à jour si un fait a été ajouté ou modifié.
- [ ] Le propriétaire a reçu : liste des fichiers de `dist/` à déposer, fichiers à supprimer sur le
      serveur, critères d'acceptation, et la commande du § 10 à lancer après dépôt.

## 12. Résumé à joindre au rapport de QA

| Contrôle | Résultat | Preuve |
|---|---|---|
| build.py | OK / KO | sortie console |
| Garde-fous dist | OK / KO | § 2 |
| Title / H1 / canonical / robots | OK / KO | § 3 |
| Liens | OK / KO | § 4 |
| Sitemap / robots | OK / KO | § 5 |
| JSON-LD | OK / KO | § 6 (+ captures validateurs) |
| Faits / prix / dates | OK / KO / [À VALIDER] | § 7 |
| Mobile / desktop | OK / KO | captures § 8 |
| Formulaires | OK / KO | § 9 |
| Prod (HTTP) | OK / KO / non testé | § 10 |
| Diff / CHANGELOG | OK / KO | § 11 |
