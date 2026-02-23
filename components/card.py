"""Composant carte pour une section regex."""


def render_card(title: str, description: str, headers: list, rows: list, extra: str = "") -> str:
    """Génère le HTML d'une carte avec un tableau."""
    
    # Construire le header du tableau
    header_html = "".join(f"<th>{h}</th>" for h in headers)
    
    # Construire les lignes
    rows_html = ""
    for row in rows:
        cells = "".join(f"<td><code>{cell}</code></td>" if i == 0 else f"<td>{cell}</td>" 
                       for i, cell in enumerate(row))
        rows_html += f"<tr>{cells}</tr>"
    
    extra_html = f'<p>{extra}</p>' if extra else ""
    
    return f"""
    <div class="card">
      <h3>{title}</h3>
      <p>{description}</p>
      <table>
        <thead><tr>{header_html}</tr></thead>
        <tbody>{rows_html}</tbody>
      </table>
      {extra_html}
    </div>
    """
