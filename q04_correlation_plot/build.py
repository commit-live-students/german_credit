# %load q04_correlation_plot/build.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
#plt.switch_backend('agg')
import sys, os
from greyatomlib.german_credit.q03_encode_features.build import q03_encode_features     
path = 'data/GermanData.csv'

def q04_correlation_plot(data):
    data_1 = q03_encode_features(data)
    data_2 = pd.DataFrame(list(data_1)[0])
    correlations = data_2.corr()
    # plot correlation matrix
    plt.figure()
    sns.heatmap(correlations)
    #fig.colorbar(cax)
    ticks = np.arange(0,9,1)
    #ax.set_xticks(ticks)
    #ax.set_yticks(ticks)
    #ax.set_xticklabels('names')
    #ax.set_yticklabels('names')
    #plt.show()
    #return correlations
    
q04_correlation_plot(path)


