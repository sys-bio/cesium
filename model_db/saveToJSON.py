# Code to generate JSON file of all models in mongoDB from original CesiumDB

import pymongo
from bson import json_util
# Grabs all of data in the mongoDB at address below ('astr') and dumps it into a json file.
jsonFile = "cesiumDBbackup.json"
astr = "mongodb+srv://data:VuRWQ@networks.wqx1t.mongodb.net"
client = pymongo.MongoClient(astr)
#print(client.list_database_names())

db = client['models']
for coll in db.list_collection_names():
    print(coll)

collection = db['models']
cur = collection.find({})
big_json_obj = json_util.dumps(cur, indent=4)
with open(jsonFile, "w") as outfile:
    outfile.write(big_json_obj)
i = 0
for i, each in enumerate(cur):
    #if i<20:
    #print(each["ID"])
    json_obj = json_util.dumps(each, indent=4)
    #print(json_obj)
    # Writing to sample.json
    #with open(jsonFile, "a") as outfile:
       # outfile.write(json_obj)
print("Number records saved:", i)
