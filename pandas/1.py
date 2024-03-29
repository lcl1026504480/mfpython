# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:42:09 2020

@author: lenovouser
"""

import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,4,1]) # similar with 1D numpy
print(s)
dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
print(df['B'])
df2 = pd.DataFrame({'A' : 1.,
                       'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                        'D' : np.array([3] * 4,dtype='int32'),
                        'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo'})
print(df2)
print(df2.dtypes)

print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
#print(df.T)
#print(df.sort_index(axis=1, ascending=False))
#print(df.sort_values(by='B'))