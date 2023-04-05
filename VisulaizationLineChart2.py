import matplotlib.pyplot as plt
import pandas as pd
Unacc = pd.read_csv("Conditions/Unacc.csv", index_col=False)
acc = pd.read_csv("Conditions/acc.csv", index_col=False)
good = pd.read_csv("Conditions/good.csv", index_col=False)
vgood = pd.read_csv("Conditions/vgood.csv", index_col=False)
def Q1MeanQ3(df, sheet_name):
    sheet_name = str(sheet_name)
    data = df[sheet_name]
    # Calculate the mean
    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    x = [mean - std_dev,mean,mean,std_dev+mean] #["Q1","Mean","Mean","Q3"]
    return x

x = ['unacc', 'acc', 'good', 'vgood'] 
x1 = Q1MeanQ3(Unacc, "buying") #["Q1","Mean","Q3"] format of what is returned
x2 = Q1MeanQ3(acc, "buying")
x3 = Q1MeanQ3(good, "buying")
x4 = Q1MeanQ3(vgood, "buying")
y1 = [x1[0],x2[0],x3[0],x4[0]]
y2 = [x1[1],x2[1],x3[1],x4[1]]
y3 = [x1[2],x2[2],x3[2],x4[2]]
y4 = [x1[3],x2[3],x3[3],x4[3]]

# Create a figure and axis
fig, axs = plt.subplots()

# Add data to the axis as lines
axs.plot(x, y1, label='Q1')
axs.plot(x, y2, label='Mean')
axs.plot(x, y4, label='Q3')

# Add title and labels to the chart
axs.set_title('Buying prices')
axs.set_xlabel('Values')
axs.set_ylabel('Price')

axs.legend()

# Show the chart
plt.show()