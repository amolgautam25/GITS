#!/usr/bin/python3

import os
import sys
import argparse
from gits_hello import gits_hello_world

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world')
gits_hello_subparser.set_defaults(func=gits_hello_world)

args = parser.parse_args()
args.func(args)
