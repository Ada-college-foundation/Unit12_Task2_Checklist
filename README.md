# Unit12 Task 2 – Evidence Checklist

> **BTEC Level 1/2 Extended Certificate in Information and Creative Technology**  
> Unit 12: Software Development · Assignment 2: Design a 2D Game using Pygame  
> Task 2: Design the Program  
> Assessor: Christopher Moss · Hand-in: Friday 27 March 2026, 3:59 pm

---

## 📋 What this project does

This is an interactive, browser-based evidence checklist for BTEC Unit 12, Task 2.  
Students tick off each piece of evidence, set a RAG (Red / Amber / Green) status, and add free-text notes. Progress is saved automatically in the browser via `localStorage` so nothing is lost on page refresh.

Students can also **download their completed checklist** at any time in three formats:

| Button | Format | Opens in |
|--------|--------|----------|
| 📄 CSV | `.csv` (UTF-8 BOM) | Excel, Google Sheets, Numbers |
| 📊 Google Sheets (.xlsx) | `.xlsx` two-sheet workbook | Google Sheets, Excel, LibreOffice |
| 📝 Word (.doc) | Word-compatible HTML | Microsoft Word, LibreOffice Writer |

All downloads reflect the **current live state** – re-download after any change to get an up-to-date copy.

---

## 🏗️ How this project was built

| Layer | Technology | Notes |
|-------|-----------|-------|
| Structure | Plain HTML5 (`index.html`) | Single-file, no build step required |
| Styling | Vanilla CSS | Embedded in `<style>` — no framework needed |
| Logic | Vanilla JavaScript (ES6+) | Embedded in `<script>` — no bundler needed |
| Persistence | Browser `localStorage` | State survives page refresh with no back-end |
| Excel/Sheets export | [SheetJS 0.20.3](https://sheetjs.com/) (CDN) | Loaded from `cdn.sheetjs.com` at runtime |
| CSV export | Pure JS `Blob` + `URL.createObjectURL` | UTF-8 BOM for correct encoding in Excel |
| Word export | Word-compatible HTML `Blob` (`application/msword`) | Opens in Word / LibreOffice Writer |
| Flask server | Python 3 · Flask ≥ 3.1 (`app.py`) | Serves `index.html` for self-hosted deployments |
| Hosting (live) | GitHub Pages (`gh-pages` branch) | Zero-cost, auto-deployed on push |

The checklist was created iteratively using **GitHub Copilot** coding agents as part of the Ada College software development curriculum.

---

## 🌐 Hosting

### Option 1 – GitHub Pages (current live hosting, zero cost)

The site is published automatically from the **`gh-pages`** branch via GitHub Pages.

**Live URL:** `https://ada-college-foundation.github.io/Unit12_Task2_Checklist/`

To update the live site, merge changes into the `gh-pages` branch:

```bash
git checkout gh-pages
git merge main          # or merge your feature branch
git push origin gh-pages
```

GitHub rebuilds the page within ~30 seconds of the push.

---

### Option 2 – Run locally with Python / Flask

Use this when you want to run the site on your own computer.

#### Prerequisites

- Python 3.8 or later — download from [python.org](https://www.python.org/downloads/)
- `pip` (bundled with Python)

#### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Ada-college-foundation/Unit12_Task2_Checklist.git
cd Unit12_Task2_Checklist

# 2. (Optional but recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
python app.py
```

Open your browser at **http://localhost:5000**

Stop the server with **Ctrl + C**.

---

### Option 3 – Deploy to a cloud platform

The `app.py` + `requirements.txt` + `Procfile` files make this ready to deploy on any Python-compatible cloud platform.

#### PythonAnywhere (free tier available)

1. Create a free account at [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Open a **Bash console** and run:

   ```bash
   git clone https://github.com/Ada-college-foundation/Unit12_Task2_Checklist.git
   cd Unit12_Task2_Checklist
   pip install -r requirements.txt
   ```

3. Go to **Web** → **Add a new web app** → choose **Manual configuration** → Python 3.  
4. Set the **Source code** directory to `/home/<username>/Unit12_Task2_Checklist`.  
5. In the **WSGI configuration file** replace its content with:

   ```python
   import sys
   sys.path.insert(0, '/home/<username>/Unit12_Task2_Checklist')
   from app import app as application
   ```

6. Click **Reload** — your site goes live at `<username>.pythonanywhere.com`.

#### Railway (free tier available)

1. Push this repository to GitHub (already done).
2. Go to [railway.app](https://railway.app/) → **New Project** → **Deploy from GitHub repo**.
3. Select this repository — Railway auto-detects Python, installs `requirements.txt`, and runs `python app.py`.
4. Your app is live at the Railway-generated URL within ~2 minutes.

#### Heroku

```bash
# Install the Heroku CLI, then:
heroku login
heroku create unit12-task2-checklist
git push heroku gh-pages:main
heroku open
```

The `Procfile` tells Heroku to run `python app.py`.

---

## 📁 Repository structure

```
Unit12_Task2_Checklist/
├── index.html          # Main checklist — the entire front-end lives here
├── app.py              # Flask web server (for self-hosted / cloud deployments)
├── requirements.txt    # Python dependencies (Flask)
├── Procfile            # Process file for Heroku / Railway deployment
└── README.md           # This file
```

---

## 🔧 Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Port the Flask server listens on |
| `FLASK_DEBUG` | `0` | Set to `1` to enable debug mode and auto-reload |

```bash
# Example: run in debug mode on port 8080
FLASK_DEBUG=1 PORT=8080 python app.py
```

---

## 📜 Licence

This project is created for educational purposes as part of the Ada College BTEC programme.
