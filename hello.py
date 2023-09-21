from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world(Ikhyun)!</p>"

@app.route("/<name>")
def hello_world_name(name):
    return f"Hello, {escape(name)}!"
