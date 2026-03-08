import streamlit as st
import pandas as pd
import plotly.express as px

# Carga de datos
try:
    car_data = pd.read_csv('Project_Sprint7/vehicles_us.csv')
except:
    car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis del Mercado de Vehículos US')

# HISTOGRAMA
build_histogram = st.checkbox('Construir Histograma de Odómetro')

if build_histogram:
    st.write('Generando histograma para la distribución de kilometraje (odómetro)...')
    # Crea histograma
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Distribución del Odómetro")
    # Muestra gráfico
    st.plotly_chart(fig_hist, use_container_width=True)

# GRÁFICO DE DISPERSIÓN
build_scatter = st.checkbox('Construir Gráfico de Dispersión')

if build_scatter:
    st.write('Generando gráfico de dispersión: Precio vs. Año del Modelo...')
    # Crea gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year", y="price",
                             title="Relación Precio vs. Año de Fabricación")
    # Muestra gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
