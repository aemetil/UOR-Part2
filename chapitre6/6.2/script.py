import requests
import json

# Télécharger les données
url = "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-principaux-etablissements-enseignement-superieur/download/?format=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Affiche la structure & variables, indentée
    print("=== Premier enregistrement ===")
    print(json.dumps(data[1], indent=2, ensure_ascii=False))
else:
    print("Erreur:", response.status_code)
