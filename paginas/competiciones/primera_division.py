# paginas/competiciones/primera_division.py
import streamlit as st
import pandas as pd

# Cargar el DataFrame de temporadas desde el archivo CSV
df_temporadas = pd.read_csv('data/df_temporadas.csv')

def display(año):
    st.title(f'Primera División - Temporada {año}')

    # Filtrar los datos para la Primera División y la temporada seleccionada
    df_seleccionado = df_temporadas[(df_temporadas['id_competicion'] == 'LaLiga1') & (df_temporadas['temporada'] == año)]

    st.write(df_seleccionado)
