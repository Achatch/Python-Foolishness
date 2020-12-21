id_array = []
count = 0
import pandas
import datetime

# Set pandas df2 to the entirety of the contents of the airports.csv & car data csv files
airports = pandas.read_csv("airports.csv")
accidents = pandas.read_csv("500k_US_Accidents.csv")
results = pandas.read_csv("results.csv")
# TODO: Add sort to lat/long and once lat/long is 1 over, break loop back
# TODO: Add time comprehension, need more accident reports?
# TODO: Geohashing.
def dictbuilder(dataframe):
    for accident in accidents.loc["ID"]
        print(accident)
x = 0
while x < 10:
    print(x, count)
    print(datetime.datetime.now())
    i = 0
    airportsLat = airports.loc[x, 'latitude_deg']
    airportsLong = airports.loc[x, 'longitude_deg']
    airportLatHigh = int(airportsLat + 1)
    airportLatLow = int(airportsLat - 1)
    airportLongHigh = int(airportsLong + 1)
    airportLongLow = int(airportsLong - 1)
    x = x + 1
    while i < len(accidents):
        accidentID = accidents.loc[i, "ID"]
        accidentLat = accidents.loc[i, 'Start_Lat']
        accidentLong = accidents.loc[i, 'Start_Lng']
        i = i + 1
        if accidentID in id_array:
            continue
        if int(accidentLat) not in range(airportLatLow, airportLatHigh):
            continue
        if int(accidentLong) not in range(airportLongLow, airportLongHigh):
            continue
        if (accidentLat + .15) > airportsLat > (accidentLat - .15):
            if (accidentLong + .15) > airportsLong > (accidentLong - .15):
                id_array.append(accidentID)
                count = count + 1
                results.loc[count] = accidents.loc[i - 1]

print("There were " + str(count) + " accidents near airports in June of 2020\n Accident IDs:\n")
print(id_array)
results.to_csv("results.csv")
