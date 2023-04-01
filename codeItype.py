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
#apparently the numbers in the list is saved as str not ints
df['doors'] = df['doors'].map(doors_replace)

doors_colm = df['doors']
persons_colm = df['persons']
#there is a problem in calculating the mean since the more is not considered a number
door_mean = float(doors_colm.mean())
print(f'Mean of doors is {door_mean}')