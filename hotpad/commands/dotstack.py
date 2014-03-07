#!/usr/bin/python

import sys
import yaml
import colorsys

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
    p.add_argument('--output', '-o')

    p.add_argument('stack')

    return p.parse_args()

def make_hex_color(c):
    return '#{:02x}{:02x}{:02x}'.format(*(int(255*x) for x in c))

def output_dot(s):
    nodes = []
    edges = []
    restypes = {}

    for r in s.resources:
        nodes.append((r.resource_name, r.resource_type))
        restypes[r.resource_type] = None
        for req in r.required_by:
            edges.append((r.resource_name, req))

    HSV_tuples = [(x*1.0/len(restypes), 0.8, 0.8) for x in range(len(restypes))]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    colors = iter(RGB_tuples)

    for k in restypes.keys():
        restypes[k] = make_hex_color(next(colors))

    print 'digraph {'
    print 'rankdir=LR;'
    for n in sorted(nodes, key=lambda x: x[1]):
        print '%s [color="%s", style=filled];' % (n[0], restypes[n[1]])
    print
    for a,b in edges:
        print '%s -> %s;' % (a,b)

    print '}'

def main():
    args = parse_args()
    setup_logging(args)

    ks = get_ksclient(args)
    s = Stack(args.stack, ksclient=ks)

    with open(args.output, 'w') if args.output else sys.stdout as fd:
        sys.stdout = fd
        output_dot(s)

if __name__ == '__main__':
    main()

