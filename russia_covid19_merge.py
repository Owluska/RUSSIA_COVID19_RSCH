# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:28:25 2020

@author: Ксения
"""


import pandas as pd
import os


def get_paths_from_folder(folder_path = '_SK/'):
   files = []
   succes_result = False
   for r, d, f in os.walk(folder_path):
        for file in f:
            files.append(os.path.join(r, file))
   if len(files) != 0:
       succes_result = True    
       return succes_result, files
   else: 
       return succes_result, files


res, paths = get_paths_from_folder('covid19-russia-regions-cases')

dfs = [pd.read_csv(p) for p in paths]

for df, p  in zip(dfs, paths):
    print("Load data '{}', shape: {} ".format(p, df.shape))
    cols = [col for col in df]
    print("Columns list: {}".format(cols),end='\n\n')

df = pd.concat(dfs, ignore_index=True)

cols = [col for col in df]
print("Data after concat, shape: {} ".format(df.shape))
print("Columns list: {}".format(cols),end='\n\n')

descr = df.describe()
print(descr)