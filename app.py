import numpy as np
import streamlit as st
from api.truedocs import run_prediction
from content import (
    instructions,
    capabilities,
    intro_to_classify,
    intro_to_extract,
    intro_to_validate,
)
from PIL import Image


def run(uploaded_file, operation, parameters):
    with st.spinner("Ejecutando predicción..."):
        result = None
        try:
            result = run_prediction(uploaded_file, operation, parameters)
            st.success("¡Documento procesado con éxito!")
            st.markdown("## Resultados")
        except Exception as e:
            st.error(f"Error: {e}")
        return result


def classify(uploaded_file):
    prediction = run(uploaded_file, "classify", {})["prediction"]
    st.write("Tipo de documento: ", prediction["documentType"])
    if "entity" in prediction:
        st.write("Entidad: ", prediction["entity"])
    st.write("Score: ", str(prediction["confidence"])[:4])


def match(uploaded_file, identifier, threshold, top_k):
    parameters = {"identifier": identifier, "threshold": threshold, "top_k": top_k}
    result = run(uploaded_file, "match", parameters)
    if result:
        st.write(result["matches"])


def validate(uploaded_file, validation_type):
    parameters = {"validationType": validation_type}
    result = run(uploaded_file, "validate", parameters)
    if result:
        st.write(result["validation"])


def show_options(uploaded_file):
    st.markdown("## Aplica IA sobre el documento")
    st.markdown(capabilities)
    st.info(
        "Con el documento ya cargado, ahora puedes ejecutar operaciones de IA sobre tu documento."
    )
    tab1, tab2, tab3 = st.tabs(["Clasifica", "Coteja", "Valida"])
    with tab1:
        st.markdown(intro_to_classify)
        if st.button("Clasifica"):
            classify(uploaded_file)
    with tab2:
        st.markdown(intro_to_extract)
        identifier = st.text_input("Palabras a buscar")
        threshold = st.text_input("Umbral de similitud (1-100)", 80)
        top_k = st.text_input("Número de coincidencias", 1)
        if st.button("Busca"):
            match(uploaded_file, identifier, threshold, top_k)
    with tab3:
        st.markdown(intro_to_validate)
        validation_type = st.selectbox("Tipo de validación", ["IsRecent", "DidExpire"])
        if st.button("Validar"):
            validate(uploaded_file, validation_type)


def main():
    st.caption("Demo del uso del API de Truedocs")
    st.markdown(instructions)
    st.warning(
        "Truedocs no guarda los documentos cargados. Tu documento se elimina al terminar la sesión.",
        icon="⚠️",
    )

    st.markdown("## Carga un documento")
    uploaded_file = st.file_uploader("Carga un archivo", type=["pdf", "jpg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(np.array(img), width=320)
        show_options(uploaded_file)
    else:
        st.info("Favor de cargar un documento.")


if __name__ == "__main__":
    main()
