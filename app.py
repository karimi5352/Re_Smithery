"""
Re-Smaithery
A minimal Flask web application starter.
"""
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/api/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"})


@app.route("/api/echo", methods=["POST"])
def echo():
    """Echo back JSON sent in the request body."""
    data = request.get_json(silent=True) or {}
    return jsonify({"you_sent": data})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
