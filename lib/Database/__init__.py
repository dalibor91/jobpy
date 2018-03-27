from os import path
from os import listdir
from lib.Helpers.Dbg import Dbg
from lib.Helpers.Properties import Properties

def check_database(config):
    Dbg.log("Checking database")
    if config.get('database', 'type') == 'sqlite':
        Dbg.log("Database sqlite")
        if path.isfile(config.get('database', 'database')):
            Dbg.log("Database found '%s'" % config.get('database', 'database'))
        else:
            __create_sqlite(config.get('database', 'database'))


def __create_sqlite(path):
    import sqlite3

    conn = sqlite3.connect(path)
    database_dir = "%s/sqlite" % Properties.get('database_dir')

    for file in listdir("%s/table"%database_dir):
        Dbg.log("Create table %s" % file)
        with open("%s/table/%s" %(database_dir, file), 'r') as tbl_read:
           cursor = conn.cursor()
           cursor.execute(tbl_read.read())
           cursor.close()

    for file in listdir("%s/index" % database_dir):
        Dbg.log("Create index %s" % file)
        with open("%s/index/%s" % (database_dir, file), 'r') as tbl_read:
            cursor = conn.cursor()
            cursor.execute(tbl_read.read())
            cursor.close()

