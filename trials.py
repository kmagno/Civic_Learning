import json
from pprint import pprint

with open('MALower.json') as data_file:
    data = json.load(data_file)

print(data["Results"][0]["Websites"]["Office"])
for i in range(len(data["Results"])):
    x = data["Results"][i]["Websites"]["Office"]
    print(x)
    print ("--------------------------------------")
# for i in range(len(data)):
#     x =data[i].Websites.Office
#     pprint(x)
