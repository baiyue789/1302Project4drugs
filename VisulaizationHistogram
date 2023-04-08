import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Car_converted.csv", index_col=False,nrows=300)
df["buying"].plot(kind='hist', label='Buying')
df["maint"].plot(kind='hist', label='Maintenance')

plt.legend()

plt.show()