# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:03:31 2022

@author: centrtal2021
"""
from matplotlib import pyplot
import pandas as pd
import seaborn as sn
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
df=pd.read_csv('F:/Master Course/Machin learning/home work/Brent Spot Price.csv')
df['Month']=pd.to_datetime(df['Month'],errors='ignore') # Month نام ستون اول که بی اسم است را ماه گذاشتم
df.set_index('Month', inplace=True)
size = round( len(df)*.8)
X_tr= df.iloc[ :size]
X_te= df.iloc[size:] 
ma =ARMA(X_tr, order=(0,3)).fit()
print(ma.summary())
print (ma.summary())
pred=ma.predict(start=len(X_tr),end=len(df)-1,dynamic=False)
pyplot.plot(pred,color='red')
pyplot.plot(X_te,color='blue')
print(pred)
