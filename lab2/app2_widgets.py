
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Widgets Playground",
    layout="wide"
)

st.title("Widgets Playground")
st.write("Explore different Streamlit widgets.")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100, value=20)
marks = st.slider("Marks", 0, 100, 75)

city = st.selectbox(
    "City",
    ["Chennai", "Mumbai", "Delhi"]
)

skills = st.multiselect(
    "Skills",
    ["Python", "ML", "SQL", "Streamlit"]
)

gender = st.radio(
    "Gender",
    ["Male", "Female", "Other"]
)

agree = st.checkbox("I agree to terms")

dob = st.date_input(
    "Date of Birth",
    date(2000, 1, 1)
)

file = st.file_uploader("Upload a file")

color = st.color_picker("Pick a color", "#00FF00")

marks_range = st.select_slider(
    "Select a range of marks",
    options=list(range(0, 101)),
    value=(40, 80)
)

if st.button("Submit"):
    st.subheader("Your Details")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Marks:", marks)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Gender:", gender)
    st.write("Agreed:", agree)
    st.write("Date of Birth:", dob)
    st.write("Selected color:", color)
    st.write("Marks range:", marks_range)

    st.write("Name type:", type(name))
    st.write("Age type:", type(age))
    st.write("Marks type:", type(marks))

    if file is not None:
        st.write("Uploaded file:", file.name)
