from re import X
from numpy import True_
import pandas as pd
import json
import pickle

d = {
  "data": {
    "area": 45,
    "property_type": "APARTMENT",
    "rooms_number": 3,
    "zip_code": 43454354,
    "land_area": 100,
    "garden": False,
    "garden_area": 25,
    "equipped_kitchen": False,
    "Locality": "Brussels",
    "Elevator": True,
    "swimming_pool": False,
    "furnished": False,
    "full_address": "zfjzofjazpof",
    "open_fire": False,
    "terrace": True,
    "terrace_area": 15,
    "facades_number": 2,
    "building_state": "NEW"
  }
}

def preprocess(input_data):
  """A function to clean incoming json data
    according to the model available"""

  #Convert json data into Pandas dataframe
  df = pd.json_normalize(input_data)

  #Onehot code for locality
  Locality_map = {'Brussels': 1, 'Flanders': 2, 'Wallonia': 3}
  df = df.applymap(lambda s: Locality_map.get(s) if s in Locality_map else s)
  
  df['terrace'] = pd.Categorical(df['terrace'], [True, False])
  df['terrace'] = df['terrace'].cat.codes

  df['Elevator'] = pd.Categorical(df['Elevator'], [True, False])
  df['Elevator'] = df['Elevator'].cat.codes

  df['garden'] = pd.Categorical(df['garden'], [True, False])
  df['garden'] = df['garden'].cat.codes
  print(df["Elevator"])

  print(df)
  #Select feature for prediction
  selected_df = df.loc[:, ["Locality", "rooms_number", "terrace",
                          "land_area", "Elevator", "garden","area", "garden_area"]]
  x = selected_df.to_numpy()
  print(x)
  #Return the selected features in numpy array
  return x

