-- Tag pour indiquer que ce modèle est mis à jour toutes les heures


WITH standardized_customers AS (
    SELECT
        *,
        -- Normalisation des numéros de téléphone
        ARRAY(
            SELECT
                CASE
                    WHEN REGEXP_CONTAINS(phone_number, r'^\+33') THEN phone_number
                    WHEN REGEXP_CONTAINS(phone_number, r'^0') THEN '+33' || SUBSTR(REGEXP_REPLACE(phone_number, r'\D', ''), 2)  -- Remplacer 0 par +33
                    ELSE phone_number  -- Pour tout autre format, garder tel quel (potentiellement à adapter pour d'autres cas)
                END AS standardized_phone_number
            FROM UNNEST(phone_numbers) AS phone_number
        ) AS standardized_phone_numbers,

        -- Normalisation des adresses e-mail (en minuscules pour consistance)
        ARRAY(
            SELECT LOWER(email)
            FROM UNNEST(emails) AS email
        ) AS standardized_emails
    FROM `dataengineerproject-439609`.`dp_lake`.`customers_raw`
),

ranked_customers AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY _dp_ingestion_timestamp DESC
        ) AS row_num
    FROM standardized_customers
)

-- Sélectionner uniquement les enregistrements uniques les plus récents
SELECT
    _dp_ingestion_timestamp,
    customer_id,
    standardized_emails AS emails,
    standardized_phone_numbers AS phone_numbers

FROM
    ranked_customers
WHERE
    row_num = 1