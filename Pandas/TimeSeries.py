import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

timeseries = pd.date_range(start='2021-01-01', end='2021-01-31', freq= 'D')

business = pd.date_range(start='2021-01-01', end='2021-03-31', freq= 'B')

periodic = pd.date_range(start = '2021-01-01', periods = 5, freq='MS')

quarterlt =pd.date_range(start = '2021-01-01', end = '2021-12-31', freq='QS')

df = pd.DataFrame(data = np.random.randint(1, 9, len(timeseries)), index = timeseries, columns =['Sales'])

print(df.rolling(window=7).mean())
df.resample('W').sum()  

# Sample time-series data
data = {
    'date': pd.date_range('2023-01-01', periods=10, freq='D'),
    'sales': [200, 220, 250, 230, 210, 300, 280, 270, 260, 240]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Resampling sales data to get weekly sums
weekly_sales = df.resample('W', on='date').sum()

# print(weekly_sales)
pd.DatetimeIndex(df['date']).day_of_week

sales_weekly=df.resample('W', on='date').agg({'sales': ['sum', 'mean']})

# print(sales_weekly)
# Downsampling Reducing the data frequency (e.g., from daily to monthly).
monthly_sales = df.resample('ME', on='date').sum()

monthly_sales

# Upsampling: Increasing the data frequency (e.g., from daily to hourly).
# hourly_sales = df.resample('h', on='date').ffill()

# print(hourly_sales)

df_copy = df.set_index('date')

# hourly_sales = df_copy.resample('h').fill()

hourly_sales = df_copy.resample('h').interpolate('linear')
hourly_sales