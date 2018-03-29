"""
{"ctrl":"test","data":null}
"""

class DaemonTest:
    def __init__(self, data):
        self.data = data

    def default(self):
        return "default data"

    def action_test(self):
        return "action_test data"
