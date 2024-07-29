# paginas/competiciones/segunda_division.py
import streamlit as st
import pandas as pd

# Cargar el DataFrame de temporadas desde el archivo CSV
df_temporadas = pd.read_csv('data/df_temporadas.csv')

def display(año):
    st.title(f'Segunda División - Temporada {año}')

    # Filtrar los datos para la Segunda División y la temporada seleccionada
    df_seleccionado = df_temporadas[(df_temporadas['id_competicion'] == 'LaLiga2') & (df_temporadas['temporada'] == año)]

    st.write(df_seleccionado)
