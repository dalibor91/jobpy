from lib.Helpers import Dbg


class Entity():
    def __init__(self, con):
        self.con = con;
        self.data = {}

    def get_table_name(self):
        return 'table';

    def set(self, name, val):
        self.data[name] = val;

    def get(self, name):
        if name in self.data:
            return self.data[name]
        return None

    def getdata(self):
        return self.data

    def getLastInsertId(self):
        c = self.con.cursor()
        Dbg.log("SELECT last_insert_rowid() as id")
        c.execute("SELECT last_insert_rowid() as id")
        u = c.fetchone()
        c.close()
        return u['id'] if 'id' in u else None

    def fetchBy(self, name, val):
        c = self.con.cursor()
        Dbg.log("SELECT * FROM %s WHERE %s = ?" % (self.get_table_name(), name))
        Dbg.log("%s = %s" % (name, val))
        c.execute("SELECT * FROM %s WHERE %s = ?" % (self.get_table_name(), name), (val,))
        u = c.fetchone()
        if u is None:
            u = {}
        c.close();
        return u

    def fetch(self, _id):
        self.data = self.fetchBy('id', _id)
        return self.data

    def delete(self, id=None):
        if id is None:
            id = self.get('id')
        c = self.con.cursor()
        Dbg.log("DELETE FROM %s WHERE id = %d" % (self.get_table_name(), int(id)))
        Dbg.log("id = %d" % int(id))
        c.execute("DELETE FROM %s WHERE id = %d" % (self.get_table_name(), int(id)))
        self.data = c.fetchone()
        c.close();
        self.con.commit()
        return self.data

    def update(self):
        q = "UPDATE %s SET " % self.get_table_name()
        up = ""
        param = ()
        for name, value in self.data.items():
            up = "%s, %s = ?" % (up, name)
            param = param + (value,)

        param = param + (self.data['id'],)
        c = self.con.cursor()
        # debug
        Dbg.log("%s %s WHERE id = ?" % (q, up[2:]))
        Dbg.log(str(param))
        c.execute("%s %s WHERE id = ?" % (q, up[2:]), param)
        self.con.commit()
        c.close()

    def save(self):
        q = "INSERT INTO %s " % self.get_table_name()
        param = ()
        columns = ""
        values = ""
        for name, value in self.data.items():
            columns = "%s, %s" % (columns, name)
            values = "%s, ?" % values
            param = param + (value,)

        c = self.con.cursor()
        Dbg.log("%s (%s) VALUES (%s)" % (q, columns[2:], values[2:]))
        Dbg.log(str(param))
        c.execute("%s (%s) VALUES (%s)" % (q, columns[2:], values[2:]), param)
        self.con.commit()
        c.close();

    def all(self):
        c = self.con.cursor()
        Dbg.log("SELECT * FROM %s" % self.get_table_name())
        c.execute("SELECT * FROM %s" % self.get_table_name())
        return c.fetchall()

class Log(Entity):
    def get_table_name(self):
        return 'job_log'

    def last_status(self, status):
        c = self.con.cursor()
        c.execute("select * FROM %s WHERE status = '%s' ORDER BY created_at DESC LIMIT 1;" % (self.get_table_name(), status))

        for i in c.fetchall():
            return i['created_at']

        return None
