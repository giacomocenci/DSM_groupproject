

import { testFunction, blockingFunction } from "./exampleFunctions.js";

document.getElementById('runButton').addEventListener('click', testFunction);
document.getElementById('runButtonBlocking').addEventListener('click', blockingFunction);
