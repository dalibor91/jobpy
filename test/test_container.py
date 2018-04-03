import sys, os, time
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import main
from lib.Daemon.Container import new_container

new_container('test')
