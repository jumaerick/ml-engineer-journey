import pandas as pd
import numpy as np

data = [['erick', 'juma'], [23, 45], [23, 45]]

df = pd.DataFrame(data, columns = ['name', 'age'])

anotherSeries = pd.Series([25,10, 48])
anotherSeriesTwo = pd.Series([25,10, 48, 23])

#Extract values 
anotherSeries.to_numpy()

#check if  empty
df.duplicated()

#check if  empty
df.drop_duplicates()

#check if the entries are present in the rows
df.isin(['erick', 'juma'])

#check if not present
~df.isin(['erick', 'juma'])

#pass a value to check for
df.isin({'name': ['erick'], 'age': [45]})

#Group by
dfTest = pd.DataFrame({'name': ['erick', 'james', 'peter', 'erick'], 'age': [25, 85, 17, 25]})

dfTest.groupby('name')[['age']].sum().sort_values(by = 'age', ascending = False)

# Filtering
dfTest[(dfTest['age'] > 30)]

mask = dfTest['age'] > 30

dfTest[mask]

groups = dfTest.groupby('name')[['age']].count().rename(columns = {'age':'count'})
maskTwo = groups['count']> 1
dfTest['age'].mask(dfTest['age'] > 60, 10)

# Return unique entries if duplicates return first occurence
maskThree = dfTest.duplicated(keep='first')
dfTest[~maskThree]

#Return first instance of duplicated rows
dfTest[maskThree]

dfTest.to_numpy()

#iterate each column as series
for item in dfTest.items():
    # print(item)
    pass

# iterate each row return is generator of series 
for item in dfTest.iterrows():
    item[1]['name'], item[1]['age']

x = lambda x : x**2

list(map(x, [2, 5, 6]))

population = pd.DataFrame({'births': [23, 45, 86], 'income': [879, 654, 244]})

tester = pd.DataFrame({'nums': [0]})

#cumulative sum along the rows default along columns
population.cumsum(axis=1)

population.T

#Works on an array or series with single item to return scalar
tester.squeeze()

#explode when storing a list of values in asingle colums
df = pd.DataFrame(
    {
        "A": [[0, 1, 2], "foo", [], [3, 4]],
        "B": 1,
        "C": [["a", "b", "c"], np.nan, [], ["d", "e"]],
    }
)

df.explode('A')

df.explode(list('AC'))

# Melt unpivot dataframe
df = pd.DataFrame(
    {
        "A": {0: "a", 1: "b", 2: "c"},
        "B": {0: 1, 1: 3, 2: 5},
        "C": {0: 2, 1: 4, 2: 6},
    }
)

df.melt(id_vars='A', value_vars=['B'])
df.melt(id_vars='A', value_vars=['B', 'C'])

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

import json
strOne = '{"name": "Erick", "City": "Nairobi"}'
strTwo = {"name": "Erick", "City": "Nairobi"}
type(json.loads(strOne))
json.dumps(strTwo)

data = {"city": "Nairobi", "active": True}

# Writing to a file named 'output.json'
with open("output.json", "w") as file:
  json.dump(data, file, indent=4)

with open("output.json", "r") as file:
   json.load(file)
   

