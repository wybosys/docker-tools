#!/usr/bin/env python3

import os, sys

dir = sys.argv[1]

for each in os.listdir(dir):
    json = dir + '/' + each + '/' + each + '-json.log'
    if os.path.isfile(json):
        print('清理 ' + json)
        os.system('truncate -s 0 ' + json)
