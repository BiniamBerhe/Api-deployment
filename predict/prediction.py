import pickle


def get_prediction(data):

    loaded_model = pickle.load(open('predict/polyreg.pkl', 'rb'))

    predict_result = round(loaded_model.predict(data)[0][0],2)

    return predict_result