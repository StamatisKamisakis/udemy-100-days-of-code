# Day 88 — Cafe & Wifi (Flask + SQLAlchemy)


A Flask web app that displays a list of cafes in London suitable for working from — showing wifi availability, power sockets, toilets, ability to take calls, seating capacity, and coffee price for each one. The data is served from a SQLite database (built on Day 66's Cafe & Wifi API) using SQLAlchemy as the ORM, and rendered through Jinja2 templates.

🔗 **Live demo:** https://stamatiskamisakis1992.pythonanywhere.com/

## Features

- Browse a list of cafes with key details at a glance:
  - 📶 Wifi
  - 🔌 Power sockets
  - 🚽 Toilet
  - 📞 Can take calls
  - 🪑 Seating capacity
  - ☕ Coffee price
- Each cafe links out to its location on Google Maps
- Cafe data stored in a SQLite database and queried via SQLAlchemy
- Server-rendered HTML using Flask's Jinja2 templating engine

## Tech Stack

- **Python** / **Flask**
- **Flask-SQLAlchemy** (ORM)
- **SQLite** (`cafes.db`)
- **Jinja2** for templating
- **HTML/CSS** for the frontend
- Deployed on **PythonAnywhere**

## Project Structure

```
Day 88/
├── main.py            # Flask app, routes, and SQLAlchemy models/queries
├── cafes.db           # SQLite database with cafe data
├── templates/
│   └── index.html     # Jinja2 template rendering the cafe list
└── static/
    └── styles.css      # Page styling
```

> Note: adjust the file names above if your actual structure differs — this reflects the typical layout for this bootcamp project.

## Running Locally

1. Clone the repo and navigate into the `Day 88` folder
2. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
   ```
3. Run the app:
   ```bash
   python main.py
   ```
4. Open `http://127.0.0.1:5000` in your browser

## What I Practiced

- Connecting Flask to a SQLite database with SQLAlchemy
- Querying and looping over database records in a Jinja2 template
- Reading and understanding an existing codebase (routing, ORM models, templating) rather than building from scratch
- Deploying a Flask app to PythonAnywhere

## Credits

Project built as part of Angela Yu's *100 Days of Code* Python bootcamp on Udemy.
