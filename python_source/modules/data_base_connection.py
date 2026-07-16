import os
import pyodbc

class database_connection():
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
        except:
            print('- connection fail')