import base64
import streamlit as st
import streamlit.components.v1 as components

from api import (
    upload_file,
    view_all_files,
    delete_file,
    view_file,
    download_file
)

from utlis import get_documents


def documents_section(token):

    st.subheader("Documents")

    response = view_all_files(token)
    if response.status_code != 200:
        st.error("Unable to load documents.")
        return

    files = response.json()
    documents = get_documents(files)

    st.caption(f"{len(documents)}/10 uploaded")

    with st.expander("Upload new document"):
        uploaded_document = st.file_uploader(
            "Choose a PDF",
            type=["pdf"],
            key="document_upload",
            label_visibility="collapsed"
        )
        if st.button("Upload", key="upload_doc_btn", disabled=uploaded_document is None):
            response = upload_file(uploaded_document, "document", token)
            if response.status_code == 200:
                st.success("Document uploaded.")
                st.rerun()
            else:
                try:
                    st.error(response.json()["detail"])
                except Exception:
                    st.error("Upload failed.")

    st.divider()

    if len(documents) == 0:
        st.info("No documents uploaded yet.")
        return

    for document in documents:

        with st.container(border=True):

            st.write(f"**{document['filename']}**")

            col1, col2, col3 = st.columns(3)

            view_key = f"viewing_doc_{document['id']}"
            if view_key not in st.session_state:
                st.session_state[view_key] = False

            with col1:
                if not st.session_state[view_key]:
                    if st.button("View", key=f"view_doc_{document['id']}"):
                        st.session_state[view_key] = True
                        st.rerun()
                else:
                    if st.button("Close", key=f"close_doc_{document['id']}"):
                        st.session_state[view_key] = False
                        st.rerun()

            with col2:
                dl = download_file(document["id"], token)
                if dl.status_code == 200:
                    st.download_button(
                        "Download",
                        data=dl.content,
                        file_name=document["filename"],
                        mime=document["content_type"],
                        key=f"download_document_{document['id']}"
                    )

            with col3:
                if st.button("Delete", key=f"delete_document_{document['id']}"):
                    response = delete_file(document["id"], token)
                    if response.status_code == 200:
                        st.success("Document deleted.")
                        st.rerun()
                    else:
                        st.error("Unable to delete document.")

            if st.session_state[view_key]:
                preview = view_file(document["id"], token)
                if preview.status_code == 200:
                    b64_pdf = base64.b64encode(preview.content).decode()
                    components.html(
                        f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="500" style="border:none;"></iframe>',
                        height=520
                    )
                else:
                    st.error("Unable to open document.")