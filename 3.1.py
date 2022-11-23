# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:23:05 2022

@author: centrtal2021
"""
from matplotlib import pyplot
import pandas as pd
import seaborn as sn
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
df=pd.read_csv('F:/Master Course/Machin learning/home work/Brent Spot Price.csv')
df['Month']=pd.to_datetime(df['Month'],errors='ignore') # Month نام ستون اول که بی اسم است را ماه گذاشتم
df.set_index('Month', inplace=True)
size = round( len(df)*.8)
X_tr= df.iloc[ :size]
X_te= df.iloc[size: ]
ar= AutoReg(X_tr, lags =2).fit()
print (ar.summary())
pred=ar.predict(start=len(X_tr),end=len(df)-1,dynamic=False)
pyplot.plot(pred,color='red')
pyplot.plot(X_te,color='blue')
print(pred)
