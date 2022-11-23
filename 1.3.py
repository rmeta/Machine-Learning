# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:57:15 2022

@author: centrtal2021
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from statsmodels.tsa.stattools import adfuller
df=pd.read_csv('F:/Master Course/Machin learning/home work/Brent Spot Price.csv')
df['Month']=pd.to_datetime(df['Month'],errors='ignore') # Month
df.set_index('Month', inplace=True)
df_stationary=df.diff().dropna()
df_stationary.plot()
d1=df_stationary['Brent crude oil spot price, Monthly (dollars per barrel)'].values
result=adfuller(d1)
