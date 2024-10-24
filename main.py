from google.cloud import storage


def upload_to_bucket(bucket_name, folder_name, filename):
    # Créer un client de Cloud Storage
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    # Définir le chemin dans lequel stocker le fichier (comme un dossier logique)
    blob = bucket.blob(f'{folder_name}/{filename}')

    # Uploader le fichier dans le bucket
    blob.upload_from_filename(filename)

    print(f'Fichier {filename} uploadé dans le dossier {folder_name} du bucket {bucket_name}.')


if __name__ == "__main__":
    bucket_name = 'gcs-dp-stacklabs-retail-api'

    # Appel à l'API Products
    products_filename = 'products.json'
    upload_to_bucket(bucket_name, 'products', products_filename)

    # Appel à l'API Sales
    sales_filename = 'sales.json'
    upload_to_bucket(bucket_name, 'sales', sales_filename)

    # Appel à l'API Customers
    customers_filename = 'customers.json'
    upload_to_bucket(bucket_name, 'customers', customers_filename)
