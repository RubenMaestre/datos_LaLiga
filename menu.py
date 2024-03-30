# menu.py
import streamlit as st

# Importa tus páginas aquí
from pages import home, overview, teams, players, matches

# Asegúrate de que cada módulo de página tenga una función 'display'
# Por ejemplo, en home.py deberías tener algo como:
# def display():
#     st.title('Inicio')
#     # Resto del contenido de la página de inicio

def create_sidebar():
    # Define los ítems del menú con las páginas que tienes
    menu_items = {
        "🏠 Inicio": home.display,
        "📊 Overview": overview.display,
        "⚽ Equipos": teams.display,
        "👥 Jugadores": players.display,
        "🏟 Partidos": matches.display,
    }

    # Insertar CSS personalizado desde un archivo separado
    with open('styles/custom_styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Configuración inicial de la página activa
    if 'active_page' not in st.session_state:
        st.session_state['active_page'] = '🏠 Inicio'

    st.sidebar.title("Menú")
    for title, page_func in menu_items.items():
        if st.sidebar.button(title):
            st.session_state['active_page'] = title  # Guarda el título de la página activa

    # Ejecutar la función de la página activa
    menu_items[st.session_state['active_page']]()

# Ahora, llamar a create_sidebar en app.py, no aquí.

