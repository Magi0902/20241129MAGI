
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

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://chinchillaz.github.io/streamlit-hw/solar_panels_edit.csv"
        m = leafmap.Map(center=[22, 120], zoom=14)
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="id",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
