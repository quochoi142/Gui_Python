import subprocess as sp
import string
p=sp.run('echo 1 | sudo -S echo 1', shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
print(p.stderr)
print(p.stdout)
