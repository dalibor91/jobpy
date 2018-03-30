import os
import sys
from signal import SIGINT
from daemonize import Daemonize
from lib.Helpers import Properties, Config, Colorized
from lib.Daemon.Controller import Controller

def __handler__(data, client, address):
    cmd = Controller(data)
    client.send(cmd.response().encode('utf-8'))

def __daemon__():
    import lib.Daemon.Server as Server
    srv = Server.Server(Properties.get('socket_file'))
    srv.setCallback(__handler__)
    srv.listen()

def __scheduler__():
    from lib.Daemon.Scheduler import Scheduler
    sch = Scheduler()
    sch.start()

def start_daemon():

    pid_file = Config.get('default', 'daemon_pid_file')
    scheduler_pid = Config.get('default', 'scheduler_pid_file')

    if os.path.isfile(pid_file):
        Colorized.red("Daemon pid file exists: %s" %pid_file)
        return False

    if os.path.isfile(scheduler_pid):
        Colorized.red("Scheduler pid file exists: %s" % scheduler_pid)
        return False

    pid = os.fork()
    if pid == 0:
        Colorized.green("Start daemon...")
        Config.reload()

        app_name = "daemon_%s" % Properties.get('app_name')

        Daemonize(
            app=app_name,
            pid=pid_file,
            action=__daemon__,
            keep_fds = []
        ).start()
        sys.exit(0)
    else:
        if os.fork() == 0:
            Colorized.green("Start scheduler...")
            Config.reload()

            app_name = "scheduler_%s" % Properties.get('app_name')

            Daemonize(
                app=app_name,
                pid=scheduler_pid,
                action=__daemon__,
                keep_fds = []#,
                #verbose = True,
                #foreground = True
            ).start()
            sys.exit(0)

    return True

def stop_daemon():
    pid_file = Config.get('default', 'daemon_pid_file')
    scheduler_pid = Config.get('default', 'scheduler_pid_file')

    if not os.path.isfile(pid_file):
        Colorized.red("Daemon pid file not found")
    else:
        try :
            with open(pid_file) as f:
                pid = (f.read())
                os.kill(int(pid.strip()), SIGINT)
        except Exception as e:
            Colorized.red(str(e))

    if not os.path.isfile(scheduler_pid):
        Colorized.red("Scheduler pid file not found")
    else:
        try :
            with open(scheduler_pid) as f:
                pid = (f.read())
                os.kill(int(pid.strip()), SIGINT)
        except Exception as e:
            Colorized.red(str(e))

def restart_daemon():
    stop_daemon()
    start_daemon()

def print_status():
    pid_file = Config.get('default', 'daemon_pid_file')
    scheduler_pid = Config.get('default', 'scheduler_pid_file')

    if not os.path.isfile(pid_file):
        Colorized.red("Daemon    : FAIL")
    else:
        try :
            with open(pid_file) as f:
                pid = (f.read())
                os.kill(int(pid.strip()), 0)
                Colorized.green("Daemon    : OK")
        except Exception as e:
            Colorized.red("Daemon    : FAIL")

    if not os.path.isfile(scheduler_pid):
        Colorized.red("Scheduler : FAIL")
    else:
        try :
            with open(scheduler_pid) as f:
                pid = (f.read())
                os.kill(int(pid.strip()), 0)
                Colorized.green("Scheduler : OK")
        except Exception as e:
            Colorized.red("Scheduler : FAIL")





