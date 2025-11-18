import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Unir Archivos Excel por Filas")

uploaded_files = st.file_uploader(
    "Cargar archivos Excel",
    type=["xls", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    dataframes = []
    for file in uploaded_files:
        try:
            df = pd.read_excel(file)
            dataframes.append(df)
        except Exception as e:
            st.error(f"Error leyendo el archivo {file.name}: {e}")
            st.stop()

    if dataframes:
        merged_df = pd.concat(dataframes, axis=0, ignore_index=True)

        # Crear archivo en memoria
        output = BytesIO()
        merged_df.to_excel(output, index=False)
        output.seek(0)

        st.success("Archivos combinados correctamente.")

        st.download_button(
            label="Descargar archivo combinado",
            data=output,
            file_name="archivos_combinados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("No se pudieron leer archivos válidos.")
else:
    st.info("Cargue uno o varios archivos Excel para iniciar.")
