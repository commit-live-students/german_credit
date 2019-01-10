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
    fig, ax = plt.subplots(figsize=(20, 15))
    rows = ceil(float(df.shape[1]) / cols)
    for i, column in enumerate(df.columns):
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.set_title(column)
        if df.dtypes[column] == np.object:
            ax.bar(df[column].value_counts().index,df[column].value_counts().values )
        else:
            ax.hist(df[column])
            plt.xticks(rotation='vertical')
            plt.subplots_adjust(hspace=0.7, wspace=0.2)
        plt.show()






