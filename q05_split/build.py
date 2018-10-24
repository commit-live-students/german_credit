# %load q05_split/build.py
import sys, os
from sklearn.model_selection import train_test_split
from greyatomlib.german_credit.q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'


def q05_split(path,test_size=0.2,random_state = 9):
    
    df = q03_encode_features(path)
    df_new,b = df
    X = df_new.drop('good|bad',axis =1)
    y = df_new['good|bad']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= test_size, random_state = 9)
    return X_train,X_test,y_train,y_test
q05_split(path,test_size=0.2,random_state = 9)    


