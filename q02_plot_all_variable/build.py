# %load q02_plot_all_variable/build.py
import pandas as pd
import numpy as np
import sys, os, itertools
from math import ceil
import matplotlib.pyplot as plt
plt.switch_backend('agg')

from greyatomlib.german_credit.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'
plt.style.use('seaborn-darkgrid')
def q02_plot_all_variable(path, cols=5):
    df = q01_load_data_and_add_column_names(path)
    rows = ceil(float(df.shape[1]) / cols)
    plt.figure(figsize=(15,30))
    for i, value in enumerate(df.columns):
        plt.subplot(rows,cols,i+1)
        if (df.dtypes[value] == np.object):
            df[value].value_counts().plot(kind='bar')
        else:
            df[value].hist()
        plt.xlabel(df.columns[i])
        plt.ylabel('Occurences')
        plt.title('{} Plot'.format(df.columns[i]))
        plt.tight_layout()






