import streamlit as st
import pandas as pd
import requests

# Title de l'onglet
st.set_page_config(
    page_title="Les Universités de France",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="auto",
)

# Affichage Streamlit
st.title("Universités françaises (Open Data)")
st.write("Données issues de l'Open Data du Ministère de l'Enseignement Supérieur.")

# Charger les données JSON depuis l'URL
url = "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-principaux-etablissements-enseignement-superieur/download/?format=json"

# Requete HTTP
response = requests.get(url)

try:
    if response.status_code == 200:
        data = response.json()

    # Extraire les informations utiles (par exemple : nom, ville, type)
    records = []
    for item in data:
        fields = item.get('fields', {})
        records.append({
            "Nom": fields.get("uo_lib"),
            "Ville": fields.get("com_nom"),
            "Type": fields.get("type_d_etablissement"),
    })
except Exception as e: 
    st.error("❌ Échec de telechargement, rafraichir la page!")
    if st.button("🔄 Rafraîchir les données"):
        st.rerun()
    st.stop()

# Convertir en DataFrame
df = pd.DataFrame(records)

# Filtre par ville
ville = st.selectbox("Choisissez une ville :", options=sorted(df["Ville"].dropna().unique()))
df_filtre = df[df["Ville"] == ville]

# Affichage du tableau filtré
st.dataframe(df_filtre)

