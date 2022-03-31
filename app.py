from flask import Flask, request, jsonify
from preprocessing import cleaning_data
from predict.prediction import get_prediction
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
            clean_input = cleaning_data.preprocess(result['data'])

            y_pred = get_prediction(clean_input)
        
            return jsonify({"prediction value": y_pred})

    else:
        data = {
                 "data": {
                        "area": 'int',
                        "property-type": "APARTMENT" " or " "HOUSE" " or " "OTHERS",
                        "rooms-number": 'int',
                        "zip-code": 'int',
                        "land-area": 'Optional[int]',
                        "garden": 'Optional[bool]',
                        "garden-area": 'Optional[int]',
                        "equipped-kitchen": 'Optional[bool]',
                        "full-address":' Optional[str]',
                        "swimming-pool": 'Optional[bool]',
                        "furnished": 'Optional[bool]',
                        "open-fire": 'Optional[bool]',
                        "terrace": 'Optional[bool]',
                        "terrace-area": 'Optional[int]',
                        "facades-number": 'Optional[int]',
                        "building-state": 'Optional'
                            "NEW"   "or" "GOOD" " or " "TO RENOVATE" " or " "JUST RENOVATED" " or " "TO REBUILD"
                    }
                }
    return jsonify("Please provide your json data in the following format \n ", data), 200
    
if __name__ == '__main__':
    app.run(host ="0.0.0.0", port=5000)


    "export FLASK_APP=app.py"
    "export FLASK_ENV=development"