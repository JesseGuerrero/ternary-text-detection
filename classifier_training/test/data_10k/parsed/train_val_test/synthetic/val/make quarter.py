import json
file_path = "Val_WikiSyntheticFullSet.json"
quarterData = {}
with open(file_path, "r") as jsonFile:
    data = dict(json.load(jsonFile))
    items = list(data.items())
    for title, caption in items[:int(len(items)/4)]:
        quarterData[title] = caption
with open("Val_WikiSyntheticQuarterSet.json", "w") as jsonFile:
     json.dump(quarterData, jsonFile)
