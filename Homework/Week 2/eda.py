# Name: Janneke Witvliet
# Student number: 10508848
"""
This script does......
"""

import csv
import numpy as np
import pandas as pd
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

data = pd.read_csv('input.csv', na_values = 'unknown')
#Preprocessing data
#Drop rows where no number in colum of Density, Mortality and GDP in present
data = data.dropna(subset= ['Pop. Density (per sq. mi.)','Infant mortality (per 1000 births)','GDP ($ per capita) dollars'])
#Makes floats from strings to then remove negative floats in colum infant mortality
data['Infant mortality (per 1000 births)'] = data['Infant mortality (per 1000 births)'].str.replace(",",".").astype(float)
print(data.loc[[14]])

#data = data.loc[data['Infant mortality (per 1000 births)'] > 0]

#print(data.loc[[14]])
#data = data.loc[~(data['Infant mortality (per 1000 births)'] < 0)]
# print(data)
