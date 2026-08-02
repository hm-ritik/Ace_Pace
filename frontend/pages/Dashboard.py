import streamlit as st

from auth import get_token, logout
from api import current_user

from components.profile import profile_section
from components.images import images_section
from components.documents import documents_section
from components.change_password import change_password_section


# -----------------------------
# Authentication
# -----------------------------

token = get_token()

if token is None:
    st.switch_page("app.py")


# -----------------------------
# Get User Details
# -----------------------------

response = current_user(token)

if response.status_code != 200:
    st.error("Session Expired")
    logout()
    st.switch_page("app.py")

user = response.json()


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Ace Pace")

st.write(f"## Welcome, {user['name']} 👋")

st.divider()


# -----------------------------
# Profile Section
# -----------------------------

profile_section(token, user)

st.divider()


# -----------------------------
# Images
# -----------------------------

images_section(token)

st.divider()


# -----------------------------
# Documents
# -----------------------------

documents_section(token)

st.divider()


# -----------------------------
# Change Password
# -----------------------------

change_password_section(token)

st.divider()


# -----------------------------
# Logout
# -----------------------------

if st.button("Logout", use_container_width=True):

    logout()

    st.switch_page("app.py")
