from google.cloud import storage
import datetime

def upload_to_bucket(bucket_name, folder_name, filename):
    # Ajouter un timestamp au nom du fichier
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename_with_timestamp = f"{filename.split('.')[0]}_{timestamp}.json"

    # Créer un client de Cloud Storage
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    # Définir le chemin du fichier dans le dossier du bucket
    blob = bucket.blob(f'{folder_name}/{filename_with_timestamp}')
    blob.upload_from_filename(filename)

    print(f'Fichier {filename} uploadé sous le nom {filename_with_timestamp} dans le dossier {folder_name} du bucket {bucket_name}.')