from flask import Flask, request, jsonify
from preprocessing import cleaning_data
from predict.prediction import get_prediction
from check_error import get_error
import pickle


app = Flask(__name__)

@app.route('/')
def home():
    return 'Alive'

@app.route('/predict', methods = ['GET','POST'])
def predict():
    
    if (request.method == 'POST'):

        result = request.get_json()

        if len(result) == 0:

            return {
                    "Inputs" : len(result),
                    "Response" : "Error: Please provide your Inputs",
                    }
        else:

            error_response = get_error(result['data'])

            if error_response == "No errors found":

                clean_input = cleaning_data.preprocess(result['data'])
                y_pred = get_prediction(clean_input)

                return jsonify({"prediction value": y_pred})
            else:
                return error_response

    else:
        data = {
                 "data": {
                        "area": 'int',
                        "property_type": "APARTMENT" " or " "HOUSE" " or " "OTHERS",
                        "rooms_number": 'int',
                        "zip_code": 'int',
                        "land_area": 'Optional[int]',
                        "garden": 'Optional[bool]',
                        "garden_area": 'Optional[int]',
                        "equipped_kitchen": 'Optional[bool]',
                        "full_address":' Optional[str]',
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
    app.run(host ="0.0.0.0", port=5000)