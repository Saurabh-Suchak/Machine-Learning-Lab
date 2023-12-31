# -*- coding: utf-8 -*-
"""FINDS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17BlOJHBsus4tAqB9THSpsXPMQpkbH5As
"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import numpy as np

data= pd.read_csv("/content/gdrive/MyDrive/ml_lab/size.csv")

data.head(4)

concept= np.array(data)[ : , : -1]
print(concept)

target=np.array(data)[:, -1]
print(target)

def train(con,tar):
  for i, val in enumerate(tar):
    if val == 'Yes' or val=='yes':
      specific_h = con[i].copy()
      break
  for i, val in enumerate(con):
    if tar[i] == 'Yes' or tar[i]=='yes':
      for x in range(len(specific_h)):
        if val[x]!= specific_h[x]:
          specific_h[x]='?'
        else:
          pass
  return specific_h

print(train(concept,target))

"""**-----------------------------Example 2--------------------------------**

"""

data2= pd.read_csv("/content/gdrive/MyDrive/ml_lab/enjoysport.csv")

print(data2.head(5))

concept2= np.array(data2)[ : , : -1]
print(concept2)

target2=np.array(data2)[:, -1]
print(target2)

print(train(concept2,target2))