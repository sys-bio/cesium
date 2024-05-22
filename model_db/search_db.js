
const cache = "./model_db/cesiumDB.json";

// May want to use Octokit (https://github.com/octokit) instead of downloading whole database.
// There may be other REST APIs available for Github repo use.

// The cache of models retrieved from a JSON file
var cachedData;

// URL for the chosen model
let url;

/**
 * Function to search for models using the cached data
 * @param {searchStr} search - The search event
 * @returns {Promise<Models>} - A promise containing the models returned by the search
 */
export async function getModels(numberOfModels) {
    try {
        let count =0;
        const models = new Map();
		await fetch(cache)
		 .then((response) => response.json())
		 .then((json) => {
	//console.log(json);
	 	  cachedData = json;
	 	  cachedData =  json;
		  
         for (const id in cachedData) {
            const modelData = cachedData[id];
            count +=1;
            models.set(id, {
              name: modelData.name,
              isEvolved: modelData.isEvolved,
              id: modelData.ID,
              modelType: modelData.modelType,
              antString: modelData.antString,
              nRxns: modelData.numReactions,
              nSpecies: modelData.numSpecies,
              nBoundrySp: modelData.numBoundary
            });
			if (count == numberOfModels) {
			  return models;
			  }
           }
		 
		 });
        return models;
    } catch (error) {
        // If there is an error, throw it
        throwError("Unable to fetch models from cache.");
    }
}

/**
 * Function to display an error message
 * @param {String} error - The error message to display
 * @returns {void}
 */
async function throwError(error) {
  const popup = document.createElement("div");
  popup.innerHTML = error.toString();
  popup.style.position = "fixed";
  popup.style.top = "50%";
  popup.style.left = "50%";
  popup.style.transform = "translate(-50%, -50%)";
  popup.style.backgroundColor = "white";
  popup.style.padding = "20px";
  popup.style.border = "1px solid black";
  popup.style.borderRadius = "10px";
  popup.style.zIndex = "100";
  document.body.appendChild(popup);
  setTimeout(() => {
    document.body.removeChild(popup);
  }, 2500);
}


// if module is defined, export the AntimonyWrapper class
if (typeof module !== 'undefined') {
  module.exports = {getModels};
}