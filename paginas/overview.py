# paginas/overview.py
import streamlit as st
from paginas.competiciones import primera_division, segunda_division, copa_del_rey, supercopa
import pandas as pd

# Cargar el DataFrame de temporadas desde el archivo CSV
df_temporadas = pd.read_csv('data/df_temporadas.csv')

def display():
    # Título de la página
    st.title("Datos generales")

    # Descripción de la página
    st.write("""
        Aquí encontrarás información detallada sobre las principales competiciones de fútbol en España.
        Utiliza los selectores a continuación para explorar los datos específicos de cada competición y temporada.
    """)

    # Dividir la interfaz en dos columnas para los selectores
    col1, col2 = st.columns(2)

    with col1:
        # Selectores de competición
        competiciones = ["Selecciona una", "Primera División", "Segunda División", "Copa del Rey", "Supercopa"]
        competicion = st.selectbox("Selecciona la competición", competiciones)

    with col2:
        if competicion != "Selecciona una":
            # Filtrar los años disponibles para la competición seleccionada
            id_competicion = competicion.replace(" ", "")
            df_filtrado = df_temporadas[df_temporadas['id_competicion'] == id_competicion]
            años = df_filtrado['temporada'].unique()
            año = st.selectbox("Selecciona una temporada", años)
        else:
            año = st.selectbox("Selecciona una temporada", [])

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
