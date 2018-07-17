import folium
import pandas as pd

map4=folium.Map(location=[40.897934,-73.885948],zoom_start=15,tiles = 'Stamen Terrain')
df=pd.read_csv('Volcanoes.txt')
for lat,lan,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	folium.Marker(location=[lat,lan],popup = name, icon= folium.Icon(color='green' if elev in range(1001,1999) else 'orange' if elev in range(2000,2999) else 'red',icon = 'cloud')).add_to(map4)
print(map4.save('test5.html'))
