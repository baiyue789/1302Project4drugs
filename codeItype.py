import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Car_converted.csv", index_col=False)
print(len(df))

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
    print(f"{sheet_name}\n")
    print('Mean:', mean)
    print('Median:', median)
    print('Variance:', variance)
    print('Standard Deviation:', std_dev,)
    print()
for col in df.columns:
    plt.boxplot(df[col])
    plt.title(f'Box Chart of {col}')
    plt.xlabel(col)
    plt.ylabel('Value')
    plt.show()