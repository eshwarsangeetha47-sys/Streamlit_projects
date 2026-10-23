
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Visualization",
    layout="wide"
)

st.title("Data Visualization")

# Sample data
np.random.seed(42)

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Math", "Science", "English"]
)

st.subheader("Sample Data")
st.dataframe(df)

# Built-in charts
st.subheader("Built-in Charts")

st.write("Line Chart")
st.line_chart(df)

st.write("Bar Chart")
st.bar_chart(df)

st.write("Area Chart")
st.area_chart(df)

# Matplotlib chart
st.subheader("Matplotlib Chart")

fig, ax = plt.subplots()

ax.hist(df["Math"], bins=10, color="skyblue")
ax.set_title("Math Score Distribution")
ax.set_xlabel("Math Scores")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# Exercise: Scatter plot
st.subheader("Scatter Plot")
st.scatter_chart(df, x="Math", y="Science")

# Exercise: Mean metric
st.subheader("Average Math Score")
st.metric("Mean Math Value", f"{df['Math'].mean():.2f}")
