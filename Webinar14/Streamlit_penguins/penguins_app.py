import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# url_data = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"
# df = pd.read_csv(url_data)

df = sns.load_dataset("penguins")

st.header("Dataset de Pinguinos")
st.dataframe(df)

species = st.selectbox("Selecciona la especie", options=[
                       'Adelie', 'Chinstrap', 'Gentoo'])
bill_length_mm = st.slider(
    'Selecciona longitud del pico', min_value=30, max_value=50, step=1)
df_filtrado = df.query(
    'species == @species and bill_length_mm >= @bill_length_mm')
st.dataframe(df_filtrado)

media = df_filtrado["bill_length_mm"].mean()
mediana = df_filtrado["bill_length_mm"].median()
desviacion = df_filtrado["bill_length_mm"].std()

st.metric("Media", f"{media:.2f}")
st.metric("Mediana", f"{mediana:.2f}")
st.metric("Desviacion", f"{desviacion:.2f}")

fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=df_filtrado,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='island',
    ax=ax
)

ax.set_title("Largo vs Profundidad del pico por isla")
ax.set_xlabel("Largo del pico (mm)")
ax.set_ylabel("Profundidad del pico (mm)")
ax.legend(title="Isla")

st.pyplot(fig)
plt.close(fig)
