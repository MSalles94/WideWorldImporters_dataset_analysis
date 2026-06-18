# Dataset Overview

<p>The WideWorldImporters is a normalized dataset that simulates a transational system. It follows the normal forms to improve data storage.</p>

## 1. Schemas and tables

<p>This dataset is organized basically in 4 schemas.</p>

## 1.1. Application
<p> This schema has tables to register basic entities of the company. We can see normalized generic tables about internal information.</p>
<p> We can see geographical data, a table with employees information. Also some master data about tables from others schemas.</p>

* People
* Cities 
    * StateProvinces
        * Countries
* DeliveryMethods
* PaymentMethods 
* TransactionTypes

### 1.2. Sales
<p>Sales schema is about the relation with customers.</p>
<p>We may find customer database with some reference entities. Also we have Orders, Invoices and Transactions, tables that register facts in time. </p>
 
* Customers 
    * CustomerCategories
    * BuyingGroups
* Orders 
    * OrderLines
* Invoices
    * InvoiceLines
* CustomerTransactions


### 1.3. Warehouse Schema
<p>Here we have data about products and inventory balance.</p>
<p>There are many reference entities about products and historic information about material movement.</p>

* StockItems
    * StockItemStockGroups
        * StockGroups
    * Colors 
    * ColdRoomTemperatures
    * PackageTypes 
* StockItemHoldings
* StockItemTransactions
    * VehicleTemperatures

### 1.4. Purchasing Schema

<p>Finally we have this schema with data about suppliers relations.</p>
<p>The main info here is suppliers master data and historical registers of materials purchase.</p>

* Suppliers
    * SupplierCategories
* PurchaseOrders
    * PurchaseOrderLines
* SupplierTransactions 
 