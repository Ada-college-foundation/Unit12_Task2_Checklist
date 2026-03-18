"""
BTEC Unit 12 – Task 2: Evidence Checklist
Flask web application

Run locally:
    python app.py

Then open http://localhost:5000 in your browser.

For production deployment see README.md.
"""

import os
from flask import Flask, send_from_directory

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = Flask(__name__, static_folder=".", static_url_path="")


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Serve the main checklist page."""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    """Serve any other static asset (CSS, JS, images, etc.)."""
    return send_from_directory(app.static_folder, filename)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
