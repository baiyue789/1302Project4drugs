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
    x = [mean - std_dev,mean,mean,std_dev+mean]
    return x


x = [1.0,2.0,3.0,4.0]
y1 = Q1MeanQ3(Unacc, "buying")
y2 = Q1MeanQ3(acc, "buying")
y3 = Q1MeanQ3(good, "buying")
y4 = Q1MeanQ3(vgood, "buying")

# Create a figure and axis
fig, axs = plt.subplots()

# Add data to the axis as lines
axs.plot(x, y1, label='Line 1')
axs.plot(x, y2, label='Line 2')
axs.plot(x, y3, label='Line 3')
axs.plot(x,y4,label='Line 4')


# Add title and labels to the chart
axs.set_title('Three Line Chart')
axs.set_xlabel('X-axis')
axs.set_ylabel('Y-axis')

# Show the chart
plt.show()