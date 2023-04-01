import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
df = pd.read_csv("car.csv", index_col=False)
#Checking new length of data types
doors_persons = {"2": 2, "3": 3, "4": 4, "5more" : 5, "more": 6}
buying_maint_safety = {"vhigh": 4, "high":3, "med":2, "low":1}
lug = {"small":1, "med":2, "big":3}
#apparently the numbers in the list is saved as str not ints

df['buying'] = df['buying'].map(buying_maint_safety)
df['maint'] = df['maint'].map(buying_maint_safety)
df['doors'] = df['doors'].map(doors_persons)
df['persons'] = df['persons'].map(doors_persons)
df['lug_boot'] = df['lug_boot'].map(lug)
df['safety'] = df['safety'].map(buying_maint_safety)
buying_colm = df['buying']
main = df['maint']
doors_colm = df['doors']
people = df['persons']
Lugs = df['lug_boot']
safe = df['safety']

#there is a problem in calculating the mean since the more is not considered a number
buying_mean= buying_colm.mean()
maint = main.mean()
door_mean = doors_colm.mean()
people = people.mean()
Lugs = Lugs.mean()
safe = safe.mean()

#all the means below
print(f'MEAN(Buying:{buying_mean} Maintence:{maint} Door:{door_mean} Persons:{people} Luggage:{Lugs} Safety:{safe})')


for sheet_name in df:
    data = df[sheet_name]
    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.set_xlabel('Data')
    ax.set_ylabel('Value')
    ax.set_title(f'Box Chart - {sheet_name}')
    plt.show()