from pathlib import Path
import json
import plotly.express as px
import pandas as pd

path = Path('eq_data/eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')

all_eq_data = json.loads(contents)

path = Path('eq_data/readable_eq_data_1_day_m1.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, titles, lons, lats = [], [], [], []
for i in all_eq_dicts:
    mag = i["properties"]["mag"]
    title = i["properties"]["title"]
    lon = i["geometry"]["coordinates"][0]
    lat = i["geometry"]["coordinates"][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(titles[:2])
print(mags[:10])
print(lons[:5])
print(lats[:5])
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
print(data.head(10))

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    color_continuous_scale=px.colors.sequential.Viridis,
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()
