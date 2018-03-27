
class Dbg:
    def __init__(self):
        pass

    @staticmethod
    def log(msg):
        print("[ LOG ] %s" % str(msg))

    @staticmethod
    def err(msg):
        print("[ ERROR ] %s" % str(msg))

    @staticmethod
    def dbg(msg):
        print("[ DEBUG ] %s" % str(msg))


class Colorized:
    def __init__(self):
        pass

    @staticmethod
    def red(msg):
        print("\u001b[31m%s\u001b[0m" % msg)
