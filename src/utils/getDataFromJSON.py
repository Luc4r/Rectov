import json, os

def getDataFromJSON(path):
	if os.path.isfile(path):
		with open(path) as jsonFile:
		  return json.loads(jsonFile.read())
	else:
		print("Failed to fetch data from {}".format(path))
		return None