import streamlit as st
from modules.analizar_temporada_equipo import analizar_temporada_equipo
import pandas as pd

def display():
    # Título de la página
    st.title("Datos generales")

    # Descripción de la página
    st.write("""
        Aquí vas a encontrar algunos datos curiosos generales de LaLiga donde por ejemplo podrás ver un histórico de la clasificación o buscar datos como máximas goleadas, goleadores, máximas tarjetas, etc...
        
        Utiliza los selectores a continuación para explorar los datos específicos de cada temporada, división y equipo.
    """)

    # Carga el DataFrame de equipos
    df_equipos = pd.read_pickle('data/df_equipos.pkl')

    # Llamada a la función para realizar el análisis
    analizar_temporada_equipo(df_equipos)
