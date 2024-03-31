# pages/inicio.py
import streamlit as st

def display():
    # Asegúrate de que la ruta a la imagen esté correcta y sea accesible
    st.image("sources/cabecera.jpg", use_column_width=True, height=300)

    # Título de bienvenida
    st.title("Bienvenidos a la página de datos de LaLiga")

    # Texto introductorio
    st.markdown("""
        ### Proyecto de Análisis de LaLiga por Rubén Maestre

        Este espacio está dedicado a compartir un exhaustivo análisis de las temporadas 2010/2011 hasta la 
        actualidad de las principales competiciones de fútbol en España: La Primera División, La Segunda 
        División, la Copa del Rey y la Supercopa de España.

        ---
    """)

    # Creación de dos columnas para los textos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            #### Sobre el Proyecto

            Este proyecto nace de mi pasión por el fútbol y por el análisis de datos. Lo que empezó como un 
            hobby se ha convertido en una minuciosa recopilación de datos que quiero compartir con la comunidad. 
            Aquí encontrarás información detallada sobre equipos, jugadores, competiciones y partidos, así 
            como estadísticas interesantes que van desde las mayores goleadas por temporada hasta el jugador 
            que más goles ha marcado.
        """)
    
    with col2:
        st.markdown("""
            #### Descubrimientos y Datos Curiosos

            Este análisis ha permitido descubrir tendencias y patrones como qué equipo recibe más goles o tarjetas 
            en los últimos 15 minutos de partido, algo crucial para entender los momentos críticos de un encuentro. 
            Este tipo de insights son los que ofrecen un valor añadido y una nueva perspectiva a los fans del fútbol 
            y a los profesionales del ámbito deportivo.
        """)

    st.markdown("""
        ---
        #### Mi Formación y Herramientas Utilizadas

        Tras mi formación en la escuela HACK A BOSS en Data Science e Inteligencia Artificial, he adquirido las 
        habilidades necesarias para manejar con destreza herramientas como Python, Pandas y Plotly. La combinación 
        de estas herramientas con la plataforma de Streamlit ha sido esencial para llevar a cabo la configuración 
        y visualización de los datos de una manera que sea tanto informativa como atractiva para el usuario.

        Este sitio es una muestra de mi trabajo y dedicación. Invito a todos a explorar los datos, descubrir las 
        estadísticas y, por supuesto, a conectar conmigo para cualquier consulta o comentario. ¡Disfruta del viaje 
        por los datos de LaLiga y descubre una perspectiva única del fútbol español!
    """)

    # Aquí puedes añadir más contenido si lo deseas, como imágenes, gráficos interactivos, etc.
