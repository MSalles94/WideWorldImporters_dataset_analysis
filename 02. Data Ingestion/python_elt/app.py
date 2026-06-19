from connect_database import sqlserver_engine,postgres_engine
import logging
from pandas import read_sql
import datetime 

log_file = f"output/logs_{datetime.date.today()}.log"

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ],
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
tables={"customers": "Sales.Customers"}

for target_table, source_table in tables.items():

    try:
        logging.info(f"🔄 Extraindo: {source_table}")

        query = f"SELECT * FROM {source_table}"
        df = read_sql(query, sqlserver_engine)

        logging.info(f"📦 {target_table}: {len(df)} linhas extraídas")
        logging.info(f"Amostra da tabela {source_table}:\n{df.head(3)}")
 

    except Exception as e:
        logging.error(f"❌ Erro na tabela {target_table}: {e}")
