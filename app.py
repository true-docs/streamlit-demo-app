import streamlit as st
from api.truedocs import run_prediction


instructions = """
# Truedocs

🚀 Bienvenido a Truedocs, donde revolucionamos el procesamiento de documentos. 

Utilizando el poder de la Inteligencia Artificial (IA), nuestra API 
está diseñada para acelerar significativamente tus flujos de trabajo de procesamiento 
de documentos. Con Truedocs, puedes clasificar fácilmente una amplia gama de documentos, 
desde documentos de identidad 🪪 hasta facturas de servicios públicos y mucho más. 
Pero eso es sólo el comienzo.

⚡ Esta aplicación de prueba demuestra el poder y capacidades de la API de Truedocs 
para aplicar inteligencia artificial sobre documentos 🖺.

Para mayor información acerca de nuestra API visita 
[api.truedocs.mx/docs](https://api.truedocs.mx/docs).

Para ver el código de esta app visita 
[nuestro repositorio en GitHub](https://github.com/true-docs/streamlit-demo-app).

## Instrucciones
1. Sube un documento.  
1. El sistema va a correr su predicción y mostrar el resultado.  
"""


def run(uploaded_file):
    with st.spinner("Ejecutando predicción..."):
        try:
            prediction = run_prediction(uploaded_file)
            st.success("¡Documento procesado con éxito!")
            st.markdown("## Resultados")
            st.write("Tipo de documento: ", prediction["documentType"])
            if "entity" in prediction:
                st.write("Entidad: ", prediction["entity"])
            st.write("Score: ", str(prediction["confidence"])[:4])
        except Exception as e:
            st.error(f"Error: {e}")


def main():
    st.caption("Demo del uso del API de Truedocs")
    st.markdown(instructions)
    st.warning(
        "Truedocs no guarda los documentos cargados. Tu documento se elimina al terminar la sesión.",
        icon="⚠️",
    )

    uploaded_file = st.file_uploader("Carga un archivo", type=["pdf", "jpg", "png"])

    if uploaded_file is not None:
        if st.button("Clasifica"):
            run(uploaded_file)
    else:
        st.info("Favor de cargar un documento.")


if __name__ == "__main__":
    main()
