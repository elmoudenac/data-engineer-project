from google.cloud import bigquery, storage
import json
import datetime
import tempfile


def load_data_to_bigquery(bucket_name, source_blob_prefix, destination_table_id):
    # Initialiser les clients BigQuery et Cloud Storage
    bq_client = bigquery.Client()
    storage_client = storage.Client()

    # Lister les fichiers dans le bucket Cloud Storage
    blobs = storage_client.list_blobs(bucket_name, prefix=source_blob_prefix)

    current_time = datetime.datetime.now().isoformat()
    for blob in blobs:
        if not blob.name.endswith('.json'):
            continue  # Ignorer les éléments qui ne sont pas des fichiers JSON

        # Lire le contenu du fichier JSON directement depuis le blob
        file_contents = blob.download_as_text()
        data = json.loads(file_contents)

        # Vérifier que la clé 'items' existe et est une liste
        if 'items' in data and isinstance(data['items'], list):
            transformed_data = []

            # Ajouter le champ de timestamp d'ingestion à chaque enregistrement
            for item in data['items']:
                item['_dp_ingestion_timestamp'] = current_time
                transformed_data.append(item)

            # Écrire les données transformées dans un fichier temporaire pour l'importation
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
                for record in transformed_data:
                    temp_file.write(json.dumps(record) + '\n')
                temp_file_path = temp_file.name

            # Configurer le job de chargement BigQuery
            job_config = bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
                autodetect=True,
                write_disposition='WRITE_APPEND',
                schema_update_options=[
                    bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
                    # Permet l'ajout de colonnes si elles n'existent pas encore
                ],
            )

            # Charger les données dans BigQuery directement depuis le fichier temporaire
            with open(temp_file_path, "rb") as source_file:
                load_job = bq_client.load_table_from_file(
                    source_file, destination_table_id, job_config=job_config
                )

            load_job.result()  # Attendre la fin du job

            # Vérifier que le chargement a fonctionné
            destination_table = bq_client.get_table(destination_table_id)
            print(
                f"Chargement terminé du fichier {blob.name} dans la table {destination_table_id}. La table contient maintenant {destination_table.num_rows} lignes.")

            # Archiver le fichier
            archive_file(blob)


def archive_file(blob):
    # Déplacer le fichier vers le bucket 'archived_files'
    storage_client = storage.Client()
    destination_bucket_name = 'gcs_stacklabs_archived'
    destination_bucket = storage_client.bucket(destination_bucket_name)

    # Définir le nom du nouvel emplacement (archivé)
    archived_blob_name = f"archived/{blob.name.split('/')[-1]}"
    new_blob = destination_bucket.blob(archived_blob_name)

    # Copier le blob vers le nouveau bucket
    new_blob.rewrite(blob)

    # Supprimer le fichier original du bucket source
    blob.delete()

    print(f"Fichier {blob.name} archivé dans le bucket {destination_bucket_name} sous le nom {archived_blob_name}.")


if __name__ == "__main__":
    # Charger les données pour chaque ensemble (customers, products, sales)
    bucket_name = "gcs-dp-stacklabs-retail-api"
    load_data_to_bigquery(bucket_name, "customers/", "dataengineerproject-439609.dp_lake.customers_raw")
    load_data_to_bigquery(bucket_name, "products/", "dataengineerproject-439609.dp_lake.products_raw")
    load_data_to_bigquery(bucket_name, "sales/", "dataengineerproject-439609.dp_lake.sales_raw")
