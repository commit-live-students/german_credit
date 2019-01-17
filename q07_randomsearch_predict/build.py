# %load q07_randomsearch_predict/build.py
import sys, os
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2
from imblearn.over_sampling import SMOTE
import pandas as pd, numpy as np
from sklearn.preprocessing import LabelEncoder
import sys, os
from sklearn.model_selection import train_test_split
# from greyatomlib.german_credit.q06_feature_preprocessing.build import q06_feature_preprocessing


''' Use the following as your param_distribution '''

parameters = {
            'n_estimators':[100,150,200],
            'max_depth':[3,4,5],
            'min_samples_split':[2,3,4]
             }

def q01_load_data_and_add_column_names(path='data/GermanData.csv'):
    df = pd.read_csv(path, header=None)
    df.columns = ['account_status', 'month', 'credit_history', 'purpose', 'credit_amount', 'savings_account/bonds', 
                                  'employment', 'installment_rate', 'personal_status/sex', 'guarantors', 'residence_since', 
                                  'property', 'age', 'other_installment_plans', 'housing', 'number_of_existing_credits', 'job', 
                                  'liable', 'telephone', 'foreign_worker', 'good/bad']
    df['good/bad']= (df['good/bad']>1).astype(int)
    return df

def q03_encode_features(path='data/GermanData.csv'):
    df = q01_load_data_and_add_column_names(path)
    df_new = df.copy()
    le = LabelEncoder()
    cols = {}
    cat_var = [a for a in range(len(df_new.dtypes)) if df_new.dtypes[a] in ['object']]
    for column in cat_var:
        df_new.iloc[:, column] = le.fit_transform(df_new.iloc[:, column]) 
        cols[column] = df.columns[column]
    return df_new, cols

def q05_split(path, test_size = 0.2, random_state=9):
    path='data/GermanData.csv'
    df, _ = q03_encode_features(path)
    y = df.iloc[:,-1]
    X = df.iloc[:,:-1]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def q06_feature_preprocessing(path, kind='regular', random_state=9, k=8):
    path='data/GermanData.csv'
    X_train, X_test, y_train, y_test = q05_split(path)
    smote = SMOTE(random_state=random_state)
    minmax = MinMaxScaler()
    kbest = SelectKBest(chi2, k=k)
    minmax.fit(X_train)
    X_train_new = minmax.transform(X_train) 
    X_train_new = pd.DataFrame(X_train_new, columns = X_train.columns)
    X_sample_s, y_sample_s = smote.fit_sample(X_train_new, y_train)
    X_imputed_train = pd.DataFrame(X_sample_s, columns = X_train.columns)
    y_imputed_train = pd.Series(y_sample_s)
    kbest.fit(X_imputed_train, y_imputed_train)
    cols = kbest.get_support(indices=True)
    X_train_final, X_test_final = X_imputed_train.iloc[:,cols], X_test.iloc[:,cols]
    return  X_train_final, X_test_final, y_imputed_train, y_test

def q07_randomsearch_predict(path):
    path = 'data/GermanData.csv'
    X_train, X_test, y_train, y_test = q05_split(path)
    random_model = RandomizedSearchCV(GradientBoostingClassifier(random_state=9), parameters)   
    random_model.fit(X_train, y_train)
    y_pred = random_model.predict(X_test)
    return roc_auc_score(y_test, y_pred)




