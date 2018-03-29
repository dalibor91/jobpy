from configparser import ConfigParser
from os import path
from shutil import copy

class Properties:
    def __init__(self):
        raise Error("Can not have instance")

    @staticmethod
    def __data(name=None, val=None):
        if not hasattr(Properties, 'runtime_data'):
            setattr(Properties, 'runtime_data', dict())

        if name is not None:
            Properties.runtime_data[name] = val

        return Properties.runtime_data

    @staticmethod
    def has(name):
        return True if name in Properties.__data() else False

    @staticmethod
    def set(name, val):
        Properties.__data(name, val)

    @staticmethod
    def get(name):
        if Properties.has(name):
            return Properties.__data()[name]
        return None

    @staticmethod
    def data():
        return Properties.__data()


class ConfigFile:
    def __init__(self):
        raise Error("Can not have instance")

    @staticmethod
    def get(section, name):
        return ConfigFile.__get_ini().get(section, name)

    @staticmethod
    def data():
        return ConfigFile.__get_ini()

    @staticmethod
    def __get_ini():
        if hasattr(ConfigFile, 'ini_data'):
            return getattr(ConfigFile, 'ini_data')

        if not path.isfile(Properties.get('config_file')):
            copy(Properties.get('default_config'), Properties.get('config_file'))

        setattr(ConfigFile, 'ini_data', ConfigParser())
        ConfigFile.ini_data.read(Properties.get('config_file'))

        return getattr(ConfigFile, 'ini_data')







