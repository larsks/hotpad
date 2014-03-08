from __future__ import absolute_import

import logging
import argparse

from hotpad.keystone import Keystone

def create_parser():
    '''Default command line parser for hotpad commands.  Includes
    all the openstack credential options.'''

    p = argparse.ArgumentParser()

    p.add_argument('--debug', action='store_const',
                   dest='loglevel', const=logging.DEBUG)
    p.add_argument('--quiet', action='store_const',
                   dest='loglevel', const=logging.WARN)
    p.add_argument('--os-username')
    p.add_argument('--os-tenant-name')
    p.add_argument('--os-tenant-id')
    p.add_argument('--os-password')
    p.add_argument('--os-auth-url')
    p.add_argument('--os-region-name')

    p.set_defaults(loglevel=logging.INFO)

    return p

def setup_logging(args):
    '''Set up logging at the appropriate log level
    as determined by command line options.'''

    logging.basicConfig(
        level = args.loglevel)

def get_ksclient(args):
    '''Return a Keystone object based on the current credentials.'''
    return Keystone(
        auth_url=args.os_auth_url,
        tenant_name=args.os_tenant_name,
        tenant_id=args.os_tenant_id,
        username=args.os_username,
        password=args.os_password,
        region_name=args.os_region_name,
        )

