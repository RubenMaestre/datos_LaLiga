# modules/navbar.py
import streamlit as st

# Ruta al logo almacenada dentro del módulo
LOGO_PATH = "sources/logo.jpg"

def create_navbar(pages_dict):
    with st.sidebar:
        st.image(LOGO_PATH, width=100)
        for page_name, page_content in pages_dict.items():
            if isinstance(page_content, dict):  # Es un submenú desplegable
                with st.expander(page_name):
                    for subpage_name, subpage_content in page_content.items():
                        if st.button(subpage_name):
                            st.session_state['active_page'] = subpage_name
                            subpage_content()
            else:
                if st.button(page_name):
                    st.session_state['active_page'] = page_name
                    page_content()
