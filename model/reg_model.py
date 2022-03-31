import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle


def model():
    """ Polynomial regression model with degree of 2 was used for the result from sklearn
    """

    #Load the data set and drop whats not needed
    df = pd.read_csv('data/final_data.csv')
    df.drop(['Unnamed: 0'], axis = 1, inplace = True)

    #Define  X(independent variable) and Y(dependent variable)
    X = df[['Number of bedrooms', 'Livable surface', 
            'Surface of living-room', 'Surface garden']].to_numpy()
    Y = df.Price.to_numpy().reshape(-1, 1)

    print('X shape:', X.shape)
    print('Y shape:', Y.shape)

    #Split the data sets into training (80%) and testing (20%)
    X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    print('X_train shape:', X_train.shape)
    print('x_test shape:', x_test.shape)
    print('Y_train shape:', Y_train.shape)
    print('y_test shape:', y_test.shape)

    #Create a pipeline with PolynomialFeatures and LinearRegression
    degree = 2
    polyreg=make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression(),
    )

    # Fit your model.
    polyreg.fit(X_train, Y_train)
    polyreg.score(x_test,y_test)

    #predict with test set and check the mean square error
    y_pred = polyreg.predict(x_test)
    mean_error = mean_squared_error(y_test,y_pred)

    print('Prediction rate in %',round(polyreg.score(x_test,y_test),2))
    print('error', round(mean_error,2))

    #Save the model in a directory
    pickle.dump(polyreg, open('../predict/polyreg.pkl', 'wb'))

    return polyreg.predict(x_test)

if __name__ == '__main__':
    model()