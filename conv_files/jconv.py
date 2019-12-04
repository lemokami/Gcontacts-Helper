import json

def conv(param_dict):
    with open("decoded-json.json","w+") as file:
        file.write(json.dumps(param_dict))