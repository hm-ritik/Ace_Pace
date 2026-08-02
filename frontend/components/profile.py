import streamlit as st

from api import (
    upload_profile_picture,
    get_profile_picture,
    delete_profile_picture
)


def profile_section(token, user):

    st.subheader("Profile")

    col1, col2 = st.columns([1, 3])

    with col1:
        response = get_profile_picture(token)
        if response.status_code == 200:
            st.image(response.content, width=140)
        else:
            st.markdown(
                """
                <div style="width:140px;height:140px;border-radius:50%;
                background:#2b2b3a;display:flex;align-items:center;
                justify-content:center;font-size:48px;color:#888;">
                👤
                </div>
                """,
                unsafe_allow_html=True
            )

    with col2:
        st.write(f"### {user['name']}")
        
    st.write("")

    with st.expander("Update profile picture"):

        uploaded_picture = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png", "webp"],
            key="profile_picture_uploader_v2",
            label_visibility="collapsed"
        )

        col_a, col_b = st.columns(2)

        with col_a:
            if st.button("Upload", use_container_width=True, disabled=uploaded_picture is None):
                response = upload_profile_picture(uploaded_picture, token)
                if response.status_code == 200:
                    st.success("Profile picture updated.")
                    st.rerun()
                else:
                    try:
                        st.error(response.json()["detail"])
                    except Exception:
                        st.error("Upload failed.")

        with col_b:
            if st.button("Remove", use_container_width=True):
                response = delete_profile_picture(token)
                if response.status_code == 200:
                    st.success("Profile picture removed.")
                    st.rerun()
                else:
                    try:
                        st.error(response.json()["detail"])
                    except Exception:
                        st.error("Unable to remove.")