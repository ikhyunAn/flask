# flask
Study flask web framework

## purpose
Implement microservice using flask and later deploy on OpenFaaS/K3s nodes

## Environment Setup
### Virtual Environment
```bash
python3 -m venv .venv
```
This creates a virtual environment in the directory named `.venv` using Python3
It will create a self-contained Python environment within the `.venv` directory. This environment will have its own isolated set of Python packages and dependencies, separate from the global Python environment on your system.

### Activate venv
```bash
. .venv/bin/activate
```
### Install Flask
```python
pip3 install Flask
```
#### usage
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
`route()` binds a function to specified url

### Run the Application
```python
flask --app hello run --debug
```
`--debug` used for debug mode
```bash
flask --app flaskr run --debug
```
run the flask application

