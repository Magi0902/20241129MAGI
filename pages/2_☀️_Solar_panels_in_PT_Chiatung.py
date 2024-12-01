import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Solar Panels in Pingtung Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=(22.439, 120.538), zoom=14, height="600px") 
        m.split_map(
            left_layer="HYBRID", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
#WORLDCOVER_2020_S2_FCC
#ESA WorldCover 2020
#https://chinchillaz.github.io/streamlit-hw/4towns_solarpanels.geojson
m.to_streamlit(height=700)


