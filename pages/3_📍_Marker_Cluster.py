import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = 'https://github.com/Magi0902/Solarpanels.csv/blob/main/%E4%BD%B3%E5%86%AC%E5%85%89%E9%9B%BB%E6%9D%BF.csv'
        regions = 'https://github.com/Magi0902/Solarpanels.csv/blob/main/PT_towns.geojson'
#https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv
#https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson
        m.add_geojson(regions, layer_name='US Regions')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )
        
m.to_streamlit(height=700)
