import streamlit as st
import pandas as pd
import plotly.express as px

st.header('US Car Sales Advertisements')

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
build_histogram = st.checkbox('Build Histogram')

if build_histogram:
    st.write('Creating a histogram for the car advertisement dataset')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
build_scatter = st.checkbox('Build Scatter Plot')

if build_scatter:
    st.write('Creating a scatter plot for the car advertisement dataset')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
