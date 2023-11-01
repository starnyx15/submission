import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the "day.csv" and "hour.csv" datasets
data_day = pd.read_csv("Bike-sharing-dataset/day.csv")
data_hour = pd.read_csv("Bike-sharing-dataset/hour.csv")

# Create a Streamlit app
st.title("Bike Rentals Data Visualization")

# Sidebar to select dataset
selected_dataset = st.sidebar.radio("Select Dataset", ("day.csv", "hour.csv"))

if selected_dataset == "day.csv":
    st.header("Day.csv Data Visualization")
    data = data_day
else:
    st.header("Hour.csv Data Visualization")
    data = data_hour

# Visualizations
# Insight 1: Daily Bike Rentals Over Time
st.subheader("Insight 1: Daily Bike Rentals Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x="dteday", y="cnt", data=data, hue="hr" if selected_dataset == "hour.csv" else None)
plt.title("Hourly Bike Rentals Over Time" if selected_dataset == "hour.csv" else "Daily Bike Rentals Over Time")
plt.xlabel("Date")
plt.ylabel("Total Rentals")
plt.xticks(rotation=45)
st.pyplot()

# Insight 2: Impact of Weather on Bike Rentals
st.subheader("Insight 2: Impact of Weather on Bike Rentals")
plt.figure(figsize=(8, 6))
sns.boxplot(x="weathersit", y="cnt", data=data)
plt.title("Impact of Weather on Bike Rentals")
plt.xlabel("Weather Situation")
plt.ylabel("Total Rentals")
st.pyplot()

# Insight 3: Bike Rentals by Season
st.subheader("Insight 3: Bike Rentals by Season")
plt.figure(figsize=(8, 6))
sns.boxplot(x="season", y="cnt", data=data)
plt.title("Bike Rentals by Season")
plt.xlabel("Season")
plt.ylabel("Total Rentals")
st.pyplot()

# Insight 4: Correlation Matrix Heatmap
# Filter only numeric columns
numeric_columns = data.select_dtypes(include=[float, int])

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

# Visualize the correlation matrix
st.subheader("Insight 4: Correlation Matrix Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
st.pyplot()

