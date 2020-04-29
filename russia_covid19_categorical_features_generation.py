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



path_cases = 'covid19-russia-regions-cases/covid19-russia-cases.csv'
cases = pd.read_csv(path_cases)
goal = 'Day-Confirmed'




path_steps='other_data/chronology.xlsx'
gov_steps=pd.read_excel(path_steps)
gov_steps.drop(['Descriprion'], axis=1)
dates=pd.to_datetime(gov_steps['Published'],errors='coerce').dt.date.copy()
#dates=dates.dt.date

steps=pd.DataFrame({'steps': 0 for i in cases.index}, index=cases.index)
step = 1
for c in cases['Date'].index:
      steps['steps'][c] = step
      for d in dates.index:
        if cases['Date'][c]==str(dates[d]):
            #print("{}\t{}".format(cases['Date'][c], dates[d]))
            dates[d]=pd.to_datetime('01-01-1987').date
            step=step+1
            break
        



path_isolation='other_data/isolation.xlsx'
isolation=pd.read_excel(path_isolation)


isolation_moscow=pd.DataFrame([isolation.loc[i] for i in isolation.index 
                                 if isolation['Country'][i] == 'Россия'
                                  and isolation['City'][i] == 'Москва'])
