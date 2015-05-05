# pygeowithin
Draw a polygon over an area, save the corners into a file in csv format
'#lat, #lon' named 'infile'

Updated the file with getPointsInPolygon.py which takes in a Feature Collection with a Polygon for a selected area and the output file. This is faster than saving the lat/lon corners into an input file.

# create database
python uploadtoMongo.py

# create index on the coordinates
Open a mongo shell.

run db.points.createIndex({"loc":"2dsphere"})

# run
For lat/lon coordinates:
python getPointsInGrid.py 'infile' 'outfile'

For GeoJson Polygon:
python getPointsInPolygon.py 'infile.geojson' 'outfile.geojson'

# plot on map
Use http://geojson.io to plot the results saved in 'outfile'.

#TODO



