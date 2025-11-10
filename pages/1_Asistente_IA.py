import streamlit as st
import google.generativeai as genai
import time

# --- 1. Configuración de Página y API ---
st.set_page_config(
    page_title="Asistente de Planificación",
    page_icon="🤖",
    layout="wide"
)

# Inyectar CSS
st.markdown("<style>footer { visibility: hidden; }</style>", unsafe_allow_html=True)

# Configurar la API de Google
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('models/gemini-pro-latest')
except Exception as e:
    st.error("Error de API Key. Asegúrate de tenerla en .streamlit/secrets.toml")
    st.stop()

# --- 2. El "Prompt Maestro" (Versión 3.0 - Súper Específico) ---
def generar_prompt_maestro(docente_nombre, docente_escuela, tipo_plan, materia, duracion, alumnos, desafios, planificacion):
    
    desafios_str = ", ".join(desafios)
    if not desafios_str:
        desafios_str = "ninguno en particular"

    prompt = f"""
    **Rol:** Eres un Asesor Pedagógico experto en inclusión y didáctica, específico de Mendoza.

    **Contexto del Docente:**
    * **Nombre:** {docente_nombre}
    * **Institución:** {docente_escuela}
    * **Tipo de Planificación Requerida:** {tipo_plan}
    * **Materia:** {materia}
    * **Duración / Período:** {duracion}
    * **Tamaño del Grupo:** {alumnos} alumnos
    * **Desafíos de Inclusión detectados:** {desafios_str}

    **Planificación Base o Tópicos del Docente (Input):**
    ---
    {planificacion}
    ---

    **Tu Tarea (Output):**
    Analiza la planificación base en el contexto dado y genera dos (2) secciones de salida CLARAS 
    y CONCISAS en formato Markdown. NO añadas introducciones ni despedidas.

    **### 1. Planificación Adaptada ({tipo_plan})**
    (Ofrece sugerencias prácticas para adaptar la planificación a los desafíos de inclusión 
    mencionados, considerando el período '{tipo_plan}' y la materia '{materia}'. Sé específico.)

    **### 2. Párrafo para Informe (GEI / Familias)**
    (Escribe un párrafo profesional, listo para "copiar y pegar" en un informe de GEI
    para la institución '{docente_escuela}', firmado conceptualmente por {docente_nombre}. 
    Debe justificar las adaptaciones.)
    """
    return prompt

# --- 3. Verificar Contexto ---
# ¡CRUCIAL! Revisar si el "perfil" está completo
if not st.session_state.get('contexto_guardado', False):
    st.warning("Por favor, ve a la página de inicio (app.py) y completa tu 'Perfil de Docente' antes de usar el asistente.")
    st.stop() # Detener la ejecución si no hay perfil

# --- 4. Interfaz de Usuario (Asistente) ---
st.title("🤖 Asistente de Planificación Inclusiva")
st.markdown(f"Hola **{st.session_state.docente_nombre}**, estás planificando para **{st.session_state.docente_escuela}**.")

# --- Barra Lateral (Inputs del Plan) ---
st.sidebar.header("Detalles de la Planificación")

# ¡TUS NUEVAS IDEAS!
tipo_plan = st.sidebar.selectbox(
    "Tipo de Planificación:", 
    ["Planificación de Clase Diaria", "Planificación Semanal", "Planificación Mensual", "Planificación Anual"], 
    key="tipo_plan"
)

# Adaptar el "label" de duración según el plan
if "Diaria" in tipo_plan:
    duracion_label = "Duración de la clase (minutos)"
    duracion_value = 45
elif "Anual" in tipo_plan:
    duracion_label = "Año del Plan (Ej. 2026)"
    duracion_value = 2026
else:
    duracion_label = "Período (Ej. 'Semana 1', 'Mayo')"
    duracion_value = "Semana 1"

duracion = st.sidebar.text_input(duracion_label, str(duracion_value), key="duracion")

materia = st.sidebar.text_input("Materia:", "Ej. Biología", key="materia")
cantidad_alumnos = st.sidebar.number_input("Cantidad de Alumnos:", min_value=1, max_value=50, value=30, key="alumnos")

with st.sidebar.expander("Desafíos de Inclusión (Requerido)"):
    desafios_aula = st.multiselect(
        "Selecciona los desafíos:",
        ["TDAH", "Dislexia", "TDA", "Autismo Leve", "Discalculia"],
        key="desafios"
    )

st.sidebar.header("Input del Docente")
planificacion_base = st.sidebar.text_area(
    f"Pega aquí tu planificación base o tópicos para el plan {tipo_plan}:", 
    height=200, 
    key="plan_base",
    placeholder=f"Ej: Para el plan {tipo_plan} de {materia} quiero cubrir..."
)

generar_button = st.sidebar.button("¡Generar Plan e Informe!", type="primary")

# --- 5. Lógica de Generación (Outputs) ---
st.header(f"Resultados para tu {tipo_plan}")

if generar_button:
    if not planificacion_base or not desafios_aula:
        st.error("Por favor, completa la planificación y los desafíos.")
    else:
        try:
            with st.spinner("🧠 Analizando... La IA está generando tu plan..."):
                
                # 1. Crear el Prompt (¡Ahora con TODO el contexto!)
                prompt_final = generar_prompt_maestro(
                    docente_nombre=st.session_state.docente_nombre,
                    docente_escuela=st.session_state.docente_escuela,
                    tipo_plan=tipo_plan,
                    materia=materia,
                    duracion=duracion,
                    alumnos=cantidad_alumnos,
                    desafios=desafios_aula,
                    planificacion=planificacion_base
                )
                
                # 2. Llamar a la IA
                response = model.generate_content(prompt_final)
                
                # 3. Mostrar los resultados
                st.success("¡Resultados generados!")
                st.markdown(response.text)
                
                with st.expander("Ver el prompt maestro (Debug)"):
                    st.text(prompt_final)

        except Exception as e:
            st.error(f"Ha ocurrido un error al contactar la IA: {e}")
else:
    st.info("Completa los datos en la barra lateral izquierda y presiona 'Generar'.")