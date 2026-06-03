--Connect DBeaver
-- Host: sqlserver
-- Port: 1433
-- User: sa
-- Password: Teste1234_
-- Database: WideWorldImporters



-- check files
RESTORE FILELISTONLY
FROM DISK = '/var/opt/mssql/backup/WideWorldImporters-Full.bak';
GO

-- restore data
RESTORE DATABASE WideWorldImporters
FROM DISK = '/var/opt/mssql/backup/WideWorldImporters-Full.bak'
WITH
MOVE 'WWI_Primary'
    TO '/var/opt/mssql/data/WideWorldImporters.mdf',

MOVE 'WWI_UserData'
    TO '/var/opt/mssql/data/WideWorldImporters_UserData.ndf',

MOVE 'WWI_Log'
    TO '/var/opt/mssql/data/WideWorldImporters.ldf',

MOVE 'WWI_InMemory_Data_1'
    TO '/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1',

REPLACE,
STATS = 10;
GO

--select database
use WideWorldImporters;


--explore database
SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_SCHEMA, TABLE_NAME
