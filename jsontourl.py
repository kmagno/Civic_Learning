import json


def get_names(name, house):
        if house == "lower":
            with open('MALower.json') as data_file:
                data = json.load(data_file)
        else:
            with open('MAUpper.json') as data_file:
                data = json.load(data_file)

        for i in range(len(data["Results"])):
            if name in data["Results"][i]["Name"]:
                x = data["Results"][i]["Websites"]["Office"]
                return x
