# Exécuter le script Python pour ingérer les données
echo "Démarrage de l'ingestion des données..."
python "/c/Users/lenovo/data-engineer-project/main.py"

# Charger les données depuis Cloud Storage vers BigQuery
echo "Chargement des données vers BigQuery..."
python "/c/Users/lenovo/data-engineer-project/load_to_bigquery.py"

# Changer de répertoire pour accéder à ton projet dbt
cd "/c/Users/lenovo/data-engineer-project/dbt_data_pipeline"

# Exécuter les transformations dbt
echo "Exécution des transformations dbt..."
dbt run --profiles-dir "/c/Users/lenovo/.dbt"

echo "Pipeline terminé."
