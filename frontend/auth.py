import streamlit as st

TOKEN_KEY = "access_token"


def save_token(token):
    st.session_state[TOKEN_KEY] = token


def get_token():
    return st.session_state.get(TOKEN_KEY)


def logout():
    st.session_state.clear()