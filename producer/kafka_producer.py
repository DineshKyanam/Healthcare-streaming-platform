from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = (
    SparkSession.builder
        .appName("Healthcare_Streaming")
        .getOrCreate()
)

# Schema for healthcare event
schema = StructType([
    StructField("patient_id", IntegerType()),
    StructField("event_type", StringType()),
    StructField("heart_rate", IntegerType()),
    StructField("blood_pressure", StringType()),
    StructField("temperature", DoubleType()),
    StructField("timestamp", StringType())
])

# Read from Kafka
df = (
    spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "healthcare_events")
        .option("startingOffsets", "latest")
        .load()
)

# Convert Kafka value (bytes) to string
json_df = df.selectExpr("CAST(value AS STRING) as json_str")

parsed_df = json_df.select(from_json(col("json_str"), schema).alias("data")).select("data.*")

# Write output to folder
query = (
    parsed_df.writeStream
        .format("json")
        .option("path", "C:/Healthcare-Compliance/spark_streaming/output")
        .option("checkpointLocation", "C:/Healthcare-Compliance/spark_streaming/checkpoints")
        .outputMode("append")
        .start()
)

query.awaitTermination()
