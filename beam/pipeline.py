import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime
import csv


def process_row(line):
    try:
        row = next(csv.reader([line]))

        quantity = int(row[2])
        unit_price = float(row[4])

        # Validation
        if quantity <= 0:
            return None

        if unit_price <= 0:
            return None

        if row[1].strip() == "":
            return None

        invoice_date = datetime.strptime(
            row[3],
            "%d-%m-%Y %H:%M"
        ).isoformat()

        return {
            "InvoiceNo": row[0],
            "Description": row[1],
            "Quantity": quantity,
            "InvoiceDate": invoice_date,
            "UnitPrice": unit_price,
            "CustomerID": row[5],
            "Country": row[6],
            "TotalAmount": round(quantity * unit_price, 2)
        }

    except (ValueError, IndexError):
        return None


# Pipeline options are supplied from the command line
options = PipelineOptions(save_main_session=True)

with beam.Pipeline(options=options) as p:

    (
        p
        | "Read CSV Files" >> ReadFromText(
            "gs://retail_sales_data_4/raw/*.csv",
            skip_header_lines=1
        )
        | "Process Rows" >> beam.Map(process_row)
        | "Filter Invalid Rows" >> beam.Filter(lambda row: row is not None)
        | "Write to BigQuery" >> WriteToBigQuery(
            table="retail-sales-analytics-501510:retail_sales.sales_transactions",
            schema={
                "fields": [
                    {"name": "InvoiceNo", "type": "STRING"},
                    {"name": "Description", "type": "STRING"},
                    {"name": "Quantity", "type": "INTEGER"},
                    {"name": "InvoiceDate", "type": "TIMESTAMP"},
                    {"name": "UnitPrice", "type": "FLOAT"},
                    {"name": "CustomerID", "type": "STRING"},
                    {"name": "Country", "type": "STRING"},
                    {"name": "TotalAmount", "type": "FLOAT"},
                ]
            },
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        )
    )
