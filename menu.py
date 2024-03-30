import streamlit as st

# Importa tus páginas aquí
from pages import home, overview, players, teams, matches

def create_sidebar():
    # Insertar CSS personalizado desde un archivo separado
    with open('styles/custom_styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Define los ítems del menú con las páginas que tienes
    menu_items = {
        "🏠 Inicio": home.display,
        "📊 Overview": overview.display,
        "⚽ Equipos": teams.display,
        "👥 Jugadores": players.display,
        "🏟 Partidos": matches.display,
    }

    st.sidebar.title("Menú")
    for title, page_func in menu_items.items():
        if st.sidebar.button(title):
            page_func()
