
[< Back ](../02.%20Explore%20database/README.md)

---

# Business Questions
<p> For better understanding the database we answer some business questions.</p>

## Level 1 — Basic

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

## Level 2 — Intermediate

<details>
<summary>11. Which customers generated the highest revenue for the company?</summary>

#### SQL Solution

```sql
SELECT
	TOP 1
		c.CustomerID,
		c.CustomerName,
		sum(il.extendedprice) AS INVOICE_
FROM WideWorldImporters.Sales.InvoiceLines il
	LEFT JOIN WideWorldImporters.Sales.Invoices i
		ON i.InvoiceID=il.InvoiceID
	LEFT JOIN WideWorldImporters.Sales.Orders o
		ON i.OrderID=o.OrderID
	LEFT JOIN WideWorldImporters.Sales.Customers c
		ON c.CustomerID=o.CustomerID
GROUP BY c.CustomerName,c.CustomerID
ORDER BY sum(il.extendedprice) DESC
```

#### Output

|CustomerID|CustomerName|INVOICE_|
|----------|------------|--------|
|149|Tailspin Toys (Inguadona, MN)|438689.81|

</details>

<details>
<summary>12. Which products generated the highest total revenue?</summary>

#### SQL Solution

```sql
SELECT
	TOP 1
		il.StockItemID,
		il.Description,
		sum(il.extendedprice) AS INVOICE_
FROM WideWorldImporters.Sales.InvoiceLines il
GROUP BY il.StockItemID,il.Description
ORDER BY sum(il.extendedprice) DESC
```

#### Output

|StockItemID|Description|INVOICE_|
|-----------|-----------|--------|
|215|Air cushion machine (Blue)|12773338.65|

</details>

<details>
<summary>13. What is the average order value per customer?</summary>

#### SQL Solution

```sql
SELECT
		top 10 --LIMIT IT 
	C.CustomerID,
	c.CustomerName,
	SUM(ol.Quantity*ol.UnitPrice)/count(distinct o.OrderID) AS AVG_ORD_VALUE
FROM WideWorldImporters.Sales.Orders o
	LEFT JOIN WideWorldImporters.Sales.OrderLines ol
		ON o.OrderID=ol.OrderID
	LEFT JOIN WideWorldImporters.Sales.Customers c
		ON C.CustomerID=o.CustomerID
GROUP BY c.CustomerName,c.CustomerID 
ORDER BY SUM(ol.Quantity*ol.UnitPrice)/count(distinct o.OrderID)  DESC 
 ```

#### Output

|CustomerID|CustomerName|AVG_ORD_VALUE|
|----------|------------|-------------|
|1058|Jaroslav Fisar|3896.600000|
|1056|Kalyani Benjaree|3446.803846|
|109|Tailspin Toys (South Laguna, CA)|3358.154736|
|1036|Erik Malk|3322.660000|
|996|Laszlo Gardenier|3249.998181|
|945|Hoc Tran|3249.642708|
|40|Tailspin Toys (Impact, TX)|3200.582038|
|977|Mauno Laurila|3143.248333|
|480|Wingtip Toys (Wapinitia, OR)|3096.135652|
|1006|Taj Syme|3065.933009|



</details>

<details>
<summary>14. Which cities have the highest average revenue per customer?</summary>

#### SQL Solution

```sql
SELECT
		top 10 --LIMIT IT 
	c2.CityID,
	c2.CityName,
	SUM(ol.Quantity*ol.UnitPrice)/count(distinct c.CustomerID) AS AVG_CUSTOMER_REV
FROM WideWorldImporters.Sales.Orders o
	LEFT JOIN WideWorldImporters.Sales.OrderLines ol
		ON o.OrderID=ol.OrderID
	LEFT JOIN WideWorldImporters.Sales.Customers c
		ON C.CustomerID=o.CustomerID
	LEFT JOIN WideWorldImporters.Application.Cities c2
		ON c2.CityID=c.PostalCityID
GROUP BY c2.CityID,	c2.CityName
ORDER BY SUM(ol.Quantity*ol.UnitPrice)/count(distinct c.CustomerID) DESC
```

#### Output

|CityID|CityName|AVG_CUSTOMER_REV|
|------|--------|----------------|
|16557|Inguadona|384393.350000|
|22453|Minidoka|379660.700000|
|24590|North Eaton|377189.800000|
|30663|Sarversville|372350.000000|
|34422|Trilby|368067.450000|
|19908|Long Meadow|367258.500000|
|21161|Mary Esther|366883.750000|
|8296|Cuyamungue|365915.450000|
|30387|San Jacinto|365330.950000|
|23026|Morrison Bluff|360652.800000|

</details>

<details>
<summary>15. What is the percentage contribution of each product category to total revenue?</summary>

#### SQL Solution

```sql
SELECT   
	sg.StockGroupName,
	SUM(ol.Quantity*ol.UnitPrice)/ SUM(SUM(ol.Quantity*ol.UnitPrice)) OVER () AS PERCENT_REVENUE
FROM WideWorldImporters.Warehouse.StockItemStockGroups sisg
	LEFT JOIN WideWorldImporters.Warehouse.StockGroups sg
		ON sg.StockGroupID=sisg.StockGroupID
	LEFT JOIN WideWorldImporters.Sales.OrderLines ol
		ON ol.StockItemID=sisg.StockItemID
GROUP BY sg.StockGroupName
ORDER BY	SUM(ol.Quantity*ol.UnitPrice) DESC;
```

#### Output

OBS: Remembering that a product may have more than one category.

|StockGroupName|PERCENT_REVENUE|
|--------------|---------------|
|Packaging Materials|0.353044|
|Clothing|0.174186|
|Computing Novelties|0.142933|
|Novelty Items|0.120607|
|T-Shirts|0.112035|
|Toys|0.052133|
|Furry Footwear|0.017753|
|USB Novelties|0.016337|
|Mugs|0.010968|

</details>

<details>
<summary>16. Which customers have not made purchases during the last month available in the dataset?</summary>

#### SQL Solution

```sql
WITH max_date AS (
        SELECT 
            DATEADD (MONTH,-1,MAX(o.OrderDate)) AS max_date
        FROM WideWorldImporters.Sales.Orders o
    ),
	last_purchase as(
	SELECT 
		o.CustomerID,
		MAX(o.OrderDate) AS max_order_date
	FROM WideWorldImporters.Sales.Orders o
	GROUP BY o.CustomerID)
SELECT 
	c.CustomerID,
	c.CustomerName,
	lp.max_order_date AS last_purchase,
	md.max_date AS filter_date
FROM last_purchase lp
	CROSS JOIN max_date md
	LEFT JOIN WideWorldImporters.Sales.Customers c
		ON c.CustomerID=lp.customerid
WHERE 1=1
	AND max_order_date <max_date
ORDER BY max_order_date
```

#### Output

|CustomerID|CustomerName|last_purchase|filter_date|
|----------|------------|-------------|-----------|
|905|Sara Huiting|2016-03-31|2016-04-30|
|66|Tailspin Toys (Madaket, MA)|2016-04-11|2016-04-30|
|128|Tailspin Toys (East Portal, CO)|2016-04-12|2016-04-30|
|15|Tailspin Toys (Batson, TX)|2016-04-13|2016-04-30|
|130|Tailspin Toys (Maple Shade, NJ)|2016-04-13|2016-04-30|
|131|Tailspin Toys (Kwethluk, AK)|2016-04-13|2016-04-30|
|467|Wingtip Toys (Mahaffey, PA)|2016-04-14|2016-04-30|
|97|Tailspin Toys (Manchester Center, VT)|2016-04-14|2016-04-30|
|811|Surendra Sahu|2016-04-18|2016-04-30|
|484|Wingtip Toys (Mauldin, SC)|2016-04-18|2016-04-30|
|936|Ludmila Smidova|2016-04-18|2016-04-30|
|946|David safranek|2016-04-19|2016-04-30|
|957|Hee-Young Suh|2016-04-19|2016-04-30|
|973|Kumar Kamei|2016-04-19|2016-04-30|
|998|Mahavir Sonkar|2016-04-20|2016-04-30|
|1030|Chompoo Atitarn|2016-04-21|2016-04-30|
|160|Tailspin Toys (Crary, ND)|2016-04-25|2016-04-30|
|190|Tailspin Toys (Teutopolis, IL)|2016-04-25|2016-04-30|
|969|Staffan Persson|2016-04-26|2016-04-30|
|932|Nicolo Cattaneo|2016-04-26|2016-04-30|
|809|Madhu Dwivedi|2016-04-26|2016-04-30|
|517|Wingtip Toys (Licking, MO)|2016-04-26|2016-04-30|
|111|Tailspin Toys (Oriole Beach, FL)|2016-04-27|2016-04-30|
|93|Tailspin Toys (Clewiston, FL)|2016-04-27|2016-04-30|
|421|Wingtip Toys (Highland Home, AL)|2016-04-27|2016-04-30|
|573|Wingtip Toys (Marin City, CA)|2016-04-28|2016-04-30|
|599|Wingtip Toys (Dickworsham, TX)|2016-04-28|2016-04-30|
|503|Wingtip Toys (Valhalla, NC)|2016-04-28|2016-04-30|
|4|Tailspin Toys (Medicine Lodge, KS)|2016-04-28|2016-04-30|
|898|Gopalgobinda Sikdar|2016-04-29|2016-04-30|
|892|Bahaar Asef zade|2016-04-29|2016-04-30|
|924|Eva Schulteisz|2016-04-29|2016-04-30|
|174|Tailspin Toys (Astor Park, FL)|2016-04-29|2016-04-30|
|30|Tailspin Toys (Koontzville, WA)|2016-04-29|2016-04-30|
|979|Melani Ravlen|2016-04-29|2016-04-30|
|816|Harsha Huq|2016-04-29|2016-04-30|
|181|Tailspin Toys (Heilwood, PA)|2016-04-29|2016-04-30|

</details>

<details>
<summary>17. Is there seasonality in sales? Which months show the highest and lowest revenue?</summary>

### About sazonality

#### SQL Solution

```sql
WITH TABLE_ AS (
	SELECT 
		YEAR(o.OrderDate) AS YEAR_,
		MONTH(o.OrderDate) as MONTH_,
		 SUM( ol.Quantity*ol.UnitPrice) AS REVENUE
	FROM WideWorldImporters.Sales.Orders o
		LEFT JOIN WideWorldImporters.Sales.OrderLines ol
			ON ol.OrderID=O.ORDERID
	GROUP BY MONTH(o.OrderDate),YEAR(o.OrderDate) 
	 ),
month_rev_prcnt AS ( 
	SELECT YEAR_,MONTH_,REVENUE/SUM(REVENUE) OVER (PARTITION BY YEAR_) AS SHARE
	FROM TABLE_
	)
SELECT 
	MONTH_,
	ROUND(SUM(CASE WHEN YEAR_=2013 THEN SHARE END)*100,2)  AS SHARE_2013,
	ROUND(SUM(CASE WHEN YEAR_=2014 THEN SHARE END)*100,2)  AS SHARE_2014,
	ROUND( SUM(CASE WHEN YEAR_=2015 THEN SHARE END)*100,2)  AS SHARE_2015
FROM month_rev_prcnt
GROUP BY MONTH_
ORDER BY MONTH_
```

#### Output

* Doesn't seem there is any relevant sazonal effect. every month has between 6 and 9 % of share in the year. 

|MONTH_|SHARE_2013|SHARE_2014|SHARE_2015|
|------|----------|----------|----------|
|1|8.150000|8.160000|8.160000|
|2|6.010000|6.940000|7.720000|
|3|8.450000|7.680000|8.320000|
|4|8.860000|8.180000|9.360000|
|5|9.720000|9.230000|8.310000|
|6|8.840000|8.600000|8.410000|
|7|9.590000|9.550000|9.570000|
|8|7.670000|8.150000|7.290000|
|9|8.340000|7.720000|8.670000|
|10|8.270000|8.950000|8.340000|
|11|8.140000|8.070000|7.600000|
|12|7.940000|8.760000|8.250000|

### Max and Min months 

#### SQL Solution


```sql
WITH TABLE_ AS (
	SELECT 
		YEAR(o.OrderDate) AS YEAR_,
		MONTH(o.OrderDate) as MONTH_,
		 SUM( ol.Quantity*ol.UnitPrice) AS REVENUE
	FROM WideWorldImporters.Sales.Orders o
		LEFT JOIN WideWorldImporters.Sales.OrderLines ol
			ON ol.OrderID=O.ORDERID
	GROUP BY MONTH(o.OrderDate),YEAR(o.OrderDate) 
	 ),
RANK_TABLE AS (SELECT 
	*,
	ROW_NUMBER() OVER (ORDER BY REVENUE ASC) AS RANK_MIN,
	ROW_NUMBER() OVER (ORDER BY REVENUE DESC) AS RANK_MAX
FROM TABLE_
WHERE 1=1)
SELECT *
FROM RANK_TABLE
WHERE RANK_MIN=1 OR RANK_MAX =1
```

#### Output

|YEAR_|MONTH_|REVENUE|RANK_MIN|RANK_MAX|
|-----|------|-------|--------|--------|
|2015|7|5339212.00|41|1|
|2013|2|2821282.20|1|41|

</details>

<details>
<summary>18. What is the average time between order placement and delivery by delivery method?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>19. Which salespeople have the highest average sales value per order?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>20. Which combinations of customer, city, and product category generate the highest revenue?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

## Level 3 — Advanced

<details>
<summary>21. Which customers show the highest revenue growth between consecutive years?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>22. How concentrated is company revenue? What percentage of total revenue is generated by the top 20% of customers?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>23. Which products demonstrate consistent sales growth over time?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>24. Which customers exhibit recurring and predictable purchasing behavior?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>25. What is the average repurchase cycle per customer?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>26. Are there customers with a high number of orders but low average revenue per order? Who are they?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>27. Which product categories have the highest growth potential based on historical sales performance?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>28. What is the impact of each salesperson on total revenue over time?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>29. Which regions have the greatest expansion potential considering customer count and average revenue?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

<details>
<summary>30. How can customers be segmented into high, medium, and low-value groups based on revenue and purchase frequency?</summary>

### SQL Solution

```sql
```

### Business Insights

-

</details>

## Level 4 — Data Warehouse & Dashboard Design

<details>
<summary>31. Which KPIs should be included in an executive sales dashboard?</summary>

### Analysis

-

</details>

<details>
<summary>32. How should a sales fact table be designed, and which dimensions are required?</summary>

### Analysis

-

</details>

<details>
<summary>33. Which metrics should be calculated in the Data Warehouse layer instead of the dashboard layer?</summary>

### Analysis

-

</details>

<details>
<summary>34. Which indicators can be used to monitor customer retention over time?</summary>

### Analysis

-

</details>

<details>
<summary>35. How should salesperson performance be measured considering order volume, revenue, and average order value?</summary>

### Analysis

-

</details>

<details>
<summary>36. Which products should be classified as strategic products for the business?</summary>

### Analysis

-

</details>

<details>
<summary>37. How can VIP customers be identified using revenue, frequency, and recency criteria?</summary>

### Analysis

-

</details>

<details>
<summary>38. Which indicators help monitor logistics and delivery efficiency?</summary>

### Analysis

-

</details>

<details>
<summary>39. Which dimensions are most relevant for explaining revenue fluctuations?</summary>

### Analysis

-

</details>

<details>
<summary>40. How can an executive view be designed to quickly answer: "Who sold what, to whom, when, and where?" using a dimensional model?</summary>

### Analysis

-

</details>

---
[< Back ](../02.%20Explore%20database/README.md)
