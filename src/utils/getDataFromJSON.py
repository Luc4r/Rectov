import json

def getDataFromJSON(path):
  with open(path) as jsonFile:
    return json.loads(jsonFile.read())
  print("Failed to fetch data from {}".format(path))
  return None