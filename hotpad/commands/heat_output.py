#!/usr/bin/env python

from __future__ import absolute_import

import os
import sys
import argparse
import yaml
import logging

from hotpad.keystone import Keystone
from hotpad.stack import Stack

def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('--debug', action='store_const',
                   dest='loglevel', const=logging.DEBUG)
    p.add_argument('--quiet', action='store_const',
                   dest='loglevel', const=logging.WARN)
    p.add_argument('--os-username')
    p.add_argument('--os-tenant-name')
    p.add_argument('--os-password')
    p.add_argument('--os-auth-url')
    p.add_argument('--os-region-name')
    p.add_argument('--api-version',
                   default='1')

    p.add_argument('stack')
    p.add_argument('output', nargs='?')

    p.set_defaults(loglevel=logging.INFO)

    return p.parse_args()

def get_ksclient(args):
    kwargs = {
        'auth_url': args.os_auth_url,
        'tenant_name': args.os_tenant_name,
        'username': args.os_username,
        'password': args.os_password,
        'region_name': args.os_region_name,
    }
    return Keystone(**kwargs)

def main():
    args = parse_args()

    logging.basicConfig(
        level = args.loglevel)

    ks = get_ksclient(args)
    s = Stack(args.stack, ksclient=ks)

    yaml.add_representer(unicode, 
                         lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:str', value))

    print yaml.dump(s.outputs,
                    default_flow_style=False)

if __name__ == '__main__':
    main()

