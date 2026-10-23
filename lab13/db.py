
import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        st.secrets["postgres"]["url"],
        cursor_factory=RealDictCursor
    )


def init_db():
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
        conn.commit()
    finally:
        conn.close()


def create_user(username, email, password_hash):
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO users (username, email, password_hash)
                VALUES (%s, %s, %s)
                RETURNING id, username, email, created_at;
                """,
                (username, email, password_hash)
            )
            user = cur.fetchone()

        conn.commit()
        return user

    finally:
        conn.close()


def get_user_by_username(username):
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, username, email, password_hash, created_at
                FROM users
                WHERE username = %s;
                """,
                (username,)
            )
            return cur.fetchone()

    finally:
        conn.close()


def get_all_users():
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, username, email, created_at
                FROM users
                ORDER BY id;
            """)
            return cur.fetchall()

    finally:
        conn.close()


def user_exists(username, email):
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT 1
                FROM users
                WHERE username = %s OR email = %s
                LIMIT 1;
                """,
                (username, email)
            )
            return cur.fetchone() is not None

    finally:
        conn.close()
