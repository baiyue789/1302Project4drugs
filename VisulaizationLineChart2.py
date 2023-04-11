import matplotlib.pyplot as plt
import pandas as pd

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
    if df == "Doors":
        x = ["doors/2.csv","doors/3.csv","doors/4.csv","doors/5.csv"]
        return x


whatever = whichcsvfileread("Conditions") #planning to replace the "maint" with lol
one = pd.read_csv(whatever[0], index_col=False)
two = pd.read_csv(whatever[1], index_col=False)
three = pd.read_csv(whatever[2], index_col=False)
four = pd.read_csv(whatever[3], index_col=False)

    
def Q1MeanQ3(df, sheet_name):
    sheet_name = str(sheet_name)
    data = df[sheet_name]
    # Calculate the mean
    mean = data.mean()
    std_dev = data.std()
    x = [mean - std_dev,mean,mean,std_dev+mean] #["Q1","Mean","Mean","Q3"]
    return x
#going to use lol2 to replace the "buying" below
def the_X_based_on_database_compare(db):
    if db == "Conditions":
        x = ['unacc', 'acc', 'good', 'vgood']
        return x
    if db == "Buying":
        x = ["vhigh", "high","med", "low"]
        return x
    if db == "Maint":
        x = ["high","med", "low"]
        return x
    if db == "P":
        x = ['2','4', "more"]
        return x
    if db == 'Doors':
        x = ['2', '3', '4', '5more']
        return x
    if db =='L':
        x = ['small', 'med', 'big']
        return x
    if db =='S':
        x = ['low', 'med', 'high']
        return x
x = the_X_based_on_database_compare("Conditions")

x1 = Q1MeanQ3(one, "lug_boot") #["Q1","Mean","Q3"] format of what is returned
x2 = Q1MeanQ3(two, "lug_boot")
x3 = Q1MeanQ3(three, "lug_boot")
x4 = Q1MeanQ3(four, "lug_boot")
y1 = [x1[0],x2[0],x3[0],x4[0]]
y2 = [x1[1],x2[1],x3[1],x4[1]]
y3 = [x1[2],x2[2],x3[2],x4[2]]
y4 = [x1[3],x2[3],x3[3],x4[3]]

# Create a figure and axis
fig, axs = plt.subplots()

# Add data to the axis as lines
axs.plot(x, y2, label='Mean')

# Add title and labels to the chart
axs.set_title('Conditions to lug_boot')
axs.set_xlabel('Condition')
axs.set_ylabel('Lug_boot')

axs.legend()

# Show the chart
plt.show()