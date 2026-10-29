from flask import Flask, send_file
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


@app.route("/")
def home():
    return send_file(os.path.join(FRONTEND_DIR, "index.html"))


@app.route("/careers.html")
def careers():
    return send_file(os.path.join(FRONTEND_DIR, "careers.html"))


@app.route("/login.html")
def login():
    return send_file(os.path.join(FRONTEND_DIR, "login.html"))


@app.route("/register.html")
def register():
    return send_file(os.path.join(FRONTEND_DIR, "register.html"))


@app.route("/<path:filename>")
def frontend_files(filename):
    file_path = os.path.join(FRONTEND_DIR, filename)

    if os.path.isfile(file_path):
        return send_file(file_path)

    return send_file(os.path.join(FRONTEND_DIR, "404.html")), 404

if __name__ == "__main__":
    app.run(debug=True)
