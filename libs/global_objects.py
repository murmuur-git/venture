"""
Global objects for package

author: murmuur
"""

class bcolors:
    """
    Object that contains text colors and formating for easy use
    """
    LIGHTGREY = '\033[97m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DARKGREY = '\033[90m'
    STRIKE = '\033[9m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

    def custom(code):
        return f'\033[{str(code)}m'
