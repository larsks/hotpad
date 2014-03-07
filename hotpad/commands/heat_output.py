#!/usr/bin/env python

from __future__ import absolute_import

import os
import sys
import argparse
import yaml

from hotpad.keystone import Keystone
from hotpad.stack import Stack
from hotpad.commands.command import \
    create_parser, \
    setup_logging, \
    get_ksclient

def parse_args():
    p = create_parser()

    p.add_argument('--api-version',
                   default='1')

    p.add_argument('stack')
    p.add_argument('output', nargs='?')

    return p.parse_args()

def main():
    args = parse_args()
    setup_logging(args)

    ks = get_ksclient(args)
    s = Stack(args.stack, ksclient=ks)

    yaml.add_representer(unicode, 
                         lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:str', value))

    print yaml.dump(s.outputs,
                    default_flow_style=False)

if __name__ == '__main__':
    main()

