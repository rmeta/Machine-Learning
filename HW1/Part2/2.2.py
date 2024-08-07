# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:18:56 2022

@author: centrtal2021
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from statsmodels.tsa.seasonal import seasonal_decompose 
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
df=pd.read_csv('F:/Master Course/Machin learning/home work/Coal Power.csv')
df['Month']=pd.to_datetime(df['Month'],errors='ignore') # Month نام ستون اول که بی اسم است را ماه گذاشتم
df.set_index('Month', inplace=True)
resulte = seasonal_decompose(df['Total consumption : Texas : electric power (total) : quarterly (short tons)'], model='additive',freq=4, extrapolate_trend =4)
resulte.plot()
plot_acf(df,lags=30,zero=False)
plot_pacf(df,lags=30,zero=False)
