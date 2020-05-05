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
        

path_cases = 'covid19-russia-regions-cases/covid19-russia-cases.csv'
cases = pd.read_csv(path_cases)
cases['Date']=pd.to_datetime(cases['Date'], errors='coerce')
goal = 'Day-Confirmed'



path_steps='other_data/chronology.xlsx'
gov_steps=pd.read_excel(path_steps)
gov_steps.drop(['Descriprion'], axis=1)
gov_steps['Date']=pd.to_datetime(gov_steps['Date'], errors='coerce')
merge=cases.merge(gov_steps, how='inner', on='Date')


path_isolation='other_data/isolation.xlsx'
isolation=pd.read_excel(path_isolation)

isolation_russia=pd.DataFrame([isolation.loc[i] for i in isolation.index 
                                 if isolation['Country'][i] == 'Россия'])
isolation_russia.drop(['Country'], axis=1, inplace=True)
isolation_russia['Date']=pd.to_datetime(isolation_russia['Date'], errors='coerce')
#isolation_russia.index=isolation_russia['Date']

merge=cases.merge(isolation_russia, how='inner', on='Date')
drop_list=['Region/City', 'Region/City-Eng']
merge.drop(drop_list, axis=1, inplace=True)
