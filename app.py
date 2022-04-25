import os
import json
import pickle
from flask import Flask, request, jsonify
from preprocessing import cleaning_data
from predict.prediction import get_prediction
from error_fix.check_error import get_error


app = Flask(__name__)

@app.route('/')
def home():
    return 'Server Alive'

@app.route('/predict', methods = ['POST'])
def predict():
    #Get the json data
    result = request.get_json()
    # Check if result is empty
    if len(result) == 0:
        return {
                "Inputs" : len(result),
                "Response" : "Error: Please provide your Inputs, for more info: https://house-pred-api.herokuapp.com/predict"
                }
    else:
        #Check for an error inside the the json data
        error_response = get_error(result["data"])

        if error_response == "No errors found":
            #Clean the data and return final result
            clean_input = cleaning_data.preprocess(result['data'])
            #Predict the price
            y_pred = get_prediction(clean_input)

            #Return the predicted price in json format   
            return jsonify({"prediction value": y_pred})

        else:
            return {
                    "Error": error_response,
                    "More info": "https://house-pred-api.herokuapp.com/predict"
                    }
@app.route('/predict', methods = ['GET'])
def home_page():
    #The response for GET method
    data = {
            "data": {
                        "area": 'int',
                        "property_type": "APARTMENT" " or " "HOUSE" " or " "OTHERS",
                        "rooms_number": 'int',
                        "zip_code": 'int',
                        "land_area": 'int',
                        "Locality": 'str',
                        "garden": 'bool',
                        "garden_area": 'int',
                        "equipped_kitchen": 'Optional[bool]',
                        "full_address":' Optional[str]',
                        "Elevator": 'bool',
                        "swimming_pool": 'Optional[bool]',
                        "furnished": 'Optional[bool]',
                        "open_fire": 'Optional[bool]',
                        "terrace": 'Optional[bool]',
                        "terrace_area": 'Optional[int]',
                        "facades_number": 'Optional[int]',
                        "building_state": 'Optional'
                            "NEW"   "or" "GOOD" " or " "TO RENOVATE" " or " "JUST RENOVATED" " or " "TO REBUILD"
                    }
                }
    return jsonify("Please provide your json data in the following format \n ", data), 200
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host ="0.0.0.0", port=5000)