import pickle

#Load the model from the directory
loaded_model = pickle.load(open('predict/polyreg.pkl', 'rb'))

def get_prediction(data):
    """A function that loads a model
        and predicts a price """
    
    #Predict the price
    predict_result = round(loaded_model.predict(data)[0][0],2)

    return predict_result