# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:28:25 2020

@author: Ксения
"""


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import category_encoders as ce

def score_dataset(X_train, X_valid, Y_train, Y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, Y_train)
    out = model.predict(X_valid) 
    return mean_absolute_error(Y_valid, out)

#dates=dates.dt.date
#dates=pd.to_datetime(gov_steps['Date'],errors='coerce').dt.date.copy()
# steps=pd.DataFrame({'steps': 0 for i in cases.index}, index=cases.index)
# step = 1
# for c in cases['Date'].index:
#       steps['steps'][c] = step
#       for d in dates.index:
#         if cases['Date'][c]==str(dates[d]):
#             #print("{}\t{}".format(cases['Date'][c], dates[d]))
#             dates[d]=pd.to_datetime('01-01-1987').date
#             step=step+1
#             break
        
def load(path, to_drop=[]):
    df = pd.read_excel(path)
    df['Date']=pd.to_datetime(df['Date'], errors='coerce')
    if to_drop != []:
        df.drop(to_drop, axis=1, inplace=True)
    return df
    
path_cases = 'other_data/covid19-russia-cases.xlsx'
path_steps='other_data/chronology.xlsx'
path_isolation='other_data/isolation.xlsx'

sets=[]
paths=[path_cases, path_steps, path_isolation]
for p in paths:
    if p == path_cases:
        drops=['Region/City', 'Region/City-Eng']
    if p == path_steps:
        drops =['Descriprion']
    if p == path_isolation:
        drops=['Country']
    sets.append(load(p, to_drop=drops))
    
# cases = pd.read_excel(path_cases)
# cases['Date']=pd.to_datetime(cases['Date'], errors='coerce')

merged=sets[0].merge(sets[1], how='inner', on='Date').merge(sets[2], how='inner', on='Date')

merged.to_excel('other_data/merged.xlsx', sheet_name='merged')


# path_steps='other_data/chronology.xlsx'
# gov_steps=pd.read_excel(path_steps)
# gov_steps.drop(['Descriprion'], axis=1)
# gov_steps['Date']=pd.to_datetime(gov_steps['Date'], errors='coerce')
# merge=cases.merge(gov_steps, how='inner', on='Date')


# path_isolation='other_data/isolation.xlsx'
# isolation=pd.read_excel(path_isolation)

# isolation_russia=pd.DataFrame([isolation.loc[i] for i in isolation.index 
#                                  if isolation['Country'][i] == 'Россия'])
# isolation_russia.drop(['Country'], axis=1, inplace=True)
# isolation_russia['Date']=pd.to_datetime(isolation_russia['Date'], errors='coerce')
# #isolation_russia.index=isolation_russia['Date']

# merge=cases.merge(isolation_russia, how='inner', on='Date')
# drop_list=['Region/City', 'Region/City-Eng']
# merge.drop(drop_list, axis=1, inplace=True)
