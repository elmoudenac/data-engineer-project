from api_handler import read_data_from_file
from storage_handler import upload_to_bucket

if __name__ == "__main__":
    bucket_name = 'gcs-dp-stacklabs-retail-api'

    # Lecture et upload des données Products
    products_filename = 'products.json'
    products_data = read_data_from_file(products_filename)
    upload_to_bucket(bucket_name, 'products', products_filename)

    # Lecture et upload des données Sales
    sales_filename = 'sales.json'
    sales_data = read_data_from_file(sales_filename)
    upload_to_bucket(bucket_name, 'sales', sales_filename)

    # Lecture et upload des données Customers
    customers_filename = 'customers.json'
    customers_data = read_data_from_file(customers_filename)
    upload_to_bucket(bucket_name, 'customers', customers_filename)