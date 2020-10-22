import os

def py_main(username):
    # Sets up main.py
    trip_quote = '"""'
    os.system('touch main.py')
    os.system(f"echo '{trip_quote}' >> main.py")
    os.system(f'echo "author: {username}" >> main.py')
    os.system(f"echo '{trip_quote}' >> main.py")
    os.system('echo "from libs import *" >> main.py')

def py_init(username):
    #sets up __init__.py
    trip_quote = '"""'
    os.system('touch libs/__init__.py')
    os.system(f"echo '{trip_quote}' >> libs/__init__.py")
    os.system('echo "Package Dependencies" >> libs/__init__.py')
    os.system("echo '' >> libs/__init__.py")
    os.system(f'echo "author: {username}" >> libs/__init__.py')
    os.system(f"echo '{trip_quote}' >> libs/__init__.py")
    os.system('echo "from .global_objects import *" >> libs/__init__.py')
    os.system('echo "from .global_functions import *" >> libs/__init__.py')

def py_global_func(username):
    # sets up global_functions.py
    trip_quote = '"""'
    os.system('touch libs/global_functions.py')
    os.system(f"echo '{trip_quote}' >> libs/global_functions.py")
    os.system('echo "Global functions for package" >> libs/global_functions.py')
    os.system("echo '' >> libs/global_functions.py")
    os.system(f'echo "author: {username}" >> libs/global_functions.py')
    os.system(f"echo '{trip_quote}' >> libs/global_functions.py")

def py_bcolors():
    trip_quote = '"""'
    os.system("echo 'class bcolors:' >> libs/global_objects.py")
    os.system(f"echo '  {trip_quote}' >> libs/global_objects.py")
    os.system('echo "   Object that contains ANSI colors and formating, for easy use" >> libs/global_objects.py')
    os.system(f"echo '  {trip_quote}' >> libs/global_objects.py")
    os.system("""echo "  LIGHTGREY = '\033[97m'" >> libs/global_objects.py""")
    os.system("""echo "  CYAN = '\033[96m'" >> libs/global_objects.py""")
    os.system("""echo "  PURPLE = '\033[95m' # Headers" >> libs/global_objects.py""")
    os.system("""echo "  PINK = '\033[94m'" >> libs/global_objects.py""")
    os.system("""echo "  BLUE = '\033[34m' # Ok blue" >> libs/global_objects.py""")
    os.system("""echo "  GREEN = '\033[92m' # Ok green" >> libs/global_objects.py""")
    os.system("""echo "  YELLOW = '\033[93m' # Warning" >> libs/global_objects.py""")
    os.system("""echo "  RED = '\033[91m' # Fail" >> libs/global_objects.py""")
    os.system("""echo "  DARKGREY = '\033[90m'" >> libs/global_objects.py""")
    os.system("""echo "  STRIKE = '\033[9m'" >> libs/global_objects.py""")
    os.system("""echo "  UNDERLINE = '\033[4m'" >> libs/global_objects.py""")
    os.system("""echo "  ITALIC = '\033[3m'" >> libs/global_objects.py""")
    os.system("""echo "  BOLD = '\033[1m'" >> libs/global_objects.py""")
    os.system("""echo "  ENDC = '\033[0m' # White" >> libs/global_objects.py""")
    os.system("echo '' >> libs/global_functions.py")
    os.system("""echo "  def custom(code):" >> libs/global_objects.py""")
    os.system("""echo "    return f'\033[{str(code)}m'" >> libs/global_objects.py""")

def py_global_obj(username):
    # sets up global_functions.py
    trip_quote = '"""'
    os.system('touch libs/global_objects.py')
    os.system(f"echo '{trip_quote}' >> libs/global_objects.py")
    os.system('echo "Global objects for package" >> libs/global_objects.py')
    os.system("echo '' >> libs/global_objects.py")
    os.system(f'echo "author: {username}" >> libs/global_objects.py')
    os.system(f"echo '{trip_quote}' >> libs/global_objects.py")
    os.system("echo '' >> libs/global_objects.py")
    py_bcolors()

def py_libs(username):
    # Creates libs (libraries folder) and adds files
    os.system('mkdir libs')
    os.system('cd libs')
    py_init(username)
    py_global_func(username)
    py_global_obj(username)
    os.system('cd ..')

def new_pyfile(username):
    """
    Creates all files needed for a python project
    """
    # Creates .env file and main.py
    os.system('touch .env')

    # Setup py
    py_main(username)

    # Setup Libraries folder
    py_libs(username)
