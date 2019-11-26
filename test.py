import subprocess
import string
pwd='1'
cmd='ls'
#Permission
# subprocess.run('echo 1 | sudo -S ls', shell=True,universal_newlines=True)
# subprocess.run('sudo killall triage',shell=True)
# subprocess.call('./abc.sh')
subprocess.call('./abc.sh hoi',shell=True)


