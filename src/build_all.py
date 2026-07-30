import json, base64, os, re

REPO = '/home/user/landing_mac'
content = open('content.html').read().strip()
style   = open('style.css').read()
script  = open('script.js').read()

# key, filename, label
CONFIG = [
  ('hero_kramer','Kramer_Horizontal00086408_V1.jpg','Héro · actrice, intensité émotionnelle'),
  ('hero_felure','Felure_Horizontal00086406_V1.jpg','Héro · actrice souriante, lumière chaude'),
  ('hero_joseph','Joseph-Breaking-Bad.jpg','Héro · acteur au téléphone'),
  ('hero_king','King_Horizontal00086407_V1.jpg','Héro · acteur en larmes'),
  ('methode_1','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-3.jpg','Méthode · spectacle (rire)'),
  ('methode_2','V1-0001_Antichrist_Screenshot_Horizontal00087169.jpg','Méthode · scène filmée'),
  ('methode_3','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-272.jpg','Méthode · lumière rouge'),
  ('stage_1','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-22.jpg','JPO · chemise & cravate'),
  ('stage_2','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-98.jpg','JPO · costume, lumière bleue'),
  ('stage_3','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-213.jpg','JPO · scène dramatique'),
  ('formation_1','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-154.jpg','Formation · veste militaire'),
  ('formation_2','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-163.jpg','Formation · salut militaire'),
  ('formation_3','METHOD_ACTING_CENTER_Spectacle_Acting_2024_Photographe_Rami_Ghorra-269.jpg','Formation · lumière verte'),
  ('film_proces_goldman','Le_Proces_Goldman_Affiche.webp','Affiche · Le Procès Goldman'),
  ('film_7_vies_lea','Les-7-vies-de-Lea_Raika_Hazanavicius.jpg','Affiche · Les 7 vies de Léa'),
  ('film_quantum_solace','Quantum-of-Solace-Olga-Kurylenko.jpg','Affiche · Quantum of Solace'),
  ('film_ni_chaines','affiche-ni-chaines-ni-maitres-66e49d69a884b564930223.jpg','Affiche · Ni chaînes ni maîtres'),
  ('film_sans_repit','Sans-repit-Jemima-West.jpg','Affiche · Sans répit'),
  ('film_les_invisibles','Les-invisibles_Deborah_Krey.jpg','Affiche · Les Invisibles'),
  ('film_dirty_difficult','Dirty-Diffficult-Dangerous.jpg','Affiche · Dirty Difficult Dangerous'),
  ('film_martyrs','Martyrs_Mylene_Jampanoi.jpg','Affiche · Martyrs'),
  ('contact_scene','Malcolm_And_Marie_Horizontal00086407_V1.jpg','Contact · travail de scène (N&B)'),
]

# validate content uses every key referenced by data-img and hero keys
used = set(re.findall(r'data-img="([^"]+)"', content))
hero_keys = {'hero_kramer','hero_felure','hero_joseph','hero_king'}
allkeys = {k for k,_,_ in CONFIG}
missing = (used | hero_keys) - allkeys
assert not missing, f'keys used but not in CONFIG: {missing}'

def images_js(url_for):
    lines = []
    for k,fn,label in CONFIG:
        lines.append(f"    {k}: {{ url: {json.dumps(url_for(fn))}, label: {json.dumps(label)} }}")
    return ",\n".join(lines)

def script_with(url_for):
    return script.replace("__IMAGES__", images_js(url_for))

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Archivo:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">')
STYLE = '<style id="mac-landing-style">\n'+style+'</style>'

def wrap_doc(images_url_for, banner=""):
    sc = "<script>\n"+script_with(images_url_for)+"</script>"
    return ("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n"
      "  <meta charset=\"utf-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      "  <title>Method Acting Center — Devenez acteur · Journées Portes Ouvertes à Paris</title>\n"
      "  <meta name=\"description\" content=\"Vous voulez devenir acteur ? Venez vivre la Méthode (Stanislavski / Actors Studio) lors d'une Journée Portes Ouvertes immersive et gratuite au Method Acting Center, Paris.\">\n"
      f"  {FONTS}\n  {STYLE}\n</head>\n<body style=\"margin:0;background:#F7F4EE\">\n"
      f"{banner}{content}\n{sc}\n</body>\n</html>\n")

# ---------- index.html (preview, references uploads/) ----------
index_html = wrap_doc(lambda fn: 'uploads/'+fn)
open(os.path.join(REPO,'index.html'),'w').write(index_html)

# ---------- landing-mac.html (WordPress block, empty urls) ----------
HEADER = ("<!--\n  ============================================================\n"
  "  METHOD ACTING CENTER — Landing \"Acteur / Journées Portes Ouvertes\"\n"
  "  Bloc HTML autonome à coller dans WordPress (bloc « HTML personnalisé »\n"
  "  Gutenberg, ou widget HTML Elementor/Divi).\n"
  "  IMAGES : renseignez les URL de la Médiathèque dans l'objet IMAGES\n"
  "  (au début du <script>, en bas de ce fichier).\n"
  "  ============================================================\n-->\n")
wp = HEADER + FONTS + "\n" + STYLE + "\n" + content + "\n<script>\n" + script_with(lambda fn: '') + "</script>\n"
open(os.path.join(REPO,'landing-mac.html'),'w').write(wp)

# ---------- maquettes (embed images from index.html) ----------
mime = {'.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.png':'image/png'}
emb = index_html
for k,fn,label in CONFIG:
    p=os.path.join(REPO,'uploads',fn)
    ext=os.path.splitext(fn)[1].lower()
    data=base64.b64encode(open(p,'rb').read()).decode()
    emb = emb.replace("uploads/"+fn, f"data:{mime[ext]};base64,{data}")
assert 'uploads/' not in emb, 'leftover uploads ref in maquette'
open(os.path.join(REPO,'maquette-ordinateur.html'),'w').write("<!-- MAQUETTE DE RELECTURE — VERSION ORDINATEUR (meme base responsive, photos embarquees) -->\n"+emb)
open(os.path.join(REPO,'maquette-telephone.html'),'w').write("<!-- MAQUETTE DE RELECTURE — VERSION TELEPHONE (meme base responsive, photos embarquees) -->\n"+emb)

print('OK')
print('index.html      ', round(len(index_html)/1024),'KB')
print('landing-mac.html', round(len(wp)/1024),'KB')
print('maquette (x2)   ', round(len(emb)/1024),'KB each')
print('image keys      ', len(CONFIG), '| data-img in content:', len(re.findall(r'data-img=', content)))
