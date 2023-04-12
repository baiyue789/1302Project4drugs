import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
Unacc = pd.read_csv("Buying/high.csv", index_col=False)
acc = pd.read_csv("Buying/low.csv", index_col=False)
good = pd.read_csv("Buying/med.csv", index_col=False)
vgood = pd.read_csv("Buying/vhigh.csv", index_col=False)
def Q1MeanQ3(df, sheet_name):
    sheet_name = str(sheet_name)
    data = df[sheet_name]
    # Calculate the mean
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    x = [q1,q2,q3]
    return x


x = ["Q1","Median","Q3"]
y1 = Q1MeanQ3(Unacc, "maint")
y2 = Q1MeanQ3(acc, "maint")
y3 = Q1MeanQ3(good, "maint")
y4 = Q1MeanQ3(vgood, "maint")

data = [y1,
        y2,
        y3,
        y4]
df = pd.DataFrame(data, index=['Price for Unacc', 'Price for Acc', 'Price for Good', 'Price for Vgood'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()