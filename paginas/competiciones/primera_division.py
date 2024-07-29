# paginas/competiciones/primera_division.py
import streamlit as st
import pandas as pd

def display(año):
    st.title(f'Primera División - Temporada {año}/{año+1}')

    # Aquí cargamos los datos específicos de la Primera División para el año seleccionado
    # Supongamos que tienes un DataFrame con datos de la Primera División por año
    df_primera = pd.read_pickle('data/df_primera.pkl')
    df_seleccionado = df_primera[df_primera['season'] == f'{año}/{año+1}']

    st.write(df_seleccionado)

display()
