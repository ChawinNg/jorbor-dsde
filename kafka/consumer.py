from dotenv import load_dotenv
load_dotenv()

import os
import json
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

print("Running Consumer")
for message in consumer:
  index, text = json.loads(message.value).values()
  print(index, text)