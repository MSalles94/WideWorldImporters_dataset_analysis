# define tables from schemass
        #target_table:source_table
Application={
#Application schema
'dim_people':'People',
'dim_cities':'Cities', 
'dim_provinces':'StateProvinces',
'dim_countries':'Countries',
'dim_DeliveryMethods':'DeliveryMethods',
'dim_PaymentMethods':'PaymentMethods', 
'dim_TransactionTypes':'TransactionTypes'}

Sales={
#Sales shcema
'dim_Customers':'Customers', 
'dim_CustomerCategories':'CustomerCategories',
'dim_BuyingGroups':'BuyingGroups',
'fact_Orders':'Orders', 
'fact_OrderLines':'OrderLines',
'fact_Invoices':'Invoices',
'fact_InvoiceLines':'InvoiceLines',
'fact_CustomerTransactions':'CustomerTransactions'}

Warehouse={
#warehouse schema
'dim_StockItems':'StockItems',
'dim_StockItemStockGroups':'StockItemStockGroups',
'dim_StockGroups':'StockGroups',
'dim_Colors':'Colors', 
'dim_ColdRoomTemperatures':'ColdRoomTemperatures',
'dim_PackageTypes':'PackageTypes', 
'fact_StockItemHoldings':'StockItemHoldings',
'fact_StockItemTransactions':'StockItemTransactions',
'fact_VehicleTemperatures':'VehicleTemperatures'
}

Purchasing={#Purchasing schema
'dim_Suppliers':'Suppliers',
'dim_SupplierCategories':'SupplierCategories',
'fact_PurchaseOrders':'PurchaseOrders',
'fact_PurchaseOrderLines':'PurchaseOrderLines',
'fact_SupplierTransactions':'SupplierTransactions'
} 

#-------------------------------------------------------
map_source_schemas={
    'Application':Application,
    'Sales':Sales,
    'Warehouse':Warehouse,
    'Purchasing':Purchasing
}
 