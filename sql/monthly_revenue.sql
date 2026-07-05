SELECT
FORMAT_TIMESTAMP('%Y-%m', InvoiceDate) AS Month,
ROUND(SUM(TotalAmount),2) AS Revenue
FROM `retail-sales-analytics-501510.retail_sales.sales_transactions`
GROUP BY Month
ORDER BY Month;
