import importlib
from lib.Helpers.Dbg import Colorized

def process_args(argv):
    import_module = 'help'
    if len(argv) > 0:
        import_module = argv[0]

    try:
        mdl = importlib.import_module('lib.args.args.%s' % str(import_module))
    except:
        mdl = importlib.import_module('lib.args.args.help')
        if len(argv) > 0:
            Colorized.red("Unknown command '%s'" % " ".join(argv))
    mdl.process(argv[1:])


class __Property:
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
        data = self.get_value().split('=', 1)
        if len(data) != 2:
            raise Error("Can not get subproperty")

        p.set_name(data[0])
        p.set_value(data[1])
        return p


class Arguments:
    def __init__(self, data):
        self.argv = data

    def get_property(self, name, prefix='--'):
        found = False
        for arg in self.argv:
            if found:
                return __Property(arg, name)
            if ("%s%s"%(prefix,name)) == ("%s%s"%(prefix,arg)):
                found = True

    def get_property_arr(self, name, prefix='--'):
        found = []
        _found = False
        for arg in self.argv:
            if _found:
                found.append(__Property(arg, name))
                _found = False
                continue
            if ("%s%s"%(prefix,name)) == ("%s%s"%(prefix,arg)):
                found = True

        return found