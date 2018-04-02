from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized

__app_name = Properties.get('app_name')

main_desc = """Lists all jobs  
Options:
    --all       - All jobs
    --active    - Stops daemon
    --inactive  - Restarts daemon

Example:
    %s list
""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or (argv[0] == '--help'):
        print(main_desc)
        return False

    from lib.Daemon.Client.job import Job

    try:

        type = 'all'
        if argv[0] == '--inactive':
            type = 'inactive'
        elif argv[0] == '--active':
            type = 'active'

        with Job() as client:
            response = client.action('list', type)
            if response:
                Colorized.green(response)

    except Exception as e:
        Colorized.red(str(e))
