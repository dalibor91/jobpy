from lib.Helpers.Properties import Properties
from lib.Helpers.Dbg import Colorized, Dbg
from lib.args import Arguments

__app_name = Properties.get('app_name')

main_desc = """Managers properties for jobs 
Options:
    add         (--name <name>)  - Add job
    remove      (--name <name>)  - Remove job 
    activate    (--name <name>)  - Activate job 
    deactivate  (--name <name>)  - Deactivate job
    run         (--name <name>)  - Run job 
    
    --help            - This message

Example:
    %s job add        --name test_job
       job remove     --name test_job
       job activate   --name test1
       job deactivate --name test1 
""".strip() % __app_name


def process(argv):
    if len(argv) == 0 or (argv[0] == '--help'):
        print(main_desc)
        return False

    ar = Arguments(argv[1:])

    if not ar.has("name"):
        Colorized.red("Name of job is missing")
        return False

    try:

        from lib.Daemon.Client.job import Job

        with Job() as client:
            action = None
            if argv[0] == 'add':
                action = 'new'
            elif argv[0] == 'remove':
                action = 'delete'
            elif argv[0] == 'activate':
                action = 'activate'
            elif argv[0] == 'deactivate':
                action = 'deactivate'
            elif argv[0] == 'run':
                action = 'run'
            else:
                raise Exception("Unknown command")

            p = ar.get_property('name')
            response = client.action(action, p.get_value())

            if response:
                Colorized.green(response)

    except Exception as e:
        Colorized.red(str(e))
