# paginas/competiciones/primera_division.py
import streamlit as st
import pandas as pd

# Cargar el DataFrame de temporadas desde el archivo CSV
df_temporadas = pd.read_csv('data/df_temporadas.csv')

def display(año):
    st.title(f'Primera División - Temporada {año}')

    # Filtrar los datos para la Primera División y la temporada seleccionada
    df_seleccionado = df_temporadas[(df_temporadas['id_competicion'] == 'LaLiga1') & (df_temporadas['temporada'] == año)]
    
    # Eliminar columnas innecesarias
    df_seleccionado = df_seleccionado.drop(columns=['id_temporada', 'temporada', 'id_competicion', 'partidos_completados'])
    
    # Convertir la fila seleccionada en un diccionario para fácil acceso
    datos = df_seleccionado.iloc[0].to_dict()

    # Dividir los datos en secciones
    secciones = {
        "Estadísticas Generales": ['estado', 'formato', 'numero_de_clubes', 'total_partidos', 'jornada', 'total_jornadas', 'progreso'],
        "Goles": ['promedio_goles_por_partido', 'promedio_goles_equipo_local', 'promedio_goles_equipo_visitante', 'porcentaje_goles_ambos_equipos', 'porcentaje_porteria_a_cero', 'porcentaje_ventaja_goles_local', 'porcentaje_ventaja_defensa_local', 'porcentaje_ventaja_local', 'goles_min_0_a_10', 'goles_min_11_a_20', 'goles_min_21_a_30', 'goles_min_31_a_40', 'goles_min_41_a_50', 'goles_min_51_a_60', 'goles_min_61_a_70', 'goles_min_71_a_80', 'goles_min_81_a_90', 'goles_min_0_a_15', 'goles_min_16_a_30', 'goles_min_31_a_45', 'goles_min_46_a_60', 'goles_min_61_a_75', 'goles_min_76_a_90', 'xg_promedio_por_partido'],
        "Corners": ['promedio_corners_por_partido', 'promedio_corners_equipo_local', 'promedio_corners_equipo_visitante', 'total_corners_temporada', 'porcentaje_mas_de_65_corners', 'porcentaje_mas_de_75_corners', 'porcentaje_mas_de_85_corners', 'porcentaje_mas_de_95_corners', 'porcentaje_mas_de_105_corners', 'porcentaje_mas_de_115_corners', 'porcentaje_mas_de_125_corners', 'porcentaje_mas_de_135_corners'],
        "Tarjetas": ['promedio_tarjetas_por_partido', 'promedio_tarjetas_equipo_local', 'promedio_tarjetas_equipo_visitante', 'total_tarjetas_temporada', 'porcentaje_mas_de_05_tarjetas', 'porcentaje_mas_de_15_tarjetas', 'porcentaje_mas_de_25_tarjetas', 'porcentaje_mas_de_35_tarjetas', 'porcentaje_mas_de_45_tarjetas', 'porcentaje_mas_de_55_tarjetas', 'porcentaje_mas_de_65_tarjetas', 'porcentaje_mas_de_75_tarjetas'],
        "Otros": ['riesgo_prediccion', 'porcentaje_mas_de_05', 'porcentaje_mas_de_15', 'porcentaje_mas_de_25', 'porcentaje_mas_de_35', 'porcentaje_mas_de_45', 'porcentaje_mas_de_55', 'porcentaje_menos_de_05', 'porcentaje_menos_de_15', 'porcentaje_menos_de_25', 'porcentaje_menos_de_35', 'porcentaje_menos_de_45', 'porcentaje_menos_de_55']
    }

    # Mostrar cada sección con los datos correspondientes
    for seccion, columnas in secciones.items():
        st.subheader(seccion)
        st.dataframe(pd.DataFrame(datos, index=[0])[columnas])

