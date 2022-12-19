import pickle
import pandas as pd

class Predict:

    def __init__(self):

        self.X_test = pd.read_csv('../data/Test_Data_X.csv', index_col=[0])

    def predictLabels(self):
        Model = pickle.load(open('Model.pkl', 'rb'))
        return Model.predict(self.X_test)