# pages/inicio.py
import streamlit as st
from PIL import Image

def display():
    # Asegúrate de que la ruta a la imagen esté correcta y sea accesible
    st.image("sources/cabecera.jpg", use_column_width=True, caption="Análisis de LaLiga", output_format="JPEG")

    # Título de bienvenida
    st.title("Bienvenidos a DataFútbol360")

    # Texto introductorio
    st.markdown("""
        ### Proyecto de análisis y datos de LaLiga, por Rubén Maestre

        No pretendo en este Streamlit crear la típica página de gráficas y algún modelo de machine learning para 
        predecir resultados utilizando el histórico. Considero que eso está muy visto. Mi idea es intentar hacer 
        algo diferente, probando opciones como procesamiento de lenguaje con LLM, elaboración de informes, 
        y alguna cosa más que se me irá ocurriendo.
                
        Para este proyecto, he trabajado con datos de fútbol, principalmente de la liga española, creando una base 
        de datos en local con información desde la temporada 2008/2009 hasta la actualidad de las principales competiciones 
        de fútbol en España: La Primera División, La Segunda División, la Copa del Rey y la Supercopa de España. En 
        un futuro, también incorporaremos datos de la Segunda B (actualmente conocida como RFEF), fútbol femenino y 
        fútbol sala.

        Llevaba tiempo recopilando todo tipo de datos de fútbol para crear diferentes proyectos y por ello decidí construirme una base de 
        datos que también me valía para practicar SQL, asignando a los equipos, competiciones y jugadores un ID único para poder identificarlos. Uno de los 
        proyectos que tengo en marcha por ejemplo con machine learning es el de predecir, mediante sus datos estadísticos y evolución de 
        sus equipos, los puntos FIFA que tendrán los jugadores en sus cartas FIFA en futuras temporadas. Pero lo contaré en otro momento, ya que además de eso, 
        estoy trabajándolo para aplicarlo también al fútbol sala.

        Pero para este proyecto que voy a enseñar aquí, no voy a explicar todo el proceso de trabajo en SQL. Eso lo 
        puedes encontrar en mi LinkedIn pinchando [aquí](https://www.linkedin.com/posts/rubenmaestrezaplana_dossier-de-creaci%C3%B3n-de-una-base-de-datos-activity-7159622820023414784-2W3-?utm_source=share&utm_medium=member_desktop). 
        Aquí trabajaré ya con los archivos pickles preparados con los datos que necesito para equipos, competiciones, 
        jugadores y partidos. No explicaré ese proceso de obtención. Simplemente, ya los tengo.

        ---
    """)

    # Creación de dos columnas para los textos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            #### Sobre el proyecto

            Este proyecto surge de darle vueltas a crear cosas diferentes y enseñar mi trabajo, en este caso con algo que me apasiona como es el fútbol y el análisis de datos. Lo que empezó como un hobby se ha convertido en una minuciosa recopilación de datos que quiero compartir con la comunidad.

Voy a ir creando secciones con ideas que pretendo que sean creativas. Por ejemplo, la idea de crear un chatbot especializado en información de fútbol de la liga española que le preguntes un dato y te lo diga. O por ejemplo, crear una sección donde busques un equipo o un jugador y te genere un informe con todos sus datos. También podría plantear la opción de un comparador de jugadores o equipos, cosas así.

        """)
    
    with col2:
        st.markdown("""
            #### Ideas creativas o disruptivas en la visualización de datos del fútbol

Mi objetivo es encontrar formas innovadoras y atractivas de presentar los datos de fútbol de manera interactiva y llamativa. Con Streamlit, puedo crear visualizaciones que no solo muestran estadísticas de manera clara, sino que también permiten a los usuarios interactuar con los datos de una forma dinámica.

Planeo implementar varias ideas creativas, como un chatbot especializado en información de fútbol de la liga española, la generación de informes detallados para equipos y jugadores, y un comparador interactivo de jugadores y equipos. Quiero que cada sección ofrezca una experiencia única y enriquecedora para los usuarios.

Además, estoy siempre abierto a nuevas ideas. Si tienes alguna propuesta creativa o disruptiva, no dudes en ponerte en contacto conmigo. Me encantaría explorar nuevas posibilidades y llevar a cabo proyectos innovadores.

        """)

    st.markdown("""
        ---
        #### Mi formación y herramientas utilizadas

        Soy un científico y analista de datos apasionado por el deporte y la gestión deportiva. Poseo un MBA en 
        Sport Management especializado en la gestión de clubes y la organización de eventos deportivos. Siempre 
        busco hacer cosas diferentes, intentando diferenciarme con ideas creativas, disruptivas e innovadoras. 
        Creo firmemente que si no te ven, no existes; y que para ser visto en el vasto escaparate que es internet 
        hoy en día, uno debe ser realmente innovador, creativo y novedoso.

        Con esta web de streamlit, verás una muestra de mi trabajo y formación. Te invito a explorar la página, descubrir las 
        secciones y, por supuesto, a conectar conmigo para cualquier consulta o comentario. ¡Disfruta del viaje 
        por los datos de LaLiga y descubre una perspectiva única del fútbol español!
    """)

    # Aquí puedes añadir más contenido si lo deseas, como imágenes, gráficos interactivos, etc.
