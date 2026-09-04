import pandas as pd
import numpy as np

df = pd.DataFrame(data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'], 'Temperature' : [32, 75, 30, 77]})

pd.pivot_table(df, index=['Date'], columns=['City'])

data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'Temperature': [32, 75, 30, 77],
        'Humidity': [80, 10, 85, 5]}

df = pd.DataFrame(data)
pd.pivot_table(df, index = 'Date', columns=['City'])

data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'Temperature': [32, 75, 30, 77, 33, 78],
        'Humidity': [80, 10, 85, 5, 81, 7]}

df = pd.DataFrame(data)

pd.pivot_table(df, index='City', values = 'Temperature', aggfunc='mean')

df.groupby('City')[['Temperature']].mean()

# Creating the DataFrame
data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-03'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles', 'Chicago'],
        'Temperature': [32, 75, 30, 77, np.nan, 76, np.nan]}
df = pd.DataFrame(data)

# create a pivot table
pivot_df = df.pivot_table(index='Date', columns='City', values='Temperature')

print("\nDefault pivot table\n", pivot_df)

# print(pd.pivot_table(df, index = 'City', values=['Temperature']))

# create a pivot table with dropna=True
pivot_df_dropna = df.pivot_table(index='Date', columns='City', values='Temperature', dropna=False)

print("\nPivot table with dropna=False:\n", pivot_df_dropna)

print("\n Pivot table with fill value \n", df.pivot_table(index='Date', columns = 'City', values = 'Temperature', fill_value=0))