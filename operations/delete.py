#these would happen as github actions
import json
import os
import sys


def delete(path):
    try:
        with open("metadata.json", "r") as f:
            data = json.load(f)
        if os.path.isfile(path):
            paths = [path]
        else:
            paths = [pt for pt in os.listdir(path)]
        for item in data:
            if item['path'] in paths:
                data.remove(item)
                break
        with open("metadata.json", "w") as f:
            json.dump(data, f)
        with open("checksum", "a") as ch:
            ch.write("1")
        print("added model")
        return
    except Exception as e:
        print(e)

delete(sys.argv[1])
