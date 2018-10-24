# %load q03_encode_features/build.py
import pandas as pd
import numpy as np
import sys, os
from sklearn.preprocessing import LabelEncoder
from greyatomlib.german_credit.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'


le = LabelEncoder()
dictionary = {}
categ = []
def q03_encode_features(path):
    df = q01_load_data_and_add_column_names(path)
    for x in df:
        if df.dtypes[x] == 'object':
            categ.append(x)
    for x in categ:
        df[x] = le.fit_transform(df[x])
    return df,dictionary


