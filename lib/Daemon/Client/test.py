from lib.Daemon.Client import Client

class Test(Client):
    def action(self, action=None):
        return super(Test, self).request(self._build_(action))

    def _build_(self, action=None, data=None):
        return super(Test, self)._build_('test', action, data)