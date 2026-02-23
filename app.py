"""Mémo Regex - Application Streamlit."""

import streamlit as st

from data.cheatsheet import SECTIONS, TIP, TAGS
from components import render_header, render_card, render_tip, render_footer


PAGE_TITLE = "Mémo Regex"
PAGE_ICON = "📖"


def load_css() -> str:
    """Charge le CSS depuis le fichier externe."""
    with open("styles/main.css", encoding="utf-8") as f:
        return f.read()


def main():
    """Point d'entrée principal."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide",
    )
    
    # Injection du CSS
    st.markdown(f"<style>{load_css()}</style>", unsafe_allow_html=True)
    
    # Header
    st.markdown(
        render_header(
            title="📖 Mémo Regex",
            subtitle="Référence rapide et concise pour les expressions régulières",
            tags=TAGS,
        ),
        unsafe_allow_html=True,
    )
    
    # Grille de cartes
    cards_html = "".join(
        render_card(
            title=section["title"],
            description=section["description"],
            headers=section["headers"],
            rows=section["rows"],
            extra=section.get("extra", ""),
        )
        for section in SECTIONS
    )
    
    st.markdown(f'<div class="grid">{cards_html}</div>', unsafe_allow_html=True)
    
    # Astuce
    st.markdown(
        render_tip(title=TIP["title"], content=TIP["content"]),
        unsafe_allow_html=True,
    )
    
    # Footer
    st.markdown(
        render_footer("Mémo Regex — Propulsé par Streamlit"),
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
