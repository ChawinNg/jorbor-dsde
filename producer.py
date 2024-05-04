from dotenv import load_dotenv
load_dotenv()

import os
import time
import json
from kafka import KafkaProducer

kafka_broker = os.environ["KAFKA_BROKER"]
kafka_topic = os.environ["KAFKA_TOPIC"]

producer = KafkaProducer(bootstrap_servers=[kafka_broker])

with open("example_json") as f:
  data = json.load(f)

  print("Running producer")
  while True:
    # content = json.dumps({
    #   "index": i,
    #   "text": random.choice(["A", "B", "C", "D"])
    # })
    
    print(f"Sending content")

    # content = json.dumps(data)
    content = "a"
    producer.send(kafka_topic, content.encode("utf-8"))

    time.sleep(0.5)