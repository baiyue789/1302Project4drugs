import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

#df = df.drop(df[df['state'] != 4].index)
#cutting the data for visualization
df = df.drop(df[df['buying'] != 2].index)
df.to_csv("lowBuying.csv",index=False)
len(df)
