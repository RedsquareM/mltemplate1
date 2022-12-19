import pickle

def main(features):

    Model = pickle.load(open('Model.pkl', 'rb'))

    return Model.predict(features)

if __name__ == '__main__':

    features = input('input path to features: ')

    main(features)