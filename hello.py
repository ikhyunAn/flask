from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

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
    url_for('static', filename='style.css')

# By default, route only answeres to GET requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
