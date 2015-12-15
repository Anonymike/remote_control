from . import app
from flask import Flask, Response, g

@app.route("/")
def hello_world():
    return 'hello'
from remote.mod_ir.controllers import mod_ir as ir_module
app.register_blueprint(ir_module)
