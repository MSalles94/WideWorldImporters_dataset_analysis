from python_source.modules.data_base_connection import database_connection
from python_source.modules.utils import mapping_paths
from python_source.modules.log_control import create_log_object
from python_source.modules.metadata import config_dateRange
 
import pandas as pd

#define paths
path_obj=mapping_paths()
DATA_LAKE_PATH=path_obj.data_lake
LOG_PATH=path_obj.logs 

#start log
logger=create_log_object( LOG_PATH)

#date configs for extraction
dt_i,dt_f,year,month=config_dateRange()
 
 
# Extract 
def extract_customers():
 
    logger.mensage(
        "Starting extraction, table: customers"
    )


    try:

        logger.mensage( "Connect to SQL Server"  )
        sqlserver_access=database_connection(database='sqlserver')
        conn=sqlserver_access.conn
 


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
            AND ValidFrom >= {dt_i}
            AND ValidFrom <= {dt_f}

        """


        logger.mensage("Execute query")


        df = pd.read_sql(
            query,
            conn
        )


        rows = len(df)
        logger.mensage(f"Rows extracted: {rows}")

        if rows == 0:
            logger.mensage("No rows extracted")
            return
 
        # save data
        year_partition=( DATA_LAKE_PATH /"customer"/ f"year={year}"  )
        month_partition=(year_partition / f"month={month}")
        file_path=(month_partition / "customers.parquet")
 
 
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

    finally:
        if "conn" in locals():
            conn.close()
            logger.mensage("Disconnect from SQL server")

 