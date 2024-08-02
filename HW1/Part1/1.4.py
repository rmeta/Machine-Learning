# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:11:00 2022

@author: centrtal2021
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from statsmodels.tsa.stattools import adfuller
df=pd.read_csv('F:/Master Course/Machin learning/home work/Coal Power.csv')
df['Month']=pd.to_datetime(df['Month'],errors='ignore') # Month نام ستون اول که بی اسم است را ماه گذاشتم
df.set_index('Month', inplace=True)
df_stationary=df.diff().dropna()
df_stationary.plot()
d1=df_stationary['Total consumption : Texas : electric power (total) : quarterly (short tons)'].values
result=adfuller(d1)
