SELECT
Description,
SUM(Quantity) AS Quantity_Sold,
ROUND(SUM(TotalAmount),2) AS Revenue
FROM `retail-sales-analytics-501510.retail_sales.sales_transactions`
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;
