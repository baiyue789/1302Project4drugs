import pandas as pd
import numpy as np
df = pd.read_csv("car.csv", index_col=False)
df = df.drop(df[df['if'] == 'unacc'].index)
print(len(df))
df.to_csv('Cars_remove_unacc.csv', index=False)
#Checking new length of data types
doors_persons = {"2": 2, "3": 3, "4": 4, "5more" : 5, "more": 6}
buying_maint_safety = {"vhigh": 4, "high":3, "med":2, "low":1}
lug = {"small":1, "med":2, "big":3}
#apparently the numbers in the list is saved as str not ints
df['doors'] = df['doors'].map(doors_persons)
df['buying'] = df['buying'].map(buying_maint_safety)
doors_colm = df['doors']
buying_colm = df['buying']
#there is a problem in calculating the mean since the more is not considered a number
door_mean = float(doors_colm.mean())
door_median = float(doors_colm.median())
buying_mean= buying_colm.mean()
buying_median = buying_colm.median()
print(f'Mean:{door_mean} Median:{door_median}')
print(f'Mean:{buying_mean} Median:{buying_median}')
