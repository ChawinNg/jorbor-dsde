from dotenv import load_dotenv
load_dotenv()

import os
import json
from datetime import datetime
from kafka import KafkaConsumer
import pymongo

import cleaner

kafka_broker = os.environ["KAFKA_BROKER"]
kafka_topic = os.environ["KAFKA_TOPIC"]
mongo_uri = os.environ["MONGO_URI"]
print(kafka_broker, kafka_topic, mongo_uri)

consumer = KafkaConsumer(
  kafka_topic,
  bootstrap_servers=[kafka_broker],
  enable_auto_commit=True,
  value_deserializer=lambda x: x.decode("utf-8"),
  group_id="group-0"
)
print(f"Connected to Kafka {kafka_broker}")

mongo = pymongo.MongoClient(mongo_uri)
print("Connected to MongoDB")

test = mongo["test"]
testcol = test["test_preprocessed"]

print("Running Consumer")
for message in consumer:
  time = datetime.fromtimestamp(int(message.timestamp) // 1000)
  offset = message.offset
  partition = [i.partition for i in consumer.assignment()]
  print(f"[{time} {partition} #{offset}] ", end="")
  
  try:
    content = json.loads(message.value)
    testcol.insert_one(cleaner.process(content))
    print(f"Consumed {len(message.value)} bytes")
  except:
    print(f"Error consuming json {message.value}")