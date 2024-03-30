# modules/navbar.py
import streamlit as st
import os
import importlib

# Ruta al logo almacenada dentro del módulo
LOGO_PATH = "sources/logo.jpg"

def auto_import_pages(pages_directory):
    pages = {}
    for filename in os.listdir(pages_directory):
        if filename.endswith(".py") and not filename.startswith("_"):
            page_name = filename[:-3]  # Elimina la extensión .py
            page_module = importlib.import_module(f'pages.{page_name}')
            pages[page_name.capitalize()] = page_module.app  # Capitaliza el nombre de la página
    return pages

def navbar():
    st.sidebar.image(LOGO_PATH, use_column_width=True)
    pages_dict = auto_import_pages("pages")
    page = st.sidebar.radio("Navegación", list(pages_dict.keys()))
    pages_dict[page]()
