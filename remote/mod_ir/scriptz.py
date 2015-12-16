import shlex

from subprocess32 import call
from time import sleep

def run_cmd(device, command):
    arg_str = 'irsend SEND_ONCE %s %s' % (device, command)
    args = shlex.split(arg_str)
    call(args)

def run_script(commands):
    for command in commands:
        device = command[0]
        key = command[1]
        arg_str = 'irsend SEND_ONCE %s %s' % (device, key)
        args = shlex.split(arg_str)
        call(args)

def tv_fox():
    #7.1
    commands = [['sharp','KEY_TUNER'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_SELECT']]
    run_script(commands)

def tv_bot():
    #7.1 > bot
    commands = [['sharp','KEY_TUNER'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_SELECT']
                ['sharp', 'KEY_VIDEO'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT']]
    run_script(commands)

def tv_nbc():
    #36.1
    commands = [['sharp','KEY_TUNER'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_RIGHT'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_RIGHT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_SELECT']]
    run_script(commands)

def tv_cbs():
    #42.1
    commands = [['sharp','KEY_TUNER'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_RIGHT'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_DOWN'],
                ['sharp', 'KEY_SELECT'],
                ['sharp', 'KEY_LEFT'],
                ['sharp', 'KEY_UP'],
                ['sharp', 'KEY_SELECT']]
    run_script(commands)
