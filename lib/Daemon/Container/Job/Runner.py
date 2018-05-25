import subprocess
import os

from lib.Helpers.Properties import Properties
from lib.Daemon.Container.Job import Job
from lib.Daemon.Container.Job import Status

class Runner():
    def __init__(self, job, pid_file, log_file):
        self.job = Job.Job(job)
        self.pid_file = pid_file
        self.log_file = log_file
        self.shell = Properties.get("shell")
        self.run_script = "%s/%s/%s.sh" % (Properties.get("runner_dir"), job, os.getpid())

        if not os.path.exists(os.path.dirname(self.run_script)):
            os.makedirs(os.path.dirname(self.run_script))

    def run(self):
        try:
            self.job.db().status(Status.STARTED)
            with open(self.run_script, 'w') as f:
                f.write(self.job.config('command').strip())

            p = subprocess.Popen(["%s %s" % (self.shell, self.run_script)], shell=True, bufsize=1024*1024*20, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)

            p.wait()
            out, err = p.communicate()
            self.job.db().status(Status.FINISHED if p.returncode == 0 else Status.FAILED)

            with open(self.log_file, "w") as log:
                log.write(out.decode('utf-8') if out is not None else "")
                log.write(err.decode('utf-8') if err is not None else "")
        except Exception:
            self.job.db().status(Status.FAILED)

        os.unlink(self.run_script)