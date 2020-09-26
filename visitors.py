#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(description='get visitor details from access logs by piping output into visitors.', usage='gunzip -c access.log.1.gz | visitors -i -c')
parser.add_argument("-c", "--count", help="print amount of unique visitors", action="store_true")
parser.add_argument("-i", "--ip", help="print unique ips", action="store_true")
parser.add_argument("-s", "--sites", help="print visited sites", action="store_true")

args = parser.parse_args()

input = sys.stdin
ips = []
req = []

for line in input:
    fields = line.strip().split()

    ip = fields[0]
    requested = fields[6]
    status_code = fields[8]

    if status_code == "200":
        if not ".svg" or ".img" or ".png" or ".css" in requested:
            if requested != "*":
                if ip not in ips:
                    ips.append(ip)
                    req.append(requested)

if args.sites:
    print '\n'.join(req)

if args.ip:
    print '\n'.join(ips)

if args.count:
    print len(ips)
