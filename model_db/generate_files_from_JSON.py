# generate Antimony model files from json file.
# File was json backup from mongodb, then: 
# File was manually exported to JSON minimal format using 
# Dadroit json viewer (https://dadroit.com/) .

import json, re, os

# Expects a JSON minified file with just one line containing entries, 
# Returns a dictionary of json entries.
def open_JSON_file(jsonfile_name:str):
    data = []
    with open(jsonfile_name, 'r') as file:   
        for one_data in file:
            #print(one_data)
            file_data = one_data.split("},{")

    # tweak format of each string in list to be valid json, then return data.
    for i, model_info in enumerate(file_data):
        if i == 0:
           model_info = model_info + "}" 
           new_entry = model_info.replace("[", "", 1)
        elif i < len(file_data) - 1:
            new_entry = "{" + model_info + "}"
        else: 
            model_info = "{" + model_info 
            new_entry = model_info.replace("}]", "}", 1)
        data.append(json.loads(new_entry))

    #for model in data:
        #print(json.dumps(model))
    return data # dict 

def generateAntFilesFromJSON(json_data:dict, file_dir:str):
    for model in json_data:
        model_id = model['ID']
        model_text = model['antString']
        model_type = model['modelType']
        #print(model_id)
        #print(model_text)
        try:
            file_name = file_dir + "/" + model_type + "_" + model_id + ".txt"  # save antimony model file in sub directory
            if(os.path.isdir(file_dir)):
                f = open(file_name, "w")
                f.write(model_text)
                f.close

        except:
            print("Error finding: " + file_dir + " directory or saving model file")

if __name__ == "__main__":
    json_name = "cesiumDB_Minified.json"
    new_data = open_JSON_file(json_name)
    generateAntFilesFromJSON(new_data,"ant_models") 
