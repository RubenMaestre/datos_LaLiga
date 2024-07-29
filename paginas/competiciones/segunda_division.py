# paginas/competiciones/segunda_division.py
import streamlit as st
import pandas as pd

def display(año):
    st.title(f'Segunda División - Temporada {año}/{año+1}')

    # Aquí cargamos los datos específicos de la Segunda División para el año seleccionado
    # Supongamos que tienes un DataFrame con datos de la Segunda División por año
    df_segunda = pd.read_pickle('data/df_segunda.pkl')
    df_seleccionado = df_segunda[df_segunda['season'] == f'{año}/{año+1}']

    st.write(df_seleccionado)

display()
