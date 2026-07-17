from python_source.modules.data_base_connection import database_connection
from python_source.modules.utils import define_path
from python_source.modules.log_control import create_log_object
 
import pandas as pd


path_obj=define_path(table_name='customers')
DATA_LAKE_PATH=path_obj.DATA_LAKE_PATH
LOG_PATH=path_obj.LOG_PATH
 
logger=create_log_object( LOG_PATH)

  
# -------------------------
# Conexão SQL Server
# -------------------------

def get_connection():

    logger.mensage(
        "Criando conexão SQL Server"
    )
    
    sqlserver_access=database_connection(database='sqlserver')
    conn=sqlserver_access.conn

    
    return conn



# -------------------------
# Extração
# -------------------------

def extract_customers():
 
    logger.mensage(
        "Iniciando ingestão customers"
    )


    try:

        conn = get_connection()


        query = """

       SELECT
            top 10
            *
        from WideWorldImporters.sales.Customers c 

        """


        logger.mensage(
            "Executando query customers"
        )


        df = pd.read_sql(
            query,
            conn
        )


        rows = len(df)


        logger.mensage(
            f"Registros extraídos: {rows}"
        )


        if rows == 0:

            logger.mensage(
                "Nenhum registro encontrado"
            )

            return



        # -------------------------
        # Salvando parquet
        # -------------------------

        file_path = (
            DATA_LAKE_PATH
            /
            "customers.parquet"
        )


        df.to_parquet(
            file_path,
            engine="pyarrow",
            index=False
        )


        logger.mensage(
            f"Arquivo salvo: {file_path}"
        )

 

        logger.mensage(
            f"Ingestão finalizada"
        )



    except Exception as error:


        logger.mensage(
            f"Erro na ingestão customers: {error}"
        )


        raise



    finally:

        if "conn" in locals():

            conn.close()

            logger.mensage(
                "Conexão encerrada"
            )



 