def process(data):
  new_data = dict()
  new_data["affiliation"] = data["abstracts-retrieval-response"]["affiliation"]
  new_data["coredata"] = data["abstracts-retrieval-response"]["coredata"]

  return new_data

# import json

# with open("example_json/202300000") as f:
#   data = json.load(f)
#   print(process(data))