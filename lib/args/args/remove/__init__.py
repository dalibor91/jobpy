from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized, Dbg
from lib.args import Arguments

__app_name = Properties.get('app_name')

main_desc = """Removes jobs from scheduler 
Options:
    --name          - Name of job   - REQUIRED
    --help          - This message

Example:
    %s property remove --name test
    
""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or argv[0] == '--help':
        print(main_desc)
        return False

    ar = Arguments(argv)

    if not ar.has('name'):
        Colorized.red("Name of job is missing")
        return False

    Dbg.log("Remove job")