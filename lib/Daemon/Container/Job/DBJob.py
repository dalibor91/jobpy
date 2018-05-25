import lib.Database.Connection as Conn
from lib.Database.Entity import Log

class DBJob:
    def __init__(self, uid):
        self.connection = Conn.Connection()
        self.uid = uid

    def status(self, status):
        log = Log(self.connection.getConnection())
        log.set('uid', self.uid)
        log.set('status', status)
        log.save()

    def last_status(self, status):
        log = Log(self.connection.getConnection())
        return log.last_status(status)

    def close(self):
        self.connection.close()