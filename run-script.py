#!/usr/bin/env python3

import os, docker, sys

all = docker.cmd('ps -a')
script = sys.argv[1]

for each in all:
    data = each.split(' ')
    id = data[0]
    print('执行' + id)
    docker.cmd('cp ' + script + ' ' + id + ':/root/tmp_script')
    docker.cmd('exec -ti ' + id + ' /root/tmp_script')
    docker.cmd('exec -ti ' + id + ' rm /root/tmp_script')
