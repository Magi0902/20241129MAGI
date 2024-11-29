import streamlit as st
import leafmap.foliumap as leafmap
import leafmap
import pandas as pd
import os
import os
import pandas as pd
import csv 

from google.colab import drive
drive.mount('/content/drive')

data_pkg_path = '/content/drive/MyDrive/data'
filename = 'Camino Francés.csv'
path = os.path.join(data_pkg_path, filename)
df = pd.read_csv(path)
df.head()

from geopy.distance import geodesic

distances = []
for i in range(len(df)):
  for j in range(i+1, len(df)):
    city1_coords = (df.loc[i, 'Latitude'], df.loc[i, 'Longitude'])
    city2_coords = (df.loc[j, 'Latitude'], df.loc[j, 'Longitude'])
    city1_name = df.loc[i, 'Town']
    city2_name = df.loc[j, 'Town']
    distance = geodesic(city1_coords, city2_coords).kilometers
    distances.append([city1_name, city2_name, distance])

output_file = 'Camino_distances.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Town1', 'Town2', 'Distance (km)'])
    writer.writerows(distances)
    print(f"城市之間的距離保存到 {output_file}")

m = leafmap.Map(center=(41, -3), zoom=6, height="600px")
add_basemap = "OpenTopoMap"
m.add_basemap(basemap=add_basemap)

##連結雲端，匯入法國之路.shp
from google.colab import drive
drive.mount('/content/drive')
data_pkg_path = '/content/drive/MyDrive/data/route' # Make sure this path is correct
filename = 'C_France.shp'
path = os.path.join(data_pkg_path, filename)

# 列印出路徑
print(path)

# 檢查一下匯入資料的路徑，才不會輸入錯誤不自知
if not os.path.exists(path):
  raise FileNotFoundError(f"Shapefile not found at: {path}")
m.add_shp(path, layer_name="C_France")
m

#連結雲端，匯入法國之路的geojson
data_pkg2_path = '/content/drive/MyDrive/data' # Make sure this path is correct
filename2 = 'Camino_France_route.geojson'
path2 = os.path.join(data_pkg2_path, filename2)
m.add_geojson(path2, layer_name="Camino Francés")
m

import geopandas as gpd

# Assuming 'df' is your Pandas DataFrame with 'Latitude' and 'Longitude' columns
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
)

# Specify the output GeoJSON file path
geojson_path = '/content/drive/MyDrive/data/Camino_Frances.geojson'  # or any desired path

# Save the GeoDataFrame to GeoJSON
gdf.to_file(geojson_path, driver='GeoJSON')

print(f"GeoJSON file saved to: {geojson_path}")
df.head()

#將前置處理好的csv做成Clusters的方式於圖台呈現
data = "/content/drive/MyDrive/data/Camino Francés.csv"
##設定圖台內容
m = leafmap.Map(basemap="OpenTopoMap", center=(41, -3), zoom=6)
m.add_points_from_xy(data, x="Latitude", y="Longitude")


route_path = "/content/drive/MyDrive/data/Camino_France_route.geojson"
###加上路徑的geojson
m.add_geojson(route_path, layer_name="Camino France Route")
####秀出圖台
m

#製作距離查詢工具區
import leafmap
import pandas as pd
import geopandas as gpd
import ipywidgets as widgets
from IPython.display import display

# 匯入前置作業計算好的小鎮距離csv
distance_path = "/content/Camino_distances.csv"

df = pd.read_csv(distance_path)

# 建立搜尋box
town1_dropdown = widgets.Dropdown(
    options=df['Town1'].unique(),
    description='Select Town 1:',
)

town2_dropdown = widgets.Dropdown(
    options=df['Town2'].unique(),
    description='Select Town 2:',
)

# 創建出按鈕計算距離
calculate_button = widgets.Button(description="Calculate Distance")

#創建出顯示的value
result_label = widgets.Label(value="")

# 計算距離
def calculate_distance(b):
    town1 = town1_dropdown.value
    town2 = town2_dropdown.value

    # Find the distance
    distance = df[(df['Town1'] == town1) & (df['Town2'] == town2)]['Distance (km)']

    if not distance.empty:
        result_label.value = f"The distance from {town1} to {town2} is {distance.values[0]:.2f} km."
    else:
        result_label.value = f"No distance data available for {town1} to {town2}."

# 按鍵連結到距離計算呈現
calculate_button.on_click(calculate_distance)

# 展現出工具
display(town1_dropdown, town2_dropdown, calculate_button, result_label)
