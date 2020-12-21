import pandas, pygeohash as pgh, datetime, numpy as np

print('Start: ' + str(datetime.datetime.now()))


# TODO YOU"RE ALMOST THERE!!!!!!!

def get_headers(csvHeaders):
    geoHeaders = []
    possLat = ['lat', 'Start_Lat', 'Latitude', 'latitude']
    possLong = ['long', 'longitude', 'Longitude', 'Start_Lng']
    for item in csvHeaders:
        for headers in possLat:
            if headers in item:
                latHeader = item
        for headers in possLong:
            if headers in item:
                longHeader = item
    geoHeaders.append(longHeader)
    geoHeaders.append(latHeader)
    return (geoHeaders)


def add_geohash(csv, headers):
    x = 0
    csvArray = []
    latHeader = headers[0]
    longHeader = headers[1]
    while x < len(csv):
        csvLat = csv.loc[x, latHeader]
        csvLong = csv.loc[x, longHeader]
        csvHash = pgh.encode(csvLat, csvLong, precision=5)
        x += 1
        csvArray.append(csvHash)
    csv['Geohash'] = csvArray
    csv = csv.sort_values(by=['Geohash'])
    return csv


def geo_compare(csvsmall, csvlarge):
    x = 0
    count = 0
    while x < 10000:
        print(x)
        smallGeo = csvsmall.loc[x, 'Geohash']
        i = 0
        x = x + 1
        while i < len(csvlarge):
            largeGeo = csvlarge.loc[i, 'Geohash']
            i += 1
            if largeGeo > smallGeo:
                break
            elif largeGeo < smallGeo:
                continue
            elif largeGeo == smallGeo:
                count += 1
    return count


if __name__ == '__main__':
    csvsmall = input('Enter your smaller csv path')
    csvsmall = pandas.read_csv(csvsmall)
    smallheader = get_headers(csvsmall)
    csvsmall = add_geohash(csvsmall, smallheader)

    csvlarge = input('Enter your larger csv path')
    csvlarge = pandas.read_csv(csvlarge)
    largeheader = get_headers(csvlarge)
    csvlarge = add_geohash(csvlarge, largeheader)
    count = geo_compare(csvsmall, csvlarge)

    print("There were " + str(count) + " accidents near airports in June of 2020\n Accident IDs:\n")
    print("Stop :" + str(datetime.datetime.now()))
