import requests

def fetch_data_from_api(endpoint, start_id=None, limit=250):
    base_url = "https://stacklabs-retail-api.com"
    headers = {
       'Authorization': 'Bearer API_KEY'
    }

    data = []
    current_start_id = start_id

    while True:
        params = {'limit': limit}
        if current_start_id:
            params['start_sales_id'] = current_start_id

        response = requests.get(f"{base_url}/{endpoint}", headers=headers, params=params)

        if response.status_code != 200:
            print(f"Erreur lors de l'appel à l'API {endpoint}: {response.status_code}")
            break

        response_data = response.json()
        items = response_data.get('items', [])
        data.extend(items)

        if len(items) < limit:
            break

        current_start_id = items[-1]['id']

    return data