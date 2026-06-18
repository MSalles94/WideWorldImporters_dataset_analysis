# End to end analytics workflow

## Overview
<p>This project intents to demonstrate data skills by creating a complete analytics workflow. There is a relational model which will be remodeled into a dimensional structure. In the top of this a dashboard will bring some insights.</p>

<p>The data set we gonna use is called :<b>Wide World Importers dataset analysis</b>. </p>

<p>The main tools for this project:</p>

* Docker 
* SQL Server
* Python    
    * Pandas
    * Pyodbc
* Postgres
* PowerBI

## Steps
### [01. Explore Dataset](/01.%20Explore%20Dataset/)
* Use Docker to run two applications
    * SQL_server to host data
    * DBeaver application to interact
* Connect with the SQLServer using DBeaver Cloud
    * Restore the Wide World Importers sample database using a .bak file
* Explore data
    * Perform an explanatory analysis
    * Answer some business questions with some SQL

### [02. Data Ingestion](/02.%20Data%20Ingestion/)
* Use docker to run tree applications
    * SQL_server with the original data
    * Postgres to be our warehouse
    * Python_elt to operate a ingestion process
* save data in postgres

### [03. Build a DataWarehouse]()
* Extract data from the source system using Python
* Transform data into a dimensional model
* Load fact and dimension tables
* Validate the resulting data warehouse

### [04. Data Validation]()
* Validate KPIs against the source system
* Verify dimensional model consistency
* Perform data quality checks

### [05. Business Intelligence]()
* Connect the data warehouse to a BI tool
* Build dashboards
* Generate business insights

