import os
from sqlalchemy import create_engine
 
sqlserver_engine = create_engine(
    f"mssql+pymssql://"
    f"{os.getenv('SQL_SERVER_USER')}:"
    f"{os.getenv('SQL_SERVER_PASSWORD')}"
    f"@{os.getenv('SQL_SERVER_HOST')}/WideWorldImporters"
)

postgres_engine = create_engine(
    f"postgresql+psycopg://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}"
    f"@postgres:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)
