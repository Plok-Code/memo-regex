"""Composant astuce/tip."""


def render_tip(title: str, content: str) -> str:
    """Génère le HTML d'une astuce."""
    return f"""
    <div class="tip">
      <strong>💡 {title}</strong><br/>
      {content}
    </div>
    """
