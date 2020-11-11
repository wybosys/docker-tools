#!/usr/bin/env python3

import os
import docker
import sys

all = docker.cmd('image ls')

for each in all:
    data = each.split(' ')
    id = data[0]
    print('删除' + id)
    docker.cmd('image rm ' + id)
