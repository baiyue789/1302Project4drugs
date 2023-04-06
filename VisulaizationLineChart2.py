import matplotlib.pyplot as plt
import pandas as pd
lol = input(str("Conditions, Buying, Maint"))

def whichcsvfileread(df):
    df = str(df)
    if df == "Conditions":
        x = ["Conditions/Unacc.csv","Conditions/acc.csv","Conditions/good.csv","Conditions/vgood.csv"]
        return x
    if df == "Buying":
        x = ["Buying/vhigh.csv","Buying/high.csv","Buying/med.csv","Buying/low.csv"]
        return x
    if df == "Maint":
        x = ["Maint/vhigh.csv","Maint/high.csv","Maint/med.csv","Maint/low.csv"]
        return x


whatever = whichcsvfileread("Maint") #planning to replace the "maint" with lol
Unacc = pd.read_csv(whatever[0], index_col=False)
acc = pd.read_csv(whatever[1], index_col=False)
good = pd.read_csv(whatever[2], index_col=False)
vgood = pd.read_csv(whatever[3], index_col=False)


def the_X_based_on_database_compare(db):
    if db == "Conditions":
        x = ['unacc', 'acc', 'good', 'vgood']
        return x
    if db == "Buying" or "Maint":
        x = ["vhigh", "high","med", "low"]
        return x 
    
def Q1MeanQ3(df, sheet_name):
    sheet_name = str(sheet_name)
    data = df[sheet_name]
    # Calculate the mean
    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    x = [mean - std_dev,mean,mean,std_dev+mean] #["Q1","Mean","Mean","Q3"]
    return x
#going to use lol2 to replace the "buying" below
x = the_X_based_on_database_compare("maint")
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