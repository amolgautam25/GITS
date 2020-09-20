#!/usr/bin/python3

import os
import sys
import argparse
from gits_hello import gits_hello_world
from gits_add import gits_add_func

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world')
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_add_subparser = subparsers.add_parser('add')
gits_add_subparser.add_argument('file_names', metavar='N', type=str, nargs='+', help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)

args = parser.parse_args()
args.func(args)
