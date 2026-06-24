# Re_Smaithery

A minimal Flask web app starter — Python backend with a simple HTML/CSS/JS frontend.

## Project structure

```
Re_Smaithery/
├── app.py              # Flask application and routes
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Home page
└── static/
    ├── style.css        # Styling
    └── app.js            # Frontend JS
```

## Setup

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then open http://localhost:5000 in your browser.

## API

- `GET /api/health` — returns `{"status": "ok"}`
- `POST /api/echo` — echoes back the JSON body you send

## Next steps

- Add a database (e.g. SQLite with SQLAlchemy)
- Add more routes and templates
- Add tests with `pytest`
