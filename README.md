# Wide World Importers dataset analysis

## Overview
<p>This project intents to demonstrate data skills by creating a complete analytics workflow. There is a relational model which will be remodeled into a dimensional structure. In the top of this a dashboard will bring some insights.</p>

<p>The main tools for this project:</p>

* Docker 
* SQL Server
* Python    
    * Pandas
    * Pyodbc
* SQLite
* PowerBI

## Steps
### [01. Infrastructure](/01.%20Infrastructure/)
* Run SQL server using Docker
* Connect with the SQLServer using DBeaver Cloud
* Restore the Wide World Importers sample database

### [02. Explore the Database](/02.%20Explore%20the%20database/)
* Understand the data and relationships
* Perform an explanatory analysis
* Answer some business questions with some SQL

### [03. Define Business requirements]()
* Identify business requirements
* Define metrics and KPIs
* Determine analytical dimensions

### [04. Build a DataWarehouse]()
* Extract data from the source system using Python
* Transform data into a dimensional model
* Load fact and dimension tables
* Validate the resulting data warehouse

### [05. Data Validation]()
* Validate KPIs against the source system
* Verify dimensional model consistency
* Perform data quality checks

### [06. Business Intelligence]()
* Connect the data warehouse to a BI tool
* Build dashboards
* Generate business insights

