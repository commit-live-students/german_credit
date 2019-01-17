# %load q05_split/build.py
import pandas as pd, numpy as np
from sklearn.preprocessing import LabelEncoder
import sys, os
from sklearn.model_selection import train_test_split

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



