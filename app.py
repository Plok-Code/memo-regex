"""Mémo Regex - Page de référence simple."""

import streamlit as st

st.set_page_config(page_title="Mémo Regex", page_icon="📖", layout="wide")

# CSS minimal
st.markdown("""
<style>
body { background: #0d1117; }
.block-container { max-width: 1100px; padding: 2rem 1rem; }
h1 { font-size: 1.8rem; margin-bottom: 0.5rem; }
.subtitle { color: #8b949e; margin-bottom: 1.5rem; }
.tag { 
    display: inline-block; 
    padding: 0.2rem 0.6rem; 
    margin: 0 0.3rem 0.3rem 0;
    background: #21262d; 
    border-radius: 12px; 
    font-size: 0.8rem; 
    color: #58a6ff;
}
.grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); 
    gap: 1rem; 
    margin-top: 1.5rem;
}
.card { 
    background: #161b22; 
    border: 1px solid #30363d; 
    border-radius: 8px; 
    padding: 1.25rem;
}
.card h3 { 
    margin: 0 0 0.5rem 0; 
    font-size: 1rem; 
    color: #f0883e; 
}
.card p { 
    margin: 0 0 0.75rem 0; 
    color: #8b949e; 
    font-size: 0.9rem;
}
table { 
    width: 100%; 
    border-collapse: collapse; 
    font-size: 0.85rem;
}
th { 
    text-align: left; 
    color: #8b949e; 
    font-weight: 500;
    border-bottom: 1px solid #30363d;
    padding: 0.4rem 0.2rem;
}
td { 
    padding: 0.4rem 0.2rem;
    border-bottom: 1px solid #21262d;
}
tr:last-child td { border-bottom: none; }
code { 
    font-family: SFMono-Regular, Consolas, monospace;
    background: #21262d;
    padding: 0.15rem 0.3rem;
    border-radius: 4px;
    color: #58a6ff;
    font-size: 0.85em;
}
.tip {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 1rem;
    margin-top: 1.5rem;
}
.tip strong { color: #3fb950; }
.footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #30363d;
    color: #8b949e;
    font-size: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 📖 Mémo Regex")
st.markdown('<p class="subtitle">Référence rapide pour les expressions régulières</p>', unsafe_allow_html=True)

# Tags
TAGS = ["Jokers", "Quantificateurs", "Classes", "Groupes", "Python"]
tags_html = "".join(f'<span class="tag">{t}</span>' for t in TAGS)
st.markdown(f'<div>{tags_html}</div>', unsafe_allow_html=True)

# Cartes
CARDS = [
    ("Jokers & Ancres", "Position et caractères.", [
        (".", "N'importe quel caractère", "a.c → abc, a1c"),
        ("^", "Début de ligne", "^hello → début"),
        ("$", "Fin de ligne", "world$ → fin"),
        ("|", "OU logique", "cat|dog"),
        ("\\", "Échappement", "\\. → point littéral"),
    ]),
    ("Quantificateurs", "S'appliquent au caractère précédent.", [
        ("?", "0 ou 1 fois", "colou?r → color, colour"),
        ("*", "0 ou plusieurs", "ab*c → ac, abc, abbc"),
        ("+", "1 ou plusieurs", "ab+c → abc, abbc"),
        ("{n}", "Exactement n", "a{3} → aaa"),
        ("{n,}", "Au moins n", r"\d{2,} → 12, 123"),
        ("{n,m}", "Entre n et m", r"\d{2,4} → 12 à 1234"),
    ]),
    ("Classes de caractères", "Raccourcis utiles. Majuscule = inverse.", [
        (r"\d", "Chiffre (0-9)", r"\D → pas un chiffre"),
        (r"\w", "Mot (lettre, chiffre, _)", r"\W → pas un mot"),
        (r"\s", "Espace blanc", r"\S → pas un espace"),
    ]),
    ("Groupes & Captures", "Isoler des parties du texte.", [
        ("(...)", "Groupe capturant", r"(\w+)@(\w+)"),
        ("(?:...)", "Non-capturant", "(?:https?)://"),
        ("(?P<name>...)", "Nommé (Python)", r"(?P<id>\d+)"),
    ]),
]

html_cards = ""
for title, desc, rows in CARDS:
    rows_html = "".join(
        f"<tr><td><code>{pat}</code></td><td>{desc}</td><td>{ex}</td></tr>"
        for pat, desc, ex in rows
    )
    html_cards += f"""
    <div class="card">
        <h3>{title}</h3>
        <p>{desc}</p>
        <table>
            <thead><tr><th>Symbole</th><th>Description</th><th>Exemple</th></tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
    """

st.markdown(f'<div class="grid">{html_cards}</div>', unsafe_allow_html=True)

# Tip
st.markdown("""
<div class="tip">
    <strong>💡 Greedy vs Lazy</strong><br>
    Par défaut, <code>.*</code> prend le maximum possible. Pour prendre le minimum, ajoute <code>?</code> : <code>.*?</code>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Mémo Regex — Un projet simple et utile</div>', unsafe_allow_html=True)
