#A datatype that stores data as rows and columns

import pandas as pd
import numpy as np

data = [['erick', 'juma'], [23, 45], [23, 45]]

df = pd.DataFrame(data, columns = ['name', 'age'])


data_dict = {'banana': 3, 'apple': 5, 'cherry': 1}

dfTwo = pd.DataFrame()

alist = sorted(data_dict.items(), key = lambda item : item[-1], reverse=True)

seriesOne = pd.Series([23, 45, 67])

#Specifying indices
seriesOne.index = ['one', 'two','three']

#Accessing value (index based)
# seriesOne[2]
seriesOne['one']

# Reset index
seriesOne.reset_index(drop=True, inplace= True)

#Specifying ranges are exclusive
seriesOne[:1]

#Assigning values
seriesOne[2] = 10

#concat (each retains its index)
seriesTwo = pd.Series(['james', 'Goes', 'to', 'Work'])

seriesC = pd.concat([seriesOne, seriesTwo])

#Arithmetic operations

seriesThree = pd.Series([52, 45, 8])

#Addition (values should be integers) and same shape
seriesOne + seriesThree

#Applying string operation to each element
seriesTwo.str.lower()
seriesTwo.name = 'profile'

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], 
                        index=['Flour', 'Milk', 'Eggs', 'Spam'], name ='Dinner')

# print(ingredients)

# reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)
