# paginas/overview.py
import streamlit as st
from paginas.competiciones import primera_division, segunda_division, copa_del_rey, supercopa
import pandas as pd

def display():
    # Título de la página
    st.title("Datos generales")

    # Descripción de la página
    st.write("""
        Aquí encontrarás información detallada sobre las principales competiciones de fútbol en España.
        Utiliza los selectores a continuación para explorar los datos específicos de cada competición y temporada.
    """)

    # Selectores de competición y año
    competiciones = ["Primera División", "Segunda División", "Copa del Rey", "Supercopa"]
    competicion = st.selectbox("Selecciona la competición", competiciones)
    
    años = {
        "Primera División": list(range(2008, 2024)),
        "Segunda División": list(range(2009, 2024)),
        "Copa del Rey": list(range(2009, 2024)),
        "Supercopa": list(range(2009, 2024))
    }
    año = st.selectbox("Selecciona el año", años[competicion])

    st.markdown("---")

    # Dividir la interfaz en dos columnas: una para la navegación y otra para el contenido
    col_navegacion, divider, col_contenido = st.columns([1, 0.3, 7])
    with col_navegacion:
        st.markdown("<h4 style='text-align: center;'>Pulse una opción para saber más</h4>", unsafe_allow_html=True)
        
        # Navegación dentro de la competición seleccionada
        if competicion == "Primera División":
            primera_division.display(año)
        elif competicion == "Segunda División":
            segunda_division.display(año)
        elif competicion == "Copa del Rey":
            copa_del_rey.display(año)
        elif competicion == "Supercopa":
            supercopa.display(año)

display()
