# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:28:25 2020

@author: Ксения
"""


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import category_encoders as ce

def score_dataset(X_train, X_valid, Y_train, Y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, Y_train)
    out = model.predict(X_valid) 
    return mean_absolute_error(Y_valid, out)



path_cases = 'covid19-russia-regions-cases/covid19-russia-cases.csv'
cases = pd.read_csv(path_cases)
goal = 'Day-Confirmed'

# Remove rows with missing target, separate target from predictors
cases.dropna(axis=0, subset=[goal], inplace=True)  
Y = cases[goal]
X = cases.drop([goal], axis = 1)

X_nulls = [col for col in cases if cases[col].isnull().any()]
X.drop(X_nulls, axis=1, inplace=True)


X['Date']=pd.to_datetime(X['Date'], errors='coerce')
X=X.assign(day=X['Date'].dt.day,
           month=X['Date'].dt.month,
           year=X['Date'].dt.year)

X = X.drop(['Date'], axis = 1)


obj_X=X.select_dtypes(include=['object'])
#print("Categorical features are:\r\n{}".format(obj_cases))

le_encoder=LabelEncoder()
le_encoded=X[obj_X.columns].apply(le_encoder.fit_transform)
X_le=X.drop(obj_X.columns, axis=1, inplace=False)
X_le=X_le.join(le_encoded)

# X = cases.drop([goal], axis = 1)

print(list(X_le.columns))

# Break off validation set from training data
X_train, X_valid, Y_train, Y_valid = train_test_split(X_le, Y,
                                                      train_size=0.8, test_size = 0.2,
                                                      random_state=0)


MAE = score_dataset(X_train, X_valid, Y_train, Y_valid)
print("MAE after categorical feature label encoding: {}".format(MAE))

ce_encoder=ce.CountEncoder()
#ce_encoded=X[obj_X.columns].apply(ce_encoder.fit_transform)

ce_encoded=ce_encoder.fit_transform(X[obj_X.columns])
X_ce=X.drop(obj_X.columns, axis=1, inplace=False)
X_ce=X_ce.join(ce_encoded)

# X = cases.drop([goal], axis = 1)

print(list(X_le.columns))

# Break off validation set from training data
X_train, X_valid, Y_train, Y_valid = train_test_split(X_ce, Y,
                                                      train_size=0.8, test_size = 0.2,
                                                      random_state=0)


MAE = score_dataset(X_train, X_valid, Y_train, Y_valid)
print("MAE after categorical feature count encoding: {}".format(MAE))



