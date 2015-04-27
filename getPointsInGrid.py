#!/usr/bin
# getPoints.py takes in some arguments and 
#generates a set of points in GeoJson
# usage - python getPointsInGrid.py <infile> <outfile> 

import csv
import pymongo
from sys import argv
import json

#Establish Mongo connection

conn = pymongo.MongoClient('mongodb://localhost', safe=True)
db = conn.grid
points = db.points

#specify input and output files
infile = argv[1]
outfile = argv[2]

f = open(infile, 'rb')
coords = csv.reader(f)

coordinates = []
for c in coords:
    x = [float(c[1]), float(c[0])]
    coordinates.append(x)

#add the origin to the end to close the polygon
coordinates.append(coordinates[0])
print "Check the coordinates [lon,lat] : ", coordinates

#get the point and query from the database
results = points.find(
        {"loc":  
            {"$geoWithin":   
                {"$geometry":
                    {"type":"Polygon",
                        "coordinates":[coordinates]
                    }
                }
            }    
        }
        )


#convert to geoJson
gj = {}
gj["type"] = "FeatureCollection"
gj["features"] = []

for r in results:
    gj["features"].append(
        {"type": "Feature",
         "geometry": r['loc'],
            "properties":{
                "title": r['title'],
                "description": r['description'],
                "marker-color": r['marker-color'],
                "marker-symbol": r['marker-symbol']
            } 
        }
    )

points = json.dumps(gj, sort_keys=True, indent=4, separators=(',', ': '))
f = open(outfile, "wb")
f.write(points)
f.close
