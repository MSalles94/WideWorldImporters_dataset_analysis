# Setup

1. dowload .bak data to populate the database


```bash
#move to the directory
cd data_lake/

#download the file
wget https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak

```
2. create docker volumes

```bash
#create the external volumes
docker volume create postgres_warehouse
docker volume create sql_server_ERP
docker volume create dbeaver_cred

```

3. start docker

```bash
#start docker containers
docker compose up -d

```

4. populate the SQL server with .bak

Use the link http://127.0.0.1:8978/ to connect in dbeaver application.

```sql
--using the dbeaver port access the application



```



