import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit_authenticator as stauth

st.set_page_config(page_title="Dashboard Matplotlib", layout="centered")
st.title("Exemple de Dashboard avec Matplotlib")

# Données
df = pd.DataFrame({
    "Catégorie": ["A", "B", "C", "D"],
    "Valeur": [10, 23, 7, 19]
})

# Graphique
fig, ax = plt.subplots()
ax.bar(df["Catégorie"], df["Valeur"])
ax.set_title("Valeur par Catégorie")

st.pyplot(fig)

# Affichage des données si coché
if st.checkbox("Afficher les données brutes"):
    st.dataframe(df)
