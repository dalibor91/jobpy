import os
from signal import SIGINT
from daemonize import Daemonize
from lib.Helpers import Properties, Config, Colorized
from lib.Daemon.Controller import Controller

def __handler__(data, client, address):
    cmd = Controller(data)
    client.send(cmd.response().encode('utf-8'))

def __daemon__():
    import lib.Daemon.Server as Server
    srv = Server.Server(Config.get('default', 'socket_file'))
    srv.setCallback(__handler__)
    srv.listen()

def start_daemon():

    pid_file = Config.get('default', 'pid_file')

    if os.path.isfile(pid_file):
        Colorized.red("Pid file exists: %s" %pid_file)
        return False

    Daemonize(
        app=Properties.get('app_name'),
        pid=Config.get('default', 'pid_file'),
        action=__daemon__,
        keep_fds = [
            Properties.get('config_file')
        ]#,
        #verbose = True,
        #foreground = True
    ).start()

    return True

def stop_daemon():
    pid_file = Config.get('default', 'pid_file')
    if not os.path.isfile(pid_file):
        Colorized.red("Pid file not found")
        return False
    try :
        with open(pid_file) as f:
            pid = (f.read())
            os.kill(int(pid.strip()), SIGINT)
    except Exception as e:
        Colorized.red(str(e))


def restart_daemon():
    stop_daemon()
    start_daemon()

def print_status():
    pid_file = Config.get('default', 'pid_file')

    if not os.path.isfile(pid_file):
        Colorized.red("Not running")
        return False
    try :
        with open(pid_file) as f:
            pid = (f.read())
            os.kill(int(pid.strip()), 0)
            Colorized.green("Running")
    except Exception as e:
        Colorized.red("Not running")





