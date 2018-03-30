from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized, Dbg
from lib.args import Arguments

__app_name = Properties.get('app_name')

main_desc = """Tests connection to daemon 
Options:
    
    default         - Run default action 
    test            - Run action named 'test'

    --help          - This message 

Example:
    %s test

""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or argv[0] == '--help':
        print(main_desc)
        return False

    if argv[0] != 'default' and argv[0] != 'test':
        Colorized.red("Unknown action '%s'" % argv[0])
        return False

    action = None if argv[0] != 'test' else 'test'

    from lib.Daemon.Client.test import Test

    with Test() as client:
        Colorized.green(str(client.action(action)))
