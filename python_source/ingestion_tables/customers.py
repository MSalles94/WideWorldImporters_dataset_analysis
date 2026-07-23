from python_source.modules.data_base_connection import db_connection
from python_source.modules.utils import mapping_paths
from python_source.modules.log_control import create_log_object
from python_source.modules.metadata import metadata_configs

  

#define paths
path_obj=mapping_paths()
DATA_LAKE_PATH=path_obj.data_lake
LOG_PATH=path_obj.logs 

#configs for the extraction
ingestion_configs=metadata_configs()

dt_i=ingestion_configs.first_date
dt_f=ingestion_configs.last_date 
log_register=ingestion_configs.log_register
 
#start log
LOG_PATH= LOG_PATH if log_register else  LOG_PATH.with_name(f'customer.log')
logger=create_log_object( LOG_PATH)
 
# Extract 
def extract_customers():
 
    logger.mensage(
        "Starting extraction, table: customers"
    )
    logger.mensage(
            f"""
            Ingestion parameters:
                    -first_date: {dt_i}
                    -last_date: {dt_f}
                    -log register: {log_register} """
        )


    try:

        logger.mensage( "Connect to SQL Server"  )
        sqlserver_access=db_connection(database='sqlserver')
    

        query = f"""
       SELECT
            TOP 10
                CustomerID
                ,CustomerName
                ,BillToCustomerID
                ,CustomerCategoryID
                ,BuyingGroupID
                ,PrimaryContactPersonID
                ,AlternateContactPersonID
                ,DeliveryMethodID
                ,DeliveryCityID
                ,PostalCityID
                ,CreditLimit
                ,AccountOpenedDate
                ,StandardDiscountPercentage
                ,IsStatementSent
                ,IsOnCreditHold
                ,PaymentDays
                ,PhoneNumber
                ,FaxNumber
                ,DeliveryRun
                ,RunPosition
                ,WebsiteURL
                ,DeliveryAddressLine1
                ,DeliveryAddressLine2
                ,DeliveryPostalCode
                ,CAST(DeliveryLocation AS  NVARCHAR(MAX)) AS DeliveryLocation
                ,PostalAddressLine1
                ,PostalAddressLine2
                ,PostalPostalCode
                ,LastEditedBy
                ,ValidFrom
                ,ValidTo
        FROM WideWorldImporters.sales.Customers c 
        WHERE 1=1
            AND ValidFrom >= '{dt_i}'
            AND ValidFrom <= '{dt_f}'

        """


        logger.mensage("Execute query")

        df =sqlserver_access.execute_query(query)
          

        rows = len(df)
        logger.mensage(f"Rows extracted: {rows}")

        if rows == 0:
            logger.mensage("No rows extracted")
            return

        list_ingestion_months=sorted(df['ValidFrom'].map(lambda x: x.replace(day=1)).unique())
        for month_i in list_ingestion_months:
            year=month_i.year
            month=month_i.month 
             
            # save data
            year_partition=( DATA_LAKE_PATH /"customers"/ f"year={year}"  )
            month_partition=(year_partition / f"month={month}")
            file_path=(month_partition / "customers.parquet")
                #create dir
            month_partition.mkdir(
                    parents=True,
                    exist_ok=True
                ) 
    
    
            df.to_parquet(
                file_path,
                engine="pyarrow",
                index=False
            )

            logger.mensage(f"Saved: {file_path}" )

        logger.mensage( f"Ingestion finish" )

    except Exception as error:
        logger.mensage(f"Error: {error}")
        raise


 