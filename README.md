# Name of the app "house-pred-api"

## Description
- This is an app that predicts a house price based on user inputs
- The inputs are accepted in the form of json data
- Outputs are provided in json format as well

## App documentations:
- There are three routes that are available in this app
- Default route with get method that will show if the server is alive
- Predict route with post and get method
: (Post) to receive json data and show prediction
: (Get) to show the required data from user

### Error handling:
- This app is designed to accept only json data, the format of the json data is mentioned in (predict: get method)
- In case a user sends incorrect json data, error message will be shown with a link to more info

## Python version
- python 3.8

## Installation
- python
- Docker
- Required python libraries which is found in "requirement.txt"

## Usage
- The app is available in this link https://house-pred-api.herokuapp.com/predict
- This app was deployed on Heroku
