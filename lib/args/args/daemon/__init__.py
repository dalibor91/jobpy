from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized, Dbg
import lib.Daemon as Daemon

__app_name = Properties.get('app_name')

main_desc = """Manages daemon 
Options:
    start       - Starts daemon
    stop        - Stops daemon
    restart     - Restarts daemon
    status      - Status of daemon
    
    --help      - This message 

Example:
    %s restart
""".strip() % __app_name


def process(argv):

    if len(argv) == 0 or (argv[0] == '--help'):
        print(main_desc)
        return False

    try:
        if argv[0] == "start":
            Daemon.start_daemon()
        elif argv[0] == "stop":
            Daemon.stop_daemon()
        elif argv[0] == "restart":
            Daemon.restart_daemon()
        elif argv[0] == "status":
            Daemon.print_status()
        else:
            Colorized.red("Unknown command '%s'" % str(argv[0]))

    except Exception as e:
        print(str(e))
        Colorized.red("There is an error")
        Dbg.err(str(e))
    return True