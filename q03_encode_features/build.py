# %load q03_encode_features/build.py
import pandas as pd
import numpy as np
import sys, os
from sklearn.preprocessing import LabelEncoder
from greyatomlib.german_credit.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q03_encode_features(data):
    data_1 = q01_load_data_and_add_column_names(data)
    data1 = data_1.copy()
    dic = {}
    df= data_1.select_dtypes(include=['object'])
    
    # Initilalizing LabelEncoder()
    le = LabelEncoder()
    
    df_encoded = df.apply(le.fit_transform)
    data_1.update(df_encoded)
    return (data_1), (data_1.shape)
    
q03_encode_features(path)


