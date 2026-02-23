import html
import base64
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Memo Regex Python",
    page_icon=".*",
    layout="wide",
)


FUNCTION_ROWS = [
    (
        "search",
        "Trouve la premiere occurrence.",
        'A) re.search(r"\\d{4}", "Pinot 2016 puis 2020").group()',
        "A) '2016'",
    ),
    (
        "findall",
        "Renvoie toutes les occurrences dans une liste.",
        'A) re.findall(r"\\d{4}", "Pinot 2016 puis 2020")',
        "A) ['2016', '2020']",
    ),
    (
        "split",
        "Decoupe le texte selon un separateur regex.",
        'A) re.split(r"\\d{4}", "Pinot 2016 puis 2020 final")',
        "A) ['Pinot ', ' puis ', ' final']",
    ),
    (
        "sub",
        "Remplace les occurrences d'un motif.",
        'A) re.sub(r"\\d{4}", "YYYY", "Pinot 2016 puis 2020")',
        "A) 'Pinot YYYY puis YYYY'",
    ),
    (
        "fullmatch",
        "Valide toute la chaine: la regex doit correspondre a 100% du texte.",
        'A) re.fullmatch(r"\\d{4}", "2026") is not None\nB) re.fullmatch(r"\\d{4}", "vin 2026") is not None',
        "A) True\nB) False",
    ),
]


CORE_REGEX_ROWS = [
    (
        ".",
        "N'importe quel caractere (sauf saut de ligne).",
        'A) re.findall(r"c.t", "cat cut c9t")\nB) re.findall(r"a.a", "aba aca xaa aax")',
        "A) ['cat', 'cut', 'c9t']\nB) ['aba', 'aca']",
    ),
    (
        "?",
        "Le ? s'applique a l'element juste avant: 0 ou 1 occurrence.",
        'A) re.findall(r"colou?r", "color colour")\nB) re.findall(r"ab?c", "ac abc abbc")',
        "A) ['color', 'colour']\nB) ['ac', 'abc']",
    ),
    (
        "*",
        "Le * s'applique a l'element juste avant: 0 ou plusieurs occurrences.",
        'A) re.findall(r"en*", "e en enn")\nB) re.findall(r"ab*c", "ac abc abbc abdc")',
        "A) ['e', 'en', 'enn']\nB) ['ac', 'abc', 'abbc']",
    ),
    (
        "+",
        "Le + s'applique a l'element juste avant: 1 ou plusieurs occurrences.",
        'A) re.findall(r"en+", "e en enn")\nB) re.findall(r"ab+c", "ac abc abbc abdc")',
        "A) ['en', 'enn']\nB) ['abc', 'abbc']",
    ),
    (
        "{n}",
        "Le {n} s'applique a l'element juste avant: exactement n occurrences.",
        'A) re.findall(r"en{2}", "en enn ennn")\nB) re.findall(r"ab{2}c", "abc abbc abbbc")',
        "A) ['enn']\nB) ['abbc']",
    ),
    (
        "{n,m}",
        "Le {n,m} s'applique a l'element juste avant: entre n et m occurrences.",
        'A) re.findall(r"ab{2,4}c", "abc abbc abbbc abbbbc abbbbbc")\nB) re.findall(r"a{2,3}", "a aa aaa aaaa")',
        "A) ['abbc', 'abbbc', 'abbbbc']\nB) ['aa', 'aaa', 'aaa']",
    ),
    (
        "|",
        "OU logique entre motifs.",
        'A) re.findall(r"crew|team", "crew and team")\nB) re.findall(r"chat|chien", "chat oiseau chien")',
        "A) ['crew', 'team']\nB) ['chat', 'chien']",
    ),
    (
        "()",
        "Groupe capturant (utile pour appliquer un quantificateur a tout un bloc).",
        'A) re.findall(r"([a-z]+) (\\d+)", "pinot 2016")\nB) re.findall(r"([A-Z][a-z]+)-(\\d+)", "Lot-42 lot-99 Bloc-7 Bloc-AB")',
        "A) [('pinot', '2016')]\nB) [('Lot', '42'), ('Bloc', '7')]",
    ),
    (
        "\\",
        "Echappe un caractere special.",
        'A) re.findall(r"\\.", "a.b c.d")\nB) re.findall(r"\\?", "ok? non oui! peut-etre?")',
        "A) ['.', '.']\nB) ['?', '?']",
    ),
]


PYTHON_REGEX_ROWS = [
    (
        r"\d",
        "Un chiffre.",
        'A) re.findall(r"\\d", "A1B2")\nB) re.findall(r"\\d+", "B12 007 code 9x")',
        "A) ['1', '2']\nB) ['12', '007', '9']",
    ),
    (
        r"\w",
        "Caractere alphanumerique + underscore.",
        'A) re.findall(r"\\w+", "mot_1 !")\nB) re.findall(r"\\w+", "mot_1 ! bon-jour")',
        "A) ['mot_1']\nB) ['mot_1', 'bon', 'jour']",
    ),
    (
        r"\s",
        "Espace, tabulation, saut de ligne.",
        'A) re.findall(r"\\s", "a b\\tc")\nB) re.findall(r"\\s+", "a   b\\tc\\nd")',
        "A) [' ', '\\t']\nB) ['   ', '\\t', '\\n']",
    ),
    (
        "[a-z]",
        "Plage de caracteres.",
        'A) re.findall(r"[a-z]", "A1b2")\nB) re.findall(r"[a-z]+", "ABC test xyz")',
        "A) ['b']\nB) ['test', 'xyz']",
    ),
    (
        "[^0-9]",
        "Tout sauf un chiffre.",
        'A) re.findall(r"[^0-9]", "A1B2")\nB) re.findall(r"[^0-9]", "7ab-9")',
        "A) ['A', 'B']\nB) ['a', 'b', '-']",
    ),
    (
        "^",
        "Debut de texte (ou debut de ligne avec MULTILINE).",
        'A) re.findall(r"^The", "The moon")\nB) re.findall(r"^abc", "xyz\\nabc", re.MULTILINE)',
        "A) ['The']\nB) ['abc']",
    ),
    (
        "$",
        "Fin de texte (ou fin de ligne avec MULTILINE).",
        'A) re.findall(r"Moon\\.$", "Go to Moon.")\nB) re.findall(r"end$", "start\\nend", re.MULTILINE)',
        "A) ['Moon.']\nB) ['end']",
    ),
    (
        r"\A",
        "Debut strict du texte.",
        'A) re.findall(r"\\AThe", "The\\nThe")\nB) re.findall(r"\\Aabc", "zabc")',
        "A) ['The']\nB) []",
    ),
    (
        r"\Z",
        "Fin stricte du texte.",
        'A) re.findall(r"Moon\\.\\Z", "to Moon.")\nB) re.findall(r"abc\\Z", "abc\\nxyz")',
        "A) ['Moon.']\nB) []",
    ),
    (
        r"\b",
        "Frontiere de mot.",
        'A) re.findall(r"\\bchat\\b", "chat chaton")\nB) re.findall(r"\\bcat\\b", "cat scatter catfish cat")',
        "A) ['chat']\nB) ['cat', 'cat']",
    ),
    (
        r"\B",
        "Pas une frontiere de mot.",
        'A) re.findall(r"\\Best", "rester est")\nB) re.findall(r"\\Ban\\B", "banane an ancre")',
        "A) ['est']\nB) ['an']",
    ),
]


def build_table(headers: list[str], rows: list[tuple[str, str, str, str]]) -> str:
    head = "".join(
        f"<th class='h{idx + 1}'>{html.escape(col, quote=False)}</th>"
        for idx, col in enumerate(headers)
    )
    body_chunks = []

    for row in rows:
        cells = []
        for idx, value in enumerate(row):
            safe_value = html.escape(value, quote=False)
            label = html.escape(headers[idx], quote=True)

            if idx == 0:
                content = f"<code class='token'>{safe_value}</code>"
            elif idx in (2, 3):
                lines = [chunk.strip() for chunk in value.split("\n") if chunk.strip()]
                content = "".join(
                    f"<div class='code-line'><code>{html.escape(chunk, quote=False)}</code></div>"
                    for chunk in lines
                )
            else:
                content = safe_value

            cells.append(f"<td class='c{idx + 1}' data-label=\"{label}\">{content}</td>")

        body_chunks.append("<tr>" + "".join(cells) + "</tr>")

    return (
        "<table class='lookup-table'>"
        "<colgroup>"
        "<col class='col1'>"
        "<col class='col2'>"
        "<col class='col3'>"
        "<col class='col4'>"
        "</colgroup>"
        f"<thead><tr>{head}</tr></thead>"
        f"<tbody>{''.join(body_chunks)}</tbody>"
        "</table>"
    )


def build_card(title: str, subtitle: str, rows: list[tuple[str, str, str, str]]) -> str:
    headers = ["Element", "Role", "Exemple", "Resultat"]
    return (
        "<article class='card'>"
        f"<h3>{html.escape(title, quote=False)}</h3>"
        f"<p>{html.escape(subtitle, quote=False)}</p>"
        f"{build_table(headers, rows)}"
        "</article>"
    )


def image_data_uri(path: str) -> str:
    try:
        data = Path(path).read_bytes()
    except OSError:
        return ""
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{encoded}"


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root {
  --bg: #f3f7ff;
  --ink: #0f172a;
  --muted: #334155;
  --card: #ffffff;
  --line: #d7e2f0;
  --primary: #2155d6;
  --primary-soft: #e9f0ff;
  --code-bg: #eef3ff;
  --code-ink: #193a9d;
  --token-bg: #10213f;
  --token-ink: #f8fbff;
  --hero-a: #0d1c3d;
  --hero-b: #17397a;
  --hero-ink: #f2f6ff;
}

html, body, [class*="css"] {
  color: var(--ink);
  font-family: "Sora", "Segoe UI", sans-serif;
}

.stApp {
  background:
    radial-gradient(1000px 520px at 95% -10%, #dbe8ff 0%, transparent 58%),
    radial-gradient(900px 520px at -10% 10%, #e7f1ff 0%, transparent 60%),
    var(--bg);
}

.block-container {
  max-width: 1180px;
  padding-top: 1.6rem;
  padding-bottom: 2.6rem;
}

.hero,
.syntax-card,
.card,
.callout {
  animation: rise 0.45s ease both;
}

@keyframes rise {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero {
  border: 1px solid #1d3f7d;
  border-radius: 18px;
  background: linear-gradient(145deg, var(--hero-a), var(--hero-b));
  box-shadow: 0 16px 34px rgba(16, 33, 63, 0.28);
  padding: 1.35rem 1.4rem;
  margin-bottom: 1rem;
}

.hero .eyebrow {
  display: inline-block;
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #dce9ff;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  padding: 0.24rem 0.62rem;
  margin-bottom: 0.7rem;
}

.hero h1 {
  margin: 0;
  color: var(--hero-ink);
  font-size: clamp(1.35rem, 3.2vw, 2.35rem);
  line-height: 1.2;
  letter-spacing: 0.5px;
}

.hero p {
  margin: 0.6rem 0 0;
  color: #d9e7ff;
  font-size: 1rem;
  line-height: 1.56;
}

.syntax-card {
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 8px 20px rgba(13, 28, 61, 0.08);
  padding: 1rem 1rem 0.9rem;
  margin-bottom: 1rem;
}

.syntax-card h2 {
  margin: 0 0 0.5rem;
  color: #0d1c3d;
  font-size: 1.05rem;
}

.syntax-card p {
  margin: 0.45rem 0;
  color: var(--muted);
  line-height: 1.6;
  font-size: 0.94rem;
}

.syntax-card pre {
  margin: 0.45rem 0 0.6rem;
}

.syntax-card pre code {
  display: block;
  font-family: "IBM Plex Mono", Consolas, monospace;
  background: #0f1f3d;
  color: #edf4ff;
  border: 1px solid #314c7d;
  border-radius: 10px;
  font-size: 0.88rem;
  line-height: 1.5;
  padding: 0.72rem 0.82rem;
}

.syntax-grid {
  display: grid;
  gap: 0.6rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.syntax-tip {
  border: 1px solid #d9e5ff;
  border-radius: 10px;
  background: #f7faff;
  padding: 0.58rem 0.65rem;
}

.syntax-tip h4 {
  margin: 0 0 0.28rem;
  color: #123066;
  font-size: 0.84rem;
}

.syntax-tip p {
  margin: 0;
  color: #334155;
  font-size: 0.84rem;
  line-height: 1.46;
}

.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.9rem;
}

.card {
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 7px 18px rgba(13, 28, 61, 0.08);
  padding: 0.9rem;
}

.card h3 {
  margin: 0;
  color: #0e2b5c;
  font-size: 0.99rem;
  font-weight: 800;
  letter-spacing: 0.3px;
}

.card p {
  margin: 0.5rem 0 0.75rem;
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.56;
}

.visual-guide .step-list {
  margin: 0.25rem 0 0.75rem 1.2rem;
  padding: 0;
  color: #20334f;
  line-height: 1.6;
  font-size: 0.9rem;
}

.visual-guide .step-list li {
  margin-bottom: 0.28rem;
}

.visual-guide .step-list a {
  color: #1642b3;
  font-weight: 700;
  text-decoration: none;
}

.visual-guide .step-list a:hover {
  text-decoration: underline;
}

.visual-guide .guide-image {
  width: 100%;
  border-radius: 10px;
  border: 1px solid #d5e2f3;
  box-shadow: 0 4px 12px rgba(13, 28, 61, 0.08);
}

.visual-guide .guide-link {
  margin: 0.72rem 0 0.1rem;
  color: #26384f;
  font-size: 0.9rem;
}

.visual-guide .guide-link a {
  color: #1642b3;
  font-weight: 700;
  text-decoration: none;
}

.visual-guide .guide-link a:hover {
  text-decoration: underline;
}

.lookup-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.92rem;
  table-layout: fixed;
}

.lookup-table th,
.lookup-table td {
  border-bottom: 1px solid #dbe5f2;
  text-align: left;
  vertical-align: top;
  padding: 0.52rem 0.3rem;
  color: #152238;
  overflow-wrap: break-word;
  word-break: normal;
}

.lookup-table th {
  background: var(--primary-soft);
  color: #1b356a;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.7px;
  font-weight: 700;
}

.lookup-table tr:last-child td {
  border-bottom: none;
}

.lookup-table .col1 {
  width: 96px;
}

.lookup-table .col2 {
  width: 24%;
}

.lookup-table .col3 {
  width: 44%;
}

.lookup-table .col4 {
  width: 24%;
}

.lookup-table td.c1 {
  width: 86px;
}

.lookup-table code {
  font-family: "IBM Plex Mono", Consolas, monospace;
  border-radius: 7px;
  border: 1px solid #d5e1ff;
  background: var(--code-bg);
  color: var(--code-ink);
  font-size: 0.82rem;
  padding: 0.1rem 0.32rem;
}

.lookup-table .code-line + .code-line {
  margin-top: 0.2rem;
}

.lookup-table td.c3 code,
.lookup-table td.c4 code {
  display: inline-block;
  line-height: 1.5;
}

.lookup-table .token {
  border: 1px solid #182f58;
  background: var(--token-bg);
  color: var(--token-ink);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.08rem 0.3rem;
}

.callout {
  margin-top: 0.9rem;
  border: 1px solid #f0cf62;
  border-radius: 12px;
  background: #fff8dd;
  color: #3f3200;
  padding: 0.8rem 0.95rem;
  font-size: 0.9rem;
  line-height: 1.55;
}

.callout code {
  font-family: "IBM Plex Mono", Consolas, monospace;
  border-radius: 7px;
  border: 1px solid #e7d59e;
  background: #fff2c1;
  color: #4a3900;
  font-size: 0.82rem;
  padding: 0.1rem 0.3rem;
}

.footer {
  margin-top: 1rem;
  padding-top: 0.7rem;
  border-top: 1px solid var(--line);
  color: #44556f;
  font-size: 0.86rem;
  text-align: center;
}

@media (max-width: 900px) {
  .lookup-table .col2 { width: 26%; }
  .lookup-table .col3 { width: 42%; }
  .lookup-table .col4 { width: 24%; }
}

@media (max-width: 760px) {
  .lookup-table,
  .lookup-table tbody,
  .lookup-table tr,
  .lookup-table td {
    display: block;
    width: 100%;
  }

  .lookup-table thead {
    display: none;
  }

  .lookup-table tr {
    border: 1px solid #d6e2f3;
    border-radius: 10px;
    background: #f8fbff;
    padding: 0.5rem 0.65rem;
    margin-bottom: 0.58rem;
  }

  .lookup-table td {
    border: 0;
    padding: 0.2rem 0;
  }

  .lookup-table td::before {
    content: attr(data-label);
    display: block;
    color: #2f456e;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.7px;
    text-transform: uppercase;
    margin-bottom: 0.1rem;
  }

  .lookup-table td:first-child {
    width: 100%;
  }

  .lookup-table .token {
    font-size: 0.76rem;
  }
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<section class="hero">
  <h1>Memo Regex pour Python</h1>
  <p>Une regex est un motif de caracteres qui permet de rechercher, extraire, valider ou remplacer du texte dans Python.</p>
</section>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<section class="syntax-card">
  <h2>Comment ecrire une regex en Python</h2>
  <pre><code>import re
resultat = re.nom_de_fonction(r"formule_regex", texte_a_traiter)</code></pre>
  <div class="syntax-grid">
    <div class="syntax-tip">
      <h4>re.nom_de_fonction(...)</h4>
      <p>Choisis la fonction selon le besoin: <code>search</code>, <code>findall</code>, <code>split</code>, <code>sub</code>.</p>
    </div>
    <div class="syntax-tip">
      <h4>r"..." (raw string)</h4>
      <p>Le <code>r</code> evite de doubler les antislashs. Exemple recommande: <code>r"\\d+"</code>.</p>
    </div>
    <div class="syntax-tip">
      <h4>Sans r</h4>
      <p>Tu dois souvent ecrire plus lourd: <code>"\\\\d+"</code>. Donc garde <code>r"..."</code> par defaut.</p>
    </div>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

guide_uri = image_data_uri("image.png")

if guide_uri:
    guide_block = (
        "<article class='card visual-guide'>"
        "<h3>Comment tester une regex en 4 etapes</h3>"
        "<ol class='step-list'>"
        "<li>Va sur <a href='https://regex101.com/' target='_blank' rel='noopener noreferrer'>regex101.com</a>.</li>"
        "<li>Selectionne Python. (zone 1)</li>"
        "<li>Ecris ton texte d'exemple a analyser. (zone 2)</li>"
        "<li>Ecris ta regex puis verifie les zones qui matchent. (zone 3)</li>"
        "<li>Ajuste la regex jusqu'au resultat attendu.</li>"
        "</ol>"
        f"<img class='guide-image' src='{guide_uri}' alt='Etapes de test regex' />"
        "</article>"
    )
else:
    guide_block = (
        "<article class='card visual-guide'>"
        "<h3>Comment tester une regex en 4 etapes</h3>"
        "<ol class='step-list'>"
        "<li>Va sur <a href='https://regex101.com/' target='_blank' rel='noopener noreferrer'>regex101.com</a>.</li>"
        "<li>Ecris ton texte d'exemple a analyser.</li>"
        "<li>Ecris ta regex puis verifie les zones qui matchent.</li>"
        "<li>Ajuste la regex jusqu'au resultat attendu.</li>"
        "</ol>"
        "<p class='guide-link'>Image manquante: ajoute <code>image.png</code> a la racine du projet.</p>"
        "<p class='guide-link'>Pour tester tes regex: "
        "<a href='https://regex101.com/' target='_blank' rel='noopener noreferrer'>https://regex101.com/</a>"
        "</p>"
        "</article>"
    )

cards_html = "".join(
    [
        build_card(
            "Fonctions re: quelle fonction utiliser?",
            "Toutes les lignes utilisent le meme regex r\"\\d{4}\" pour se concentrer uniquement sur le role de chaque fonction.",
            FUNCTION_ROWS,
        ),
        guide_block,
        build_card(
            "Regex essentielles: syntaxe de base",
            "Chaque formule a 2 exemples (A/B) pour comparer rapidement les cas d'usage.",
            CORE_REGEX_ROWS,
        ),
        build_card(
            "Regex Python specifiques",
            "Raccourcis et ancres Python avec 2 exemples par ligne pour mieux visualiser le comportement.",
            PYTHON_REGEX_ROWS,
        ),
    ]
)

st.markdown("<section class='grid'>" + cards_html + "</section>", unsafe_allow_html=True)

st.markdown(
    """
<div class="callout">
  <b>Greedy vs lazy:</b> <code>r"\"(.+)\""</code> prend le plus long match,
  <code>r"\"(.+?)\""</code> s'arrete au premier match.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="footer">
Memo optimise pour l'apprentissage des regex dans le module Python <code>re</code>.
</div>
""",
    unsafe_allow_html=True,
)
