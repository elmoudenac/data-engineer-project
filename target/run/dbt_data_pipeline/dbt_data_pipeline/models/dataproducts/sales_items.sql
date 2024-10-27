
  
    

    create or replace table `dataengineerproject-439609`.`dp_dataproducts`.`sales_items`
      
    partition by timestamp_trunc(sales_datetime, day)
    

    OPTIONS()
    as (
      -- Config pour indiquer le modèle incrémental


-- Extraction des informations nécessaires pour chaque vente et chaque produit
    SELECT
        CONCAT(CAST(s.id AS STRING), '_', s.item_product_sku) AS pk,  -- Clé primaire unique pour chaque vente
        safe_cast(s.sales_datetime AS datetime) AS sales_datetime,  -- Date de la vente
        s.item_amount,  -- Montant total par produit et par vente
        s.item_product_sku AS product_sku,  -- SKU du produit vendu
        s.item_quantity,  -- Quantité d'items vendus
        p.product_description,  -- Description du produit
        ((p.unit_amount - s.item_amount) / p.unit_amount) * 100 AS discount_perc  -- Pourcentage de réduction
    FROM `dataengineerproject-439609`.`dp_hub`.`sales_staging` AS s
    LEFT JOIN `dataengineerproject-439609`.`dp_hub`.`products_staging` AS p
    ON s.item_product_sku = p.product_sku  -- Associer la description des produits
    );
  