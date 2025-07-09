import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Matplotlib", layout="centered")

st.title("Bienvenue sur le Dashboard !")

# Ton dashboard ici :
df = pd.DataFrame({
    "Catégorie": ["A", "B", "C", "D"],
    "Valeur": [10, 23, 7, 19]
})

fig, ax = plt.subplots()
ax.bar(df["Catégorie"], df["Valeur"])
ax.set_title("Valeur par Catégorie")

st.pyplot(fig)

if st.checkbox("Afficher les données brutes"):
    st.dataframe(df)
