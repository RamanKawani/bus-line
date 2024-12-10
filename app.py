import streamlit as st
import pandas as pd

# Attempt to import folium
try:
    import folium
    from folium.plugins import MarkerCluster
    st.success("Folium has been imported successfully!")
except ImportError:
    st.error("Folium is not installed. Please make sure it's listed in the requirements.txt file.")

# Your app logic goes here
def display_bus_lines():
    # Load the bus line data (ensure your CSV has latitudes and longitudes)
    data = pd.read_csv("bus_lines.csv")  # Replace with your actual data path
    st.write(data)

    # Creating a folium map for bus lines (simplified example)
    map_center = [37.687, 44.000]  # Center of Erbil, adjust as needed
    bus_map = folium.Map(location=map_center, zoom_start=12)

    # Adding bus stops (example)
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],  # Assuming CSV has lat/long columns
            popup=row['stop_name']  # Assuming CSV has a stop name column
        ).add_to(bus_map)

    # Display the map in Streamlit
    folium_static(bus_map)

# Run your app
if __name__ == "__main__":
    display_bus_lines()

