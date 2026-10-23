
import streamlit as st
from psycopg2 import IntegrityError

from db import (
    init_db,
    create_user,
    get_user_by_username,
    get_all_users,
    user_exists
)
from auth import (
    hash_password,
    verify_password,
    validate_username,
    validate_email,
    validate_password
)

st.set_page_config(
    page_title="Login and Signup",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login / Signup System")
st.caption("User authentication with PostgreSQL")

try:
    init_db()
except Exception:
    st.error(
        "Could not connect to the database. "
        "Check your Neon connection string in "
        "lab13/.streamlit/secrets.toml."
    )
    st.stop()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.logged_in:
    login_tab, signup_tab = st.tabs(["Login", "Signup"])

    with login_tab:
        st.subheader("Login")

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input(
                "Password",
                type="password"
            )
            login_button = st.form_submit_button(
                "Login",
                use_container_width=True
            )

        if login_button:
            user = get_user_by_username(username.strip())

            if user and verify_password(
                password,
                user["password_hash"]
            ):
                st.session_state.logged_in = True
                st.session_state.user = {
                    "id": user["id"],
                    "username": user["username"],
                    "email": user["email"]
                }
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with signup_tab:
        st.subheader("Create an account")

        with st.form("signup_form"):
            new_username = st.text_input("Choose a username")
            new_email = st.text_input("Email address")
            new_password = st.text_input(
                "Choose a password",
                type="password"
            )
            confirm_password = st.text_input(
                "Confirm password",
                type="password"
            )
            signup_button = st.form_submit_button(
                "Create account",
                use_container_width=True
            )

        if signup_button:
            new_username = new_username.strip()
            new_email = new_email.strip().lower()

            if not validate_username(new_username):
                st.error(
                    "Username must contain 3–50 letters, "
                    "numbers, or underscores."
                )
            elif not validate_email(new_email):
                st.error("Enter a valid email address.")
            elif not validate_password(new_password):
                st.error(
                    "Password must be at least 6 characters "
                    "and contain a letter and a number."
                )
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            elif user_exists(new_username, new_email):
                st.error(
                    "That username or email is already registered."
                )
            else:
                try:
                    create_user(
                        new_username,
                        new_email,
                        hash_password(new_password)
                    )
                    st.success(
                        "Account created! Open the Login tab "
                        "and sign in."
                    )
                except IntegrityError:
                    st.error(
                        "That username or email is already registered."
                    )
                except Exception:
                    st.error(
                        "Could not create the account. "
                        "Please check your database connection."
                    )

else:
    st.success(
        f"Welcome, {st.session_state.user['username']}!"
    )
    st.subheader("Dashboard")

    st.write("**User ID:**", st.session_state.user["id"])
    st.write("**Username:**", st.session_state.user["username"])
    st.write("**Email:**", st.session_state.user["email"])

    st.divider()
    st.subheader("Registered Users")

    try:
        users = get_all_users()
        if users:
            st.dataframe(
                [dict(user) for user in users],
                use_container_width=True
            )
        else:
            st.info("No users registered yet.")
    except Exception:
        st.error("Could not load registered users.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

st.divider()
st.caption("Lab 13 | Streamlit + PostgreSQL + Password Hashing")
