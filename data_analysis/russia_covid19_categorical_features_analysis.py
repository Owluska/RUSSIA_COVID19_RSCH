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

def score_dataset(X_train, X_valid, Y_train, Y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, Y_train)
    out = model.predict(X_valid) 
    return mean_absolute_error(Y_valid, out)




path_cases = 'covid19-russia-regions-cases/covid19-russia-cases.csv'
cases = pd.read_csv(path_cases)

obj_cases=cases.select_dtypes(include=['object'])
print("Categorical features are:\r\n{}".format(obj_cases))
cases_nulls = [col for col in cases if cases[col].isnull().any()]

# Remove rows with missing target, separate target from predictors
cases.dropna(axis=0, subset=['Confirmed'], inplace=True)  
Y = cases.Confirmed
#axis   	Whether to drop labels from the index or columns(0 or ‘index’, 1 or ‘columns’).
X = cases.drop(['Confirmed'], axis = 1)
X.drop(cases_nulls, axis=1, inplace=True)


# Break off validation set from training data
X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y,
                                                      train_size=0.8, test_size = 0.2,
                                                      random_state=0)



# num_train=X_train.select_dtypes(exclude=['object'])
# num_valid=X_valid.select_dtypes(exclude=['object'])

# Columns that can be safely label encoded

# Fitting a label encoder to a column in the training data creates a
# corresponding integer-valued label for each unique value that appears
# in the training data. In the case that the validation data contains
# values that don't also appear in the training data, the encoder will
# throw an error, because these values won't have an integer assigned to
# them. Notice that the 'Condition2' column in the validation data contains
# the values 'RRAn' and 'RRNn',
# but these don't appear in the training data -- thus, if we try to use
# a label encoder with scikit-learn, the code will throw an error.

# set is a container filled by randomly ordered unique values
good_labels = [col for col in obj_cases if 
                   set(X_train[col]) == set(X_valid[col])]
        
# Problematic columns that will be dropped from the dataset
bad_labels = list(set(obj_cases)-set(good_labels))
        
print('Categorical columns that will be label encoded:', good_labels)
print('\nCategorical columns that will be dropped from the dataset:', bad_labels)


if(bad_labels != []):
    labels_train=X_train.drop(bad_labels, axis=1)
    labels_valid=X_valid.drop(good_labels, axis=1)
    

if(good_labels != []):
    label_encoder=LabelEncoder()
    labels_train=[label_encoder.fit_transform(X_train(col)) for col in good_labels] 
    labels_valid=[label_encoder.transform(X_valid(col)) for col in good_labels]    
    MAE_le=score_dataset(labels_train, labels_valid, Y_train, Y_valid)
    print("MAE from Label Encoding: {}".format(MAE_le))

obj_unique=list(map(lambda col: X_train[col].nunique(), obj_cases))
d=dict(zip(obj_cases, obj_unique))
d=sorted(d.items(), key=lambda x: x[1])
print("Cardinality of categorical features: {}".format(d))

low_cardinality = [col for col in obj_cases if X_train[col].nunique() < 10]
high_cardinality=list(set(obj_cases)-set(low_cardinality))

print('Categorical columns that will be one-hot encoded:', low_cardinality)
print('Categorical columns that will be dropped from the dataset:', high_cardinality)

