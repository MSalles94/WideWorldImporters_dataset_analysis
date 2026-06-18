import json
import logging
import pyodbc

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with open("config.json", "r") as f:
    config = json.load(f)

sql_cfg = config["sqlserver"]

conn_string = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={sql_cfg['host']},{sql_cfg['port']};"
    f"DATABASE={sql_cfg['database']};"
    f"UID={sql_cfg['user']};"
    f"PWD={sql_cfg['password']};"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_string)

    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")

    version = cursor.fetchone()[0]

    logging.info("✅ Conexão com SQL Server realizada com sucesso")
    logging.info(f"Versão: {version}")

    conn.close()

except Exception as e:
    logging.error(f"❌ Erro na conexão: {e}")