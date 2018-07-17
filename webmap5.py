import folium
import pandas as pd

map5=folium.Map(location=[40.897934,-73.885948],zoom_start=7,tiles = 'Stamen Terrain')
df=pd.read_csv('Volcanoes.txt')
def color(elev):
	if elev in range(0,1000):
		col = 'green'
	elif elev in range(1001,1999):
		col = 'blue'	
	elif elev in range(2000,2999):
		col = 'orange'
	else:
		col='red'
	return col
for lat,lan,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	folium.Marker(location=[lat,lan],popup = name, icon= folium.Icon(color=color(elev),icon = 'cloud')).add_to(map5)
print(map5.save('test6.html'))