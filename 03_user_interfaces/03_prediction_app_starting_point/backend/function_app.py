import azure.functions as func
import datetime
import json
import logging
import pickle
import pandas as pd


app = func.FunctionApp()

        
@app.route(route="score_model", auth_level=func.AuthLevel.ANONYMOUS)
def score_model(req: func.HttpRequest) -> func.HttpResponse:
    
    
    return json.dumps({
        "message": f"Model scoring",                   
        "status_code": 200
        })
        
                    
    