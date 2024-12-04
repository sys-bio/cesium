import asyncio
import json
import os
import aiofiles
import tellurium as te

#  Given a bunch of model files (text) in a subdirectory, go through them and generate a json database that
#  stores the number of species and reactions in the Antimony formatted model, the model type, and
#  relative file path of the model. 'Oscillator' and 'random' are the current model types available.

async def process_model(file_path, filename, directory):
    async with aiofiles.open(os.path.join(file_path, filename), "r") as file:
        model_string = await file.read()
        print(filename)
        r = te.loada(model_string)
        numSpecies = r.getNumFloatingSpecies()
        numReactions = r.getNumReactions()

        if "oscillator" in filename:
            modelType = "oscillator"
        elif "random" in filename:
            modelType = "random"
        else:
            modelType = "-"

        directory.append({
            "numSpecies": numSpecies,
            "numReactions": numReactions,
            "modelType": modelType,
            "path": file_path + "/" + filename
        })

async def main():
    dir_path = "model_db"  # relative path for now
    directory = []
    x = 0
    for path in os.listdir(dir_path):
      #  file_path = os.path.join(dir_path, path)
        file_path = dir_path + "/" + path
        if os.path.isdir(file_path):
            for filename in os.listdir(file_path):
                #if "bestmodel" in filename:  # filter as needed
                await process_model(file_path, filename, directory)
                x+=1
                print(x)

    with open(os.path.join(dir_path, "cesium_metadata.json"), "w") as outfile:
        json.dump(directory, outfile, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
    
