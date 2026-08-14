from pathlib import Path
from PIL import Image
import html
import re

ROOT = Path(__file__).resolve().parents[1]
PEOPLE = ROOT / "assets" / "people"
HTML = ROOT / "index.html"
CSS = ROOT / "styles.css"

MAPPING = {
    "Rajeev Ahuja": "rajeev-ahuja",
    "Deb Ranjan Banerjee": "deb-ranjan-banerjee",
    "Aditi Chandrasekar": "aditi-chandrasekhar",
    "Aditi Chandrasekhar": "aditi-chandrasekhar",
    "Peter Comba": "peter-comba",
    "Étienne Derat": "etienne-derat",
    "Odile Eisenstein": "odile-eisenstein",
    "Sagar Ghorai": "sagar-ghorai",
    "Subhas Ghosal": "subhas-ghosal",
    "E. D. Jemmis": "ed-jemmis",
    "Milan Kumar Jena": "milan-kumar-jena",
    "B. Kiran": "b-kiran",
    "Sandeep Kumar": "sandeep-kumar",
    "Arup Mahata": "arup-mahata",
    "Satoshi Maeda": "satoshi-maeda",
    "Sabyasachi Mishra": "sabyasachi-mishra",
    "T. Pradeep": "t-pradeep",
    "Sai G. Ramesh": "sai-g-ramesh",
    "N. Satyamurthy": "n-satyamurthy",
    "Henry F. Schaefer III": "henry-f-schaefer-iii",
    "Sason Shaik": "sason-shaik",
    "A. Sirohiwal": "a-sirohiwal",
    "R. B. Sunoj": "rb-sunoj",
    "R. S. Swathi": "rs-swathi",
    "Soujanya Yarasi": "soujanya-yarasi",
    "Anoop Ayyappan": "anoop-ayyappan",
    "Manoj Kumar T. K.": "manoj-kumar-tk",
    "Sherin D. R.": "sherin-dr",
    "Susmita De": "susmita-de",
    "C. H. Suresh": "ch-suresh",
    "Mahesh Hariharan": "mahesh-hariharan",
    "P. N. V. Pavankumar": "pnv-pavankumar",
    "Bharatam V. Prasad": "bharatam-v-prasad",
    "G. Narahari Sastry": "g-narahari-sastry",
    "G. Subramanian": "govindan-subramanian",
    "Govindan Subramanian": "govindan-subramanian",
    "Ashwini Kr. Phukan": "ashwini-kr-phukan",
    "Jayasree E. G.": "jayasree-eg",
    "Pancharatna P. D.": "pancharatna-pd",
    "P. Parameswaran": "p-parameswaran",
    "D. L. V. K. Prasad": "dlvk-prasad",
    "Biswarup Pathak": "biswarup-pathak",
    "Dandamudi Usharani": "dandamudi-usharani",
    "Dibyendu Mallick": "dibyendu-mallick",
    "Priyakumari C. P.": "priyakumari-cp",
    "Naiwrit Karmodak": "naiwrit-karmodak",
}

TARGET = set(MAPPING.values())
assert len(TARGET) == 44, len(TARGET)

# Validate the complete local asset set before touching HTML/CSS.
files = sorted(PEOPLE.glob("*.webp"))
existing = {p.stem for p in files}
assert existing == TARGET, (sorted(TARGET - existing), sorted(existing - TARGET))
for p in files:
    with Image.open(p) as im:
        im.load()
        assert im.size == (480, 600), (p.name, im.size)
        assert im.format == "WEBP", (p.name, im.format)

# Rewrite each person card to a local image path only.
text = HTML.read_text(encoding="utf-8")
card_re = re.compile(r'<(?:a|article)\s+class="person-card"[^>]*>.*?</(?:a|article)>', re.S)
seen = set()

def patch_card(match):
    card = match.group(0)
    nm = re.search(r"<h3>(.*?)</h3>", card, re.S)
    if not nm:
        return card
    name = html.unescape(re.sub(r"<[^>]+>", "", nm.group(1))).strip()
    slug = MAPPING.get(name)
    if not slug:
        return card
    seen.add(slug)
    mark = re.search(r'<span class="person-mark">.*?</span>', card, re.S)
    mark_html = mark.group(0) if mark else ""
    img = (
        f'<img class="person-photo" src="assets/people/{slug}.webp" '
        f'alt="{html.escape(name, quote=True)}" loading="lazy" decoding="async" '
        f'width="480" height="600">'
    )
    portrait = f'<span class="portrait">{mark_html}{img}</span>'
    new, n = re.subn(
        r'<span class="portrait">.*?</span>(?=<span class="person-copy">)',
        portrait,
        card,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise RuntimeError(f"Could not patch portrait block for {name}")
    return new

out = card_re.sub(patch_card, text)
assert seen == TARGET, sorted(TARGET - seen)
assert not re.findall(r'<img class="person-photo"[^>]+src="https?://', out)
assert len(re.findall(r'<img class="person-photo"[^>]+src="assets/people/', out)) == 44
HTML.write_text(out, encoding="utf-8")

# Replace the old circular thumbnails with restrained 4:5 portrait cards.
s = CSS.read_text(encoding="utf-8")ns = re.sub(
    r'\.person-card\{padding:1rem 0;border-bottom:1px solid var\(--line\);display:grid;grid-template-columns:[^;]+;',
    '.person-card{padding:1rem 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:68px 1fr auto;',
    s,
)
s = re.sub(
    r'\.person-mark\{width:\d+px;height:\d+px;border-radius:[^;]+;',
    '.person-mark{width:56px;height:70px;border-radius:10px;',
    s,
)
s = re.sub(
    r'\.portrait\{width:\d+px;height:\d+px;position:relative;display:block(?:;overflow:hidden;border-radius:[^}]+)?\}',
    '.portrait{width:56px;height:70px;position:relative;display:block;overflow:hidden;border-radius:10px}',
    s,
)
s = re.sub(
    r'\.person-photo\{position:absolute;inset:0;width:\d+px;height:\d+px;border-radius:[^;]+;object-fit:cover;object-position:[^;]+;',
    '.person-photo{position:absolute;inset:0;width:56px;height:70px;border-radius:10px;object-fit:cover;object-position:center center;',
    s,
)
s = re.sub(
    r'\.compact-list \.person-card\{grid-template-columns:[^}]+\}\.compact-list \.person-mark\{[^}]+\}',
    '.compact-list .person-card{grid-template-columns:52px 1fr}.compact-list .portrait,.compact-list .person-photo,.compact-list .person-mark{width:48px;height:60px;border-radius:9px}',
    s,
)
CSS.write_text(s, encoding="utf-8")

print("Verified and linked 44 local 480x600 WebP portraits; CSS updated to 4:5 thumbnails.")
