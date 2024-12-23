-- Tag to indicate that this model is updated every hour
{{
    config(
        materialized='view',
        schema='hub',
        tags=["hourly"]
    )
}}

WITH ranked_sales AS (
    -- Assign a row number to each sale based on customer_id and timestamp, to keep the most recent entry
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY id
            ORDER BY _dp_ingestion_timestamp DESC
        ) AS row_num
    FROM {{ source('dp_lake', 'sales_raw') }}
),

-- Filter to only include the most recent entry for each sale (i.e., row_num = 1)
deduplicated_sales AS (
    SELECT *
    FROM ranked_sales
    WHERE row_num = 1
)

-- Flatten items array for each sale and select relevant fields
SELECT
    ds._dp_ingestion_timestamp,
    ds.id,
    ds.datetime AS sales_datetime,
    ds.customer_id,
    ds.total_amount,
    item.amount AS item_amount,
    item.quantity AS item_quantity,
    item.product_sku AS item_product_sku
FROM
    deduplicated_sales AS ds,
    UNNEST(ds.items) AS item
