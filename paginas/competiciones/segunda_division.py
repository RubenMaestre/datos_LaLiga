# paginas/competiciones/segunda_division.py
import streamlit as st
import pandas as pd
import numpy as np

# Cargar el DataFrame de temporadas
df_temporadas = pd.read_pickle('data/df_temporadas.pkl')

def display(año):
    st.title(f'Segunda División - Temporada {año}')

    # Filtrar los datos para la Segunda División y la temporada seleccionada
    df_seleccionado = df_temporadas[(df_temporadas['id_competicion'] == 'LaLiga2') & (df_temporadas['temporada'] == año)]

    st.write(df_seleccionado)
