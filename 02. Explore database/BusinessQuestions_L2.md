
[<./02. Explore DataBase](../02.%20Explore%20database/README.md)

[<./02. Explore DataBase/Questions summary](../02.%20Explore%20database/businessQuestions.md) 

---

# Level 2 — Intermediate

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

#### SQL Solution

```sql
WITH _TABLE AS (SELECT	
	o.OrderID, 
	i.DeliveryMethodID,
	DATEDIFF(SECOND,o.PickingCompletedWhen, i.ConfirmedDeliveryTime) AS DIF_TIME
FROM WideWorldImporters.Sales.Orders o
	LEFT JOIN WideWorldImporters.Sales.Invoices i
		ON i.OrderID=o.OrderID)
SELECT 
	T.DeliveryMethodID,dm.DeliveryMethodName,
	AVG( DIF_TIME/(60*60.0))  AS HOURS_
FROM _TABLE AS T
	LEFT JOIN WideWorldImporters.Application.DeliveryMethods dm
		ON dm.DeliveryMethodID=T.DeliveryMethodID
WHERE T.DeliveryMethodID IS NOT NULL
GROUP BY T.DeliveryMethodID,dm.DeliveryMethodName
```

#### Output

|DeliveryMethodID|DeliveryMethodName|HOURS_|
|----------------|------------------|------|
|3|Delivery Van|23.0483864|


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



---

[<./02. Explore DataBase](../02.%20Explore%20database/README.md)

[<./02. Explore DataBase/Questions summary](../02.%20Explore%20database/businessQuestions.md) 