# paginas/competiciones/supercopa.py
import streamlit as st
import pandas as pd

# Cargar el DataFrame de temporadas
df_temporadas = pd.read_pickle('data/df_temporadas.pkl')

def display(año):
    st.title(f'Supercopa - Temporada {año}')

    # Filtrar los datos para la Supercopa y la temporada seleccionada
    df_seleccionado = df_temporadas[(df_temporadas['id_competicion'] == 'SuperCopaESP') & (df_temporadas['temporada'] == año)]

    st.write(df_seleccionado)
