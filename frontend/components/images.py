import streamlit as st

from api import (
    upload_file,
    view_all_files,
    delete_file,
    view_file,
    download_file
)

from utlis import get_images


def images_section(token):

    st.subheader("Images")

    response = view_all_files(token)
    if response.status_code != 200:
        st.error("Unable to load images.")
        return

    files = response.json()
    images = get_images(files)

    st.caption(f"{len(images)}/10 uploaded")

    with st.expander("Upload new image"):
        uploaded_image = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png", "webp"],
            key="image_upload",
            label_visibility="collapsed"
        )
        if st.button("Upload", key="upload_image_btn", disabled=uploaded_image is None):
            response = upload_file(uploaded_image, "photo", token)
            if response.status_code == 200:
                st.success("Image uploaded.")
                st.rerun()
            else:
                try:
                    st.error(response.json()["detail"])
                except Exception:
                    st.error("Upload failed.")

    st.divider()

    if len(images) == 0:
        st.info("No images uploaded yet.")
        return

    for image in images:

        with st.container(border=True):

            st.write(f"**{image['filename']}**")

            col1, col2, col3 = st.columns(3)

            view_key = f"viewing_{image['id']}"
            if view_key not in st.session_state:
                st.session_state[view_key] = False

            with col1:
                if not st.session_state[view_key]:
                    if st.button("View", key=f"view_{image['id']}"):
                        st.session_state[view_key] = True
                        st.rerun()
                else:
                    if st.button("Close", key=f"close_{image['id']}"):
                        st.session_state[view_key] = False
                        st.rerun()

            with col2:
                dl = download_file(image["id"], token)
                if dl.status_code == 200:
                    st.download_button(
                        "Download",
                        data=dl.content,
                        file_name=image["filename"],
                        mime=image["content_type"],
                        key=f"download_{image['id']}"
                    )

            with col3:
                if st.button("Delete", key=f"delete_{image['id']}"):
                    response = delete_file(image["id"], token)
                    if response.status_code == 200:
                        st.success("Deleted.")
                        st.rerun()
                    else:
                        st.error("Delete failed.")

            if st.session_state[view_key]:
                preview = view_file(image["id"], token)
                if preview.status_code == 200:
                    st.image(preview.content)
                else:
                    st.error("Unable to open image.")