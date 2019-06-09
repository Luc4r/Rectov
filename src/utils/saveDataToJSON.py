import json, operator

from src.utils.getDataFromJSON import getDataFromJSON

def saveResultToJSON(new_result):
  path = "src/data/scores.json"
  scores_limit = 1000
  data = getDataFromJSON("src/data/scores.json")

  data_new = [new_result]
  if data:
    data.append(new_result)
    data_sorted = sorted(data, key=operator.itemgetter('score'), reverse=True)
    data_new = data_sorted[:scores_limit]

  with open(path, "w") as json_file:
    json.dump(data_new, json_file)