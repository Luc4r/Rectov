import json, operator

from src.utils.getDataFromJSON import getDataFromJSON

def saveResultToJSON(newResult):
  path = "src/data/scores.json"
  scoresLimit = 1000

  data = getDataFromJSON("src/data/scores.json")
  
  newData = [newResult]
  if data:
    data.append(newResult)
    dataSorted = sorted(data, key=operator.itemgetter('score'), reverse=True)
    newData = dataSorted[:scoresLimit]

  with open(path, "w") as jsonFile:
    json.dump(newData, jsonFile)