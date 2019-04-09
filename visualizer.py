#!/usr/bin/env python
# Name: Janneke Witvliet
# Student number: 10508848
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt
from statistics import mean

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

# Global dictionary for the data
data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}
# making a reader that goes through the csvfile
with open('movies.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    #iterate through the rows in the csvfile
    for row in reader:

        year = row[2]
        rating = row[1]
        # checking if key is in the dictionary
        if year in data_dict:
            data_dict[year].append(float(rating))
        else:
            continue

# iterating through the keys to obtain ratings per year
years_list = []
ratings_list = []
for key in data_dict:
    # get the mean rating per year
    mean_rating = mean(data_dict[key])
    years_list.append(int(key))
    ratings_list.append(float(mean_rating))

# getting al the keys in a list

plt.plot(years_list, ratings_list)
plt.ylabel('Average movie rating')
plt.xlabel('Year of movierelease')
plt.ylim((0,10))
plt.show()


if __name__ == "__main__":
    print(data_dict)
