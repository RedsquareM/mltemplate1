from sklearn import metrics
from preprocess import *
from train import *
from predict import *


#Flask app
import warnings
warnings.filterwarnings("ignore")

from flask import Flask

app = Flask(__name__)

def main():
    # preprocess data
    Preprocess('data.csv')

    # develop and train model
    Train()

    # perform predictions + evaluation
    y_true = pd.read_csv('../data/Test_Data_y.csv', index_col=[0])
    y_pred = Predict().predictLabels()
    return metrics.accuracy_score(y_true, y_pred), metrics.confusion_matrix(y_true, y_pred)

@app.route('/')
def home():
    accuracy, cm = main()
    return f'Model Accuracy: {accuracy}\nConfusion Matrix:\n\t{cm}'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='127.0.0.1')
