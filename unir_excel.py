import streamlit as st
import pandas as pd

st.title("Unir Archivos Excel por Columnas")

uploaded_files = st.file_uploader("Cargar archivos Excel", type=["xls", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    dataframes = []
    for file in uploaded_files:
        df = pd.read_excel(file)
        dataframes.append(df)
    
    # Unir archivos por columnas
    merged_df = pd.concat(dataframes, axis=1)
    
    # Guardar el archivo combinado
    output_file = "archivos_combinados.xlsx"
    merged_df.to_excel(output_file, index=False)
    
    # Descargar el archivo combinado
    with open(output_file, "rb") as file:
        st.download_button("Descargar archivo combinado", file, file_name=output_file)
