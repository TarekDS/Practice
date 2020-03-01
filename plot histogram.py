# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:04:20 2019

@author: T
"""

import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/mammographic-masses/mammographic_masses.data"
mam = pd.read_csv(url, header= None)

mam.columns = ["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

mam.dtypes

mam.loc [:,"BI-RADS"] = pd.to_numeric(mam.loc[:,"BI-RADS"], errors= 'coerce')

hasnan = np.isnan(mam.loc[:, "BI-RADS"])

print(hasnan)

mam.loc[hasnan,"BI-RADS"] = np.median(mam.loc[:, "BI-RADS"])

plt.hist(mam.loc[:, "BI-RADS"])

toohigh = mam.loc[:, "BI-RADS"] > 6

mam.loc[toohigh, "BI-RADS"] = 6

import pandas as pd
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
Adult = pd.read_csv(url, header=None)

Adult.sum(axis=1)
Adult.head

import pandas as pd
import matplotlib.pyplot as plt
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data"
BloodDonation = pd.read_csv(url)
BloodDonation.columns = ["MostRecent", "Donations", "Volume", "First", "Donated"]

plt.hist(BloodDonation.loc[:,"Donated"])


import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
Iris = pd.read_csv(url, header=None)
Iris.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
scatter_matrix(Iris)
Iris.dtypes

import numpy as np
import pandas as pd

# The url for the data
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.hungarian.data"
Heart = pd.read_csv(url, header=None)
# Replace the default column names 
Heart.columns = ["age", "sex", "cp", "trestbps", "chol", "fbs",
                 "restecg", "thalach", "exang", "oldpeak", "slope",
                 "ca", "thal", "num"]

Heart.dtypes
Heart.loc [:,"chol"] = pd.to_numeric(Heart.loc[:,"chol"], errors= 'coerce')

Heart["chol"].median()
Heart["chol"].std()


Heart.loc[HasNan, "chol"] = np.median(Heart.loc[:,"chol"])

Heart["chol"].isnull().sum()

HasNan = np.isnan(Heart.loc[:,"chol"])

Heart.loc[HasNan, "chol"] = np.median(Heart.loc[:,"chol"])
#output  67.65771142295964
Heart.loc[HasNan, "chol"] = np.nanmedian(Heart.loc[:,"chol"])
64.98224504483035



