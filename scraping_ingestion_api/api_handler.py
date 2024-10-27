import os

import requests
# Code pour récupérer les données de l'API Stack Labs via les endpoints avec pagination
api_key = os.getenv("API_KEY")
def fetch_data_from_api(endpoint, start_id=None, limit=250):
    base_url = "https://stacklabs-retail-api.com"
    headers = {
       'Authorization': 'Bearer ' + api_key
    }

    data = []
    current_start_id = start_id

    while True:
        # Préparer les paramètres de la requête
        params = {'limit': limit}
        if current_start_id:
            params['start_sales_id'] = current_start_id

        # Faire l'appel à l'API
        response = requests.get(f"{base_url}/{endpoint}", headers=headers, params=params)

        if response.status_code != 200:
            print(f"Erreur lors de l'appel à l'API {endpoint}: {response.status_code}")
            break

        # Ajouter les résultats actuels
        response_data = response.json()
        items = response_data.get('items', [])
        data.extend(items)

        # Vérifier s'il y a plus de données à récupérer
        if len(items) == 0 :
            break

        # Mettre à jour le `current_start_id` pour le prochain appel
        current_start_id = items[-1]['id']

    return data