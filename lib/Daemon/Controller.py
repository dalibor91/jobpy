import json
import importlib

class Controller:
    def __init__(self, data):
        self.data = data

    def _err_(self, msg):
        return "%s\n" % json.dumps({ "error": True, "msg": msg })

    def _ok_(self, data = None):
        return "%s\n" % json.dumps({ "error" : False, "data": data })

    def process(self):
        try:
            data = json.loads(self.data)

            if ('ctrl' in data) and ('data' in data):

                controller = "Daemon%s" % str(data['ctrl']).title()
                action = ('action_%s' % str(data['action'])) if 'action' in data else 'default'
                data = data['data']

                try:
                    m = importlib.import_module('lib.Daemon.Controllers.%s' % controller)

                    mod = getattr(m, controller)(data)
                    if not hasattr(mod, action):
                        raise Exception("not found")

                    a = getattr(mod, action)

                    return self._ok_(a())

                except Exception as e:
                    return self._err_(str(e))

                return self._err("module %s action %s not found" % (controller, action))

            return self._err_("invalid format sent")

        except Exception as e:
            return self._err_(str(e))

        return self._err_("unable to parse")


    def response(self):
        return self.process()
