import pickle
import sklearn
import pandas as pd
from sklearn.gaussian_process.kernels import RBF

from sklearn.gaussian_process.kernels import RBF

class Train:

    # takes in a features and attributes arrays
    def __init__(self):

        K = 1.0 * RBF(1.0)

        # X and y
        self.X = pd.read_csv('../data/Train_Data_X.csv', index_col=[0])
        self.y = pd.read_csv('../data/Train_Data_y.csv', index_col=[0])

        # Model
        self.model = sklearn.gaussian_process.GaussianProcessClassifier(kernel=K)

        # call
        self.trainModel()

    def trainModel(self):
        self.model.fit(self.X, self.y)
        pickle.dump(self.model, open('Model.pkl', 'wb'))

if __name__ == "__main__":
    multi_model = Train()