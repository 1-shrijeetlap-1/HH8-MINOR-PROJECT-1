# HH8-MINOR-PROJECT-1
# Honeypot Login Project

A web-based honeypot application designed to simulate a realistic login interface. Its primary purpose is to capture and log credentials, IP addresses, and other metadata from unauthorized access attempts.

##  Features

-   **Realistic Login Interface**: A "fake" login interface located at the "root URL".

-   **Credential Harvesting**: It takes user input credentials filled in on the login page.
-   **Metadata Logging**: It captures attacker's IP address, User Agent String, and request headers.
-   **Admin Dashboard**: A secured way to access statistics as well as captured log information.
-   **SQLite Database**: A lightweight, zero-configuration storage solution that will be used for storing logs.
-   **Session Security**: Simple session based security mechanism for the admin panel.

###  Technology Stack

-   **Backend**: Python, Flask
-   **Database**: SQLite

-   **Frontend**: HTML, CSS (Custom Styling)

## Project Structure
In the
Hone
└── app.py           # Main Flask application and database initialization
└── honeypot.db       # SQLite database file created on first run
├── static/             # CSS and static assets
│   └── dashboard.css
└── templates/        # HTML templates
├── login.html      # The honeypot login page
├── admin_login.html# Admin authentication page

└── admin.html       # Admin dashboard for viewing log files.

```python

  Installation & Setup

1.  **Prerequisites**: You need to have Python installed.
2.  **Clone or Download** the repository to your local machine.
3.  **Set up a Virtual Environment** (Recommended):
```
python -m venv .venv
# Windows
.ven # macOS/Linux source .venv ```

4.  **Install Dependencies**:
    This project requires `Flask`.
    ```bash
    pip install flask
    ```

5.  **Initialize the Database**:
    The database `honeypot.db` is automatically created when you run the application for the first time.

## Usage

1.  **Start the Application**:
    ```bash
    python app.py
    ```


2.  **Access the Honeypot**:
    Open your browser and navigate to `http://127.0.0.1:5000/`.
    -   Any attempt to log in here will be recorded.
    -   The user will always see an "Invalid username or password" error.
<img width="1917" height="911" alt="Screenshot 2026-01-31 182538" src="https://github.com/user-attachments/assets/2ace7951-e1ad-4078-8c22-c7f89e8246fd" />

<img width="1917" height="918" alt="Screenshot 2026-01-31 182600" src="https://github.com/user-attachments/assets/64afdb44-a9dc-4ac6-91e2-0c599e382b9e" />

<img width="1916" height="912" alt="Screenshot 2026-01-31 182640" src="https://github.com/user-attachments/assets/a6913655-44f9-4d37-9602-72e57135463c" />

3.  **Access the Admin Dashboard**:
    Navigate to `http://127.0.0.1:5000/admin`.
    -   **Admin Key**: `admin123` (Default)
    -   Here you can view a table of all captured login attempts and summary statistics.

## Disclaimer

This project is for **educational and research purposes only**. Ensure you have permission to run this on any network you do not own. usage of honeypots may be subject to legal restrictions in some jurisdictions.
