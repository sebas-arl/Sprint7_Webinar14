import streamlit as st
import os

st.set_page_config(page_title="Data Science Portfolio", layout="wide")

st.sidebar.title("Navigation")
selection = st.sidebar.radio(
    "Go to", ["Home", "Coin Flip Simulation", "Tips Analysis", "Penguins Dashboard", "Sprint 7: Data Analysis Project"])

# Función para ejecutar archivos de forma segura


def run_app(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            exec(f.read(), globals())
    else:
        st.error(f"File not found: {path}")


if selection == "Home":
    st.title("Data Science & Marketing Analytics Portfolio")
    st.write("""
    Welcome! I am a **Marketing Strategist & Data Scientist** with 5 years of experience in Media Buying.
    This portfolio showcases my transition into Data Science, focusing on:
    * **Statistical Analysis**
    * **Data Visualization**
    * **Predictive Simulations**
    """)

elif selection == "Coin Flip Simulation":
    run_app("Coin_Simulation/moneda_app.py")

elif selection == "Tips Analysis":
    run_app("Webinar14/Streamlit/analisis_app.py")

elif selection == "Penguins Dashboard":
    run_app("Webinar14/Streamlit_penguins/penguins_app.py")

elif selection == "Project Sprint 7: US Car Sales Analysis":
    run_app("Project_Sprint7/sprint7_project.py")
