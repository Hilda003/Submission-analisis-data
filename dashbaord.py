import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


day_df = pd.read_csv("./data/day.csv")
hour_df = pd.read_csv("./data/hour.csv")

st.title("Bike Sharing Data Dashboard")


st.sidebar.header("Filters")
view_option = st.sidebar.selectbox("Choose View", ["Weekday vs. Weekend Rentals", "Hourly Rentals", "Correlation Heatmap"])

if view_option == "Weekday vs. Weekend Rentals":
    st.header("Bike Rentals on Weekdays vs. Weekends")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='workingday', y='cnt', data=day_df, ax=ax)
    ax.set_xticklabels(['Weekend', 'Weekday'])
    ax.set_xlabel("Day Type")
    ax.set_ylabel("Total Rentals")
    st.pyplot(fig)

elif view_option == "Hourly Rentals":
    st.header("Bike Rentals by Hour of the Day")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='hr', y='cnt', data=hour_df, estimator='mean', ci=None, ax=ax)
    ax.set_xlabel("Hour of the Day")
    ax.set_ylabel("Average Bike Rentals")
    ax.set_title("Bike Rentals by Hour")
    st.pyplot(fig)

elif view_option == "Correlation Heatmap":
    st.header("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    numeric_cols = day_df.select_dtypes(include=['number'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    st.pyplot(fig)


st.sidebar.text("Select an option to visualize data")
