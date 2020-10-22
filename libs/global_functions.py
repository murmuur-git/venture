"""
Global functions for package

author: murmuur
"""

import os

def verify_path(file_path):
    """
    Gets contents in file given a relative path to where command was run

    Note: confidently works on macos file system, others unknown
    """
    if os.path.exists(file_path) == False:
        return None
    return 'Hello'
