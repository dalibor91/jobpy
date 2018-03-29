from lib.Helpers import Config, Properties
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:

    __sqlite_engine = None

    def __init__(self):
        self.database = Config.get('database', 'database')
        self.type = Config.get('database', 'type')


    def get_engine(self, cached=True):
        if self.type == 'sqlite':
            if self.__sqlite_engine is None:
                self.__sqlite_engine = self.__get_sqlite()
            return self.__sqlite_engine if cached else self.__get_sqlite()


    def get_sesson(self, cached=True):
        return sessionmaker(bind=self.get_engine(cached))


    def __logging(self):
        return Properties.get('log_level') == 'log'


    def __get_sqlite(self):
        return create_engine('sqlite://%s'%self.database, echo=self.__logging())