import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Car_converted.csv", index_col=False)
plt.scatter(df['buying'],df['maint'] )

# Add labels and a title
plt.xlabel('Buying Price')
plt.ylabel('Maintience Price')
plt.title('Scatter Plot')

# Show the plot

plt.show()