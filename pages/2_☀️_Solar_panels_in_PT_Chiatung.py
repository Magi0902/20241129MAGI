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

m.to_streamlit(height=700)

import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace this with your actual df)
data = {
    'Year': [100, 107, 108, 109, 110, 111, 112, 100, 106, 108, 109, 110, 111, 109, 110, 111, 109, 110, 112, 109, 111, 112, 108, 112, 107, 109, 110, 111, 112, 107, 109, 110],
    'Town': ['林邊鄉', '林邊鄉', '林邊鄉', '林邊鄉', '林邊鄉', '林邊鄉', '林邊鄉', '佳冬鄉', '佳冬鄉', '佳冬鄉', '佳冬鄉', '佳冬鄉', '佳冬鄉', '車城鄉', '車城鄉', '車城鄉', '獅子鄉', '獅子鄉', '獅子鄉', '枋山鄉', '枋山鄉', '枋山鄉', '牡丹鄉', '牡丹鄉', '恆春鎮', '恆春鎮', '恆春鎮', '恆春鎮', '恆春鎮','東港鎮', '東港鎮', '東港鎮'],
    'Area': [156453.68, 18733, 67137.46, 119872.68, 336490.39, 122791.45, 41549.61, 143619.8, 6053.69, 583.84, 841439.33, 114509.9, 82910.6, 70875.71, 88487.58, 12396.14, 1582.52, 24336.35, 5951.08, 16295.76, 12684.43, 3170.56, 1687.69, 16618.48, 4161.69, 3131.49, 47053.37, 36137.05, 29409.58,20160.91 ,48536.06 , 38827.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Pivot the data to prepare for stacked bar plot
df_pivot = df.pivot_table(index='Town', columns='Year', values='Area', fill_value=0)

# Plotting the stacked bar chart
ax = df_pivot.plot(kind='bar', stacked=True, figsize=(10, 7), colormap='Paired')

# Adding labels and title
ax.set_xlabel("Town")
ax.set_ylabel("Area")
ax.set_title("各鄉鎮光電板設置面積堆疊圖")

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
