import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# html = """<h4>Volcano information:</h4> Height: %s m"""
html = """Volcano name:<br><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br><br>Elevation: %s m"""
 
def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    if 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location = [33.29, -111.85], zoom_start = 6, tiles = "Stamen Terrain")

# using feature group to keep the code organized.
fgv = folium.FeatureGroup(name = "Volcanoes map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (name, name, el), width = 200, height = 100)
    fgv.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))

fgp = folium.FeatureGroup(name = "Populations map")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("housingMap.html")

