import streamlit as st


st.set_page_config(
    page_title="Mémo Regex — Guide Ultime",
    page_icon="📖",
    layout="wide",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap');

:root {
  --bg-1: #0c0f1a;
  --bg-2: #1a2233;
  --card: #121826;
  --ink: #e9eef5;
  --muted: #a8b3c7;
  --accent: #ffb000;
  --accent-2: #5ad0ff;
  --line: #273047;
  --good: #54d68a;
}

html, body, [class*="css"]  {
  font-family: "Space Grotesk", system-ui, -apple-system, Segoe UI, sans-serif;
  color: var(--ink);
}

body {
  background: radial-gradient(1200px 800px at 10% -10%, #2a3550 0%, transparent 60%),
              radial-gradient(900px 600px at 90% 10%, #1f2c4d 0%, transparent 55%),
              linear-gradient(180deg, var(--bg-1), var(--bg-2));
}

.block-container {
  padding-top: 2.5rem;
  padding-bottom: 4rem;
  max-width: 1200px;
}

.hero {
  display: grid;
  gap: 1rem;
  padding: 2.25rem 2rem;
  border-radius: 20px;
  background: linear-gradient(135deg, #141b2d 0%, #0f1422 100%);
  border: 1px solid var(--line);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
}

.hero h1 {
  font-family: "Source Serif 4", serif;
  font-size: 2.8rem;
  margin: 0;
  letter-spacing: 0.5px;
}

.hero p {
  margin: 0;
  color: var(--muted);
  font-size: 1.1rem;
}

.pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.pill {
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  background: rgba(90, 208, 255, 0.12);
  border: 1px solid rgba(90, 208, 255, 0.4);
  color: #bfeaff;
  font-size: 0.85rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.25rem;
  margin-top: 2rem;
}

.card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 1.5rem;
  min-height: 220px;
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.2);
}

.card h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1.2rem;
  color: var(--accent);
}

.card p {
  margin: 0 0 0.75rem 0;
  color: var(--muted);
  line-height: 1.6;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 0.75rem;
  font-size: 0.95rem;
}

.table th, .table td {
  border-bottom: 1px solid var(--line);
  padding: 0.5rem 0.3rem;
  text-align: left;
}

.table th {
  color: #c9d4e6;
  font-weight: 600;
}

.tag {
  display: inline-block;
  padding: 0.15rem 0.45rem;
  border-radius: 6px;
  background: rgba(255, 176, 0, 0.15);
  color: #ffd27a;
  font-size: 0.8rem;
  margin-left: 0.25rem;
}

.callout {
  background: linear-gradient(135deg, rgba(84, 214, 138, 0.12), rgba(90, 208, 255, 0.12));
  border: 1px solid rgba(84, 214, 138, 0.35);
  border-radius: 16px;
  padding: 1.25rem 1.5rem;
  margin-top: 1.5rem;
}

.callout strong {
  color: var(--good);
}

.footer {
  margin-top: 2.5rem;
  color: var(--muted);
  font-size: 0.9rem;
  border-top: 1px solid var(--line);
  padding-top: 1rem;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<section class="hero">
  <h1>📖 Mémo Regex — Le Guide Ultime</h1>
  <p>Un condensé clair, visuel et actionnable pour travailler vite avec les expressions régulières.</p>
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
    <p>Définir la position de la recherche ou remplacer n'importe quel caractère.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>.</code></td><td>N'importe quel caractère (sauf saut de ligne)</td><td><code>c.t</code> → cat, cut, c9t</td></tr>
        <tr><td><code>^</code></td><td>Début de ligne/texte</td><td><code>^The</code> → The (si en début)</td></tr>
        <tr><td><code>$</code></td><td>Fin de ligne/texte</td><td><code>Moon.$</code> → Moon. (fin)</td></tr>
        <tr><td><code>|</code></td><td>OU logique</td><td><code>crew|team</code> → crew ou team</td></tr>
        <tr><td><code>\\</code></td><td>Échappe un caractère spécial</td><td><code>\\.</code> → un vrai point</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>2. Les Quantificateurs</h3>
    <p>Ils s'appliquent au caractère ou groupe juste avant.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>?</code></td><td>0 ou 1 fois</td><td><code>re?</code> → r ou re</td></tr>
        <tr><td><code>*</code></td><td>0, 1 ou plusieurs fois</td><td><code>en*</code> → e, en, enn…</td></tr>
        <tr><td><code>+</code></td><td>1 ou plusieurs fois</td><td><code>en+</code> → en, enn (pas “e”)</td></tr>
        <tr><td><code>{n}</code></td><td>Exactement n fois</td><td><code>en{2}</code> → enn</td></tr>
        <tr><td><code>{n,}</code></td><td>Au moins n fois</td><td><code>\\d{3,}</code> → 123, 4567</td></tr>
        <tr><td><code>{n,m}</code></td><td>Entre n et m fois</td><td><code>\\d{2,4}</code> → 12, 123, 1234</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>3. Les Classes de Caractères</h3>
    <p>Raccourcis indispensables. La majuscule est l'inverse.</p>
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
    <p><span class="tag">Crochets</span> <code>[abc]</code>, <code>[a-z]</code>, <code>[A-Z]</code>, <code>[^0-9]</code></p>
  </div>

  <div class="card">
    <h3>4. Frontières de Mots</h3>
    <p>Délimiter un mot par ses frontières invisibles.</p>
    <table class="table">
      <thead>
        <tr><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
      </thead>
      <tbody>
        <tr><td><code>\\b</code></td><td>Frontière de mot</td><td><code>\\blo</code> → lo de local</td></tr>
        <tr><td><code>\\B</code></td><td>Pas une frontière</td><td><code>\\Best</code> → est de rester</td></tr>
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
        <tr><td><code>(?:...)</code></td><td>Groupe non-capturant</td><td><code>(?:crew|team)</code></td></tr>
        <tr><td><code>(?P&lt;nom&gt;)</code></td><td>Groupe nommé (Python)</td><td><code>(?P&lt;word&gt;[a-z]+)</code></td></tr>
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
  <strong>💡 Le piège du “gourmand” (Greedy vs Lazy)</strong><br/>
  Par défaut, les regex avalent le plus de texte possible. Exemple : <code>"(.+)"</code> sur
  <code>"Texte 1" et "Texte 2"</code> capturera tout entre le premier et le dernier guillemet.<br/>
  <strong>Solution</strong> : rendre le quantificateur paresseux avec <code>*?</code>, <code>+?</code> ou <code>.+?</code>
  pour s'arrêter à la première correspondance.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="footer">
  Mémo Regex prêt à être déployé avec Streamlit. Éditez librement le contenu dans <code>app.py</code>.
</div>
""",
    unsafe_allow_html=True,
)
