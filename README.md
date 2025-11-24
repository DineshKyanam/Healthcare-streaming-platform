#  Real-Time-Healthcare-Monitoring-Analytics-Pipeline

**Real-time healthcare analytics system with Power BI dashboards powered by Kafka, Spark Streaming, Delta Lake, and Airflow**

---

##  Project Overview

This project demonstrates a complete end-to-end real-time healthcare analytics system where patient vitals are streamed, processed, stored, and visualized using modern data engineering practices.

**Key Highlights:**
- Real-time Power BI dashboards for patient vital monitoring
- HIPAA-compliant PHI/PII masking
- Kafka-based event streaming
- Spark Structured Streaming for real-time processing
- Delta Lake Bronze/Silver/Gold architecture
- Airflow orchestration for ETL automation

---

##  Power BI Dashboards

###  Dashboard 1: Healthcare Real-Time Monitoring

![Healthcare Real-Time Monitoring Dashboard](https://raw.githubusercontent.com/DineshKyanam/Healthcare-streaming-platform/main/dashboards/screenshots/powerbi%20dashboard1.png)

**Features:**
- **Temperature trend over time** – Track patient temperature changes continuously
- **Heart rate trend over time** – Monitor cardiac activity in real-time
- **Vitals grouped by blood pressure** – Analyze patterns across BP categories
- **Medication and event-type comparisons** – Understand treatment impact
- **Real-time data ingestion** – Live updates reflected in visuals

**Target Users:** Nurses, clinicians, and monitoring teams tracking patient vitals live

---

###  Dashboard 2: Healthcare Real-Time KPIs

![Healthcare Real-Time KPIs](https://raw.githubusercontent.com/DineshKyanam/Healthcare-streaming-platform/main/dashboards/screenshots/powerbi%20dashboard2.png)

**Key Performance Indicators:**
- **Total patients monitored** – Overall system coverage
- **Average heart rate** – Population-level cardiac health
- **Average temperature** – System-wide temperature monitoring
- **Temperature by blood pressure** – Correlation analysis
- **Vitals grouped by event type** – Event-based health metrics

**Purpose:** Instant overview of overall patient stability and system performance

---

##  End-to-End Pipeline Architecture

```
Patient Vitals → Kafka Producer → Kafka Topic → Spark Structured Streaming → 
PHI/PII Masking → Delta Lake (Bronze → Silver → Gold) → Airflow Orchestration → Power BI
```

### **Pipeline Components:**

####  **Kafka**
- Streams patient events: temperature, heart rate, blood pressure, medication events
- Real-time data ingestion with high throughput

####  **Spark Structured Streaming**
- Reads data from Kafka in real-time
- Performs PHI/PII masking for HIPAA compliance
- Validates schema and removes bad records
- Writes to Delta Lake in Bronze/Silver/Gold layers

####  **Delta Lake**
- **Bronze Layer:** Raw ingested data
- **Silver Layer:** Cleaned and validated data
- **Gold Layer:** Aggregated analytics-ready data
- Supports ACID transactions and time travel

####  **Apache Airflow**
- Runs daily ETL tasks
- Data quality checks
- Automated data refresh workflows
- Pipeline monitoring and alerting

####  **Power BI**
- Connects to curated Gold Layer
- Visualizes real-time insights
- Interactive dashboards for stakeholders

---

##  PHI / PII Masking Logic

Sensitive patient information is transformed to simulate HIPAA-style de-identification:

| Field | Masking Logic |
|-------|---------------|
| **Name** | Masked except first letter (e.g., John Doe → J*** D***) |
| **SSN** | Only last 4 digits shown (e.g., ***-**-1234) |
| **Phone** | Middle digits masked (e.g., (555) ***-7890) |
| **DOB** | Only year retained (e.g., 1985-**-**) |
| **Address** | City and state only (e.g., Boston, MA) |

**Result:** Analytics can be performed while protecting patient identity and ensuring compliance

---

##  Project Folder Structure

```
healthcare-compliance-automation/
│
├── airflow/
│   └── dags/                          # Airflow DAG definitions
│
├── data/
│   ├── raw/                           # Raw streaming data (generated at runtime)
│   ├── masked/                        # PHI/PII masked data
│   └── processed/                     # Gold layer processed data
│
├── producer/
│   └── kafka_producer.py              # Kafka event producer
│
├── spark_streaming/
│   ├── streaming_job.py               # Main Spark streaming application
│   └── masking_functions.py           # PHI/PII masking functions
│
├── dashboards/
│   ├── healthcare_overview.pbix       # Power BI dashboard file
│   └── screenshots/
│       ├── powerbi dashboard1.png     # Monitoring dashboard screenshot
│       └── powerbi dashboard2.png     # KPIs dashboard screenshot
│
├── docker-compose.yml                 # Docker services configuration
│
└── README.md                          # Project documentation
```

**## Note:**  
Folders like `raw/`, `masked/`, `processed/`, and `logs/` may appear empty because data is generated only when Kafka, Spark, and Airflow are running. This is normal and expected in a streaming pipeline.

---

##  How to Run the Pipeline

### **Prerequisites**
- Docker & Docker Compose
- Apache Spark installed
- Python 3.8+
- Power BI Desktop

### **Step-by-Step Instructions**

#### **1️ Start Kafka, Zookeeper, and Airflow**
```bash
docker-compose up -d
```

#### **2️ Run the Kafka Producer**
```bash
python producer/kafka_producer.py
```

#### **3️ Start Spark Streaming Job**
```bash
spark-submit spark_streaming/streaming_job.py
```

#### **4️ Open Airflow UI**
Navigate to: `http://localhost:8080`

**Trigger the DAG:**
- DAG Name: `healthcare_pipeline_dag`
- Enable and trigger manually or wait for scheduled run

#### **5️ Open Power BI Dashboard**
- Launch Power BI Desktop
- Open: `dashboards/healthcare_overview.pbix`
- Refresh data to see real-time updates

---

##  Key Features of This Project

 **Real-time healthcare monitoring** with sub-second latency  
 **Power BI dashboards** with trending analytics  
 **Kafka-based event ingestion** for high-throughput streaming  
 **Spark Structured Streaming** with PHI/PII masking  
 **Delta Lake** Bronze/Silver/Gold architecture  
 **Airflow orchestration** for automated ETL  
 **Production-ready GitHub structure**  
 **HIPAA-compliant data handling**  
 **Recruiter-friendly and technically comprehensive**  

---

##  Future Enhancements

This project is under continuous improvement. Planned features:

-  Real-time dashboard auto-refresh via DirectQuery
-  Additional vitals monitoring (SpO2, respiratory rate)
-  Alerting system for critical events (e.g., temperature spikes)
-  Advanced data quality checks inside Spark
-  ML models for anomaly detection
-  Integration with cloud platforms (AWS/Azure)
-  Multi-patient comparative analytics

---

##  Technologies Used

| Category | Technologies |
|----------|-------------|
| **Streaming** | Apache Kafka, Spark Structured Streaming |
| **Storage** | Delta Lake, Parquet |
| **Orchestration** | Apache Airflow |
| **Visualization** | Power BI |
| **Languages** | Python, SQL |
| **Containerization** | Docker, Docker Compose |

---

##  Contact

**Dinesh Kyanam**  
Data Engineer | Real-Time Streaming | Cloud | Big Data

 **GitHub:** [github.com/DineshKyanam](https://github.com/DineshKyanam)  
 **LinkedIn:** [linkedin.com/in/dinesh-kyanam-180b611a2](https://linkedin.com/in/dinesh-kyanam-180b611a2)  
 **Email:** kyanamdinesh18@gmail.com



---

