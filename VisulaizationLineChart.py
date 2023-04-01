import matplotlib.pyplot as plt
import pandas as pd
Unacc = pd.read_csv("Unacc.csv", index_col=False)
acc = pd.read_csv("acc.csv", index_col=False)
good = pd.read_csv("good.csv", index_col=False)
vgood = pd.read_csv("vgood.csv", index_col=False)
def Q1MeanQ3(df, sheet_name):
    sheet_name = str(sheet_name)
    data = df[sheet_name]
    # Calculate the mean
    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    x = [mean - std_dev,mean,std_dev+mean]
    return x


x = [1.0,2.0,3.0]
y1 = Q1MeanQ3(Unacc, "buying")
y2 = Q1MeanQ3(acc, "buying")
y3 = Q1MeanQ3(good, "buying")
y4 = Q1MeanQ3(vgood, "buying")

# Create a figure and axis
fig, axs = plt.subplots(2,2)

# Add data to the axis as lines
axs[0, 0].plot(x, y1)
axs[0, 1].plot(x, y2)
axs[1, 0].plot(x, y3)
axs[1, 1].plot(x, y4)

# Add title and labels to the chart
fig.suptitle('Four Plot Line Chart')
axs[0, 0].set_ylabel('Unacc')
axs[0, 1].set_ylabel('Acc')
axs[1, 0].set_ylabel('Good')
axs[1, 1].set_ylabel('Vgood')
for ax in axs.flat:
    ax.set_xlabel('X-axis')

# Show the chart
plt.show()