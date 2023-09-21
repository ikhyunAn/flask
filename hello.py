from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world(Ikhyun)!</p>"

@app.route("/<name>")
def hello_world_name(name):
    return f"Hello, {escape(name)}!"

@app.route('/home_route')
def hello():
    return 'This is home'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post #{post_id}'

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('show_post', post_id=99))