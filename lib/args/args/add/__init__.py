from lib.Helpers.Properties import Properties

__app_name = Properties.get('app_name')

main_desc="""Adds new job to scheduler 
Options:
    --name          - Name of job 
    --property      - Add property
    --run           - When to run 
    --user          - Run as user 
    --help          - Show this message 
    
Example:
    %s add --name "test_job" \
    --run "* * * * *" \
    --property on_fail="echo 'test' | mail -s 'test' dalibor@dalibor.me" \
    --property email_fail=dalibor@dalibor.me
""".strip() % __app_name


def process(argv):
    if len(argv) == 0:
        print(main_desc)