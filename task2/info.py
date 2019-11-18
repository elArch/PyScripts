#!/usr/bin/python3

import os
import re
import sys
import subprocess

def checkArgs() :
     if len(sys.argv) < 3 :
        print( 'Please Define all available arguments:\n'
               '\t\t\t\t\t1st: Target Type [--timer | --service]\n'
               '\t\t\t\t\t2nd: Target Name ' )
        exit(1)
    else :
        return
        getinfo(sys.argv[1], sys.argv[2])



def getInfo(_type, _name) :

    if (_type == '--timer'):
        _target = _name + '.' + _type[2:]

    if (_type == '--service'):
        _target = _name + '.' + _type[2:]

    try :
        _output = subprocess.Popen(['systemctl', 'status', _target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _stdout = _output.communicate()[0].decode('utf-8').split('\n')


        # There we Create Dictionary
        _state_dict = dict()
        for _line in _stdout :
            _key_value = re.split(r':',_line, maxsplit=1)
            if len(_key_value) == 2 :
                print (_key_value)
                _state_dict = {_key_value[0]: _key_value[1]}
            continue
        
        if (_type == '--service') :
            print('{}{}{}'.format(_state_dict.get('Active')))
        
        if (_type == '--timer') :
            print('Status: {}'.format(_state_dict.get('Active')))

    except Exception as e :
        print('%r'%e)
        print('Target Object {} not found'.format(_target))


def main() :
   if __name__ == '__main__' :
    sys.exit(main())
