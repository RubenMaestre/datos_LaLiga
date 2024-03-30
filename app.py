import streamlit as st
from pages import overview, teams, players, matches

PAGES = {
    "Vista General": overview,
    "Equipos": teams,
    "Jugadores": players,
    "Partidos": matches
}

st.sidebar.title('Navegación')
selection = st.sidebar.radio("Ir a:", list(PAGES.keys()))
page = PAGES[selection]

page.app()
