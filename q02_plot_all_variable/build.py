# %load q02_plot_all_variable/build.py
import pandas as pd
import numpy as np
import sys, os
from math import ceil
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from greyatomlib.german_credit.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names

path = 'data/GermanData.csv'
def q02_plot_all_variable(path,rand_var=5):
    data = q01_load_data_and_add_column_names(path)
    numeric_cols = data.select_dtypes(include=['int64'])
    pd.plotting.scatter_matrix(numeric_cols)
    plt.show()
    




