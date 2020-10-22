"""
CLI tool to initialize a new project

author: murmuur
"""
from libs import *

def init():
    """
    Sets up the CLI
    """
    description = 'Initializes a project'
    parser = argparse.ArgumentParser(description=description,
                                     epilog='project type arguments are mutually exclusive')

    parser.add_argument('location', action='store', nargs=1, type=str,
                    help=f'{bcolors.YELLOW}Location of new project{bcolors.ENDC}')

    # Arguments for which type of project to create
    type_group = parser.add_mutually_exclusive_group(required=False)
    type_group.add_argument('-b','--blank', action='store_const', dest='type', const='b',
                       help=f'{bcolors.BLUE}Creates a new blank project (default){bcolors.ENDC}')
    type_group.add_argument('-p','--python', action='store_const', dest='type', const='p',
                       help=f'{bcolors.BLUE}Creates a new python project{bcolors.ENDC}')
    type_group.add_argument('--shell', action='store_const', dest='type', const='s',
                       help=f'{bcolors.BLUE}Creates a new shell project{bcolors.ENDC}')
    parser.set_defaults(type='b')

    global ARGS
    ARGS = parser.parse_args()

def main():
    init()
    print(ARGS)


if __name__ == '__main__':
    main()
