call C:\Users\lenovo\data-engineer-project\.venv\Scripts\activate

echo Démarrage de l'ingestion des données...
python "C:\Users\lenovo\data-engineer-project\scripts\main.py"

echo Chargement des données vers BigQuery...
python "C:\Users\lenovo\data-engineer-project\scripts\load_to_bigquery.py"

cd "C:\Users\lenovo\data-engineer-project\dbt_data_pipeline"
echo Exécution des transformations dbt...
dbt run --profiles-dir "C:\Users\lenovo\.dbt"

echo Pipeline terminé.
