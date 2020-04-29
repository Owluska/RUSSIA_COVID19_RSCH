# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:28:25 2020

@author: Ксения
"""


import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def score_dataset(X_train, X_valid, Y_train, Y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, Y_train)
    out = model.predict(X_valid) 
    return mean_absolute_error(Y_valid, out)

def drop_n_score_missed(X_train, X_valid, Y_train, Y_valid):
    dropped_X_train = X_train.drop(cases_nulls, axis=1)
    dropped_X_valid = X_valid.drop(cases_nulls, axis=1)
    
    MAE_dropped=score_dataset(dropped_X_train, dropped_X_valid, Y_train, Y_valid)
    print("MAE from dataset without misssing values: {}".format(MAE_dropped))
    
    train_list=[dropped_X_train, dropped_X_valid, Y_train, Y_valid]
    return MAE_dropped, train_list

def impute_n_score_missed(X_train, X_valid, Y_train, Y_valid, strategy='mean'):
    imputer=SimpleImputer()
    
    imputed_X_train = pd.DataFrame(imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(imputer.transform(X_valid))
    
    imputed_X_train.columns=X_train.columns
    imputed_X_valid.columns=X_valid.columns
    
    MAE_imputed=score_dataset(imputed_X_train, imputed_X_valid, Y_train, Y_valid)
    print("MAE from dataset after misssing values were imputed\r\nstrategy={}: {}".format(strategy, MAE_imputed))
    
    train_list=[imputed_X_train, imputed_X_valid, Y_train, Y_valid]
    return MAE_imputed, train_list


path_cases = 'covid19-russia-regions-cases/covid19-russia-cases.csv'
path_tests = 'covid19-russia-regions-cases/covid19-tests-and-other.csv'

cases = pd.read_csv(path_cases)
#tests = pd.read_csv(path_cases)
Y = cases.Confirmed

#axis   	Whether to drop labels from the index or columns(0 or ‘index’, 1 or ‘columns’).
X = cases.drop(['Confirmed'], axis = 1)


#cases_col = [col for col in cases]
cases_nulls = [col for col in cases if cases[col].isnull().any()]
print("Found missed values in {}".format(cases_nulls))

obj_cases=cases.select_dtypes(include=['object'])
print("Categorical features are:\r\n{}".format(obj_cases))

X_no_cat=cases.drop(obj_cases, axis=1)

X_train, X_valid, Y_train, Y_valid = train_test_split(X_no_cat, Y, train_size=0.8, test_size=0.2,
                                                      random_state=0)
df_dict={}

if( len(cases_nulls) != 0):   

    MAE, _list = drop_n_score_missed(X_train, X_valid, Y_train, Y_valid)
    df_dict.update({MAE:_list})
    
    
    MAE, _list = impute_n_score_missed(X_train, X_valid, Y_train, Y_valid)
    df_dict.update({MAE:_list})
    
    MAE, _list = impute_n_score_missed(X_train, X_valid, Y_train, Y_valid, strategy='most_frequent')
    df_dict.update({MAE:_list})
    
    MAE, _list = impute_n_score_missed(X_train, X_valid, Y_train, Y_valid, strategy='median')
    df_dict.update({MAE:_list})
    key=min(df_dict.keys())
    _X_train, _X_valid, Y_train, Y_valid = df_dict[key] 
    
    
    

