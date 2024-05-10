from dotenv import load_dotenv
load_dotenv()

import os
import json
import sys
from kafka import KafkaProducer

kafka_broker = os.environ["KAFKA_BROKER"]
kafka_topic = os.environ["KAFKA_TOPIC"]

producer = KafkaProducer(
  bootstrap_servers=[kafka_broker],
  max_request_size=12000000
)

print("Running producer")
dir = f"example_json/{sys.argv[1]}"
files = os.listdir(dir)
for i, file in enumerate(files):
  print(f"{i:04} of {len(files)}: {file}")
  with open(os.path.join(dir, file), "r") as f:
    data = json.load(f)
    content = json.dumps(data)
    
    future = producer.send(kafka_topic, content.encode("utf-8"))
    future.get(timeout=60)

# print("Running producer")
# i = 0
# while True:
#   print(f"Sending content {i}")

#   content = f"content-{i}"
#   producer.send(kafka_topic, content.encode("utf-8"))

#   time.sleep(0.05)
#   i += 1