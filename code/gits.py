#!/usr/bin/python3

import sys
import argparse
from gits_logging import init_gits_logger
from gits_hello import gits_hello_world
from gits_add import gits_add_func
from gits_commit import gits_commit_func
from gits_set import gits_set_func
from gits_setupstream import upstream
from gits_create_branch import create_branch
from gits_super_reset import super_reset

from gits_rebase import gits_rebase
from gits_reset import gits_reset

from gits_profile import gits_set_profile
from gits_pr_update import gits_pr_update_func
from gits_status import gits_status
from gits_diff import gits_diff

logger_status = init_gits_logger()
if not logger_status:
    print("ERROR: logger not initialised")
    sys.exit(1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world')
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_set_subparser = subparsers.add_parser('set')
gits_set_subparser.add_argument('--parent', help='git parent branch')
gits_set_subparser.set_defaults(func=gits_set_func)

gits_add_subparser = subparsers.add_parser('add')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='+',
                                help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)


gits_commit_subparser = subparsers.add_parser('commit')
gits_commit_subparser.add_argument('-m',
                                   required=True,
                                   help='git commit message')
gits_commit_subparser.add_argument('--amend',
                                   action='store_true',
                                   help='amend commit message')
gits_commit_subparser.set_defaults(func=gits_commit_func)

gits_create_subparser = subparsers.add_parser('create')
gits_create_subparser.add_argument('-b', help="branch name to create")
gits_create_subparser.set_defaults(func=create_branch)


gits_upstream_subparser = subparsers.add_parser('upstream')
gits_upstream_subparser.add_argument('--remote',
                                     help='the remote branch name')
gits_upstream_subparser.add_argument('--local',
                                     help="local branch name")
gits_upstream_subparser.add_argument('--upstream',
                                     help="the upstream branch name")
gits_upstream_subparser.set_defaults(func=upstream)

gits_profile_subparser = subparsers.add_parser('profile', help='profie help')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email',
                                    required=True,
                                    help='email to be used')
gits_profile_subparser.add_argument('--name',
                                    required=True,
                                    help='name to be used')

gits_pr_subparser = subparsers.add_parser('sync', help='sync help')
gits_pr_subparser.set_defaults(func=gits_pr_update_func)
gits_pr_subparser.add_argument('--upstream', nargs='?')

gits_super_reset_subparser = subparsers.add_parser('super-reset')
gits_super_reset_subparser.add_argument('--name', help="Name of the repository to super reset")
gits_super_reset_subparser.set_defaults(func=super_reset)

gits_rb_subparser = subparsers.add_parser('rebase', help='sync help')
gits_rb_subparser.set_defaults(func=gits_rebase)

gits_reset_subparser = subparsers.add_parser('reset', help='sync help')
gits_reset_subparser.set_defaults(func=gits_reset)
gits_reset_subparser.add_argument('--branch', required=True, help='branch to be used')

gits_status_subparser=subparsers.add_parser('status')
gits_status_subparser.set_defaults(func=gits_status)

gits_diff_subparser=subparsers.add_parser('diff')
gits_diff_subparser.set_defaults(func=gits_diff)


args = parser.parse_args()
args.func(args)
