from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# on Chrome http://127.0.0.1:5000/

# Hello, World!