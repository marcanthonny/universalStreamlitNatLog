import streamlit as st
import pandas as pd
from utils.helpers import load_data

# Set the title of the app
st.title("My Streamlit App")

# Load sample data
data = load_data("data/sample_data.csv")

# Display the data in the app
st.write("Here is the sample data:")
st.dataframe(data)

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Page 2"])

if page == "Home":
    st.write("Welcome to the home page!")
elif page == "Page 2":
    st.write("You can navigate to Page 2 from the sidebar.")