import azure.functions as func
import datetime
import json
import logging
import pickle
import pandas as pd


app = func.FunctionApp()

        
@app.route(route="score_model", auth_level=func.AuthLevel.ANONYMOUS)
def score_model(req: func.HttpRequest) -> func.HttpResponse:
    
    # Getting supplier and quantity from request
    supplier = req.params.get('supplier')
    quantity = req.params.get('quantity')
    
    # Load Model 
    model = pickle.load(open('./gbm_500.pkl', 'rb'))
    
    # Define the possible suppliers
    suppliers = ['Aromatico', 'Beans Inc.', 'Fair Trade AG', 'Farmers of Brazil', 'Handelskontor Hamburg']
    
    # Create a dictionary for the DataFrame
    data = {
        "quantity_ordered": [quantity],
    }
    
    # Add supplier one-hot encoding to the dictionary
    for s in suppliers:
        data[f'd_{s}'] = [1 if s == supplier else 0]
    
    # Create the DataFrame
    test_data = pd.DataFrame(data)
    
    prediction = model.predict(test_data)[0]
    logging.warning(f"Predictions: {prediction}") 
    
    return json.dumps({
        "message": f"""Model scored successfully! with quantity: {quantity} and supplier: {supplier}, "prediction": {prediction}""",           
        "prediction": prediction,
        "status_code": 200
        })
        
                    
    