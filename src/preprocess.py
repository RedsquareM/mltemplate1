import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import configparser
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
import traceback

from logger import Logger

TEST_SIZE = 0.2
SHOW_LOG = True

class Preprocess:

    # takes in a csv data file
    def __init__(self, data):

        self.df = pd.read_csv(data)

        # call
        self.preprocessData()

    def preprocessData(self):

        # encoding
        le = LabelEncoder()
        columns = ['species','island']
        for col in columns:
            self.df[col] = le.fit_transform(self.df[col])
            self.df[col] = le.fit_transform(self.df[col])
        self.df['sex'] = self.df['sex'].replace(0, 2, inplace=True)
        self.df['sex'] = self.df['sex'].replace(['MALE','FEMALE'], [0,1], inplace=True)

        # standardization
        ss = StandardScaler()
        columns = ['Delta 15 N (o/oo)','Delta 13 C (o/oo)']
        for col in columns:
            self.df[col] = ss.fit_transform(self.df[[col]])

        # normalization
        mms = MinMaxScaler()
        columns = ['culmen_length_mm','culmen_depth_mm','flipper_length_mm','body_mass_g']
        for col in columns:
            self.df[col] = mms.fit_transform(self.df[[col]])

        # NaN values
        self.df = self.df.fillna(0)

        # X and y
        X = self.df.drop(['species'], axis=1)
        y = self.df['species']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


        # saving
        X.to_csv('Data_X.csv')
        y.to_csv('Data_y.csv')

        X_train_df = pd.DataFrame(X_train)
        X_train_df.to_csv('Train_Data_X.csv')

        y_train_df = pd.DataFrame(y_train)
        y_train_df.to_csv('Train_Data_y.csv')

        X_test_df = pd.DataFrame(X_test)
        X_test_df.to_csv('Test_Data_X.csv')

        y_test_df = pd.DataFrame(y_test)
        y_test_df.to_csv('Test_Data_y.csv')
