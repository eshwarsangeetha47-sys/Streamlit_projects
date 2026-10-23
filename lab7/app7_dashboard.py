
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("Interactive Sales Dashboard")

# Generate sample sales data
np.random.seed(42)

df = pd.DataFrame({
    "Year": np.random.choice([2022, 2023, 2024], 200),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], 200
    ),
    "Product": np.random.choice(["A", "B", "C"], 200),
    "Sales": np.random.randint(1000, 10000, 200)
})

# Add dates for the date range filter
df["Date"] = pd.date_range(
    "2022-01-01", periods=200, freq="D"
)

# Sidebar filters
st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

region = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

product = st.sidebar.multiselect(
    "Product",
    sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

date_range = st.sidebar.date_input(
    "Date range",
    value=(df["Date"].min().date(),
           df["Date"].max().date())
)

# Filter the data
filtered = df[
    df["Year"].isin(year)
    & df["Region"].isin(region)
    & df["Product"].isin(product)
]

if len(date_range) == 2:
    filtered = filtered[
        (filtered["Date"].dt.date >= date_range[0])
        & (filtered["Date"].dt.date <= date_range[1])
    ]

# Key Performance Indicators
st.subheader("Key Performance Indicators")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Sales",
    f"{filtered['Sales'].sum():,}"
)

average = filtered["Sales"].mean()
c2.metric(
    "Average Sales",
    f"{average:,.0f}" if pd.notna(average) else "0"
)

c3.metric("Records", len(filtered))

if not filtered.empty:
    # Bar chart: sales by region
    st.subheader("Sales by Region")
    region_sales = filtered.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)

    # Line chart: sales by year
    st.subheader("Sales by Year")
    year_sales = filtered.groupby("Year")["Sales"].sum()
    st.line_chart(year_sales)

    # Pie chart: sales by product
    st.subheader("Sales by Product")
    pie_data = (
        filtered.groupby("Product")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        pie_data,
        names="Product",
        values="Sales",
        title="Sales by Product"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Download filtered data
    st.subheader("Download Data")

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Filtered CSV",
        data=csv,
        file_name="filtered_sales.csv",
        mime="text/csv"
    )
else:
    st.warning("No sales records match your selected filters.")

# Show data table
st.subheader("Filtered Sales Data")
st.dataframe(filtered)
