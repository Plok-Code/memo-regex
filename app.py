import streamlit as st


st.set_page_config(
    page_title="Mémo Regex",
    page_icon="📖",
    layout="wide",
)

st.markdown(
    """
<style>
:root {
  --bg: #0d1117;
  --bg-card: #161b22;
  --border: #30363d;
  --text: #c9d1d9;
  --text-muted: #8b949e;
  --accent: #58a6ff;
  --accent-2: #f0883e;
  --green: #3fb950;
}

html, body, [class*="css"] {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--text);
}

body {
  background: var(--bg);
}

.block-container {
  max-width: 1200px;
  padding: 2rem 1rem;
}

/* Header */
.hero {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 1.5rem;
}

.hero h1 {
  margin: 0 0 0.5rem 0;
  font-size: 1.8rem;
  font-weight: 600;
}

.hero p {
  margin: 0 0 1rem 0;
  color: var(--text-muted);
}

.pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.pill {
  background: rgba(88, 166, 255, 0.1);
  border: 1px solid rgba(88, 166, 255, 0.3);
  color: var(--accent);
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

/* Cards */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1.25rem;
}

.card h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1rem;
  color: var(--accent-2);
}

.card p {
  margin: 0 0 0.75rem 0;
  color: var(--text-muted);
  font-size: 0.9rem;
}

/* Tables */
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.table th, .table td {
  text-align: left;
  padding: 0.5rem 0.25rem;
  border-bottom: 1px solid var(--border);
}

.table th {
  color: var(--text-muted);
  font-weight: 500;
}

.table tr:last-child td {
  border-bottom: none;
}

code {
  font-family: SFMono-Regular, Consolas, monospace;
  background: #21262d;
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  font-size: 0.85em;
  color: var(--accent);
}

.tag {
  background: rgba(240, 136, 62, 0.15);
  color: #ffab70;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

/* Callout */
.callout {
  background: rgba(63, 185, 80, 0.1);
  border: 1px solid rgba(63, 185, 80, 0.3);
  border-radius: 10px;
  padding: 1.25rem;
  margin-top: 1.5rem;
}

.callout strong {
  color: var(--green);
}

/* Footer */
.footer {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 0.85rem;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<section class="hero">
  <h1>📖 Mémo Regex</h1>
  <p>Guide visuel et concis pour les expressions régulières.</p>
  <div class="pill-row">
    <span class="pill">Jokers & ancres</span>
    <span class="pill">Quantificateurs</span>
    <span class="pill">Classes</span>
    <span class="pill">Frontières</span>
    <span class="pill">Groupes</span>
    <span class="pill">Python re</span>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="grid">
  <div class="card">
    <h3>1. Les Bases : Jokers & Ancres</h3>
    <p>Définir la position ou remplacer un caractère.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>.</code></td><td>N'importe quel caractère</td><td><code>c.t</code> → cat, cut, c9t</td></tr>
        <tr><td><code>^</code></td><td>Début de ligne/texte</td><td><code>^The</code> → The (début)</td></tr>
        <tr><td><code>$</code></td><td>Fin de ligne/texte</td><td><code>end$</code> → end (fin)</td></tr>
        <tr><td><code>|</code></td><td>OU logique</td><td><code>cat|dog</code> → l'un ou l'autre</td></tr>
        <tr><td><code>\\</code></td><td>Échappe un caractère</td><td><code>\\.</code> → un vrai point</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>2. Les Quantificateurs</h3>
    <p>S'appliquent au caractère ou groupe précédent.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>?</code></td><td>0 ou 1 fois</td><td><code>colou?r</code> → color, colour</td></tr>
        <tr><td><code>*</code></td><td>0 ou plusieurs</td><td><code>ab*c</code> → ac, abc, abbc</td></tr>
        <tr><td><code>+</code></td><td>1 ou plusieurs</td><td><code>ab+c</code> → abc, abbc</td></tr>
        <tr><td><code>{n}</code></td><td>Exactement n fois</td><td><code>a{3}</code> → aaa</td></tr>
        <tr><td><code>{n,}</code></td><td>Au moins n fois</td><td><code>\\d{3,}</code> → 123, 4567</td></tr>
        <tr><td><code>{n,m}</code></td><td>Entre n et m fois</td><td><code>\\d{2,4}</code> → 12 à 1234</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>3. Les Classes de Caractères</h3>
    <p>Raccourcis utiles. La majuscule est l'inverse.</p>
    <table class="table">
      <thead>
        <tr><th>Raccourci</th><th>Signification</th><th>Inverse</th></tr>
      </thead>
      <tbody>
        <tr><td><code>\\d</code></td><td>Chiffre (0-9)</td><td><code>\\D</code> → tout sauf chiffre</td></tr>
        <tr><td><code>\\w</code></td><td>Caractère de mot</td><td><code>\\W</code> → tout sauf mot</td></tr>
        <tr><td><code>\\s</code></td><td>Espaces (tab, nl)</td><td><code>\\S</code> → tout sauf espace</td></tr>
      </tbody>
    </table>
    <p><span class="tag">Crochets</span> <code>[abc]</code>, <code>[a-z]</code>, <code>[^0-9]</code></p>
  </div>

  <div class="card">
    <h3>4. Frontières de Mots</h3>
    <p>Délimiter un mot par ses frontières invisibles.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>\\b</code></td><td>Frontière de mot</td><td><code>\\bcat</code> → cat au début</td></tr>
        <tr><td><code>\\B</code></td><td>Pas une frontière</td><td><code>\\Bcat</code> → cat au milieu</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>5. Groupes & Captures</h3>
    <p>Isoler et réutiliser des morceaux du texte.</p>
    <table class="table">
      <thead>
        <tr><th>Syntaxe</th><th>Rôle</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>(...)</code></td><td>Groupe capturant</td><td><code>([a-z]+) (\\d+)</code></td></tr>
        <tr><td><code>(?:...)</code></td><td>Non-capturant</td><td><code>(?:crew|team)</code></td></tr>
        <tr><td><code>(?P&lt;nom&gt;)</code></td><td>Groupe nommé</td><td><code>(?P&lt;word&gt;[a-z]+)</code></td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>6. Spécificités Python</h3>
    <p>Différence entre début/fin de ligne et texte complet.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Comportement</th></tr>
      </thead>
      <tbody>
        <tr><td><code>^</code> / <code>$</code></td><td>Dépend de <code>re.MULTILINE</code></td></tr>
        <tr><td><code>\\A</code></td><td>Toujours début du texte</td></tr>
        <tr><td><code>\\Z</code></td><td>Toujours fin du texte</td></tr>
      </tbody>
    </table>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="callout">
  <strong>💡 Greedy vs Lazy</strong><br/>
  Par défaut, les regex avalent le plus de texte possible. Exemple : <code>"(.+)"</code> sur
  <code>"Texte 1" et "Texte 2"</code> capture tout entre le premier et dernier guillemet.<br/>
  <strong>Solution</strong> : rendre paresseux avec <code>*?</code>, <code>+?</code> ou <code>.+?</code>
  pour s'arrêter à la première correspondance.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="footer">
  Mémo Regex — Guide de référence pour expressions régulières
</div>
""",
    unsafe_allow_html=True,
)
