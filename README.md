# pygeowithin

Draw a polygon over a map and get back every point that falls inside it. A small Python + MongoDB geospatial toolkit: load your points once into a `2dsphere`-indexed collection, then query them by an area and export the matches as GeoJSON to plot on [geojson.io](https://geojson.io).

## 📖 Full guide

**Everything is documented on the companion site:**
👉 **https://ruffyleaf.github.io/pygeowithin/**

It covers the data model, loading points, both query scripts (by lat/lon corners or by GeoJSON polygon), the output format, a worked example, and the gotchas (Python 2, `lon,lat` ordering, index-first, closed polygon ring).

## Quick start

```bash
# Requires: a local MongoDB at mongodb://localhost, `pip install pymongo`, Python 2

# 1. Create the database/collection and geospatial index (mongo shell)
#    use grid
#    db.points.createIndex({"loc":"2dsphere"})

# 2. Load points from the CSV (speedcam_map.csv is hardcoded in the script)
python uploadtoMongo.py

# 3. Find points inside an area — two options:

#    a) from a list of "lat, lon" corners (e.g. coord.in)
python getPointsInGrid.py coord.in outfile.geojson

#    b) from a GeoJSON polygon (drawn on geojson.io) — faster to set up
python getPointsInPolygon.py area.geojson outfile.geojson

# 4. Plot the result
#    open https://geojson.io → Open file → outfile.geojson
```

## Files

| File | Role |
| --- | --- |
| `uploadtoMongo.py` | Load CSV points into `grid.points` as GeoJSON documents |
| `getPointsInGrid.py` | Query points inside a polygon built from a `lat, lon` corner CSV |
| `getPointsInPolygon.py` | Query points inside a polygon supplied as a GeoJSON file (faster setup) |
| `coord.in` | Example corner list (a rectangle over Singapore) |
| `grid.geojson` | Example `FeatureCollection` output of points |
| `docs/index.html` | Source for the [documentation site](https://ruffyleaf.github.io/pygeowithin/) |
| `.github/workflows/deploy-pages.yml` | GitHub Actions workflow that publishes `docs/` to GitHub Pages on every push to `master` |

## Notes

- Coordinate order is `[longitude, latitude]` in storage and GeoJSON (input CSV is `lat, lon`).
- The `2dsphere` index on `loc` must exist before running a query.
- Scripts use Python 2 syntax; see the guide's *Gotchas* for the small port to Python 3.
