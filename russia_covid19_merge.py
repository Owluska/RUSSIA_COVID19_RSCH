# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:28:25 2020

@author: Ксения
"""


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def score_dataset(X_train, X_valid, Y_train, Y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, Y_train)
    out = model.predict(X_valid) 
    return mean_absolute_error(Y_valid, out)

def set_df_indexes(df):
    raws_count=df.shape[0]
    df.index=[i for i in range(raws_count)]
    return df
        
def choose_category_value(df, cat, value):
    df=df[df[cat] == value].copy()
    df=set_df_indexes(df)
    return df

def load(path, cats=[], cat_values=[], to_drop=[]):
    df = pd.read_excel(path)
    df['Date']=pd.to_datetime(df['Date'], dayfirst=True,errors='coerce')
    if cats!=[] and cat_values!=[]:
      for c, cv in zip(cats, cat_values):
        #print(df.describe())
        df=choose_category_value(df, c, cv)
    if to_drop != []:
        df.drop(to_drop, axis=1, inplace=True)
   # df.dropna(axis=0, how='any', inplace=True)
    return df
    
def get_raws(df, col, value):
   i = df.columns.get_loc(col)
   raws=[raw[1:] for raw in df.itertuples() if raw[i+1] == value] 
   raws = pd.DataFrame(raws, columns=df.columns)    
   return raws

def merge_dfs(dfs, suffs, how='left', on='Date'):
  ln=len(dfs)
  mgd=pd.DataFrame(dfs[0])
  for i in range(ln):  
    if(i > ln-2):
      break
    mgd=pd.merge(mgd, dfs[i+1], suffixes=[suffs[i], suffs[i+1]], how='left', on='Date')
  return mgd

def transform_df(df, col):
  uniq=pd.unique(df[col])
  dfs=[get_raws(df, col, u) for u in uniq]

  sffxs=['_'+str(u) for u in uniq]
  df = merge_dfs(dfs, sffxs)
  return df

def drop_missed_in_raws(df):

  print("Got df with shape {}".format(df.shape))
  #_df=df.isnull()
  missed = [label for label, raw in df.iterrows() if raw.isnull().any()]
  if missed !=[]:  
    print("Found missed values in {} raws".format(len(missed)))
    df.drop(missed, axis=0, inplace=True)
  else:
    print("Raws with missed values didn't found")    
  print("Returning df with shape: {}".format(df.shape))
  return df

def drop_missed_in_cols(df):

  print("Got df with shape {}".format(df.shape))
  missed = [col for col in mrgd if mrgd[col].isnull().any()]
  if missed !=[]:  
    print("Found missed values in {} cols".format(len(missed)))
    df.drop(missed, axis=0, inplace=True)
  else:
    print("Cols with missed values didn't found")    
  print("Returning df with shape: {}".format(df.shape))
  return df  




#path_gd = '/content/drive/My Drive/CVD19_RUS_DS/'    
folder = 'data_xl/'    
path_cases = 'covid19-russia-cases.xlsx'
path_steps='chronology.xlsx'
path_isolation='isolation.xlsx'

path_cases=folder+path_cases
path_steps=folder+path_steps
path_isol=folder+path_isolation

print("Paths to data:\r\nCases: {}\r\nSteps: {}\r\nIsolation: {}".format(path_cases,
                                            path_steps, path_isol))

cases=load(path_cases, cats=['Region/City'], cat_values=['Москва'],
                        to_drop=['Region/City', 'Region/City-Eng',
                                   'Day-Deaths', 'Day-Recovered'])
steps=load(path_steps, to_drop=['Descriprion'])
isol=load(path_isol, cats=['Country','City'],
              cat_values=['Россия','Москва'],
                  to_drop=['Country','City'])






#mrgd=transform_df(cases, 'Region_ID')

mrgd=pd.merge(cases, steps, how='left', on='Date')
mrgd=pd.merge(mrgd, isol, how='left', on='Date')
print(mrgd)


