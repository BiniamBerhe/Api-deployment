from re import X
from numpy import True_
import pandas as pd
import json
import pickle


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

  #Select feature for prediction
  selected_df = df.loc[:, ["Locality", "rooms_number", "terrace",
                          "land_area", "Elevator", "garden","area", "garden_area"]]
  x = selected_df.to_numpy()

  #Return the selected features in numpy array
  return x

