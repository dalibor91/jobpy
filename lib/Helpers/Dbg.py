from lib.Helpers.Properties import Properties


class Dbg:
    def __init__(self):
        pass

    @staticmethod
    def log(msg):
        if Properties.get('log_level') == 'INFO' or Properties.get('log_level') == 'DEBUG' :
            print("[ INFO  ] %s" % str(msg))

    @staticmethod
    def err(msg):
        if Properties.get('log_level') == 'ERROR':
            print("[ ERROR ] %s" % str(msg))

    @staticmethod
    def dbg(msg):
        if Properties.get('log_level') == 'DEBUG':
            print("[ DEBUG ] %s" % str(msg))


class Colorized:
    def __init__(self):
        pass

    @staticmethod
    def red(msg):
        print("\u001b[31m%s\u001b[0m" % msg)

    @staticmethod
    def green(msg):
        print("\u001b[32m%s\u001b[0m" % msg)
