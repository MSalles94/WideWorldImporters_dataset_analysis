import os
from sqlalchemy import create_engine,text
import time
from pandas import read_sql
 
sqlserver_engine = create_engine(
    f"mssql+pymssql://"
    f"{os.getenv('SQL_SERVER_USER')}:"
    f"{os.getenv('SQL_SERVER_PASSWORD')}"
    f"@{os.getenv('SQL_SERVER_HOST')}/{os.getenv('SQL_SERVER_DB')}"
)

postgres_engine = create_engine(
    f"postgresql+psycopg://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}"
    f"@postgres:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)

def try_to_connect(MAX_RETRIES = 30):
    # func to test sql server connection
    response=False
    for attempt in range(MAX_RETRIES):
        try:
            with sqlserver_engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            print("SQL Server ready")
            response=True
            break

        except Exception:
            print(f"Waiting SQL Server ({attempt+1}/{MAX_RETRIES})")
            time.sleep(5)

    else:
        response=False
        raise Exception("Could not connect to SQL Server")
    response=('The Database connection is ready' 
                    if response 
                    else 'could not connect')
    return response

def ensure_schema(engine=postgres_engine, schema_name='bronze'):
    #func to verify the schema existence and create it
    
    with engine.begin() as conn:
        schema_exists = conn.execute(
            text("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.schemata
                    WHERE schema_name = :schema_name
                )
            """),
            {"schema_name": schema_name}
        ).scalar()

        if not schema_exists:
            conn.execute(
                text(f"CREATE SCHEMA {schema_name}")
            )

        response =(f'Schema verification: {schema_name} schema already exists' 
                    if schema_exists 
                    else f'Schema creation - {schema_name} schema')

        return response

def read_table(table_name,engine=sqlserver_engine):
    query=f""" 
            SELECT TOP 99  
                GETDATE() AS extraction_datetime,
                * 
            FROM {table_name} """
    df = read_sql(query, engine)
    return df

def load_table(df,table_name,schema_name,engine=postgres_engine):
    df.to_sql(
            name=table_name,
            schema=schema_name,
            con=engine,
            if_exists="replace",
            index=False
        )
    return
