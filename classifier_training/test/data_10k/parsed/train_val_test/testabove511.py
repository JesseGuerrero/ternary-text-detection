import os, json
from glob import glob
file_paths = [y for x in os.walk("..") for y in glob(os.path.join(x[0], '*.json'))]
count = 0
total = 0
for file_path in file_paths:
    data={}
    with open(file_path, "r") as jsonFile:
        data = dict(json.load(jsonFile))
        for title, caption in data.items():
            total += 1
            if len(caption[0]) > 512: #len(title) > 512 or len(caption[0]) > 512 or len(caption) > 1: #isinstance(title, list) or
                print(file_path + " " + title + " len:" + str(len(caption[0])))
                count += 1
    #             data[title] = [caption[0][:511]]
    # with open(file_path, "w") as jsonFile:
    #     json.dump(data, jsonFile)

print(f'{count} / {total} ')

