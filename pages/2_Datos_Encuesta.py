import streamlit as st

st.set_page_config(page_title="Datos de la Encuesta", page_icon="📊")

st.title("📊 Los Datos que validan este Proyecto")
st.markdown("Hicimos una encuesta '360' y esto es lo que encontramos:")

# --- Datos de Docentes ---
st.header("El Dolor del Docente (62 Encuestados)")

st.subheader("El 35.5% se siente 'Poco Preparado'")
st.markdown("La calificación promedio de preparación fue de **3.79 sobre 5**.")
# (Aquí puedes poner un gráfico si quieres)

st.subheader("El 'Dolor' es el Tiempo y la Burocracia")
st.markdown("""
* **GEI:** 29 menciones
* **Burocracia (Informes):** 28 menciones
* **Planificar:** 24 menciones
* **Inclusión (TDAH/Dislexia):** 19 menciones
""")

# --- Datos de Padres ---
st.header("El Impacto en la Familia (37 Encuestados)")

st.subheader("El 43.2% se siente 'Confundido'")
st.markdown("Calificaron la claridad de la información con **5 o menos sobre 10**.")

st.subheader("Citas de Oro de los Padres:")
st.warning("Quiero: \"Que se evalúe el proceso y no solo el resultado\"")
st.info("Pido: \"Una aplicación de herramientas pedagógicas para acompañar dificultades\"")

st.header("Nuestra Solución")
st.success("Nuestro Asistente ataca estos problemas: le ahorra **tiempo** al docente (burocracia) y le da **claridad** al padre (proceso) con un solo clic.")