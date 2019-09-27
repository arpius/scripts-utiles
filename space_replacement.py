#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys


parser = argparse.ArgumentParser(prog='space_replacement',
                                 usage='%(prog)s path replacement',
                                 description='Replaces spaces in a file name.')

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='the files path')
parser.add_argument('Replacement',
                    metavar='replacement',
                    type=str,
                    help='the replacement character')

args = parser.parse_args()
path = args.Path
replacement = args.Replacement

if not os.path.isdir(path):
    print("The specified path does not exist.")
    sys.exit()

files = os.listdir(path)

for file in files:
    old_name = os.path.join(path, file)
    new_name = replacement.join(old_name.split())

    os.rename(old_name, new_name)
