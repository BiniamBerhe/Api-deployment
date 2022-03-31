from re import X
import pandas as pd
import json
import pickle

d = {
  "data": {
    "area": 54,
    "property-type": "APARTMENT",
    "rooms-number": 2,
    "land-area": 45,
    "garden": True,
    "garden-area": 35.5,
    "furnished": True,
    "facades-number": 2
  }
}

def preprocess(input_data):

    df = pd.json_normalize(input_data)
    
    selected_df = df.loc[:, ["rooms-number", "land-area", "area", "garden-area"]]
    x = selected_df.to_numpy()

    return x