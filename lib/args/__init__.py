import importlib
from lib.Helpers.Dbg import Colorized, Dbg

def process_args(argv):
    import_module = 'help'
    if len(argv) > 0:
        import_module = argv[0]

    try:
        mdl = importlib.import_module('lib.args.args.%s' % str(import_module))
    except Exception as e:
        mdl = importlib.import_module('lib.args.args.help')
        if len(argv) > 0:
            Colorized.red("Unknown command '%s'" % " ".join(argv))
        Dbg.err(str(e))
    mdl.process(argv[1:])


class __Property__:
    def __init__(self, val, name=None):
        self.value = val
        self.name = name

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def set_value(self, v):
        self.value = v
        return self

    def set_name(self, n):
        self.name = name
        return self

    def get_subproperty(self, char='='):
        p = Property()
        data = self.get_value().split(char, 1)
        if len(data) != 2:
            raise Error("Can not get subproperty")

        p.set_name(data[0])
        p.set_value(data[1])
        return p


class Arguments:
    def __init__(self, data):
        self.argv = data

    def has(self, c):
        '''
        Check if arguments have this parameters
        :param c: list or one paramentr
        :return: boolean True or False
        '''
        if isinstance(c, str):
            return True if self.get_property(c) is not None else None
        elif isinstance(c, set):
            for item in c:
                if self.get_property(item) is None:
                    return False
            return True
        return False

    def get_property(self, name, prefix='--'):
        found = False
        for arg in self.argv:
            if found:
                return __Property__(arg, name)
            if ("%s%s"%(prefix,name)) == arg:
                found = True
        return None

    def get_property_arr(self, name, prefix='--'):
        found = []
        _found = False
        for arg in self.argv:
            if _found:
                found.append(__Property__(arg, name))
                _found = False
                continue
            if ("%s%s"%(prefix,name)) == arg:
                _found = True

        return found