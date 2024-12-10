import streamlit as st
import pandas as pd

# Load bus line data (adjust the path to your CSV file)
data = pd.read_csv('bus_lines.csv')

# Function to display bus line information
def display_bus_info(bus_line):
    bus_data = data[data['Bus Line'] == bus_line]
    st.write("### Bus Line Information")
    st.write(f"**Bus Line**: {bus_data['Bus Line'].values[0]}")
    st.write(f"**Start**: {bus_data['Start'].values[0]}")
    st.write(f"**End**: {bus_data['End'].values[0]}")
    st.write(f"**Stops**: {bus_data['Stops'].values[0]}")
    st.write(f"**Timetable**: {bus_data['Timetable'].values[0]}")

# Title of the app
st.title("Erbil Bus Lines")

# Dropdown for selecting bus line
bus_line = st.selectbox("Select a bus line", data['Bus Line'].unique())

# Display selected bus line information
display_bus_info(bus_line)

# Optional: Allow users to search for bus stops or other functionality
search_stop = st.text_input("Search for a bus stop")
if search_stop:
    filtered_data = data[data['Stops'].str.contains(search_stop, case=False)]
    st.write(f"### Bus Lines that pass through {search_stop}")
    st.dataframe(filtered_data[['Bus Line', 'Start', 'End', 'Timetable']])
