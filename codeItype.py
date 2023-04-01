import pandas as pd
import numpy as np
df = pd.read_csv("car.csv", index_col=False)
# Identify missing data
df.isna().sum()
# Drop rows with missing data
df = df.dropna()
# Fill in missing data with the mean value
df = df.fillna(df.mean())
df.isna().sum()
df.info()
df.duplicated().sum()
df = df.drop_duplicates()
len(df)
#Checking new length of data types
doors_persons = {"2": 2, "3": 3, "4": 4, "5more" : 5, "more": 6}
buying_maint_safety = {"vhigh": 4, "high":3, "med":2, "low":1}
lug = {"small":1, "med":2, "big":3}
#apparently the numbers in the list is saved as str not ints
df['doors'] = df['doors'].map(doors_persons)
doors_colm = df['doors']
#there is a problem in calculating the mean since the more is not considered a number
door_mean = float(doors_colm.mean())
door_median = float(doors_colm.median())
print(f'Mean:{door_mean} Median:{door_median}')