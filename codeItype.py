import pandas as pd
import numpy as np
df = pd.read_csv("car.csv")
print(df.isna().sum())
#Checking data to see if there are any missing Data points
df.dropna(inplace=True)
#If missing data point delete said line
print(len(df))
#Checking new length of data types
