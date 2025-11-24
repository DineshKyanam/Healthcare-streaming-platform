🏥 Healthcare-streaming-platform — End-to-End Real-Time Data Engineering Project

A complete HIPAA-friendly healthcare data pipeline built using Kafka, Spark Structured Streaming, Delta Lake, Airflow, and Power BI to automate compliance reporting, PHI masking, and hospital performance analytics.

This project simulates a real production-grade healthcare data platform capable of processing streaming patient events, masking sensitive PHI/PII, enforcing data quality, and generating clinical & compliance dashboards.

🚀 Architecture Overview
Healthcare Source Data (CSV/JSON)
           │
           ▼
   Kafka Producer → Kafka Topic
           │
           ▼
   Spark Structured Streaming
      - PHI/PII Masking
      - Validation & Cleanup
      - Deduplication
           │
           ▼
       Delta Lake
   (Bronze → Silver → Gold)
           │
           ▼
        Airflow DAG
   - Daily ETL Scheduling
   - DQ Checks & Logging
           │
           ▼
     Power BI Dashboards
   - Patient Metrics
   - Diagnosis Trends
   - Hospital KPIs
   - Compliance Reports

🏗️ Tech Stack
Layer	Technology
Streaming	Apache Kafka, Zookeeper
Real-time Processing	PySpark, Spark Structured Streaming
Storage	Delta Lake (Bronze/Silver/Gold)
Orchestration	Apache Airflow
Programming	Python
Dashboards	Power BI
Deployment	Docker / Docker Compose
📁 Project Folder Structure
healthcare-compliance-automation/
│
├── airflow/
│   ├── dags/
│   │   └── healthcare_pipeline_dag.py
│   └── docker-compose.yml
│
├── data/
│   ├── raw/          # incoming patient/claims files
│   ├── masked/       # PHI/PII masked outputs
│   └── processed/    # curated tables (Gold layer)
│
├── logs/
│
├── producer/
│   ├── kafka_producer.py
│   └── sample_data.csv
│
├── scripts/
│   └── helper utilities
│
├── spark_streaming/
│   ├── streaming_job.py
│   ├── masking_functions.py
│   └── configs/
│
├── dashboards/
│   ├── healthcare_overview.pbix
│   └── screenshots/
│
└── docker-compose.yml

🔐 PHI/PII Masking Rules

Your pipeline performs healthcare-grade data anonymization:

Field	Masking Applied
Patient Name	First letter + masked (e.g., J*****)
SSN	Show last 4 digits only
Phone	Masked middle digits
Address	City + State only
Date of Birth	Year only
Email	First 2 chars + domain masked

Ensures HIPAA-safe handling of health records.

⚡ Real-Time Processing Logic
✔ Spark Structured Streaming Performs:

Reads events from Kafka topic: healthcare.data

Schema validation

Null / corrupt record handling

Deduplication using patient + timestamp

PHI/PII masking

Writes to Delta Lake:

Bronze → raw ingest

Silver → cleaned + masked

Gold → analytics-ready

📅 Airflow Pipeline (ETL DAG)

Daily DAG performs:

Trigger streaming/batch sync

Validate Delta tables

Run quality checks

Generate logs

Create Gold-layer aggregated tables

Export data for Power BI

📊 Power BI Dashboards

Your dashboards visualize key healthcare insights:

1. Patient Admissions Overview

Daily/weekly/monthly admissions

Trends over time

Department-level breakdown

2. Diagnosis & Treatment Trends

Top diagnoses

Case severity distribution

Patient outcomes

3. Hospital Operational KPIs

Bed occupancy rate

Average length of stay

Doctor/Dept performance

4. Compliance Monitoring Dashboard

Masking success rate

Missing PHI counts

Invalid record tracking

▶️ How to Run the Project (Fully Reproducible)
1️⃣ Start Kafka & Airflow
docker-compose up -d

2️⃣ Run Producer
python producer/kafka_producer.py

3️⃣ Start Spark Stream
spark-submit spark_streaming/streaming_job.py

4️⃣ Open Airflow UI
http://localhost:8080


Trigger DAG:
healthcare_pipeline_dag

5️⃣ Load dashboards in Power BI

Open:

dashboards/healthcare_overview.pbix

🎯 Key Highlights for Recruiters / Resume

✔ Real-time streaming pipeline with Kafka & Spark
✔ Delta Lake Bronze-Silver-Gold architecture
✔ PHI/PII masking (HIPAA compliance simulation)
✔ Automated Airflow ETL workflows
✔ Clean folder structure for production systems
✔ Power BI dashboards for insights
✔ End-to-end data engineering implementation

🧑‍💻 Author

Dinesh Kyanam
Data Engineer | Real-Time Streaming | Cloud | Big Data
🔗 GitHub: your link
🔗 LinkedIn: your link

