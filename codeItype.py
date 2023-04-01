import pandas as pd
import numpy as np
df = pd.read_csv("car.csv")
print(df.isna().sum())
#Checking data to see if there are any missing Data points
df.dropna(inplace=True)
#If missing data point delete said line
print(len(df))
#Checking new length of data types
doors_replace = {"2": 2, "3": 3, "4": 4, "5more" : 5}
person_replace = {"2": 2, "4":4, "more": 6}
#apparently the numbers in the list is saved as str not ints
df['doors'] = df['doors'].map(doors_replace)

doors_colm = df['doors']
#there is a problem in calculating the mean since the more is not considered a number
door_mean = float(doors_colm.mean())
door_median = float(doors_colm.median())
print(f'Mean:{door_mean} Median:{door_median}')

