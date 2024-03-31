# menu.py
import streamlit as st
from paginas import inicio, overview, teams, players, matches

def create_sidebar():
    with open('styles/custom_styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    menu_items = {
        "🏠 Inicio": home.display,
        "📊 Overview": overview.display,
        "⚽ Equipos": teams.display,
        "👥 Jugadores": players.display,
        "🏟 Partidos": matches.display,
    }

    st.sidebar.title("Menú")

    if 'active_page' not in st.session_state:
        # Esto establecerá la página de inicio como predeterminada
        st.session_state['active_page'] = "🏠 Inicio"

    for title, page_func in menu_items.items():
        if st.sidebar.button(title):
            st.session_state['active_page'] = title

    # Llama a la función de la página actual
    menu_items[st.session_state['active_page']]()