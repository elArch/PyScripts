#!/usr/bin/python3

# Version = 1.0

import re
import sys
import subprocess


def check_args():
    if len(sys.argv) < 3:
        print(
            '\nPlease Define all available arguments:'
            '\n\t1-st argument is Target Type [--timer | --service]'
            '\n\t2-nd argument is Target Name'
        )
        exit(1)
    else:
        return sys.argv[1], sys.argv[2]


def show_active_service_or_timer(_type, _name):

    _target = _name + '.' + _type[2:]

    try:
        _output = subprocess.Popen(['systemctl', 'status', _target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _stdout = _output.communicate()[0].decode('utf-8').split('\n')

        # State Dictionary
        _state_dict = dict()
        for _line in _stdout:
            _key_value = re.split(r':', _line, maxsplit=1)
            if len(_key_value) == 2:
                _state_dict = {_key_value[0]: _key_value[1]}

        if _type == '--service':
            print('{}{}{}'.format(_state_dict.get('Active')))

        if _type == '--timer':
            print('Status: {}'.format(_state_dict.get('Active')))

    except ValueError as e:
        print('%r' % e)
        print('Target Object {} not found'.format(_target))
        exit(1)


def main():
    if __name__ == '__main__':
        object_type, name = check_args()
        show_active_service_or_timer(object_type, name)
        sys.exit()
