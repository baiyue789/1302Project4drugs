import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
df = pd.read_csv("car.csv", index_col=False)
#Checking new length of data types
doors_persons = {"2": 2, "3": 3, "4": 4, "5more" : 5, "more": 6}
buying_maint_safety = {"vhigh": 4, "high":3, "med":2, "low":1}
lug = {"small":1, "med":2, "big":3}
state_change = {"unacc":1, "acc":2, "good":3, "vgood":4}
#apparently the numbers in the list is saved as str not ints

df['buying'] = df['buying'].map(buying_maint_safety)
df['maint'] = df['maint'].map(buying_maint_safety)
df['doors'] = df['doors'].map(doors_persons)
df['persons'] = df['persons'].map(doors_persons)
df['lug_boot'] = df['lug_boot'].map(lug)
df['safety'] = df['safety'].map(buying_maint_safety)
df['state'] = df['state'].map(state_change)

for sheet_name in df:
    data = df[sheet_name]
    # Calculate the mean
    mean = data.mean()
    # Calculate the median
    median = data.median()
    # Calculate the variance
    variance = data.var()# Calculate the standard deviation
    std_dev = data.std()
    # Print the results
    print(f"{sheet_name}")
    print('Mean:', mean)
    print('Median:', median)
    print('Variance:', variance)
    print('Standard Deviation:', std_dev)
for col in df.columns:
    plt.boxplot(df[col])
    plt.title(f'Box Chart of {col}')
    plt.xlabel(col)
    plt.ylabel('Value')
    plt.show()