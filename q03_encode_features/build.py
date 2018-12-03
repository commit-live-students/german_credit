# %load q03_encode_features/build.py
import pandas as pd
import numpy as np
import sys, os
from sklearn.preprocessing import LabelEncoder
from greyatomlib.german_credit.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'

def q03_encode_features(path):
    dict1 = {}
    data = q01_load_data_and_add_column_names(path)
    data_copy = data.copy()

    cat_features = data.select_dtypes(include=['object'])
    cat_features_array = np.array(cat_features.columns)


    lE = LabelEncoder()
    for i in range(len(cat_features_array)):
        data_copy.loc[:,cat_features_array[i]] = lE.fit_transform(data_copy.loc[:,cat_features_array[i]])
        
    return data_copy,dict1






