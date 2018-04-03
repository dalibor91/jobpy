import sys, os, time
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import main
from lib.Daemon.Container import new_container


for i in range(1, 20):
    print("Container: %d" % i)
    new_container('test')
    time.sleep(1)
