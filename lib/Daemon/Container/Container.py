import os


class Container:

    data = {
        "stdin" : os.devnull,
        "stdout" : os.devnull,
        "stderr" : os.devnull,
        "envvars": [],
        "pidfile": None,
        "homedir": "."
    }

    name = 'container'

    def __init__(self, name):
        self.name = name

    def set_stdin(self, stdin):
        self.data['stdin'] = stdin;
        return self

    def set_stdout(self, stdout):
        self.data['stdout'] = stdout
        return self

    def set_stderr(self, stderr):
        self.data['stderr'] = stderr
        return self

    def set_envvar(self, name, val):
        self.data['envvars'].append([name, val])
        return self

    def set_pidfile(self, pfile):
        self.data['pidfile'] = pfile

    def set_homedir(self, homedir):
        self.data['homedir'] = homedir
        return self

    def run(self):
        pass