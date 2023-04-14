import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv("heatMap.csv")

# Create a scatter plot with the latitude and longitude as the x and y coordinates,
# and the safety grade as the color of the points
plt.scatter(df["longitude"], df["latitude"], c=df["safety grade"], cmap="viridis")

# Set the axis labels and the title of the plot
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Safety Grade Heat Map")

# Show the plot
plt.show()