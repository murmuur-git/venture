"""
Venture
 a CLI tool to initialize a new project

author: murmuur
"""
# Import Globals
from .libs import *

# Import local dependencies
from .libs import config_editor as config
from .libs import file_prep as prep

# Import dependencies
import os, argparse, sys, json, requests

def init():
    """
    Sets up the CLI
    """
    description = 'Initializes a project'
    parser = argparse.ArgumentParser(description=description,
                                     epilog='project type arguments are mutually exclusive')


    # Modes
    mode_group = parser.add_mutually_exclusive_group(required=False)
    mode_group.add_argument('--setup', action='store_const', dest='mode', const='s',
                    help=f'{bcolors.YELLOW}Runs config setup, use if config is missing or damaged{bcolors.ENDC}')
    mode_group.add_argument('--config', action='store_const', dest='mode', const='c',
                    help=f'{bcolors.YELLOW}Outputs config file{bcolors.ENDC}')

    # Commands
    subparsers = parser.add_subparsers(title='Commands', help='Commands help')
    # ---> Init
    parser_init = subparsers.add_parser('init', help=f'{bcolors.BLUE}Initializes a new project{bcolors.ENDC}')
    parser_init.add_argument('location', action='store', nargs=1, type=str,
                        help=f'{bcolors.RED}Location for new project{bcolors.ENDC}')

    type_group = parser_init.add_mutually_exclusive_group(required=False)
    type_group.add_argument('--blank', action='store_const', dest='type', const='b',
                       help=f'{bcolors.PINK}Creates a new blank project (default){bcolors.ENDC}')
    type_group.add_argument('-p','--python', action='store_const', dest='type', const='p',
                       help=f'{bcolors.PINK}Creates a new python project{bcolors.ENDC}')
    type_group.add_argument('--shell', action='store_const', dest='type', const='s',
                       help=f'{bcolors.PINK}Creates a new shell project{bcolors.ENDC}')

    parser_init.add_argument('-r','--remote', action='store_true', dest='remote',
                        help=f'{bcolors.DARKGREY}Creates remote github repository along on project initialization{bcolors.ENDC}')
    parser_init.add_argument('-v','--verbose', action='store_true', dest='verbose',
                        help=f'{bcolors.DARKGREY}Changes output to be verbose{bcolors.ENDC}')

    # Sets defaults
    remote = config.defaults(root_path).remote()
    verbose = config.defaults(root_path).verbose()
    type = config.defaults(root_path).type()
    parser_init.set_defaults(type=type,verbose=verbose, remote=remote)


    global ARGS
    ARGS = parser.parse_args()

def setup_config():
    """
    Sets up config file by asking for input from user
    """
    print(f'[{bcolors.CYAN}?{bcolors.ENDC}] Please enter the following information...')
    username = input(f'[{bcolors.DARKGREY}github.com{bcolors.ENDC}] username = ')
    access_token = input(f'[{bcolors.DARKGREY}github.com{bcolors.ENDC}] access_token = ')
    config.create_config(username,access_token, root_path)
    print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Setup config file at {root_path}/config.ini')

def print_config():
    """
    Outputs contents of config file to console
    """
    config.display_config('config.ini')

def make_remote_repo():
    """
    Makes remote repo and returns the clone url
    """
    # Contact API
    description = project_name + ' repository'
    payload = {'name': project_name, 'description': description}
    login = requests.post('https://api.github.com/' + 'user/repos', auth=(username,access_token), data=json.dumps(payload))
    try:
        return json.loads(login.text)['clone_url']
    except KeyError:
        raise ConnectionAbortedError("Trouble making repository at... github.com/" + username +'/'+ project_name)

def initialize_project():
    """
    Goes through process of initializing a project
    """
    path = ARGS.location[0]
    type = ARGS.type
    verbose = ARGS.verbose
    remote = ARGS.remote

    # Checks if path is valid
    try:
        is_valid_path(path)
    except FileExistsError as err:
        print(f'{bcolors.RED}FileExistsError{bcolors.ENDC}:', err,
            f'\nUse {bcolors.YELLOW}[-h]{bcolors.ENDC} option for help')
        exit()

    # Makes github repo
    if remote:
        # Create Github remote repository
        if verbose: print(f'[{bcolors.BLUE}~{bcolors.ENDC}] Contacting github API')
        try:
            remote_url = make_remote_repo()
        except ConnectionAbortedError as err:
            print(f'{bcolors.RED}ConnectionAbortedError{bcolors.ENDC}:', err,
                f'\nUse {bcolors.YELLOW}[-h]{bcolors.ENDC} option for help')
            exit()
        if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created github remote repository')

    # Change into new project directory
    parent_dir = os.path.abspath(os.path.join(path, os.pardir))
    os.chdir(parent_dir)
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Changed to new directory')

    # Setup type of project
    if type == 'p':
        if verbose: print(f'[{bcolors.BLUE}~{bcolors.ENDC}] Creating python project from templat')
        prep.new_pyfile(project_name, root_path)
        if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Python project created')
    else:
        os.mkdir(path)
        if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created new directory')
    os.system(f'echo "# {project_name}" >> {project_name}/README.md')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created README.md')

    # Change into new project
    os.chdir(path)
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Changed to new directory')

    # Initialize new repository
    os.system('git init')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created git repository')

    # Creates and checkouts to dev branch
    os.system('git checkout -b dev')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created and checkout to dev branch')

    # Adds to origin
    if remote:
        # Add remote repo to origin
        remote_ssh = 'git@github.com:' + username + '/' + project_name + '.git'
        os.system('git remote add origin ' + remote_ssh)
        if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Added url to origin')

    # Stage all files
    os.system('git add .')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Staged all files')

    # Initial commit
    os.system('git commit -m "initial commit"')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Committed initial commit')

    # Pushes to github repo
    if remote:
        # Push to github
        os.system('git push -u origin master')
        if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Pushed to github')

def main():
    global username, access_token, project_name, root_path
    #Get root path
    root_path = os.path.abspath(os.path.join(__file__, os.pardir))

    init()

    # Check if mode is in setup
    mode = ARGS.mode
    if mode == 's':
        setup_config()
        exit()

    # Get config data
    username, access_token = config.get_github_info()

    # Run mode
    if mode == 'c':
        print_config()
    else:
        project_name = ARGS.location[0].split('/')[-1]
        initialize_project()


if __name__ == '__main__':
    main()
