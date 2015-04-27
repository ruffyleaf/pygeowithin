#!/usr/bin
# upload the data into mongoDB

import csv
import pymongo

#Establish Mongo connection

conn = pymongo.MongoClient('mongodb://localhost', safe=True)
db = conn.grid
points = db.points

#Read csv data
datafile = open('speedcam_map.csv', 'rb')
geodata = csv.reader(datafile)

#Check input file
#i = 0
#for i, row in enumerate(geodata):
#    print row[0:4]
#    i += 1
#    if i == 10:
#        break

#create the records for upload

#skip the header line
geodata.next()

for row in geodata:
    code = row[0]
    title = row[1]
    lat = float(row[2])
    lon = float(row[3])

    #set color based on code
    if row[0] == '1':
        description = "grid"
        markercolor = '#000000'
        markersymbol = 'circle'
    elif row[0] == '2':
        description = "accident"
        markercolor = '#ee2a2a'
        markersymbol = 'danger'
    elif row[0] == '3':
        description = 'lamp post'
        markercolor = '#ffe800'
        markersymbol = 'marker-stroked'
    elif row[0] == '4':
        description = 'traffic light'
        markercolor = '#009647'
        markersymbol = 'car'
    elif row[0] == '5':
        description = 'road hump'
        markercolor = '#808080'
        markersymbol = 'roadblock'
    else:
        description = 'N/A'
        markercolor = '#ffffff'
        markersymbol = 'theatre'
    
    record = {
            'code': code,
            'title': title,
            'loc' : {'type': 'Point', 'coordinates':[lon, lat]},
            'description': description,
            'marker-color': markercolor,
            'marker-symbol': markersymbol
    }

    points.insert(record)

