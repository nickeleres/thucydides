import json
from pprint import pprint
json_data = open('thucydides.json')

dataa = json.load(json_data)
data = dataa[0]["commit_title"]

pprint(data)
json_data.close()
