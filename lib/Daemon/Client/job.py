from lib.Daemon.Client import Client

class Job(Client):
    def action(self, action=None, data=None):
        return super(Job, self).request(self._build_(action, data))

    def _build_(self, action=None, data=None):
        return super(Job, self)._build_('job', action, data)