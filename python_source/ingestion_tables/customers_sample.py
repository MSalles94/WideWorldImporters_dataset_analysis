import logging
from pathlib import Path
from datetime import datetime

import pandas as pd
import pyodbc


# -------------------------
# Configuração de caminhos
# -------------------------

BASE_PATH = Path(__file__).parent

DATA_LAKE_PATH = (
    BASE_PATH
    / "data_lake"
    / "bronze"
    / "customers"
)

LOG_PATH = (
    BASE_PATH
    / "logs"
    / "ingestion.log"
)


DATA_LAKE_PATH.mkdir(
    parents=True,
    exist_ok=True
)

LOG_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)


# -------------------------
# Configuração de logging
# -------------------------

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)


logger = logging.getLogger(__name__)


# -------------------------
# Conexão SQL Server
# -------------------------

def get_connection():

    logger.info(
        "Criando conexão SQL Server"
    )

    conn = pyodbc.connect(
        """
        DRIVER={ODBC Driver 18 for SQL Server};
        SERVER=localhost;
        DATABASE=WideWorldImporters;
        UID=sa;
        PWD=SuaSenha;
        TrustServerCertificate=yes;
        """
    )

    return conn



# -------------------------
# Extração
# -------------------------

def extract_customers():

    start_time = datetime.now()

    logger.info(
        "Iniciando ingestão customers"
    )


    try:

        conn = get_connection()


        query = """

        SELECT *
        FROM Sales.Customers

        """


        logger.info(
            "Executando query customers"
        )


        df = pd.read_sql(
            query,
            conn
        )


        rows = len(df)


        logger.info(
            f"Registros extraídos: {rows}"
        )


        if rows == 0:

            logger.warning(
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


        logger.info(
            f"Arquivo salvo: {file_path}"
        )


        elapsed = (
            datetime.now()
            - start_time
        )


        logger.info(
            f"Ingestão finalizada em {elapsed}"
        )



    except Exception as error:


        logger.exception(
            f"Erro na ingestão customers: {error}"
        )


        raise



    finally:

        if "conn" in locals():

            conn.close()

            logger.info(
                "Conexão encerrada"
            )



# -------------------------
# Main
# -------------------------

if __name__ == "__main__":

    extract_customers()