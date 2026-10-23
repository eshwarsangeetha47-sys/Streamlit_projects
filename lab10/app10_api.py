
import streamlit as st
import requests

st.set_page_config(
    page_title="Weather API Demo",
    layout="wide"
)

st.title("Weather API Demo")
st.write("Explore API responses and JSON data.")

city = st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city name.")
    else:
        with st.spinner("Fetching weather..."):
            # Simulated response for this lab
            resp = {
                "city": city.strip(),
                "temperature": 30,
                "condition": "Sunny",
                "humidity": 65
            }

        st.subheader("JSON Response")
        st.json(resp)

        c1, c2, c3 = st.columns(3)
        c1.metric("Temperature", f"{resp['temperature']} °C")
        c2.metric("Condition", resp["condition"])
        c3.metric("Humidity", f"{resp['humidity']}%")

        st.success("Demo completed successfully.")

st.divider()
st.subheader("HTTP Methods")

st.markdown("""
- **GET** — Retrieve data
- **POST** — Send data
- **PUT** — Update data
- **DELETE** — Delete data
""")

st.info(
    "This app uses simulated weather data, not live weather."
)
