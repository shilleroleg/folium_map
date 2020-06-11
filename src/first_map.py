import folium
from folium.plugins import MarkerCluster

# Create base map
mp = folium.Map(location=[54.9893, 82.9070],
                zoom_start=11,
                tiles='OpenStreetMap')
# Other tiles: Stamen Terrain, Stamen Toner, Mapbox Bright, Mapbox Control Room and other

# Create Cluster
marker_cluster = MarkerCluster().add_to(mp)

# Plot markers and add to marker_cluster
folium.Marker(location=[55.0017, 83.0076],
              popup='<i>Green Woodland</i>',
              tooltip='Click me!',
              icon=folium.Icon(icon='cloud')).add_to(marker_cluster)
folium.Marker(location=[55.0095, 82.6673],
              popup='<b>Tolmachevo Airport</b>').add_to(marker_cluster)

# Enable lat/lon popovers
mp.add_child(folium.LatLngPopup())

# Save the map
mp.save("map1.html")
