import sys
import os
import datetime
from daemonize import Daemonize
from lib.Helpers import Properties
from lib.Daemon.Container.Job.Runner import Runner


def new_container(name):
    #need to implement reaper
    #that will reap zombies created
    #like this
    if os.fork() == 0:
        app_name = "name_%s" % str(datetime.datetime.now().strftime('%s'))
        lock_dir = "%s/%s" % (Properties.get('lock_dir'), name)
        log_file = "%s/%s/%s" % (Properties.get('log_dir'), name, datetime.datetime.now().strftime("%Y/%m/%d/%H_%M_%S.log"))

        if not os.path.isdir(lock_dir):
            os.mkdir(lock_dir)

        if not os.path.isdir(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))

        for pid in range(1, 1024):
            if not os.path.exists("%s/%d.pid" % (lock_dir, pid)):
                break

        app_pid = "%s/%d.pid" % (lock_dir, pid)

        runner = Runner(name, app_pid, log_file)
        runner.run()
        sys.exit(0)


