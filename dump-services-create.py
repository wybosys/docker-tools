#!/usr/bin/env python3

import os, docker, json

all = docker.cmd('service ls')
runs = []
rms = []

for each in all:
    data = list(filter(lambda e: e != '', each.split(' ')))
    id = data[0]
    repl = data[3].split('/')[1]
    image = data[4]

    jsobj = json.loads(docker.cmd('service inspect ' + id, False))[0]
    spec = jsobj['Spec']['TaskTemplate']
    network = spec['Networks'][0]

    run = ['docker service create ']
    rm = ['docker service rm']

    rm.append(id)

    for each in spec['Placement']['Constraints']:
        run.append('--constraint "' + each + '"')

    net = json.loads(docker.cmd('network inspect ' + network['Target'], False))[0]
    run.append('--network ' + net['Name'])
    run.append('--replicas ' + repl)
    run.append(image)

    rms.append(' '.join(rm))
    runs.append(' '.join(run))

print(runs)
open('run-services', 'w').write('\n'.join(runs))
open('remove-services', 'w').write('\n'.join(rms))
