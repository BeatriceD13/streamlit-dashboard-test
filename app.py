import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit_authenticator as stauth

st.set_page_config(page_title="Dashboard Matplotlib", layout="centered")

# --- Authentification ---
hashed_passwords_bea = 'TestBlueline2026$'
hashed_passwords_dave = 'TestBlueline2026$'


users = {
    "beatrice": "Beatrice Desrochers",
    "dave": "Dave Murray"
}

passwords = {
    "beatrice": hashed_passwords_bea,  # hash de Beatrice
    "dave": hashed_passwords_dave      # hash de Jean
}
authenticator = stauth.Authenticate(
    users,
    passwords,
    "app_dashboard",
    "abcdef",  # clé secrète
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.title(f"Bienvenue {name} !")
    
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
    
    authenticator.logout('Logout', 'sidebar')

elif authentication_status is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")
else:
    st.info("Veuillez vous connecter")
