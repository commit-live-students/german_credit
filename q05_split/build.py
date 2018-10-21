# %load q05_split/build.py
import pandas as pd
import sys, os
from sklearn.model_selection import train_test_split
from greyatomlib.german_credit.q03_encode_features.build import q03_encode_features
pd.set_option('display.max_columns', 500)
path = 'data/GermanData.csv'

def q05_split(data, test_size = 0.2, random_state = 9):
    
    data_1 = q03_encode_features(data)
    data_2 = pd.DataFrame(list(data_1)[0])
    X = data_2.iloc[:, :-1]
    y = data_2.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size, random_state)
    return (X_train, X_test, y_train, y_test)
    
#q05_split(data = path, test_s= 0.2, random_s = 9)


