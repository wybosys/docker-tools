#!/usr/bin/env python3

import os
import docker
import sys

docker.cmd('container prune -f')
all = docker.cmd('image ls')

for each in all:
    data = list(filter(lambda e: e != '', each.split(' ')))
    name = data[0]
    id = data[2]
    print('删除' + name)
    docker.cmd('image rm ' + id)
