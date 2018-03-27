from lib.Helpers.Properties import Properties

__app_name = Properties.get('app_name')

main_desc = """Updates jobs in scheduler 
Options:
    --name          - Name of job 
    --id            - Job id
    
    --property      - Adds property
    --del_property  - Removes property 
    --field         - Updates field

Example:
    %s property update --field name="test_1234" --property email_on_fail=dalibor.menkovic@gmail.com
    
""".strip() % __app_name


def process(argv):
    if len(argv) == 0:
        print(main_desc)