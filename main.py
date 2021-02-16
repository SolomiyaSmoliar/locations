import folium
import pandas
data = pandas.read_csv('C:/Users/Solomiya/Downloads/Stan_1900.csv', error_bad_lines=False)
print(data)
lat = data['lat']
lon = data['lon']
m = folium.Map([48.314775, 25.082925],
                zoom_start=10)
fg = folium.FeatureGroup(name='kosiv')

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln],
                                popup='1900',
                                icon = folium.Icon()))
m.add_child(fg)
m.save('C:/Users/Solomiya/Documents/Visual Studio/location/index.html')