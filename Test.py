# This allows the user to set a particular coordinate and determine how many airports are within a particular range
# Of that coordinate
import geopy.distance
import pandas

from tqdm import tqdm


id_array = []
count = 0

# Set pandas df2 to the entirety of the contents of the airports.csv & car data csv files
df1=pandas.read_csv("airports.csv")
df2=pandas.read_csv("500k_US_Accidents.csv")
df3=pandas.read_csv("results.csv")

print("Please enter your radius in Nm.")
distance = int(input())
x = 0
while x < len(df1):
    print(count, x)
    coords_2 = df1.loc[x, 'latitude_deg'], df1.loc[x, 'longitude_deg']  # Retrieve lat & long from particular cells
    x = x + 1
    i = 0
    while i < len(df2): # Iterate through the entire file
        coords_1 = df2.loc[i, 'Start_Lat'], df2.loc[i, 'Start_Lng'] # Retrieve lat & long from particular cells
        difference = geopy.distance.distance(coords_1, coords_2).nm # Calculate distance between two points
        if difference < distance:
            count = count + 1
            df3.loc[count] = df2.loc[i]
        i = i + 1

print("There were "+str(count)+" accidents near airports in June of 2020\n Accident IDs:\n")
df3.to_csv("results.csv")