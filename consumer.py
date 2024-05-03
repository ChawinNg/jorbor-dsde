from dotenv import load_dotenv
load_dotenv()

import os
import json
from datetime import datetime
from kafka import KafkaConsumer
import pymongo

kafka_broker = os.environ["KAFKA_BROKER"]
consumer = KafkaConsumer(
  "raw",
  bootstrap_servers=[kafka_broker],
  enable_auto_commit=True,
  value_deserializer=lambda x: x.decode("utf-8"))

mongo_uri = os.environ["MONGO_URI"]
mongo = pymongo.MongoClient(mongo_uri)
test = mongo["test"]
testcol = test["test"]

print("Running Consumer")
for message in consumer:
  time = datetime.fromtimestamp(int(message.timestamp) // 1000)
  try:
    content = json.loads(message.value)
    # testcol.insert_one(content)
    print(f"[{time}] Consumed {len(message.value)} bytes")
  except:
    print(f"[{time}] Error consuming json")