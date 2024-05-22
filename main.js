
import {getModels} from "./model_db/search_db.js";

const modelListTextArea = document.getElementById("model_list");

window.onload = function() {
 initLoad();
}


async function initLoad() {
var modelList;
 await getModels(3).then((response) => {modelList = response;})
  .catch((err) => console.error(err));
  modelListTextArea.value = outputResults(modelList);
  	
	
}

/**
 * @param {model Map object} list of models to grab info out of
 * @returns {string} - A string containing model info
 
 **/
function outputResults(modelMap) {
  let modelListStr = '';
  for(let i=0; i< modelMap.size; i++) {
      const modelData = modelMap.get(i.toString());
      modelListStr = modelListStr + "ID: " + modelData.id + ", Model Type: " + modelData.modelType + ",\n";
	  modelListStr = modelListStr + "Number of species: " + modelData.nSpecies + ", Number of reactions: " + modelData.nRxns + "\n";
      modelListStr = modelListStr + modelData.antString + "\n";	
  }
  	  
  return modelListStr;
}