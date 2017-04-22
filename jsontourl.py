import json


def get_names(name, house):
        with open('MALower.json') as data_file:
            data = json.load(data_file)
        if data == null:
            with open('MAUpper.json') as data_file:
                data = json.load(data_file)

        for i in range(len(data["Results"])):
            if name in data["Results"][i]["Name"]:
                x = data["Results"][i]["Websites"]["Office"]
                return x
