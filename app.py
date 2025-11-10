import streamlit as st

# --- Configuración de la Página ---
# (Esto es lo primero que debe ir)
st.set_page_config(
    page_title="Asistente de Planificación Inclusiva",
    page_icon="🚀",
    layout="wide"
)

# --- Título y Header ---
st.title("Asistente de Planificación Inclusiva 🚀")
st.markdown("Genera adaptaciones y párrafos de informe para GEI en segundos, no en horas.")

# --- BARRA LATERAL (Sidebar) ---
# Usamos la barra lateral para el "Contexto" y dejamos el área principal para los resultados.
st.sidebar.header("1. Contexto del Aula")
rol_docente = st.sidebar.selectbox("Mi Rol:", ["Titular", "Suplente"])
cantidad_alumnos = st.sidebar.number_input("Cantidad de Alumnos:", min_value=1, max_value=50, value=30)
desafios_aula = st.sidebar.multiselect(
    "Desafíos de Inclusión (Selecciona):",
    ["TDAH", "Dislexia", "TDA", "Autismo Leve", "Discalculia"]
)

st.sidebar.header("2. Input del Docente")
planificacion_base = st.sidebar.text_area("Pega aquí tu planificación base:", height=250)

# Botón "Mágico"
generar_button = st.sidebar.button("¡Generar Adaptación e Informe!")

# --- ÁREA PRINCIPAL (Resultados) ---
st.header("Resultados Generados")

if generar_button:
    # --- Aquí es donde se llama a la IA ---
    # (Por ahora, usamos texto de ejemplo)
    
    st.info("¡Resultados generados con éxito!")
    
    # Placeholder 1: La IA procesaría la "planificacion_base" y los "desafios_aula"
    with st.container(border=True):
        st.subheader("1. Planificación Adaptada (Sugerencias)")
        st.markdown(f"""
        **Basado en tu rol ({rol_docente}) y los desafíos ({', '.join(desafios_aula)}):**

        * **Para TDAH:** Te sugiero dividir la actividad principal en dos bloques de 15 minutos (Técnica Pomodoro).
        * **Para Dislexia:** Asegúrate de usar una fuente clara (ej. OpenDyslexic) y entrega este glosario de términos clave: [Glosario].
        * ... (más sugerencias de la IA) ...
        """)

    # Placeholder 2: La IA generaría el informe
    with st.container(border=True):
        st.subheader("2. Párrafo para Informe (GEI / Familias)")
        st.markdown(f"""
        **Párrafo sugerido (listo para copiar y pegar):**

        "Para la presente planificación, y considerando un grupo de {cantidad_alumnos} alumnos, se han implementado adaptaciones metodológicas 
        específicas para los estudiantes con {', '.join(desafios_aula)}. Estas incluyen: (1) segmentación de actividades para 
        manejo de la atención (TDAH) y (2) provisión de material de lectura adaptado y glosarios visuales (Dislexia). 
        El objetivo es asegurar el acceso equitativo al contenido y evaluar el proceso de aprendizaje."
        """)
else:
    st.warning("Por favor, completa los campos en la barra lateral y presiona 'Generar'.")