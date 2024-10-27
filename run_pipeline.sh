# Exécuter le script Python pour ingérer les données
echo "Démarrage de l'ingestion des données..."
python "/c/Users/lenovo/data-engineer-project/main.py"

# Pause de 10 secondes pour permettre aux fichiers d'être uploadés avant de continuer
#sleep 10

# Charger les données depuis Cloud Storage vers BigQuery
echo "Chargement des données vers BigQuery..."
python "/c/Users/lenovo/data-engineer-project/load_to_bigquery.py"

# Pause de 10 secondes pour s'assurer que les fichiers sont bien présents
#sleep 10

# Changer de répertoire pour accéder à ton projet dbt
cd "/c/Users/lenovo/data-engineer-project/dbt_data_pipeline"

# Exécuter les transformations dbt
echo "Exécution des transformations dbt..."
dbt run --profiles-dir "/c/Users/lenovo/.dbt"

echo "Pipeline terminé."
