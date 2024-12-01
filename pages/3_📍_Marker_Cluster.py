import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
***顯示不出來，但資料正確
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

        m = leafmap.Map(center=[22.43, 120.54], zoom=14)
        cities = 'https://chinchillaz.github.io/streamlit-hw/4towns_solarpanels.geojson'
        regions = 'https://github.com/Magi0902/Solarpanels.csv/blob/main/4towns_solarpanels.geojson'
#https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv
#https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson
        m.add_geojson(regions, layer_name='PT towns')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=["year", "town", "location", "l_number", "x", "y", "company"],
            spin=True,
            add_legend=True,
        )
        
m.to_streamlit(height=700)
