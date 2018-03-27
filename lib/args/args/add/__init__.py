from lib.Helpers.Properties import Properties
from lib.args import Arguments
from lib.Helpers.Dbg import Colorized, Dbg

__app_name = Properties.get('app_name')

main_desc="""Adds new job to scheduler 
Options:
    --name          - Name of job        - REQUIRED
    --run           - When to run        - REQUIRED
    --user          - Run as user        - REQUIRED
    
    --property      - Add property
    --desc          - Set description
    --help          - Show this message 
    
Example:
    %s add --name "test_job" \
    --run "* * * * *" \
    --property on_fail="echo 'test' | mail -s 'test' dalibor@dalibor.me" \
    --property email_fail=dalibor@dalibor.me
""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or (argv[0] == '--help'):
        print(main_desc)
        return False

    args = Arguments(argv)

    if not args.has(set(["name", "run", "user"])):
        Colorized.red("Some of parameters are missing!")
        return False

    name = args.get_property('name')
    run = args.get_property('run')
    user = args.get_property('user')
    property = args.get_property_arr('property')

    Dbg.log("Adding new job")
    Dbg.log("Name    : %s" % name.get_value())
    Dbg.log("Run     : %s" % run.get_value())
    Dbg.log("User    : %s" % user.get_value())

    for p in property:
        Dbg.log("Attr    : %s" % p.get_value())
