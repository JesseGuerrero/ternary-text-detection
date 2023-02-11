import os, json
from glob import glob
file_paths = [y for x in os.walk("..") for y in glob(os.path.join(x[0], '*.json'))]
for file_path in file_paths:
    data={}
    with open(file_path, "r") as jsonFile:
        data = dict(json.load(jsonFile))
        for title, caption in data.items():
            if isinstance(title, list) or len(title) > 512 or len(caption[0]) > 512 or len(caption) > 1:
                print(file_path + " " + title + " len:" + str(len(caption[0])))
                # data[title] = caption[0][:511]
    # with open(file_path, "w") as jsonFile:
    #     json.dump(data, jsonFile)

