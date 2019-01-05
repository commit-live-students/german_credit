# %load q01_load_data_and_add_column_names/build.py
import pandas as pd


path = 'data/GermanData.csv'

def q01_load_data_and_add_column_names(path):
    df = pd.read_csv(path, header=None)
    df.columns = ['account_status', 'month', 'credit_history', 'purpose', 'credit_amount', 'savings_account/bonds', 
                                  'employment', 'installment_rate', 'personal_status/sex', 'guarantors', 'residence_since', 
                                  'property', 'age', 'other_installment_plans', 'housing', 'number_of_existing_credits', 'job', 
                                  'liable', 'telephone', 'foreign_worker', 'good/bad']
    df['good/bad']= (df['good/bad']>1).astype(int)
    return df




