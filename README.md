# Retail Sales Analytics Pipeline on Google Cloud Platform (GCP)

## Project Overview

This project demonstrates an end-to-end batch data engineering pipeline built on **Google Cloud Platform (GCP)**. The pipeline ingests retail sales data stored in **Google Cloud Storage (GCS)**, processes and validates it using **Apache Beam** running on **Dataflow**, loads the transformed data into **BigQuery**, and visualizes business insights using **Looker Studio**.

The project was built to showcase core GCP Data Engineering concepts such as data ingestion, ETL processing, cloud storage, analytics, visualization, IAM configuration, and monitoring.

---

## Architecture

```
Retail CSV Files
        │
        ▼
Google Cloud Storage (Raw)
        │
        ▼
Apache Beam Pipeline
        │
        ▼
Google Cloud Dataflow
        │
        ▼
Data Validation & Transformation
        │
        ▼
BigQuery
        │
        ▼
Looker Studio Dashboard
```

---

## Technologies Used

* Google Cloud Storage (GCS)
* Apache Beam (Python)
* Google Cloud Dataflow
* BigQuery
* Looker Studio
* Cloud IAM
* Cloud Logging
* Python 3

---

## Project Workflow

1. Uploaded retail sales CSV files into a Google Cloud Storage bucket.
2. Apache Beam pipeline read all CSV files from GCS.
3. Performed data validation:

   * Removed records with invalid Quantity.
   * Removed records with invalid UnitPrice.
   * Removed records with empty Product Description.
4. Converted InvoiceDate into TIMESTAMP format.
5. Calculated a new field:

   * **TotalAmount = Quantity × UnitPrice**
6. Loaded transformed data into BigQuery.
7. Created analytical SQL queries.
8. Built an interactive dashboard using Looker Studio.

---

## Data Validation

The pipeline validates each record before loading it into BigQuery.

Validation rules:

* Quantity must be greater than 0
* UnitPrice must be greater than 0
* Description cannot be empty

Invalid records are skipped.

---

## Data Transformation

The pipeline performs the following transformations:

* Converts Quantity to Integer
* Converts UnitPrice to Float
* Converts InvoiceDate to TIMESTAMP
* Calculates TotalAmount

---

## BigQuery Analytics

Sample analyses include:

* Total Revenue
* Revenue by Country
* Monthly Revenue Trend
* Top Selling Products
* Top Customers

---

## Looker Studio Dashboard

The dashboard contains:

* Total Revenue
* Total Orders
* Unique Customers
* Average Order Value
* Monthly Revenue Trend
* Revenue by Country
* Sales Distribution by Country
* Top 10 Products
* Top Customers
* Country Filter
* Date Filter

---

## Project Structure

```
Retail-Sales-GCP/
│
├── beam/
│   ├── pipeline.py
│   └── requirements.txt
│
├── sql/
│   ├── total_revenue.sql
│   ├── revenue_by_country.sql
│   ├── monthly_revenue.sql
│   ├── top_products.sql
│   └── top_customers.sql
│
├── architecture/
│   └── architecture.png
│
├── screenshots/
│   ├── 1_gcs_bucket.png
│   ├── 2_dataflow_job.png
│   ├── 3_bigquery_table.png
│   ├── 4_bigquery_query.png
│   ├── 5_looker_dashboard.png
│   ├── 6_cloud_logging.png
│   └── 7_iam_roles.png
│
├── README.md
└── .gitignore
```

---

## Results

* Successfully processed **486,930+ retail sales records**
* Loaded curated data into BigQuery
* Generated analytical insights using SQL
* Built an interactive Looker Studio dashboard
* Configured IAM roles for secure access
* Monitored pipeline execution using Cloud Logging

---

## Future Improvements

* Schedule the pipeline using Cloud Scheduler
* Orchestrate workflows using Cloud Composer (Airflow)
* Add data quality checks using Great Expectations
* Implement incremental data loading
* Add CI/CD using GitHub Actions

---

## Author

**Sahil Rawat**

Aspiring Data Engineer | Google Cloud Platform | Apache Beam | Dataflow | BigQuery | SQL | Python
