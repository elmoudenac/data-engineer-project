from api_handler import fetch_data_from_api
from storage_handler import upload_to_bucket
from fetch_last_id import fetch_max_id_from_sales
if __name__ == "__main__":
    last_id = fetch_max_id_from_sales()
    bucket_name = 'gcs-dp-stacklabs-retail-api'

    all_products_data = fetch_data_from_api('products', limit=250)
    products_filename = 'products.json'
    upload_to_bucket(bucket_name, 'products', products_filename)

    all_sales_data = fetch_data_from_api('sales', start_id=last_id)
    sales_filename = 'sales.json'
    upload_to_bucket(bucket_name, 'sales', sales_filename)

    all_customers_data = fetch_data_from_api('customers', limit=250)
    customers_filename = 'customers.json'
    upload_to_bucket(bucket_name, 'customers', customers_filename)