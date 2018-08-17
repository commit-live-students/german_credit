import sys, os
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score
from greyatomlib.german_credit.q06_feature_preprocessing.build import q06_feature_preprocessing
path = 'data/GermanData.csv'

""" Use the following as your param_distribution """

#parameters = {'n_estimators':[100,150,200],'max_depth':[3,4,5],'min_samples_split':[2,3,4]}


