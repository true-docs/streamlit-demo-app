import streamlit as st
from api.truedocs import run_prediction


instructions = """# Truedocs
⚡ Esta aplicación demuestra el poder y capacidades de la API de Truedocs 
para aplicar inteligencia artificial sobre documentos 🖺.

Para mayor información acerca de nuestra API visita [api.truedocs.mx/docs](https://api.truedocs.mx/docs).

## Instrucciones
1. Sube un documento.  
1. El sistema va a correr su predicción y mostrar el resultado.  
"""

def main():
    st.caption("Demo del uso del API de Truedocs")
    st.markdown(instructions)
    st.warning("Truedocs no guarda los documentos cargados. Tu documento se elimina al terminar la sesión.", icon="⚠️")

    uploaded_file = st.file_uploader('Carga un archivo', type=['pdf', 'jpg', 'png'])

    if uploaded_file is not None:
        with st.spinner('Ejecutando predicción...'):
            try:
                prediction = run_prediction(uploaded_file)
                st.success('¡Documento clasificado con éxito!')
                st.markdown('## Resultados')
                st.write("Tipo de documento: ", prediction["documentType"])
                if 'entity' in prediction:
                    st.write("Entidad: ", prediction["entity"])
                st.write("Score: ", str(prediction["confidence"])[:4])
            except Exception as e:
                st.error(f'Error: {e}')
    else:
        st.info('Favor de cargar un documento.')

if __name__ == "__main__":
    main()