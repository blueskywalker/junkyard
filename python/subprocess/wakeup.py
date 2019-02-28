
import subprocess

p=subprocess.Popen(['python','lazy_hello.py'])
print p.pid
status = p.wait()
print status

