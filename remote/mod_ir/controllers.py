import shlex

from flask import Blueprint, request, Response, \
                  jsonify, g, session

from subprocess32 import call
from .scriptz import *

mod_ir = Blueprint('ir', __name__, url_prefix='/ir')

def run_command(device, command):
    arg_str = 'irsend SEND_ONCE %s %s' % (device, command)
    args = shlex.split(arg_str)
    call(args)


@mod_ir.route('/send', methods=['POST'])
def send_command():
    params = request.args
    device = str(params.get('device'))
    command = str(params.get('command'))
    run_command(device, command)
    return "okay"

@mod_ir.route('/tv/on', methods=['POST'])
@mod_ir.route('/tv/off', methods=['POST'])
def power_tv():
    run_command('sharp', 'KEY_POWER')
    return "okay"

@mod_ir.route('/tv/input', methods=['POST'])
def input_tv():
    run_command('sharp', 'KEY_VIDEO')
    return "okay"

@mod_ir.route('/tv', methods=['POST'])
def select_tv():
    params = request.args
    channel = str(params.get('channel'))
    if channel == 'fox':
        tv_fox()
    elif channel == 'nbc':
        tv_nbc()
    elif channel == 'cbs':
        tv_cbs()
    elif channel == 'bot':
        tv_bot()
    elif channel == 'chrome':
        tv_chrome()
    else:
        tv_fox()
    return "okay"

@mod_ir.route('/soundbar/on', methods=['POST'])
@mod_ir.route('/soundbar/off', methods=['POST'])
def power_soundbar():
    run_command('soundbar', 'KEY_POWER')
    return "okay"

@mod_ir.route('/soundbar', methods=['POST'])
def soundbar_buttonz():
    params = request.args
    button = str(params.get('button'))
    if button == 'vol_up':
        run_command('soundbar', 'KEY_VOLUMEUP')
    elif button == 'vol_down':
        run_command('soundbar', 'KEY_VOLUMEDOWN')
    elif button == 'mute':
        run_command('soundbar', 'KEY_MUTE')
    elif button == 'optical':
        run_command('soundbar', 'BTN_0')
    elif button == 'bot':
        run_command('soundbar', 'BTN_1')
    return "okay"
