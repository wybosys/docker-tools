#!/usr/bin/env python3

import os, docker, sys

all = docker.cmd('ps -a')
script = sys.argv[1]

for each in all:
    data = each.split(' ')
    id = data[0]
    print('删除' + id)
    docker.cmd('rm -f ' + script + ' ' + id)
