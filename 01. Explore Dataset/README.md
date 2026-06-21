| [< Cover](../) |

---

# Explore dataset

<p>Before starting doing analysis we need an appropriated server to run the application to host the data simulating a real transactional system. </p>

  
## 1. Run applications in Docker 
 
<p>Docker is the tool for isolate applications satisfying it's dependences. Basically is a more secure and reproducible way to get things done.</p>

### 1.1 Configure docker-compose file

<p> To make it happend we need a file .yml to configure owr enviroment <a href="./docker-compose.yml">docker-compose.yml</a>. With this file docker is able to create the docker images and start running the applications in containers.
</p>
 
<p>In this file we may find configuration parameters to define: </p>

* SQL Server container
    * with an external volume to persist data
    * define a directory were the database backup is (we will detail it later)
    * connections parameters of the database ( password and port)
* DBeaver container 
    * port
    * external volume 
* Network to make possible both applications interact

### 1.2. Create external volumes

<p>Before run docker, create a volume to be shared between projects. This way we may connect with the same docker volume from different docker projects.</p>

```bash
# create a docker volume
    # observe that both are configured in docker-compose.yml

docker volume create sql_server_ERP
docker volume create dbeaver_cred
```

### 1.3. Run Docker

<p>Once the configuretion file is done we only have to command to run docker: </p>

```bash
# this command build up an run docker
    # it should be used in same directory .yml file is

docker-compose up -d
```

<p>Now both containers are running.</p>

## 2 Connect DBeaver with SQL Server

<p> To acces DBeaver Cloud we need to open the browser and get the address baset in the configured port.</p>

```bash
# to get info about the running containers

docker ps
```
<p> Once in the DBeaver web we need two little condigurations to access the database.</p>

### 2.1. Configure the access to DBeaver

<p>It's the easiest part. Only choose a username and password.</p>


### 2.2. Define the connection with SQL Server

<p>Now we need to create a connection with the database.</p>

<img 
src="../images/1.2_create_connection.png" 
width="800">

<p>We need the following parameters:
</p>

* Driver = sqlserver
* Host = sqlserver (container name)
* Port = 1433 (defined in docker)
* User name = sa
* Password = Teste1234_ (defined in docker) 

<p>Now we can perform SQL commands to interact with the SQL server.</p>

## 3. Restore data using .bak

<p>.bak files are backups formats for databases. Once the file accessible for our SQL Server container (defined in docker-compose), we may operate a restoration process </p>


### 3.1. Download the database backup .bak

<p>The data we are working with is a knon sample called WideWorldImporters from Microsoft. It's a fictional data used to demonstrate applications in SQL Server</p>
<p>This data simulate a basic relational database of a ditribution company.</p>
<p>As it's a popular dataset there exists many sources. We gonna take it from the github repo: <a href="https://github.com/Microsoft/sql-server-samples">SQL Server Samples</a>. </p> 

```bash
# save the .bak file
    # it should be saved in the same directory we configured to be the backup in .yml 

wget https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak
```

### 3.2. Restore database

<p>Using SQL we may restore the database in SQL server once the .bak directory is mapped as a volume. Perform the following commands to populate SQL server with .bak data.</p>

```sql
-- discover the logic names
    -- This names will be used in following command
RESTORE FILELISTONLY
FROM DISK = '/var/opt/mssql/backup/WideWorldImporters-Full.bak';
```

<p>Second we run the restoration command. </p>

```sql
--restore database using .bak
RESTORE DATABASE WideWorldImporters
FROM DISK = '/var/opt/mssql/backup/WideWorldImporters-Full.bak'
WITH
MOVE 'WWI_Primary' TO '/var/opt/mssql/data/WideWorldImporters.mdf',
MOVE 'WWI_UserData' TO '/var/opt/mssql/data/WideWorldImporters_UserData.ndf',
MOVE 'WWI_Log' TO '/var/opt/mssql/data/WideWorldImporters.ldf',
MOVE 'WWI_InMemory_Data_1' TO '/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1.ndf',
REPLACE,
STATS = 10;

```

<p> Now the data is ready to be explored.</p>

```sql
-- check if the database is created
    --look for the name: WideWorldImporters

SELECT name
FROM sys.databases
ORDER BY name;

```

<p>OBS: In DBeaver cloud, if the left tree doesn't update with the new database try to reconnect the app.</p>

<img 
src="../images/1.3_DBeaver_ready.png" 
width="800"> 

## 4. Data Exploration

<p> This step deals with data exploration. We will do it by answering some busines questions, in this process we will understand the business and start to think about data modeling.</p>

 
### 4.1. Business questions 

<p>Asking questions to the dataset is a good way to understand data. This step is focused in answer some business questions using SQL.</p>
 
<p>The questions may be found here: <a href="./businessQuestions/README.md">Questions summary</a> . Here we have the solutions organized by level of difficulty in SQL:</p>

* [Level 1](./businessQuestions/BusinessQuestions_L1.md) - Basic
* [Level 2](./businessQuestions/BusinessQuestions_L2.md) - Intermediate
* [Level 3](./businessQuestions/BusinessQuestions_L3.md) - Advanced
* [Level 4](./businessQuestions/BusinessQuestions_L4.md) - Data Warehouse & Dashboard Design

### 4.2. Dataset Overview

<p>Here we map and describe the known information about the transactional data.</p> 

<p>The details are here:  <a href="./Data_overview.md">Dataset Overview</a>
</p>


---
| [< Cover](../) |
