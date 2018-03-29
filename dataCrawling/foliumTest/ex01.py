import folium

latitude = 37.5666512
longitude = 126.9696842

map_osm = folium.Map(location=[latitude, longitude])
map_osm.save('c:/test/map1.html')
print(type(map_osm))

map_osm = folium.Map(location=[latitude, longitude], zoom_start=10)
map_osm.save('c:/test/map2.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Terrain')
map_osm.save('c:/test/map3.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Toner')
map_osm.save('c:/test/map4.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=15)
folium.Marker(location=[latitude, longitude], popup='서울특별시청').add_to(map_osm)
map_osm.save('c:/test/map5.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=15)
folium.Marker(location=[latitude, longitude], popup='서울특별시청').add_to(map_osm)
folium.CircleMarker(location=[37.5662952,126.9757564], radius=40,color='#123423',
                    fill_color='#234FF0', fill=True, popup='덕수궁').add_to(map_osm)
map_osm.save('c:/test/map6.html')