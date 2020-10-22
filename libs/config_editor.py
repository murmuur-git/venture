import configparser

def create_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['github.com'] = {'User': '<username>',
                            'AccessToken': '<access token>'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
