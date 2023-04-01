import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("car.csv", index_col=False)
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
print(f'Mean number of doors:{door_mean} Median number of doors:{door_median}')
print(f'Mean:{buying_mean} Median:{buying_median}')

# create a scatter chart of columns 'A' and 'B'
plt.scatter(df['doors'], df['persons'])
plt.title("Scatter Chart")
plt.xlabel("number of doors")
plt.ylabel("People who can fit")
plt.show()