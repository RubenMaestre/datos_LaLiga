import streamlit as st

# Importa tus páginas aquí
from pages import home, overview, market, salary_predictor, about

def create_sidebar():
    # Insertar CSS personalizado desde un archivo separado
    with open('styles/custom_styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Define los ítems del menú usando emojis o imágenes como iconos
    menu_items = {
        "🏠 Inicio": home.display,
        "📊 Una visión general": overview.display,
        "🔍 Explora el mercado": market.display,
        "💰 Predictor Salarial": salary_predictor.display,
        "❤️ Acerca de": about.display,
    }

    with st.sidebar:
        st.image('path_to_your_logo.png', width=100)
        for title, page_func in menu_items.items():
            if st.button(title):
                page_func()
