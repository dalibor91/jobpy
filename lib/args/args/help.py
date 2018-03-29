main_desc="""Smart task scheduler for running scripts 
on unix based systems 
Options:
    help       - Print this help message 
    add        - Print help message for add 
    update     - Print help message for update
    remove     - Print help message for remove
    property   - Print help message for property 
    
    daemon     - Print help message for daemon
""".strip()

def process(argv):
    print(main_desc)
    return True