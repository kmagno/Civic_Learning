import json
from pprint import pprint

with open('MALower.json') as data_file:
    data = json.load(data_file)

pprint(data)
