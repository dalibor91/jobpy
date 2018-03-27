from lib.Helpers.Properties import Properties

__app_name = Properties.get('app_name')

main_desc = """Managers properties for jobs 
Options:
    add             - Name of property 
    remove          - Remove property
    --name          - Name of property
    --value         - Default value 

Example:
    %s property add --name test --value "/bin/bash /tmp/test1.sh"
""".strip() % __app_name


def process(argv):
    if len(argv) == 0:
        print(main_desc)