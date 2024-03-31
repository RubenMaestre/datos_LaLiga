import pandas as pd
import plotly.express as px
import streamlit as st

def analizar_temporada_equipo(df_equipos):
    """
    Función para analizar la temporada y el equipo seleccionado.
    
    :param df_equipos: DataFrame de equipos con las columnas 'id_temporada', 'nombre_equipo', 'id_equipo' y 'posicion_liga'.
    """
    # Extrae las temporadas y divisiones únicas
    temporadas_divisiones = df_equipos['id_temporada'].unique()
    temporadas = sorted(set(x.split('_')[0] for x in temporadas_divisiones))

    # Selector de temporada
    temporada_seleccionada = st.selectbox('Selecciona una temporada:', temporadas)

    # Filtrar divisiones basadas en la temporada seleccionada
    divisiones = sorted(x.split('_')[1] for x in temporadas_divisiones if temporada_seleccionada in x)

    # Selector de división
    division_seleccionada = st.selectbox('Selecciona la división:', divisiones)

    # Filtrar el DataFrame basado en la temporada y división seleccionadas
    df_filtrado = df_equipos[df_equipos['id_temporada'].str.startswith(temporada_seleccionada) & df_equipos['id_temporada'].str.endswith(division_seleccionada)]

    # Selector de equipo basado en id_equipo, pero mostrando nombre_equipo
    equipo_seleccionado = st.selectbox('Selecciona un equipo:', df_filtrado['nombre_equipo'].unique())

    # Obtener id_equipo basado en nombre_equipo seleccionado
    id_equipo_seleccionado = df_filtrado[df_filtrado['nombre_equipo'] == equipo_seleccionado]['id_equipo'].iloc[0]

        # Filtrar filas del equipo seleccionado
    df_equipo = df_filtrado[df_filtrado['id_equipo'] == id_equipo_seleccionado]

    # Configurar colores basados en la división
    color = 'blue' if 'LaLiga1' in division_seleccionada else 'green'

    # Preparar los datos para la gráfica
    df_equipo['posicion_liga'] = df_equipo['posicion_liga'].fillna(23)
    
    # Crear la gráfica con Plotly
    fig = px.bar(df_equipo, x='id_temporada', y='posicion_liga', color_discrete_sequence=[color],
                 title=f'Posición de {equipo_seleccionado} en la Temporada {temporada_seleccionada}',
                 labels={'id_temporada': 'Temporada', 'posicion_liga': 'Posición en Liga'})
    
    # Invertir eje Y para que la posición 1 esté arriba
    fig.update_yaxes(autorange="reversed")
    
    # Ajustar límites del eje Y y mejorar la apariencia
    fig.update_yaxes(range=[1, 23], tickmode='array', tickvals=list(range(1, 24)))
    fig.update_layout(yaxis_tickformat = 'd')

    # Mostrar la gráfica
    st.plotly_chart(fig, use_container_width=True)
