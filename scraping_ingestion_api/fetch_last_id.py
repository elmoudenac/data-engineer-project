from google.cloud import bigquery

def fetch_max_id_from_sales():
    # Initialize the BigQuery client
    client = bigquery.Client()

    # Define the SQL query to get the maximum id from the table
    query = """
        SELECT MAX(id) AS max_id
        FROM `dataengineerproject-439609.dp_lake.sales_normalized`
    """

    # Execute the query
    query_job = client.query(query)
    results = query_job.result()

    # Fetch the maximum id from the results
    for row in results:
        max_id = row.max_id
        return max_id if max_id is not None else None

    return None

