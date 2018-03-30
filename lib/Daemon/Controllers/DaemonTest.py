"""
{"ctrl":"test","data":null}
"""
from datetime import datetime

class DaemonTest:
    def __init__(self, data):
        self.data = data

    def default(self):
        return "[ %s ] You called 'default' action in daemon." % str(datetime.now())

    def action_test(self):
        return "[ %s ] You called 'action_test' action in daemon" % str(datetime.now())
