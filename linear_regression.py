# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:50:20 2020

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
args = (0,100,1001)
x = np.linspace(*args).reshape(-1,1)
y = (np.sin(x)).reshape(-1,1)
#y = (x**2).reshape(1,-1)
#
f = np.polyfit(x,y)

#lr = LinearRegression()
#lr.fit(x,y)
#y_bar = lr.predict(x)
#
#plt.plot(x.reshape(-1),y.reshape(-1))
#plt.plot(x.reshape(-1), y_bar.reshape(-1))
#plt.show()

