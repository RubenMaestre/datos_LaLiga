# paginas/competiciones/supercopa.py
import streamlit as st
import pandas as pd

def display(año):
    st.title(f'Supercopa - Temporada {año}/{año+1}')

    # Aquí cargamos los datos específicos de la Supercopa para el año seleccionado
    # Supongamos que tienes un DataFrame con datos de la Supercopa por año
    df_supercopa = pd.read_pickle('data/df_supercopa.pkl')
    df_seleccionado = df_supercopa[df_supercopa['season'] == f'{año}/{año+1}']

    st.write(df_seleccionado)

display()
