#!/usr/bin
# getPoints.py takes in some arguments and 
#generates a set of points in GeoJson
# usage - python getPointsInGrid.py <infile> <outfile> 

import csv
import pymongo
from sys import argv
import json

#Establish Mongo connection

conn = pymongo.MongoClient('mongodb://localhost')
db = conn.grid
points = db.points

infile = argv[1]
outfile = argv[2]

f = open(infile, 'rb')
polygon = json.load(f)

#get the point and query from the database
results = points.find(
        {"loc":  
            {"$geoWithin":   
                {"$geometry":
                    {"type":polygon['features'][0]['geometry']['type'],
                        "coordinates":polygon['features'][0]['geometry']['coordinates']
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
