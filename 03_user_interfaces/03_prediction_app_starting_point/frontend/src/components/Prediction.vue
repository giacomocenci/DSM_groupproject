


<!-- Script Part -->
<script setup lang="ts">
import { ref, computed } from 'vue'

const backendUrl = computed(() => {
  return import.meta.env.VITE_APP_BACKEND_URL
})



// Make a get request to the backend to get a prediction
const getPrediction = async () => {  
  window.console.log('fetching data')

  prediction.value = ''
  
  loading.value = true; // Set loading to true
      try {
        const response = await fetch(`${backendUrl.value}/score_model?supplier=${selectedSupplier.value}&quantity=${quantity.value}`);
        const data = await response.json();        
        prediction.value = data.prediction.toFixed(2);
        
      } catch (error) {
        alert('could not fetch data')
        window.console.error('Error fetching data:', error);        
      }
      loading.value = false; 
    }
</script>



<!-- Template Part -->
<template>
  
 
  <div>
      MY APP
  </div>
    
    
  <div> Dev Info </div>
  <div> Backend URL: {{ backendUrl }}</div>
  

 
</template>

<style scoped>

div {  
  margin: 1em;
  text-align: right;
}

label {  
  margin-right: 1em;
}

button {
  font-size: 1em;
  padding: 0.5em 1em;
  background-color: cadetblue;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.hint {
  font-size: 0.8em;
  color: #888;
}

.prediction {
  font-size: 1.5em;
  margin: 1em;
  color: cadetblue;
  text-align: center;
}


.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #4CAF50;
  animation: spin 1s ease infinite;
  margin: auto;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }

}
</style>
