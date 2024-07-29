# paginas/competiciones/copa_del_rey.py
import streamlit as st
import pandas as pd

def display(año):
    st.title(f'Copa del Rey - Temporada {año}/{año+1}')

    # Aquí cargamos los datos específicos de la Copa del Rey para el año seleccionado
    # Supongamos que tienes un DataFrame con datos de la Copa del Rey por año
    df_copa = pd.read_pickle('data/df_copa.pkl')
    df_seleccionado = df_copa[df_copa['season'] == f'{año}/{año+1}']

    st.write(df_seleccionado)

display()
