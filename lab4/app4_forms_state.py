
import streamlit as st

st.set_page_config(
    page_title="Forms + Session State",
    layout="wide"
)

st.title("Forms + Session State")

# Counter using session state
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write("Counter:", st.session_state.count)

# Login form
with st.form("login_form"):
    st.subheader("Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    submit = st.form_submit_button("Login")

if submit:
    if user == "admin" and pwd == "1234":
        st.session_state.logged_in = True
        st.success("Login successful!")
    else:
        st.error("Invalid credentials")

if st.session_state.get("logged_in"):
    st.info("Welcome, admin! You are now logged in.")

# Extra exercise: Reset counter
if st.button("Reset Counter"):
    st.session_state.count = 0

# Extra exercise: Add 5
if st.button("Add 5"):
    st.session_state.count += 5

st.write("Updated Counter:", st.session_state.count)
