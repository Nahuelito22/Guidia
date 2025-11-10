import streamlit as st

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Bienvenida - Asistente Docente",
    page_icon="👋",
    layout="centered"
)

# --- Inyección de CSS (Opcional, pero recomendado) ---
st.markdown("""
<style>
    footer { visibility: hidden; }
    /* (Puedes añadir más estilos aquí) */
</style>
""", unsafe_allow_html=True)


# --- Título ---
st.title("Bienvenido/a al Asistente Inclusivo 🚀")
st.markdown("Antes de comenzar, necesitamos un poco de contexto sobre ti.")

# --- Inicializar Estado de Sesión (st.session_state) ---
# Esto es como una "mini-base de datos" temporal
if 'docente_nombre' not in st.session_state:
    st.session_state.docente_nombre = ""
if 'docente_apellido' not in st.session_state:
    st.session_state.docente_apellido = ""
if 'docente_escuela' not in st.session_state:
    st.session_state.docente_escuela = ""
if 'contexto_guardado' not in st.session_state:
    st.session_state.contexto_guardado = False

# --- Formulario de "Perfil" ---
# Usamos un formulario para que no se recargue con cada campo
with st.form(key="perfil_form"):
    st.header("Tu Perfil de Docente")
    
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Tu Nombre", value=st.session_state.docente_nombre)
    with col2:
        apellido = st.text_input("Tu Apellido", value=st.session_state.docente_apellido)
    
    escuela = st.text_input("Escuela/Institución", 
                            value=st.session_state.docente_escuela,
                            placeholder="Ej. IES 9-023 Maipú")
    
    # El botón de guardado del formulario
    submit_button = st.form_submit_button(label="Guardar Contexto")

# --- Lógica de Guardado ---
if submit_button:
    if nombre and apellido and escuela:
        st.session_state.docente_nombre = nombre
        st.session_state.docente_apellido = apellido
        st.session_state.docente_escuela = escuela
        st.session_state.contexto_guardado = True
        st.success(f"¡Contexto guardado! Hola, {nombre}. Ahora puedes ir al 'Asistente IA' en el menú de la izquierda.")
        st.balloons()
    else:
        st.error("Por favor, completa todos los campos del perfil.")

# --- Barra Lateral ---
st.sidebar.header("Navegación")
if st.session_state.contexto_guardado:
    st.sidebar.success(f"Usuario: {st.session_state.docente_nombre} {st.session_state.docente_apellido}")
    st.sidebar.info(f"Escuela: {st.session_state.docente_escuela}")
    st.sidebar.markdown("¡Ahora selecciona una página arriba!")
else:
    st.sidebar.warning("Por favor, guarda tu contexto en la página de inicio.")