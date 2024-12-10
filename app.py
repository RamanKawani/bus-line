import subprocess
import sys

# Function to install a package if it's not already installed
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if folium is installed, if not, install it
try:
    import folium
except ImportError:
    print("folium not found, installing...")
    install_package("folium")
    import folium

# Import required libraries after installing
import streamlit as st
import pandas as pd
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Load bus line data (ensure your CSV has latitudes and longitudes)
data = pd.read_csv('bus_lines.csv')

# Function to create the map with bus stops
def create_map(bus_line):
    # Filter the data for the selected bus line
    bus_data = data[data['Bus Line'] == bus_line]

    # Initialize a Folium map centered on Erbil (you can adjust the coordinates if necessary)
    m = folium.Map(location=[36.1910, 43.9983], zoom_start=12)

    # Create a marker cluster to group the stops together on the map
    marker_cluster = MarkerCluster().add_to(m)

    # Add bus stops as markers
    for index, row in bus_data.iterrows():
        folium.Marker(
            location=[row['Stop 1 Lat'], row['Stop 1 Long']],
            popup=f"Stop 1: {row['Stops']}",
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)
        folium.Marker(
            location=[row['Stop 2 Lat'], row['Stop 2 Long']],
            popup=f"Stop 2: {row['Stops']}",
            icon=folium.Icon(color='green')
        ).add_to(marker_cluster)

    return m

# Title of the app
st.title("Erbil Bus Lines with Map")

# Dropdown for selecting bus line
bus_line = st.selectbox("Select a bus line", data['Bus Line'].unique())

# Display selected bus line information
st.write(f"### Details for {bus_line}")
st.write(data[data['Bus Line'] == bus_line])

# Show the map for the selected bus line
st.write("### Bus Stops on Map")
bus_map = create_map(bus_line)

# Display the map in the app
folium_static(bus_map)
