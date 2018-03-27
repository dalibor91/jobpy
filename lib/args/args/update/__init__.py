from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized, Dbg
from lib.args import Arguments


__app_name = Properties.get('app_name')

main_desc = """Updates jobs in scheduler 
Options:
    --name          - Name of job       - REQUIRED 
    
    --property      - Adds property
    --del_property  - Removes property 
    --field         - Updates field

Example:
    %s property update --field name="test_1234" --property email_on_fail=dalibor.menkovic@gmail.com
    
""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or argv[0] == '--help':
        print(main_desc)
        return False

    ar = Arguments(argv)

    if not ar.has('name'):
        Colorized.red("Name of job is missing")
        return False



