import time
from lib.Helpers import Config


class Scheduler:
    def __init__(self):
        pass

    def start(self):
        check_interval = Config.get('scheduler', 'check_interval')
        while True:
            time.sleep(int(check_interval) if int(check_interval) > 5 else 5)
