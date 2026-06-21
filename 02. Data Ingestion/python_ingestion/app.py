# import libs
from utils.database_manipulation import read_table,load_table,try_to_connect,ensure_schema
from utils.tables_map import map_source_schemas
from utils.logs_manager import define_log,map_log_folder
import os
 
#define the log folder with current datetime
log_file_path=map_log_folder()

#define a general log file
logger_pipeline=define_log('_pipeline_log',log_file_path)
logger_pipeline.info("Starting process: DATA INGESTION") 

#Test database connection
logger_pipeline.info("Checking SQL Server connection...")
logger_pipeline.info(f"-     Test result: {try_to_connect(MAX_RETRIES = 30)}")


#check if schema exists in postgress
schema_name='bronze' 
logger_pipeline.info(ensure_schema(schema_name=schema_name))

logger_pipeline.info(f" - Starting  schemas reading")

for source_schema_name,dict_tables in map_source_schemas.items():
    num_of_tables=len(dict_tables.keys())
    logger_pipeline.info(f"- Reading tables from schema: {source_schema_name} - {num_of_tables} tables")
    
    #start log file for this schema step
    logger_schema_step = define_log(f"schema_{source_schema_name}",log_file_path)
    logger_schema_step.info(f"Schema step - {source_schema_name} - {num_of_tables} tables")

    count_tables=0
    for  target_table_name,source_table_name in  dict_tables.items():
        
        count_tables += 1

        logger_pipeline.info(f"- {count_tables}   {target_table_name}")
        logger_schema_step.info('---------------------------------')
        logger_schema_step.info(f"Read table: {count_tables} - {source_table_name}")
        
        try:
            df =read_table(table_name=f"{source_schema_name}.{source_table_name}")
 
            logger_schema_step.info(
            f"  {len(df)} extracted rows from {os.getenv('SQL_SERVER_DB')}.{source_schema_name}.{source_table_name}"
            )

            logger_schema_step.info(f" Load data into {schema_name}.{target_table_name}")
            load_table(df,
                       table_name=target_table_name,
                       schema_name=schema_name)
            
            logger_schema_step.info(f"Table Ingestion Completed ")

        except Exception as e:
            logger_schema_step.error(f"Error in {target_table_name}: {e}")
            logger_pipeline.error(f"Error in {target_table_name}: {e}")
            


logger_pipeline.info(f"Data ingestion completed")