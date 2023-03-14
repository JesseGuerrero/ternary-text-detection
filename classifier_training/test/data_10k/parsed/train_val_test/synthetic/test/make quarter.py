import json
file_path = "Test_WikiChatGPTSyntheticFullSet.json"
quarterData = {}
with open(file_path, "r") as jsonFile:
    data = dict(json.load(jsonFile))
    items = list(data.items())
    for title, caption in items[:int(len(items)/4)]:
        quarterData[title] = caption
with open("Test_WikiChatGPTSyntheticQuarterSet.json", "w") as jsonFile:
     json.dump(quarterData, jsonFile)
