SELECT
Country,
ROUND(SUM(TotalAmount),2) AS Revenue
FROM `retail-sales-analytics-501510.retail_sales.sales_transactions`
GROUP BY Country
ORDER BY Revenue DESC;
