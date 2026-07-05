SELECT
CustomerID,
ROUND(SUM(TotalAmount),2) AS Revenue
FROM `retail-sales-analytics-501510.retail_sales.sales_transactions`
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY Revenue DESC
LIMIT 10;
