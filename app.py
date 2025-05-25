import streamlit as st
import pandas as pd
import plotly.express as px 


# Encabezado
st.header("Análisis de Datos de Vehículos")

# Leer archivo CSV
df = pd.read_csv("vehicles_us.csv")  

# Mostrar los primeros datos
st.write("Primeras filas del conjunto de datos:")
st.dataframe(df.head())

# Botón para mostrar el histograma
if st.checkbox("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios")
    st.plotly_chart(fig)

if st.checkbox("Mostrar gráfico de dispersión Precio vs Año"):
    fig_scatter = px.scatter(df, x="model_year", y="price", title="Precio según el Año del Vehículo", opacity=0.5)
    st.plotly_chart(fig_scatter)