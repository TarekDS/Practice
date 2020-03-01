# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:47:18 2019

@author: T
"""

import pandas as pd

import matplotlib.pyplot as plt

car = pd.DataFrame()

car.head()

car.loc[:, "buying"] = ["vhigh","high","vhigh","med"]

car.loc[:, "doors"] = [2,2,4,4]

car.loc[4] = ["vlow", 3]


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"

cars = pd.read_csv(url ,header = None)

cars.head()

cars.columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "evaluation"]

cars.loc[:, "doors"].unique()

fivemore = cars.loc[:, "doors"] == "5more"

print(fivemore)

cars.loc[fivemore, "doors"] = 5

plt.hist(cars.loc[:, "doors"])

# Use the pandas package
import pandas as pd
# The url for the data
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
Adult = pd.read_csv(url, header=None)
Adult.head()

import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data"
Votes = pd.read_csv(url, header=None)
Votes.head()

Votes.replace(to_replace="?", value=float("NaN"))

Votes[5].isnull().sum()

Votes.shape




