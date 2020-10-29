#!/usr/bin/env python3

import os, docker, json

all = docker.cmd('ps -a')
runs = []
rms = []

for each in all:
    data = each.split(' ')
    id = data[0]
    name = data[len(data) - 1]

    jsobj = json.loads(docker.cmd('inspect ' + id, False))[0]
    config = jsobj['Config']
    network = jsobj['NetworkSettings']
    ports = network['Ports']
    mounts = jsobj['Mounts']

    run = ['docker run -dti']
    rm = ['\n# ' + name + '\n', 'docker rm -f']

    run.append('-h ' + name)
    run.append('--name ' + name)
    rm.append(id)

    for key in ports:
        cfg = ports[key]
        if cfg:
            cfg = cfg[0]
            run.append('-p ' + cfg['HostIp'] + ':' + str(cfg['HostPort']) + ':' + key)

    for mount in mounts:
        typ = mount['Type']
        if typ == 'volume':
            continue
        if typ == 'bind':
            run.append('-v ' + mount['Source'] + ':' + mount['Destination'])
            continue
        raise Exception('No support mount type ' + mount['Type'])

    if 'Networks' in network:
        net = network['Networks']
        if 'internal' in net:
            nid = net['internal']['NetworkID']
            netobj = json.loads(docker.cmd('network inspect ' + nid, False))[0]
            run.append('--network ' + netobj['Name'])

    run.append(config['Image'])

    rms.append(' '.join(rm))
    runs.append(' '.join(run))

print(runs)
open('run-containers', 'w').write('\n'.join(runs))
open('remove-containers', 'w').write('\n'.join(rms))
            
