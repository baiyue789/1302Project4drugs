import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Car_converted.csv", index_col=False)
def the_X_based_on_database_compare(db):
    if db == "C":
        x = ['unacc', 'acc', 'good', 'vgood']
        return x
    if db == "B":
        x = ["vhigh", "high","med", "low"]
        return x
    if db == "M":
        x = ["high","med", "low"]
        return x
    if db == "P":
        x = ['2','4', "more"]
        return x
    if db == 'D':
        x = ['2', '3', '4', '5more']
        return x
    if db =='L':
        x = ['small', 'med', 'big']
        return x
    if db =='S':
        x = ['low', 'med', 'high']
        return x
        
lol = 'state'
grouped = df.groupby(lol)
counts = grouped.size()
y= the_X_based_on_database_compare("C")
plt.pie(counts, labels=y)
plt.show()