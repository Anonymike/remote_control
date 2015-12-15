import shlex

from flask import Blueprint, request, Response, \
                  jsonify, g, session

from subprocess32 import call

mod_ir = Blueprint('ir', __name__, url_prefix='/ir')

def run_command(device, command):
    arg_str = 'irsend SEND_ONCE %s %s' % (device, command)
    args = shlex.split(arg_str)
    call(args)


@mod_ir.route('/send', methods=['PUT'])
def send_command():
    params = request.args
    target = str(params.get('device'))
    command = str(params.get('command'))
    return "lol okay!"