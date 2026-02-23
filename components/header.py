"""Composant header."""


def render_header(title: str, subtitle: str, tags: list) -> str:
    """Génère le HTML du header."""
    tags_html = "".join(f'<span class="tag">{tag}</span>' for tag in tags)
    
    return f"""
    <section class="hero">
      <h1>{title}</h1>
      <p>{subtitle}</p>
      <div class="tags">{tags_html}</div>
    </section>
    """
