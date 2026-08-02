import requests
from config import BASE_URL


# ==========================================
# Helper
# ==========================================

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }


# ==========================================
# Authentication
# ==========================================

def login(email, password):
    data = {
        "email": email,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/students/login",
        json=data
    )


def register(name, email, password, token):
    data = {
        "name": name,
        "email": email,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/students/register",
        json=data,
        headers=get_headers(token)
    )


def current_user(token):
    return requests.get(
        f"{BASE_URL}/students/me",
        headers=get_headers(token)
    )


def change_password(current_password, new_password, token):
    data = {
        "current_password": current_password,
        "new_password": new_password
    }

    return requests.put(
        f"{BASE_URL}/students/change-password",
        json=data,
        headers=get_headers(token)
    )


# ==========================================
# Profile Picture
# ==========================================

def upload_profile_picture(uploaded_file, token):
    files = {
        "profile": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    return requests.post(
        f"{BASE_URL}/files/profile_picture",
        files=files,
        headers=get_headers(token)
    )


def get_profile_picture(token):
    return requests.get(
        f"{BASE_URL}/files/profile_picture",
        headers=get_headers(token)
    )


def delete_profile_picture(token):
    return requests.delete(
        f"{BASE_URL}/files/",
        headers=get_headers(token)
    )


# ==========================================
# Files
# ==========================================

def upload_file(uploaded_file, category, token):
    files = {
        "profile": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    params = {
        "category": category
    }

    return requests.post(
        f"{BASE_URL}/files/upload_file",
        files=files,
        params=params,
        headers=get_headers(token)
    )


def view_all_files(token):
    return requests.get(
        f"{BASE_URL}/files/viewallfiles",
        headers=get_headers(token)
    )


def view_file(file_id, token):
    return requests.get(
        f"{BASE_URL}/files/viewfile",
        params={"file_id": file_id},
        headers=get_headers(token)
    )


def download_file(file_id, token):
    return requests.get(
        f"{BASE_URL}/files/downloadfile",
        params={"file_id": file_id},
        headers=get_headers(token)
    )


def delete_file(file_id, token):
    return requests.delete(
        f"{BASE_URL}/files/deletefile",
        params={"file_id": file_id},
        headers=get_headers(token)
    )