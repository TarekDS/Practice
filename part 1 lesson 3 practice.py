# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:31:48 2019

@author: T
"""

json_obj = {"name": "tariq",
            "age":"33",
            "siblinegs": ["tasmia", "raisa"],
            "cars": {"toyota":["sads", "rav4"],
                     "honda": ["civic", "accord"]
                     }
            }
            
print(json_obj["name"])
print(json_obj["siblinegs"][0])


import json as j

json_data = '{"name": "tariq", "age": "three"}'
python_object = j.loads(json_data)

print(python_object["name"])

jason_array= '{"drinks": ["coffee", "tea", "water"]}'
data = j.loads(jason_array)

for element in data ["drinks"]:
    print(element)
    
d={}
d["name"] = "steve"
d["County"]="pakistan"

print(d)
json_object = j.dumps(d)
print(json_object)




json_array= '{"drinks": "coffee", "TV": "samsung"}'
loadinpy = j.loads(json_array)

print(loadinpy)

print(j.dumps(loadinpy, sort_keys= True, indent=4))


import requests
response = requests.get("https://en.wikipedia.org/robots.txt")

txt = response.text

print(txt)




json_object2 = {"attribute1":["value1", "value2"],
                "attribute2": ["value3","value4"],
                "attribute3":{"attributewithinatt":["value5a","value5b"],
                              "2ndattributewithinatt":["value6"]
                              }
                }



print(json_object2["attribute3"]["attributewithinatt"][1])

python_object2= j.dumps(json_object2)
python_load1 = j.loads(python_object2)

print(python_load1["attribute3"]["attributewithinatt"][1])

print(python_object2["attribute2"])

for element in python_load1 ["attribute3"]["2ndattributewithinatt"]: 
    print (element)
    
    
    
from bs4 import BeautifulSoup
url = "https://wiki.python.org/moin/IntroductoryBooks"
response = requests.get(url)

print(response.content)
content = response.content

soup = BeautifulSoup(content, "lxml")
print(soup.prettify())

all_a = soup.find_all("a")
for x in all_a: print(x)

all_a_https = soup.find_all("a","http")
print(all_a_https[1])

for x in all_a_https: print (x.attrs['href'])

#PUTTING THIS DATA IN A DICTIONARY

new_d={}
for a in all_a_https:
    title=a.string.strip()
    data[title]=a.attrs['href']
    
print(data)

import urllib.request as ur
url = "https://www.govtrack.us/data/congress/113/votes/2013/s11/data.json"
print(url)

data = j.loads(ur.urlopen(url))

#importing pandas
import pandas as pd
#assigning url variable
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
#reading CSV 
web_data = pd.read_csv(url, header=None)
#printin first 5 rows 
print(web_data.head())
#renaming a few columns
web_data.rename(columns={0:"index", 1:"type", 13:"country"})

timeserise = pd.read_csv("https://library.startlearninglabs.uw.edu/DATASCI400/Datasets/BeijingPM2_IOT.csv",
                         parse_dates=['TimeStamp'],
                         infer_datetime_format=True)

print(timeserise.head())
dataextraction1= timeserise[(timeserise["Attribute"]== 'precipitation')| 
        (timeserise["Attribute"]== 'Temp')|
        (timeserise["Attribute"]== 'HUMI')].copy()

print(dataextraction1.head())

dataextraction1 = dataextraction1.set_index(['TimeStamp'])

print(dataextraction1['2010'])

dataextraction1 ['Value'] = dataextraction1['Value'].astype(float)
dataextraction1 = dataextraction1.dropna(axis=0 , how='any')

print(dataextraction1)

groupbyyear = dataextraction1.groupby ([dataextraction1.index.year, dataextraction1.Attribute])
print(groupbyyear)
