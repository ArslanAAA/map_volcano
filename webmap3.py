import folium
import pandas as pd

map4=folium.Map(location=[40.897934,-73.885948],zoom_start=15,tiles = 'Stamen Terrain')
df=pd.read_csv('Volcanoes.txt')
for lat,lan,name in zip(df['LAT'],df['LON'],df['NAME']):
	folium.Marker(location=[lat,lan],popup = name, icon= folium.Icon(icon='cloud')).add_to(map4)
print(map4.save('test4.html'))
