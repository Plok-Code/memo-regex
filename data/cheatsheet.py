"""Données du mémo Regex."""

SECTIONS = [
    {
        "title": "Jokers & Ancres",
        "description": "Définir la position ou remplacer un caractère.",
        "headers": ["Symbole", "Signification", "Exemple"],
        "rows": [
            [".", "N'importe quel caractère", "c.t → cat, cut"],
            ["^", "Début de ligne", "^The → début"],
            ["$", "Fin de ligne", "end$ → fin"],
            ["|", "OU logique", "cat|dog → l'un ou l'autre"],
            ["\\", "Échappement", "\\. → un vrai point"],
        ],
    },
    {
        "title": "Quantificateurs",
        "description": "S'appliquent au caractère ou groupe précédent.",
        "headers": ["Symbole", "Signification", "Exemple"],
        "rows": [
            ["?", "0 ou 1 fois", "colou?r → color, colour"],
            ["*", "0 ou plusieurs", "ab*c → ac, abc, abbc"],
            ["+", "1 ou plusieurs", "ab+c → abc, abbc"],
            ["{n}", "Exactement n", "a{3} → aaa"],
            ["{n,}", "Au moins n", "\\d{2,} → 12, 123"],
            ["{n,m}", "Entre n et m", "\\d{2,4} → 12 à 1234"],
        ],
    },
    {
        "title": "Classes de caractères",
        "description": "Raccourcis. La majuscule = l'inverse.",
        "headers": ["Raccourci", "Signification", "Inverse"],
        "rows": [
            ["\\d", "Chiffre (0-9)", "\\D → tout sauf chiffre"],
            ["\\w", "Mot (a-z, A-Z, 0-9, _)", "\\W → tout sauf mot"],
            ["\\s", "Espace (espace, tab, nl)", "\\S → tout sauf espace"],
        ],
        "extra": "Crochets: [abc], [a-z], [^0-9] (négation)",
    },
    {
        "title": "Frontières",
        "description": "Délimiter un mot.",
        "headers": ["Symbole", "Signification", "Exemple"],
        "rows": [
            ["\\b", "Frontière de mot", "\\bcat → cat au début"],
            ["\\B", "Pas une frontière", "\\Bcat → cat au milieu"],
        ],
    },
    {
        "title": "Groupes & Captures",
        "description": "Isoler et réutiliser des morceaux.",
        "headers": ["Syntaxe", "Rôle", "Exemple"],
        "rows": [
            ["(...)", "Groupe capturant", "(\\w+) (\\d+)"],
            ["(?:...)", "Non-capturant", "(?:http|https)"],
            ["(?P<name>...)", "Groupe nommé", "(?P<id>\\d+)"],
        ],
    },
    {
        "title": "Python: début/fin",
        "description": "Différences importantes.",
        "headers": ["Symbole", "Comportement"],
        "rows": [
            ["^ / $", "Dépend de re.MULTILINE"],
            ["\\A", "Toujours début du texte"],
            ["\\Z", "Toujours fin du texte"],
        ],
    },
]

TIP = {
    "title": "Greedy vs Lazy",
    "content": """Par défaut, les regex sont gourmandes. <code>(.+)</code> sur <code>"a" et "b"</code> capture <code>"a" et "b"</code> entier.
Rendre paresseux: <code>*?</code>, <code>+?</code> ou <code>.+?</code> pour s'arrêter à la première correspondance.""",
}

TAGS = ["Jokers", "Quantificateurs", "Classes", "Frontières", "Groupes", "Python re"]
