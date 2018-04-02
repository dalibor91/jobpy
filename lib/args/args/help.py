main_desc="""Smart task scheduler for running scripts 
on unix based systems 
Options:
    help       - Print this help message 
    daemon     - Print help message for daemon
    job        - Print help message for job manipulation
    list       - Print help message for listing
""".strip()

def process(argv):
    print(main_desc)
    return True