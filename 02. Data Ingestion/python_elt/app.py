# import libs
from utils.database_manipulation import read_table,load_table,try_to_connect,ensure_schema
from utils.tables_map import tables_map
from utils.logs_manager import define_log,map_log_folder
import os
 
log_file_path=map_log_folder()

#define a log file
logger_pipeline=define_log('_pipeline_log',log_file_path)
logger_pipeline.info("Starting data ingestion process") 

#Test database connection
logger_pipeline.info("Check postgress connection")
logger_pipeline.info(f"     Connection test: {try_to_connect(MAX_RETRIES = 30)}")


#check if schema exists
schema_name='bronze' 
logger_pipeline.info(ensure_schema(schema_name=schema_name)    )
 

# loop to ingest data - extract and load
for target_table, source_table in tables_map.items():
    #start log
    logger_pipeline.info(f"Starting  {target_table} step")
    logger = define_log(target_table,log_file_path)
     

    try:
        logger.info(f'Starting ELT process in the table: {target_table}')
        logger.info(f'  Full reference: {os.getenv('POSTGRES_DB')}.{schema_name}.{target_table}')
        logger.info(f"  Extracting data from {os.getenv('SQL_SERVER_DB')}.{source_table}")
        logger.info('----------------------------------------------------------------------')
        
        #read
        logger.info(f"Read data from table: {source_table}")
        df =read_table(table_name=source_table)

        logger.info(
            f"  {len(df)} extracted rows from {os.getenv('SQL_SERVER_DB')}.{source_table}"
        )

        #load
        logger.info(f"Load data into table: {schema_name}")
        load_table(df,table_name=target_table,schema_name=schema_name)

        logger.info(f"{ target_table} - Process Completed")

    except Exception as e:
        logger.error(f"Error in {target_table}: {e}")

logger_pipeline.info(f"Data ingestion completed")