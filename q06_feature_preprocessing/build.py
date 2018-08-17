import sys, os
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from imblearn.over_sampling import SMOTE
from greyatomlib.german_credit.q05_split.build import q05_split
path = 'data/GermanData.csv'

