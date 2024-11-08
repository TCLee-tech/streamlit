# streamlit run uber_pickups.py

import streamlit as st
import pandas as pd
import numpy as np

# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(page_title="Streamlit App", page_icon=":snowflake:") # in brower tab

st.title("Uber pickups in NYC")

# https://docs.streamlit.io/develop/api-reference/layout/st.sidebar
# https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox
st.sidebar.selectbox("This is a Selectbox in a Sidebar", ("New York", "London", "Hong Kong"))

# https://docs.streamlit.io/develop/api-reference/status/st.success
st.sidebar.success("Success text in sidebar", icon="✅")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the readr know the data is loading
data_load_state = st.text("data loading ...")
# Load 10,000 rows of data into the dataframe
data = load_data(10000)
# Notify the reader that the data was successfully loaded
data_load_state.text("Done! (using st.cache_data)")

# Show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Draw histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# Plot data on a map
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)