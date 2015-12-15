from flask import Blueprint, request, Response, \
                  jsonify, g, session

mod_ir = Blueprint('ir', __name__, url_prefix='/ir')

@mod_ir.route('/send', methods=['PUT'])
def send_command():
    params = request.args
    target = str(params.get('device'))
    command = str(params.get('command'))
    print target
    print command
    return "lol okay!"
