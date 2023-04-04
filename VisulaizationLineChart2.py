import matplotlib.pyplot as plt
import pandas as pd
Unacc = pd.read_csv("highBuying.csv", index_col=False)
acc = pd.read_csv("lowBuying.csv", index_col=False)
good = pd.read_csv("medBuying.csv", index_col=False)
vgood = pd.read_csv("vhighBuying.csv", index_col=False)
def Q1MeanQ3(df, sheet_name):
    sheet_name = str(sheet_name)
    data = df[sheet_name]
    # Calculate the mean
    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    x = [mean - std_dev,mean,mean,std_dev+mean]
    return x


x = ["Q1","Mean","Mean","Q3"]
y1 = Q1MeanQ3(Unacc, "high")
y2 = Q1MeanQ3(acc, "low")
y3 = Q1MeanQ3(good, "med")
y4 = Q1MeanQ3(vgood, "vhigh")

# Create a figure and axis
fig, axs = plt.subplots()

# Add data to the axis as lines
axs.plot(x, y1, label='Unacc')
axs.plot(x, y2, label='acc')
axs.plot(x, y3, label='goog')
axs.plot(x, y4, label='vgood')


# Add title and labels to the chart
axs.set_title('Buying prices')
axs.set_xlabel('Values')
axs.set_ylabel('Price')

axs.legend()

# Show the chart
plt.show()