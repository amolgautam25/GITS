#!/usr/bin/python3

import os
import sys
import argparse
from gits_hello import gits_hello_world
from gits_add import gits_add_func
from gits_commit import gits_commit_func
from gits_setupstream import upstream

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world')
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_add_subparser = subparsers.add_parser('add')
gits_add_subparser.add_argument('file_names', metavar='N', type=str, nargs='+', help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)

gits_commit_subparser = subparsers.add_parser('commit')
gits_commit_subparser.add_argument('-m', required=True, help='git commit message')
gits_commit_subparser.add_argument('--amend', action='store_true', help='amend commit with previous commit message')
gits_commit_subparser.set_defaults(func=gits_commit_func)

gits_upstream_subparser = subparsers.add_parser('upstream')
gits_upstream_subparser.add_argument('--remote', help='the remote branch we want to use')
gits_upstream_subparser.add_argument('--local', help="local branch we want to track")
gits_upstream_subparser.add_argument('--upstream', help="the upstream branch we want to track to")
gits_upstream_subparser.set_defaults(func=upstream)

args = parser.parse_args()
args.func(args)
