
import datetime
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
        with open("checksum", "w") as ch:
            ch.write(datetime.datetime.now().__str__())
        print("deleted model")
        return
    except Exception as e:
        print(e)

delete(sys.argv[1])
