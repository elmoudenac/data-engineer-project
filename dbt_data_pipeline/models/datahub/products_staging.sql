-- Tag pour indiquer que ce modèle est mis à jour toutes les heures
{{
    config(
        materialized='view',
        schema='hub',
        tags=["hourly"]
    )
}}

WITH ranked_products AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY product_sku
            ORDER BY _dp_ingestion_timestamp DESC
        ) AS row_num
    FROM {{ source('dp_lake', 'products_normalized') }}
)

-- Sélectionner uniquement les enregistrements uniques les plus récents
SELECT
    _dp_ingestion_timestamp,
    product_sku,
    unit_amount,
    description AS product_description,
    supplier

FROM
    ranked_products
WHERE
    row_num = 1
