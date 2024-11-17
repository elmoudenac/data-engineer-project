# Data Engineering Pipeline Project

## But du Projet
Ce projet consiste à créer un pipeline de données complet qui extrait des informations de différentes sources d'API, les traite, les stocke dans un data lake et les charge dans une base de données analytique. Les données sont ensuite préparées pour être analysées via des outils comme Power BI et Dataiku. L'objectif principal est de démontrer la capacité à intégrer, transformer, et analyser des données à grande échelle dans un environnement cloud.

## Stack Technique Utilisée
- **Python** : Extraction des données depuis l'API, nettoyage des données, et orchestration des étapes du pipeline.
- **API REST** : Accès aux différentes sources de données (éléments produits, ventes, clients).
- **Google Cloud Storage** : Stockage des fichiers JSON transformés et archivage des fichiers sources.
- **BigQuery** : Chargement, normalisation, et analyse des données dans un environnement SQL.
- **Power BI** : Création de tableaux de bord pour visualiser les données.
- **Dataiku** : Transformation supplémentaire des données et analyses avancées.

## Étapes Principales
1. **Extraction des Données depuis l'API**
   - Utilisation de scripts Python pour extraire les données via des endpoints REST avec pagination.
2. **Transformation et Nettoyage des Données**
   - Les données sont enrichies avec un timestamp d'ingestion et nettoyées (élimination des doublons, transformation des numéros de téléphone, formatage des dates).
3. **Chargement dans Cloud Storage et BigQuery**
   - Les données sont d'abord stockées sur Cloud Storage, puis chargées dans BigQuery où elles sont divisées en couches (lake, hub, dataproducts).
4. **Analyse et Visualisation**
   - Utilisation de Power BI pour des rapports en temps réel et exploration des données avec Dataiku.

## Comment Exécuter le Projet
1. **Configurer les Clés API** : Définir la variable d'environnement `API_KEY` avec votre clé d'authentification.
2. **Lancer le Pipeline** : Exécuter `main.py` pour extraire les données, les nettoyer, et les charger dans BigQuery.
3. **Visualiser les Données** : Accéder à BigQuery pour des analyses SQL ou se connecter à Power BI pour la visualisation.

