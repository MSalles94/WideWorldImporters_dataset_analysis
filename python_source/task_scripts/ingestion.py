from python_source.modules.date_parameters import airflow_date_reference  
from python_source.ingestion_tables.customers import extract_customers

def main(): 
    data_parameters=airflow_date_reference()

    extract_customers()

if __name__ == "__main__":
    main()