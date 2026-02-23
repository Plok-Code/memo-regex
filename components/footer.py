"""Composant footer."""


def render_footer(text: str) -> str:
    """Génère le HTML du footer."""
    return f"""
    <div class="footer">
      {text}
    </div>
    """
