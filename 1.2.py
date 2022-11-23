# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as pd 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from statsmodels.tsa.stattools import adfuller
df=pd.read_csv('F:/Master Course/Machin learning/home work/Coal Power.csv')
df['Month']=pd.to_datetime(df['Month'],errors='ignore') # Month نام ستون اول که بی اسم است را ماه گذاشتم
df.set_index('Month', inplace=True)
df.plot(figsize=(15,6))
d1=df['Total consumption : Texas : electric power (total) : quarterly (short tons)'].values
result=adfuller(d1)
df['Total consumption : Texas : electric power (total) : quarterly (short tons)'].rolling(window=20).mean().plot()
df['moving avrage']= df['Total consumption : Texas : electric power (total) : quarterly (short tons)'].rolling(window=20).mean()
d2= df['moving avrage'].values
result2=adfuller(d2[19:])
