from lib.Helpers.Properties import Properties

__app_name = Properties.get('app_name')

main_desc = """Removes jobs from scheduler 
Options:
    --name          - Name of job 
    --id            - Job id

Example:
    %s property remove --name test
    
""".strip() % __app_name


def process(argv):
    if len(argv) == 0:
        print(main_desc)