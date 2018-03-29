

class Controller:
    def __init__(self, data):
        self.data = data

    def process(self):
        return self

    def response(self):
        return "Recieved : %s\n" % self.data
