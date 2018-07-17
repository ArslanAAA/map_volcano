import folium
map3=folium.Map(location=[40.897934,-73.885948],zoom_start=15,tiles='Stamen Terrain')

#add markers
folium.Marker(location=[40.897934,-73.885948],popup='I am here',icon=folium.Icon(icon = 'cloud')).add_to(map3)
folium.Marker(location=[40.8895439,-73.9015249],popup='and here too',icon=folium.Icon(color = 'green')).add_to(map3)
print(map3.save('test3.html'))
