# JEE Exam Registration System

A command-line exam registration and management system for the JEE (Joint Entrance Examination), built in Python with SQLite for local persistent storage. It lets candidates register, log in to view their exam details, and lets an admin manage records — all from a simple terminal menu.

## Overview

The system models a simplified version of a real-world exam registration portal. Candidates register once with their personal, academic, and category details and receive a computer-generated 8-digit Application Number and a password. They can later use these credentials to view their allotted exam paper, city, date, and center. Administrative functions (viewing all records, searching, updating, deleting) are also available from the same menu.

The project is organized as small, single-responsibility modules — database setup, input validation, authentication, registration/record management, and record viewing — rather than one large script.

## Features

- **New Registration** — collects candidate details (name, parents' names, DOB, category, gender, Aadhaar, email, mobile, address, city, state, pincode, exam paper, preferred exam city), validates each field, and auto-generates a unique 8-digit Application Number.
- **All Records (admin-protected)** — lists every registered candidate. Gated behind an admin password (`VITBhopal@123`) so it can't be accessed casually from the main menu.
- **Search Candidate** — look up a single candidate by Application Number + password.
- **Update Record** — candidates can edit any single field of their own record after authenticating with Application Number + password.
- **Delete Candidate** — permanently removes a record, after verifying Application Number + password.
- **Login To View Your Details** — candidates authenticate and see their full exam details: paper, category, city, a fixed exam date/shift, reporting/closing times, and a mock allotted exam center.

## Technologies / Tools Used

- **Python 3** — core application logic
- **SQLite3** (`sqlite3` module) — lightweight, file-based relational database (`jee.db`), no separate DB server needed
- **hashlib (SHA-256)** — one-way password hashing; raw passwords are never stored
- **Standard library only** — `random` (ID/mock data generation), `os` (path handling); no third-party packages
- **Git** — version control

## Architecture / Module Breakdown

| File | Responsibility |
|---|---|
| `main.py` | Entry point; displays the menu and routes user choices |
| `db.py` | SQLite connection handling and `Register` table creation |
| `auth.py` | Password hashing (`hash_pw`) and verification (`check_pw`) |
| `validators.py` | Input validation for DOB, category, gender, Aadhaar, email, mobile, pincode, paper |
| `registration.py` | Registration, update, and delete operations |
| `view.py` | Admin record listing, search, and candidate login/view |

**Workflow:** `main.py` initializes the database on startup, then loops on a menu. Each menu option delegates to a function in `registration.py` or `view.py`, which validates input (via `validators.py`), authenticates where required (via `auth.py`), and reads/writes through `db.py`.

## Steps to Install & Run

1. Clone the repo:
   ```
   git clone https://github.com/tanish05-bit/jee-registration-system.git
   cd jee-registration-system
   ```
2. Make sure you have Python 3.8+:
   ```
   python --version
   ```
3. No external dependencies are required. The project uses Python's built-in libraries and SQLite, so no `pip install` is needed.
4. Run it:
   ```
   python main.py
   ```

`jee.db` is created automatically on first run and is git-ignored, so everyone who clones the repo starts with a clean database.

## Instructions for Testing

Since this is an interactive CLI, testing is manual — run `python main.py` and exercise each menu option:

1. **Register (1)** — enter a full set of valid details and confirm you receive an Application Number and password. Then try invalid inputs (bad DOB format, wrong-length Aadhaar, disallowed email domain, non-6-digit pincode, invalid category/gender/paper) and confirm each is rejected with a re-prompt.
2. **All Records (2)** — confirm the menu now asks for an admin password. Enter the wrong password and confirm access is denied; enter `VITBhopal@123` and confirm the record list is shown, with hashed passwords never displayed.
3. **Search (3)** — search using the Application Number and password from step 1; confirm the correct record is returned, and confirm a wrong password/App No. is rejected.
4. **Update (4)** — authenticate and update a single field (e.g. Address); confirm the change is reflected when searching again.
5. **Delete (5)** — authenticate and delete a record; confirm it no longer appears in Search or All Records.
6. **Login (6)** — log in with valid Application Number + password and confirm exam details (paper, city, date, mock center) are displayed correctly.
7. **Exit (7)** — confirm the program terminates cleanly.

