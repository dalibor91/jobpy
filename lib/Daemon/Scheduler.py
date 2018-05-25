import time
import datetime
from lib.Helpers import Config
from lib.Daemon.Client.job import Job
from lib.Database.Connection import Connection


class Scheduler:

    db_connection = None

    def __init__(self):
        pass

    def start(self):
        check_interval = Config.get('scheduler', 'check_interval')
        self.runing_time_total = 0
        self.runing_time = 0
        self.sleep_time  = int(check_interval) if int(check_interval) > 5 else 5
        while True:
            time.sleep(self.sleep_time)
            self.runing_time_total += self.sleep_time
            self.runing_time += self.sleep_time

            with Job() as jobCli:
                jobs = jobCli.action('list', 'active')
                for job_name in jobs.split("\n"):
                    #check last run
                    #check how often should run
                    #get last status
                    #if it failed use fail retry
                    print("[%s] Run %s" % (str(datetime.datetime.now()), job_name))
                    #jobCli.action('run', job_name)

