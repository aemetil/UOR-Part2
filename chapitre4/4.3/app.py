import streamlit as st

st.title("Coupe du monde 2022")
st.subheader("Ballon officiel de la compétition")
st.image("Al-Rihla.jpg", caption="Ballon officiel : Al Rihla")

st.markdown("""
Bienvenue sur mon application **Streamlit** réalisée pour l’exercice 4.3.

Vous y trouverez une illustration du ballon officiel de la Coupe du monde 2022 et quelques éléments de contexte.

Cette app est un bon exemple d'outil léger de présentation de données en Python.
""")

st.subheader("Et vous ?")
pays = st.text_input("Votre équipe préférée?")
if pays:
    st.write(f"🏆 {pays} mérite aussi de gagner la coupe du monde!")
