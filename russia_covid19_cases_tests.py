# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:28:25 2020

@author: Ксения
"""


import pandas as pd
from sklearn.impute import SimpleImputer



path_cases = 'covid19-russia-regions-cases/covid19-russia-cases.csv'
path_tests = 'covid19-russia-regions-cases/covid19-tests-and-other.csv'

cases = pd.read_csv(path_cases)
tests = pd.read_csv(path_cases)


cases_col = [col for col in cases]
cases_nulls = [col for col in cases if cases[col].isnull().any()]
# cases_na = [col for col in cases if cases[col].isna().any()]

# cases_nulls = []
# for col in cases:
#     if cases[col].isnull().any():
#         cases_nulls.append(col)

# print(cases_nulls, cases_na)

tests_col = [col for col in tests]
tests_nulls = [col for col in tests if tests[col].isnull().any()]
# tests_na = [col for col in tests if tests[col].isna().any()]
# print(tests_nulls, tests_na)

my_imputer = SimpleImputer()
imputed_cases = pd.DataFrame(my_imputer.fit_transform(cases))
imputed_tests = pd.DataFrame(my_imputer.transform(tests))

# Imputation removed column names; put them back
imputed_cases.columns =cases.columns
imputed_tests.columns =tests.columns