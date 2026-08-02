# Ace Pace (Student Space) 
website link : https://ace-pace-2.onrender.com

A simple file storage app I built for a small group of students — think of it as a private locker where you can keep your important documents and photos, view them, download them, and manage your profile.

Built it mainly to solve a real problem: needed a lightweight, secure place for ~10 people to store stuff without dealing with the usual bloat of Google Drive permissions and folder sharing chaos.

---

## What it does

* Login with email/password (no public signup — accounts are created manually by an admin, so it stays invite-only)
* Upload profile picture
* Upload up to 10 photos and 10 documents per account
* View, download, and delete your own files
* Change your password
* Every file is encrypted before it touches the disk, so even if someone got access to the storage directly, they'd just see garbage bytes

---

## Tech Stack

### Backend

* FastAPI (async, all the way through)
* SQLAlchemy (async) + PostgreSQL (hosted on Supabase)
* JWT auth via `python-jose`
* Password hashing with `pwdlib` (argon2)
* File encryption at rest using Fernet (`cryptography`)
* File type validation via `filetype` (checks actual file signatures, not just extensions)

### Frontend

* Streamlit — kept it simple on purpose. No React, no build step, just fast to ship.

### Hosting

* Backend: Render
* Frontend: Render (Streamlit)
* Database: Supabase (Postgres)

---

## Why these choices

I originally built this with SQLite for speed during development, but SQLite doesn't survive redeploys on most hosting platforms (the disk gets wiped), so I moved to Supabase Postgres before going live.

Similarly, admin-only registration was a deliberate choice — this isn't a public app, and I wanted control over who gets an account rather than dealing with open signup and the spam/abuse that comes with it.

Every file is encrypted before it's saved to disk, and every request that touches a specific file checks that the file actually belongs to the logged-in user — so there's no way for one user to view, download, or delete another user's files just by guessing an ID.

---

## Project Structure

```text
student_space/
├── backend/
│   └── app/
│       ├── core/          # database connection, auth dependencies, encryption, password hashing
│       ├── models/        # SQLAlchemy models (Student, UploadedFiles, ProfilePicture)
│       ├── repository/    # raw DB queries
│       ├── routes/        # API endpoints
│       ├── schemas/       # Pydantic request/response models
│       ├── services/      # business logic (auth, file handling, limits)
│       └── main.py
└── frontend/
    ├── components/        # profile, images, documents, change password sections
    ├── pages/
    │   └── Dashboard.py
    ├── api.py             # all HTTP calls to the backend
    ├── auth.py            # session token handling
    ├── config.py          # backend URL
    └── app.py             # login page
```

---



## What's next (maybe)

* Password reset via email
* Admin dashboard to see all users and manage accounts without touching the DB directly
* Better mobile styling


  Backend made by - Ritik 
