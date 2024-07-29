# paginas/competiciones/primera_division.py
import streamlit as st
import pandas as pd

def display(año, df_temporadas, df_equipos):
    st.title(f'Primera División - Temporada {año}')

    # Filtrar los datos para la Primera División y la temporada seleccionada
    df_temporada_seleccionada = df_temporadas[(df_temporadas['id_competicion'] == 'LaLiga1') & (df_temporadas['temporada'] == año)]
    df_equipos_seleccionados = df_equipos[df_equipos['id_temporada'] == df_temporada_seleccionada['id_temporada'].values[0]]

    # Agregar columna de escudos con valores predeterminados
    df_equipos_seleccionados['escudos'] = '-'

    # Calcular los puntos totales
    df_equipos_seleccionados['Puntos'] = df_equipos_seleccionados['victorias'] * 3 + df_equipos_seleccionados['empates']

    # Ordenar equipos por posición en la liga
    df_equipos_ordenados = df_equipos_seleccionados.sort_values(by='posicion_liga')

    # Renombrar columnas
    df_equipos_ordenados.rename(columns={
        'posicion_liga': 'Posición',
        'nombre_equipo': 'Equipo',
        'goles_marcados': 'GF',
        'goles_concedidos': 'GC',
        'diferencia_goles': 'DFG'
    }, inplace=True)

    # Resetear el índice para eliminar la columna de índice
    df_equipos_ordenados.reset_index(drop=True, inplace=True)

    # Datos de estadísticas generales
    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("Estadísticas Generales")
        st.write(f"Estado: {df_temporada_seleccionada['estado'].values[0]}")
        st.write(f"Formato: {df_temporada_seleccionada['formato'].values[0]}")
        st.write(f"Número de clubes: {df_temporada_seleccionada['numero_de_clubes'].values[0]}")
        st.write(f"Total de partidos: {df_temporada_seleccionada['total_partidos'].values[0]}")
        st.write(f"Total de jornadas: {df_temporada_seleccionada['total_jornadas'].values[0]}")
        st.write(f"Progreso: {df_temporada_seleccionada['progreso'].values[0]}%")
        st.write(f"Promedio goles por partido: {df_temporada_seleccionada['promedio_goles_por_partido'].values[0]}")
        st.write(f"Promedio tarjetas por partido: {df_temporada_seleccionada['promedio_tarjetas_por_partido'].values[0]}")
        st.write(f"Promedio corners por partido: {df_temporada_seleccionada['promedio_corners_por_partido'].values[0]}")

    with col2:
        st.subheader("Clasificación de Equipos")
        st.markdown(df_equipos_ordenados[['escudos', 'Posición', 'Equipo', 'Puntos', 'victorias', 'empates', 'derrotas', 'GF', 'GC', 'DFG']].to_html(index=False), unsafe_allow_html=True)
