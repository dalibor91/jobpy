import os
import yaml
from lib.Helpers.Properties import Properties

class Job:
    data = {
        "stdin" : os.devnull,
        "stdout" : os.devnull,
        "stderr" : os.devnull,
        "envvars": [],
        "pidfile": None,
        "homedir": "."
    }

    name = 'container'

    __yaml_data     = None
    __yaml_data__   = None

    def __init__(self, name):
        file_dest = "%s/%s.yml" %(Properties.get('jobs_dir'), name)

        if not os.path.exists(file_dest):
            raise Exception("Job file %s does not exists " % job_dest)

        with open(file_dest, 'r') as yml_read:
            self.__yaml_data = yml_read.read()

    def __yaml(self):
        if self.__yaml_data__ is None:
            self.__yaml_data__ = yaml.load(self.__yaml_data)
        return self.__yaml_data__

    def config(self, name):
        return self.__yaml()[name]

    def attribute(self, name):
        return self.config('attributes')[name]

