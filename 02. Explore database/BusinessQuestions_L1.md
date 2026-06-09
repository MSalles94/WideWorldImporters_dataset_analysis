
[<./02. Explore DataBase](../02.%20Explore%20database/README.md)

[<./02. Explore DataBase/Questions summary](../02.%20Explore%20database/businessQuestions.md) 

---
# Level 1 — Basic

<details>
<summary>1. Who are the top 10 customers by number of orders placed?</summary>

#### SQL Solution

```sql
SELECT 
	TOP 10
		o.CustomerID,
		c.CustomerName,
		count(*) AS ORDERS_
FROM WideWorldImporters.Sales.Orders AS o
	LEFT JOIN WideWorldImporters.Sales.Customers AS c
		ON o.CustomerID=c.CustomerID
GROUP BY 
	o.CustomerID,c.CustomerName
ORDER BY COUNT(*) DESC;
	
```
#### Output
|CustomerID|CustomerName|ORDERS_|
|----------|------------|-------|
|90|Tailspin Toys (Tolna, ND)|150|
|831|Bhaavan Rai|147|
|968|Anca Gogean|146|
|804|Aleksandrs Riekstins|145|
|405|Wingtip Toys (Bourbonnais, IL)|145|
|143|Tailspin Toys (Ashtabula, OH)|144|
|70|Tailspin Toys (New Baden, IL)|144|
|110|Tailspin Toys (North Crows Nest, IN)|143|
|183|Tailspin Toys (Tierra Verde, FL)|141|
|910|Elina Kaleja|140|


</details>

<details>
<summary>2. What are the top 10 best-selling products by quantity sold?</summary>

#### SQL Solution

```sql
SELECT 
	TOP 10
		ol.StockItemID,
		ol.Description, 
		SUM(ol.Quantity) AS Quantity_
FROM WideWorldImporters.Sales.OrderLines AS ol 	
GROUP BY 
	ol.StockItemID,
	ol.Description
ORDER BY SUM(ol.Quantity) DESC 	;
	
```
#### Output

|StockItemID|Description|Quantity_|
|-----------|-----------|---------|
|191|Black and orange fragile despatch tape 48mmx75m|207324|
|192|Black and orange fragile despatch tape 48mmx100m|193680|
|189|Clear packaging tape 48mmx75m|158626|
|188|3 kg Courier post bag (White) 300x190x95mm|152375|
|185|Shipping carton (Brown) 356x356x279mm|152125|
|184|Shipping carton (Brown) 305x305x305mm|151875|
|187|Express post box 5kg (White) 350x280x130mm|149825|
|177|Shipping carton (Brown) 413x285x187mm|147675|
|179|Shipping carton (Brown) 229x229x229mm|146375|
|186|Shipping carton (Brown) 457x457x457mm|144950|



</details>

<details>
<summary>3. What is the company's total revenue?</summary>

#### SQL Solution

```sql
SELECT  
	YEAR(i.InvoiceDate) AS YEAR_,
	SUM(il.ExtendedPrice) AS INVOICE_
FROM WideWorldImporters.Sales.invoices i
	LEFT JOIN WideWorldImporters.Sales.InvoiceLines il
		ON i.InvoiceID=il.InvoiceID
GROUP BY YEAR(InvoiceDate)
ORDER BY YEAR(i.InvoiceDate);
```

#### Output
 
|YEAR_|INVOICE_|
|-----|--------|
|2013|52563272.64|
|2014|57418916.89|
|2015|62090220.81|
|2016|25971029.11|

</details>

<details>
<summary>4. How many customers exist in each customer category?</summary>

#### SQL Solution

```sql
SELECT   
	cc.CustomerCategoryName,
	COUNT(*) AS CUSTOMERS_
FROM WideWorldImporters.Sales.Customers c 
	LEFT JOIN WideWorldImporters.Sales.CustomerCategories cc
		ON cc.CustomerCategoryID=c.CustomerCategoryID
GROUP BY cc.CustomerCategoryName
ORDER BY
	COUNT(*) DESC;
```

#### Output

|CustomerCategoryName|CUSTOMERS_|
|--------------------|----------|
|Novelty Shop|459|
|Supermarket|58|
|Computer Store|51|
|Gift Store|48|
|Corporate|47|


</details>

<details>
<summary>5. How many products exist in each product category?</summary>

### SQL Solution

```sql
SELECT   
	sg.StockGroupName,
	COUNT(*) AS ITEMS_
FROM WideWorldImporters.Warehouse.StockItemStockGroups sisg
	LEFT JOIN WideWorldImporters.Warehouse.StockGroups sg
		ON sg.StockGroupID=sisg.StockGroupID
GROUP BY sg.StockGroupName
ORDER BY	COUNT(*) DESC;
```

#### Output

Obs: the products may be in more than one group.

|StockGroupName|ITEMS_|
|--------------|------|
|Novelty Items|91|
|Computing Novelties|83|
|Clothing|74|
|Packaging Materials|67|
|Mugs|42|
|T-Shirts|26|
|Furry Footwear|24|
|Toys|21|
|USB Novelties|14|

</details>

<details>
<summary>6. Which are the top 10 provinces with the highest number of registered customers?</summary>

#### SQL Solution

```sql
SELECT TOP 10
	c2.CountryName,
	sp.StateProvinceName,
	--c.CityName,
	COUNT(*) AS CUSTOMERS_
FROM WideWorldImporters.Application.Cities c
	LEFT JOIN WideWorldImporters.Application.StateProvinces sp
		ON c.StateProvinceID=sp.StateProvinceID
	LEFT JOIN WideWorldImporters.Application.Countries c2
		ON c2.CountryID=sp.CountryID
	LEFT JOIN WideWorldImporters.Sales.Customers c3
		ON c3.PostalCityID=c.CityID
GROUP BY 
	c2.CountryName,
	sp.StateProvinceName
	--c.CityName
ORDER BY COUNT(*)DESC;
```

#### Output

|CountryName|StateProvinceName|CUSTOMERS_|
|-----------|-----------------|----------|
|United States|Texas|2396|
|United States|Pennsylvania|1830|
|United States|New York|1650|
|United States|California|1612|
|United States|Illinois|1532|
|United States|Ohio|1348|
|United States|Missouri|1261|
|United States|Wisconsin|1193|
|United States|Minnesota|1145|
|United States|Iowa|1138|

</details>

<details>
<summary>7. What was the total revenue by item category?</summary>

#### SQL Solution

```sql
SELECT 
	sg.StockGroupName,
	SUM(il.extendedPrice) AS INVOICE_
FROM WideWorldImporters.Sales.InvoiceLines il
	LEFT JOIN WideWorldImporters.Warehouse.StockItemStockGroups sisg
		ON sisg.StockItemID=il.StockItemID
	LEFT JOIN WideWorldImporters.Warehouse.StockGroups sg
		ON sg.StockGroupID=sisg.StockGroupID
GROUP BY sg.StockGroupName
ORDER BY SUM(il.extendedPrice) DESC
```

#### Output

|StockGroupName|INVOICE_|
|--------------|--------|
|Packaging Materials|115763819.96|
|Clothing|53407430.60|
|Computing Novelties|43013371.32|
|Novelty Items|40055230.49|
|T-Shirts|32736884.40|
|Toys|17338935.25|
|Furry Footwear|5904665.80|
|USB Novelties|5433733.42|
|Mugs|3647949.50|

</details>

<details>
<summary>8. What was the total revenue by month?</summary>

#### SQL Solution

```sql
SELECT  
	MONTH(i.InvoiceDate) AS MONTH_,
	SUM(il.ExtendedPrice) AS INVOICE_
FROM WideWorldImporters.Sales.invoices i
	LEFT JOIN WideWorldImporters.Sales.InvoiceLines il
		ON i.InvoiceID=il.InvoiceID
GROUP BY MONTH(InvoiceDate)
ORDER BY MONTH(i.InvoiceDate);
```

#### Output

|MONTH_|INVOICE_|
|------|--------|
|1|19179545.13|
|2|16605198.12|
|3|19429902.66|
|4|20448386.73|
|5|21216970.17|
|6|14779250.65|
|7|16472303.41|
|8|13247592.22|
|9|14173302.85|
|10|14585844.30|
|11|13576485.06|
|12|14328658.15|

</details>

<details>
<summary>9. Which is the invoice per salespeople registered in 2015?</summary>

#### SQL Solution

```sql
SELECT  
	p.FullName,
	SUM(ol.Quantity*ol.UnitPrice) AS SALES_VALUE
FROM WideWorldImporters.Sales.Orders o
	LEFT JOIN WideWorldImporters.Application.People p
		ON p.PersonID=o.SalespersonPersonID
	LEFT JOIN WideWorldImporters.Sales.OrderLines ol
		ON o.OrderID=ol.OrderID
WHERE 1=1
	AND o.OrderDate BETWEEN '2015-01-01' AND '2015-12-31'
GROUP BY p.FullName
ORDER BY SUM(ol.Quantity*ol.UnitPrice) DESC
```

#### Output

|FullName|SALES_VALUE|
|--------|-----------|
|Lily Code|5914162.35|
|Archer Lamble|5721441.35|
|Jack Potter|5704722.05|
|Hudson Hollinworth|5664518.25|
|Sophia Hinton|5578303.55|
|Hudson Onslow|5573308.70|
|Kayla Woodcock|5567103.40|
|Taj Shand|5423122.90|
|Anthony Grosse|5342283.60|
|Amy Trefl|5328921.30|

</details>

<details>
<summary>10. Which delivery methods are most frequently used by customers?</summary>

#### SQL Solution

```sql
SELECT
	dm.DeliveryMethodID,
	dm.DeliveryMethodName,
	count(*) CUSTOMERS_
FROM WideWorldImporters.Sales.Customers c
	LEFT JOIN WideWorldImporters.Application.DeliveryMethods dm
		ON dm.DeliveryMethodID=c.DeliveryMethodID
GROUP BY dm.DeliveryMethodName,dm.DeliveryMethodID

```

#### Output

|DeliveryMethodID|DeliveryMethodName|CUSTOMERS_|
|----------------|------------------|----------|
|3|Delivery Van|663|

</details>

---

[<./02. Explore DataBase](../02.%20Explore%20database/README.md)

[<./02. Explore DataBase/Questions summary](../02.%20Explore%20database/businessQuestions.md) 