# Mémo Regex

Référence rapide pour les expressions régulières, en français.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.42+-red.svg)

## Démarrage

```bash
# Installation
pip install -r requirements.txt

# Lancement
streamlit run app.py
```

## Structure

```
.
├── app.py              # Application principale
├── requirements.txt    # Dépendances
├── styles/
│   └── main.css       # Styles CSS
├── components/
│   ├── card.py        # Composant carte
│   ├── header.py      # Composant header
│   ├── tip.py         # Composant astuce
│   └── footer.py      # Composant footer
└── data/
    └── cheatsheet.py  # Données du mémo
```

## Contenu

- **Jokers & Ancres** — `.` `^` `$` `|` `\`
- **Quantificateurs** — `?` `*` `+` `{n}` `{n,}` `{n,m}`
- **Classes** — `\d` `\w` `\s` et leurs inverses
- **Frontières** — `\b` `\B`
- **Groupes** — `(...)` `(?:...)` `(?P<name>...)`
- **Python** — `\A` `\Z` vs `^` `$`

## Personnalisation

Modifiez `data/cheatsheet.py` pour ajouter ou modifier du contenu.

## Licence

MIT
