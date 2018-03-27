from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized, Dbg
from lib.args import Arguments

__app_name = Properties.get('app_name')

main_desc = """Managers properties for jobs 
Options:
    add             - Name of property   - REQUIRED
    remove          - Remove property    - REQUIRED
    --name          - Name of property   - REQUIRED
    
    --value         - Default value 
    --help          - This message

Example:
    %s property add --name test --value "/bin/bash /tmp/test1.sh"
""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or (argv[0] == '--help'):
        print(main_desc)
        return False

    if argv[0] == 'add':
        ar = Arguments(argv[1:])

        if not ar.has("name"):
            Colorized.red("Name of property is missing")
            return False

        Dbg.log("Adding new property")

    elif argv[0] == 'remove':

        ar = Arguments(argv[1:])
        if not ar.has("name"):
            Colorized.red("Name of property is missing")
            return False

        Dbg.log("Removing property")

    else:
        Colorized.red("Unknown command.")
        print(main_desc)
        return False