import configparser, os, ast
from .globals import *

def create_config(root_path, username='', access_token=''):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['defaults'] = {'remote': False,
                            'verbose': False,
                            'type': 'b'}
    config['github.com'] = {'User': '',
                            'AccessToken': ''}
    with open(os.path.abspath(root_path+'/config.ini'), 'w') as configfile:
        config.write(configfile)

def display_config(filename):
    os.system(f'cat {filename}')

def get_github_info(root_path):
    config = configparser.ConfigParser()
    config.read(os.path.abspath(root_path+'/config.ini'))
    username = config['github.com']['User']
    access_token = config['github.com']['AccessToken']
    if len(username) > 0 and len(access_token) > 0:
        print(f'[{bcolors.CYAN}?{bcolors.ENDC}] Please enter the following information...')
        username = input(f'[{bcolors.DARKGREY}github.com{bcolors.ENDC}] username = ')
        access_token = input(f'[{bcolors.DARKGREY}github.com{bcolors.ENDC}] access_token = ')
    return username, access_token

class defaults():
    def __init__(self, root_path):
        self.root_path = root_path
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath(self.root_path+'/config.ini'))

    def remote(self):
        return ast.literal_eval(self.config['defaults']['remote'])
    def verbose(self):
        return ast.literal_eval(self.config['defaults']['remote'])
    def type(self):
        return self.config['defaults']['remote']
