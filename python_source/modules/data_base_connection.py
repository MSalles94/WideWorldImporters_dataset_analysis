import os
import pyodbc
import urllib.parse
from sqlalchemy import create_engine
from pandas import read_sql

class database_connection():
    #based in pyodbc
    def __init__(self,database='sqlserver'):
        self.database=database
        self.__define_connection_string()
        self.__connect()

 

    def __define_connection_string(self):
        database=self.database

        if database=='sqlserver': 
            connection_string = f"""
                    DRIVER={{ODBC Driver 18 for SQL Server}};
                    SERVER={os.getenv("SQL_SERVER_HOST")};
                    DATABASE={os.getenv("SQL_SERVER_DB")};
                    UID={os.getenv("SQL_SERVER_USER")};
                    PWD={os.getenv("SQL_SERVER_PASSWORD")};
                    TrustServerCertificate=yes;
                """
        elif database=='postgres':
            connection_string = f"""
                    DRIVER={{ODBC Driver 18 for SQL Server}};
                    SERVER={os.getenv("SQL_SERVER_HOST")};
                    DATABASE={os.getenv("SQL_SERVER_DB")};
                    UID={os.getenv("SQL_SERVER_USER")};
                    PWD={os.getenv("SQL_SERVER_PASSWORD")};
                    TrustServerCertificate=yes;
                """

        else :
            pass

        self.connection_string=connection_string


    def __connect(self):

        try: 
            self.conn=pyodbc.connect(
                            self.connection_string
                        )
            print(f'- {self.database} connected')
        except Exception as e:
            print('- connection fail')
            print(f"""error: 
                    {e}""")


#-----------------------------------------------------------------------------
class db_connection():
    #based in sqlalchemy
    def __init__(self,database='sqlserver'):

        if database=='sqlserver': 

            connection_string = f"""
                                DRIVER={{ODBC Driver 18 for SQL Server}};
                                SERVER={os.getenv("SQL_SERVER_HOST")};
                                DATABASE={os.getenv("SQL_SERVER_DB")};
                                UID={os.getenv("SQL_SERVER_USER")};
                                PWD={os.getenv("SQL_SERVER_PASSWORD")};
                                TrustServerCertificate=yes;
                            """

            params = urllib.parse.quote_plus(connection_string )

            self.engine = create_engine(
                f"mssql+pyodbc:///?odbc_connect={params}",
                fast_executemany=True
            )
            
        elif database=='postgres':
            pass

    def execute_query(self,command):

        with self.engine.connect() as conn:

            
            df = read_sql(command, conn)

        return df