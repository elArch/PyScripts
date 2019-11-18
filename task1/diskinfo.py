#!/usr/bin/env python3

#******************************************************************************#
#   df - report file system disk space usage
#   -h --human-readable     Print sizes in powers of 1024 (e.g., 1023M)
#   -a --all                Include pseudo, duplicate, inaccessible file systems
#   --output                Use the output format defined
#******************************************************************************#
#   lsblk - list block devices
#   -o --output list        Specify which output colums to print
#******************************************************************************#

import os
import sys
import subprocess

def getObjectPath() :
    if len(sys.argv) < 2 :
        print('Please specify a path to the file with device name')
        exit(1)
    elif os.path.exists(sys.argv[1]) :
         with open(sys.argv[1], 'r') as inf :
            return inf.read().strip()
    else:
        print('Path to file with device name does not exists')
        exit(1)

def getDiskDeviceInfo(_object_path) :
    try :
        res_df = subprocess.Popen( ['df', '-a', '-h', '--output', _object_path], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        list_keys = res_df.stdout.readline().decode('utf-8').strip('\n').split()
        list_values = res_df.stdout.readline().decode('utf-8').strip('\n').split()
        dc = dict(zip(list_keys, list_values))
    except :
        print('Can not get device info through df - utility, Please check the device path: {}'.format(_object_path))
        exit(1)

    try :
        res_lsblk = subprocess.Popen( ['lsblk','-o', 'TYPE', '/dev/sda'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        key = res_lsblk.stdout.readline().decode('utf-8').strip('\n')
        value = res_lsblk.stdout.readline().decode('utf-8').strip('\n')
        dc[key] = value
    except :
        print('Can not get device info through lsblk - utility, Please check the device path: {}'.format(_object_path))
        exit(1)

    if _object_path[-1].isdigit() :
        print(('{} {} {} {} {} {}').format(dc.get('File'), dc.get('TYPE'), dc.get('Size'), dc.get('Avail'), dc.get('Type'),dc.get('Mounted')))
    else :
        print(('{} {} {}').format(dc.get('File'), dc.get('TYPE'),dc.get('Size')))

def main() :
    _object_path = getObjectPath()
    getDiskDeviceInfo(_object_path)


if __name__ == '__main__' :
    sys.exit(main())
