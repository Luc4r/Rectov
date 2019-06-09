import json, os

def getDataFromJSON(path):
	if os.path.isfile(path):
		with open(path) as json_file:
		  return json.loads(json_file.read())
	else:
		print("Failed to fetch data from {}".format(path))
		return None