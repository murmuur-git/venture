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
                       help=f'{bcolors.PINK}Creates a new blank project (default){bcolors.ENDC}')
    type_group.add_argument('-p','--python', action='store_const', dest='type', const='p',
                       help=f'{bcolors.PINK}Creates a new python project{bcolors.ENDC}')
    type_group.add_argument('--shell', action='store_const', dest='type', const='s',
                       help=f'{bcolors.PINK}Creates a new shell project{bcolors.ENDC}')

    parser.add_argument('-v','--verbose', action='store_true', dest='verbose',
                       help=f'{bcolors.PINK}Creates a new shell project{bcolors.ENDC}')


    parser.set_defaults(verbose=False, type='b')

    global ARGS
    ARGS = parser.parse_args()

def main():
    init()

    path = ARGS.location[0]
    verbose = ARGS.verbose

    # Checks if path is valid
    try:
        is_valid_path(path)
    except FileExistsError as err:
        print(f'{bcolors.RED}FileExistsError{bcolors.ENDC}:', err,
            f'\nUse {bcolors.YELLOW}[-h]{bcolors.ENDC} option for more info')

    # Creates new directory
    os.mkdir(path)
    if verbose: print(f'[{bcolors.BLUE}~{bcolors.ENDC}] Created new directory')

    # Change to path
    os.chdir(path)
    if verbose: print(f'[{bcolors.BLUE}~{bcolors.ENDC}] Changed to new directory')

    # Initialize new repository
    if verbose: print(f'[{bcolors.LIGHTGREY}~{bcolors.ENDC}] Creating git repository')
    os.system('git init')





if __name__ == '__main__':
    main()
