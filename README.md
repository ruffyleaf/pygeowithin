# pygeowithin
Draw a polygon over an area, save the corners into a file in csv format
'#lat, #lon' named 'infile'

# create database
python uploadtoMongo.py

# create index on the coordinates
Open a mongo shell.

run db.points.createIndex({"loc":"2dsphere"})

# run
python getPointsInGrid.py 'infile' 'outfile'

# plot on map
Use http://geojson.io to plot the results saved in 'outfile'.


