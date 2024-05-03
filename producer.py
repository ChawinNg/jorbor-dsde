from dotenv import load_dotenv
load_dotenv()

import os
import time
import json
import random
from kafka import KafkaProducer

kafka_broker = os.environ["KAFKA_BROKER"]

producer = KafkaProducer(bootstrap_servers=[kafka_broker])

with open("example_json") as f:
  data = json.load(f)

  print("Running producer")
  for i in range(100):
    # content = json.dumps({
    #   "index": i,
    #   "text": random.choice(["A", "B", "C", "D"])
    # })
    content = json.dumps(data)
    
    print(f"Sending {content}")
    producer.send("raw", content.encode("utf-8"))

    time.sleep(5)