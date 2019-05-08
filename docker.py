import subprocess

def cmd(str, lines = True):
    res = subprocess.getoutput('docker ' + str)
    if not lines:
        return res
    return res.split('\n')[1:]
