import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Streamlit app title and introduction
st.title("Bike Sharing Dataset Visualization")

st.write("This app allows you to visualize the Bike Sharing dataset.")

# Sidebar for dataset selection
dataset_selection = st.sidebar.selectbox("Select Dataset", ("day.csv", "hour.csv"))

# Display the selected dataset
if dataset_selection == "day.csv":
    st.header("Day Dataset")
    st.write(day_df)
else:
    st.header("Hour Dataset")
    st.write(hour_df)

# Data visualization options
st.sidebar.markdown("## Data Visualization Options")

# Visualization type selection
visualization_type = st.sidebar.selectbox(
    "Select Visualization Type",
    ("Line Chart", "Bar Chart", "Histogram"),
)

# Visualize the selected dataset
if dataset_selection == "day.csv":
    st.subheader("Visualizations for Day Dataset")

    if visualization_type == "Line Chart":
        st.line_chart(day_df)
    elif visualization_type == "Bar Chart":
        st.bar_chart(day_df)
    elif visualization_type == "Histogram":
        column = st.selectbox("Select Column for Histogram", day_df.columns)
        st.bar_chart(day_df[column].value_counts())

else:
    st.subheader("Visualizations for Hour Dataset")

    if visualization_type == "Line Chart":
        st.line_chart(hour_df)
    elif visualization_type == "Bar Chart":
        st.bar_chart(hour_df)
    elif visualization_type == "Histogram":
        column = st.selectbox("Select Column for Histogram", hour_df.columns)
        st.bar_chart(hour_df[column].value_counts())
