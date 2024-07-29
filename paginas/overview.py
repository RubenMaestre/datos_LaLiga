# paginas/overview.py
import streamlit as st
from paginas.competiciones import primera_division, segunda_division, copa_del_rey, supercopa
import pandas as pd

# Cargar el DataFrame de temporadas
df_temporadas = pd.read_pickle('data/df_temporadas.pkl')

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

    # Filtrar los años disponibles para la competición seleccionada
    df_filtrado = df_temporadas[df_temporadas['id_competicion'] == competicion.replace(" ", "")]
    años = df_filtrado['temporada'].unique()
    año = st.selectbox("Selecciona el año", años)

    st.markdown("---")

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
