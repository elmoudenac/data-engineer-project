-- back compat for old kwarg name
  
  
        
            
            
        
    

    

    merge into `dataengineerproject-439609`.`dp_dataproducts`.`sales_items` as DBT_INTERNAL_DEST
        using (-- Config pour indiquer le modèle incrémental


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
        ) as DBT_INTERNAL_SOURCE
        on (
                DBT_INTERNAL_SOURCE.pk = DBT_INTERNAL_DEST.pk
            )

    
    when matched then update set
        `pk` = DBT_INTERNAL_SOURCE.`pk`,`sales_datetime` = DBT_INTERNAL_SOURCE.`sales_datetime`,`item_amount` = DBT_INTERNAL_SOURCE.`item_amount`,`product_sku` = DBT_INTERNAL_SOURCE.`product_sku`,`item_quantity` = DBT_INTERNAL_SOURCE.`item_quantity`,`product_description` = DBT_INTERNAL_SOURCE.`product_description`,`discount_perc` = DBT_INTERNAL_SOURCE.`discount_perc`
    

    when not matched then insert
        (`pk`, `sales_datetime`, `item_amount`, `product_sku`, `item_quantity`, `product_description`, `discount_perc`)
    values
        (`pk`, `sales_datetime`, `item_amount`, `product_sku`, `item_quantity`, `product_description`, `discount_perc`)


    