from . import app
from flask import Flask, Response, g

@app.route("/")
def hello_world():
    return 'hello'
