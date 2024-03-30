import streamlit as st
from menu import create_sidebar

# Configuraciones globales de la app, como el título y la configuración de la página
st.set_page_config(page_title="Mi Proyecto Streamlit")

# Puedes llamar aquí a cualquier configuración global adicional si es necesario

# Llama a la función de la barra lateral que crea el menú
create_sidebar()
