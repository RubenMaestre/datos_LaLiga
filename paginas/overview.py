# paginas/overview.py
import streamlit as st
from paginas.competiciones import primera_division, segunda_division, copa_del_rey, supercopa
import pandas as pd

# Cargar los DataFrames desde los archivos CSV
df_temporadas = pd.read_csv('data/df_temporadas.csv')
df_equipos = pd.read_csv('data/df_equipos.csv')
df_jugadores = pd.read_csv('data/df_jugadores.csv')
df_partidos = pd.read_csv('data/df_partidos.csv')

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
            # Mapear el nombre de la competición al id_competicion
            id_competicion_map = {
                "Primera División": "LaLiga1",
                "Segunda División": "LaLiga2",
                "Copa del Rey": "CopaReyESP",
                "Supercopa": "SuperCopaESP"
            }
            id_competicion = id_competicion_map.get(competicion, "")
            # Filtrar los años disponibles para la competición seleccionada
            df_filtrado = df_temporadas[df_temporadas['id_competicion'] == id_competicion]
            años = df_filtrado['temporada'].unique()
            año = st.selectbox("Selecciona una temporada", años)
        else:
            año = st.selectbox("Selecciona una temporada", [])

    st.markdown("---")

    # Navegación dentro de la competición seleccionada
    if competicion == "Primera División":
        primera_division.display(año, df_temporadas, df_equipos)
    elif competicion == "Segunda División":
        segunda_division.display(año, df_temporadas, df_equipos)
    elif competicion == "Copa del Rey":
        copa_del_rey.display(año, df_temporadas, df_equipos)
    elif competicion == "Supercopa":
        supercopa.display(año, df_temporadas, df_equipos)

display()
