import folium
import os
import json


m = folium.Map(location=[45.943161, 24.96676], zoom_start=7)

tooltip = 'Click For More Info'

f = open('locatii.json')

data = json.load(f)
i=1
for loc in data['data']:
    
    folium.Marker([loc['coord1'],loc['coord2']],
                    popup=f"Locatie {i}",
                    tooltip=loc['nume']).add_to(m),
    i=i+1

f.close()

m.save('map.html')