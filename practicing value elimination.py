# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:13:40 2019

@author: T
"""

import numpy as np

flaggood = ([1,2,3,4,5,6,7,8])
xy = np.array([1,2,3,4,5,6,77,8,9,0])
print(xy)

limithi = np.mean(xy) + 2*np.std(xy)
limitlo = np.mean(xy) - 2*np.std(xy)

print(limitlo)

flagbad = (xy < limitlo) | (xy > limithi)

flagbad

xy[flagbad] = np.mean(xy)

xy[flagbad] = np.median(flaggood)


a = "x"
type(xy)
xy.dtype.name

straray = np.array(["aa","abc","c","7"])
daycare.dtype.name

daycare = np.array ([1,2,3,4,5," ", "?", 99])

flagnonint = (daycare != " ") & (daycare != "?")

daycare = daycare[flagnonint]

daycare = daycare.astype(int)

print (daycare > 4)

c = "7"
type(c)
2+int(c)


a = 5.1
b = np.array([3]) + a

type(b)

c = "7"
int(2 + c)
type(s)
