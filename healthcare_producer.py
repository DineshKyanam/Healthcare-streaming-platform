from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

def generate_healthcare_event():
    return {
        "patient_id": random.randint(1000, 9999),
        "event_type": random.choice(["vitals", "lab_result", "medication"]),
        "heart_rate": random.randint(60, 120),
        "blood_pressure": f"{random.randint(90, 140)}/{random.randint(60, 90)}",
        "temperature": round(random.uniform(97.0, 102.5), 1),
        "timestamp": datetime.utcnow().isoformat()
    }

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("📡 Sending Healthcare events to Kafka...")

while True:
    event = generate_healthcare_event()
    producer.send('healthcare_events', event)
    print("Sent:", event)
    time.sleep(1)
