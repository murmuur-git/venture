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


    # Modes
    mode_group = parser.add_mutually_exclusive_group(required=False)
    mode_group.add_argument('--setup', action='store_const', dest='mode', const='s',
                    help=f'{bcolors.YELLOW}Runs setup, use if config is missing or damaged{bcolors.ENDC}')
    mode_group.add_argument('--config', action='store_const', dest='mode', const='c',
                    help=f'{bcolors.YELLOW}Outputs config file{bcolors.ENDC}')

    # Commands
    subparsers = parser.add_subparsers(title='Commands', help='Commands help')
    # ---> Init
    parser_init = subparsers.add_parser('init', help=f'{bcolors.BLUE}Initializes a new project{bcolors.ENDC}')
    parser_init.add_argument('location', action='store', nargs=1, type=str)

    type_group = parser_init.add_mutually_exclusive_group(required=False)
    type_group.add_argument('-b','--blank', action='store_const', dest='type', const='b',
                       help=f'{bcolors.PINK}Creates a new blank project (default){bcolors.ENDC}')
    type_group.add_argument('-p','--python', action='store_const', dest='type', const='p',
                       help=f'{bcolors.PINK}Creates a new python project{bcolors.ENDC}')
    type_group.add_argument('--shell', action='store_const', dest='type', const='s',
                       help=f'{bcolors.PINK}Creates a new shell project{bcolors.ENDC}')
    parser_init.add_argument('-v','--verbose', action='store_true', dest='verbose',
                        help=f'{bcolors.PINK}Changes output to be verbose{bcolors.ENDC}')
    parser_init.set_defaults(mode='n', type='b',verbose=False)


    global ARGS
    ARGS = parser.parse_args()

def setup_config():
    """
    Sets up config file by asking for input from user
    """
    print(f'[{bcolors.CYAN}?{bcolors.ENDC}] Please enter the following information...')
    username = input(f'[{bcolors.DARKGREY}github.com{bcolors.ENDC}] username = ')
    access_token = input(f'[{bcolors.DARKGREY}github.com{bcolors.ENDC}] access_token = ')
    config.create_config(username,access_token)
    print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created config file')

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
        raise ConnectionAbortedError("Remote repository already exists with name... " + project_name)

def initialize_project():
    """
    Goes through process of initializing a project
    """
    path = ARGS.location[0]
    type = ARGS.type
    verbose = ARGS.verbose

    # Checks if path is valid
    try:
        is_valid_path(path)
    except FileExistsError as err:
        print(f'{bcolors.RED}FileExistsError{bcolors.ENDC}:', err,
            f'\nUse {bcolors.YELLOW}[-h]{bcolors.ENDC} option for more info')
        exit()

    # Create Github remote repository
    if verbose: print(f'[{bcolors.BLUE}~{bcolors.ENDC}] Contacting github API')
    try:
        remote_url = make_remote_repo()
    except ConnectionAbortedError as err:
        print(f'{bcolors.RED}ConnectionAbortedError{bcolors.ENDC}:', err,
            f'\nUse {bcolors.YELLOW}[-h]{bcolors.ENDC} option for more info')
        exit()
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created github remote repository')

    # Creates new directory
    os.mkdir(path)
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created new directory')

    # Change to path
    os.chdir(path)
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Changed to new directory')

    # Initialize new repository
    os.system('git init')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created git repository')

    # Add remote repo to origin
    remote_ssh = 'git@github.com:' + username + '/' + project_name + '.git'
    os.system('git remote add origin ' + remote_ssh)
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Added url to origin')

    # Create README.md
    os.system('touch README.md')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Created README.md')

    # Setup type of project
    if type == 'p':
        if verbose: print(f'[{bcolors.BLUE}~{bcolors.ENDC}] Creating python project from templat')
        prep.new_pyfile(username)
        if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Python project created')

    # Stage all files
    os.system('git add .')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Staged all files')

    # Initial commit
    os.system('git commit -m "initial commit"')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Committed changes')

    # Push to github
    os.system('git push -u origin master')
    if verbose: print(f'[{bcolors.GREEN}*{bcolors.ENDC}] Pushed to github')

def main():
    init()

    # Get Config Data
    config = ConfigParser()
    config.read('config.ini')
    global username, access_token, project_name
    try:
        username = config['github.com']['User']
        access_token = config['github.com']['AccessToken']
    except KeyError:
        print(f'{bcolors.RED}KeyError{bcolors.ENDC}: config file is missing or damaged, use {bcolors.PINK}venture --setup{bcolors.ENDC}',
            f'\nUse {bcolors.YELLOW}[-h]{bcolors.ENDC} option for more info')
        exit()


    mode = ARGS.mode
    if mode == 's':
        setup_config()
    elif mode == 'c':
        print_config()
    elif mode == 'i':
        project_name = ARGS.location[0].split('/')[-1]
        initialize_project()

if __name__ == '__main__':
    main()
