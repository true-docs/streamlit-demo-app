import pandas as pd
import streamlit as st
from api.truedocs import run_prediction


def main():
    st.title('Demo de clasificación de documentos')
    st.markdown('## Instrucciones')
    st.markdown('1. Sube un documento.')
    st.markdown('2. El sistema va a correr su predicción y mostrar el resultado.')

    st.warning("Truedocs no guarda los documentos cargados. Tu documento se elimina al terminar la sesión.", icon="⚠️")

    uploaded_file = st.file_uploader('Carga un archivo', type=['pdf', 'jpg', 'png'])

    if uploaded_file is not None:
        with st.spinner('Clasificando documento...'):
            try:
                prediction = run_prediction(uploaded_file)
                st.success('¡Documento clasificado con éxito!')
                st.markdown('## Resultados')
                st.write("Tipo de documento: ", prediction["documentType"])
                st.write("Entidad: ", prediction["entity"])
                st.write("Score: ", str(prediction["confidence"])[:4])
            except Exception as e:
                st.error(f'Error: {e}')
    else:
        st.info('Favor de cargar un documento.')

if __name__ == "__main__":
    main()