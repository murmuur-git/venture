import configparser, os

def create_config(username, access_token):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['github.com'] = {'User': username,
                            'AccessToken': access_token}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def display_config(filename):
    os.system(f'cat {filename} | less')
