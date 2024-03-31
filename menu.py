# menu.py
import streamlit as st
from paginas import inicio, overview, teams, players, matches

def create_sidebar():
    # Define tus estilos CSS aquí directamente
    st.markdown("""
        <style>
            /* Estilos generales del sidebar */
            .css-1lcbmhc {
                background-color: #000; /* fondo negro */
                color: white; /* texto en blanco */
            }
            /* Estilos de los botones del sidebar para que parezcan enlaces de menú */
            .css-1lcbmhc .stButton>button {
                width: 100%;
                border-radius: 0;
                border: none;
                background-color: transparent;
                color: white;
                padding: 10px 0;
                text-align: left;
                font-size: 16px;
            }
            /* Cambia el color de fondo del botón en hover */
            .css-1lcbmhc .stButton>button:hover {
                background-color: #333; /* Un poco más claro que el fondo negro */
            }
            /* Estilos para el título del menú en el sidebar */
            .css-1lcbmhc .sidebar-content h1 {
                color: white; /* Color del título */
                font-size: 25px; /* Tamaño del título */
                margin-bottom: 30px; /* Espacio debajo del título */
            }
            /* Estilos para modificar la imagen (icono del menú) */
            .css-1lcbmhc img {
                max-width: 50px; /* Cambiar según el tamaño deseado */
                margin-bottom: 20px; /* Espacio debajo del logo */
            }
        </style>
    """, unsafe_allow_html=True)

    menu_items = {
        "🏠 Inicio": inicio.display,
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