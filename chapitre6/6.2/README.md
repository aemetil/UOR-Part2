# Universités françaises – Open Data

Ce projet est une application Streamlit qui affiche les principaux établissements d'enseignement supérieur en France à partir d'un jeu de données Open Data.

## Fonctionnalités

- Chargement automatique des données JSON depuis le site du Ministère de l'Enseignement Supérieur
- Filtrage des universités par ville
- Affichage interactif sous forme de tableau

## Installation locale

> Testée avec Python 3.11

1. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
2. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

## Source des données

- [Open Data – Ministère de l'Enseignement Supérieur](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-principaux-etablissements-enseignement-superieur/table/?disjunctive.type_d_etablissement&disjunctive.typologie_d_universites_et_assimiles)

---

_Projet réalisé dans le cadre de l'exercice 6.2(Bonus) – Informatique Fondamentale_
