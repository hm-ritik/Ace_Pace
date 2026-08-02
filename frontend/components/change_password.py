import streamlit as st

from api import change_password


def change_password_section(token):

    st.subheader("🔒 Change Password")

    current_password = st.text_input(
        "Current Password",
        type="password",
        key="current_password"
    )

    new_password = st.text_input(
        "New Password",
        type="password",
        key="new_password"
    )

    if st.button(
        "Update Password",
        use_container_width=True
    ):

        if current_password == "" or new_password == "":

            st.warning("Please fill all fields.")

            return

        response = change_password(
            current_password,
            new_password,
            token
        )

        if response.status_code == 200:

            st.success("Password updated successfully.")

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error("Unable to update password.")