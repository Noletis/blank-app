import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL de la API (reemplázala con la que necesites)
API_URL = "https://jsonplaceholder.typicode.com/posts"

# Función para obtener datos de la API
def obtener_datos():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error al obtener datos de la API")
        return []

# Título de la aplicación
st.title("Visor de Datos desde API")

# Obtener datos
datos = obtener_datos()

# Convertir a DataFrame
df = pd.DataFrame(datos)

# Mostrar tabla
df_columns = df.columns.tolist()
st.write("Vista de datos obtenidos:")
st.dataframe(df)

# Seleccionar columnas para gráficos
if len(df_columns) >= 2:
    x_axis = st.selectbox("Selecciona columna para el eje X", df_columns)
    y_axis = st.selectbox("Selecciona columna para el eje Y", df_columns)
    
    # Crear gráfico dinámico
    fig = px.scatter(df, x=x_axis, y=y_axis, title="Visualización de datos")
    st.plotly_chart(fig)
