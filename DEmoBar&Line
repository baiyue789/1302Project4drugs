import sys
import matplotlib


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Car_Converted.csv')
pf = pd.read_csv('Car_Converted.csv')
y=0
pf.plot(y= "buying")
plt.ylabel("Buying Value")
plt.xlabel("Number of Cars")
plt.title("Buying Value vs Number of Cars")
plt.show()
pf =pd.read_csv('Car_Converted.csv', nrows = 433)
pf["state"].plot(kind = 'hist')
pf["buying"].plot(kind = 'hist')
plt.legend()
plt.show()
columns = ['buying']
df1 = pd.DataFrame(df.loc[434:864])
print(df1)
df1["state"].plot(kind = 'hist')
df1["buying"].plot(kind = 'hist')
plt.legend()
plt.show()
df2 = pd.DataFrame(df.loc[866:1295])
print(df2)
df2["state"].plot(kind = 'hist')
df2["buying"].plot(kind = 'hist')
plt.legend()
plt.show()
df3 = pd.DataFrame(df.loc[1297:1729])
print(df3)
df3["state"].plot(kind = 'hist')
df3["buying"].plot(kind = 'hist')
plt.legend()
plt.show()