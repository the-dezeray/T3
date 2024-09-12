import sys

def check_terminal():
    pass
def check_dependencies():
    if getattr(sys, 'frozen', False):
        # The script is running in a bundle
        return  # No need to check dependencies
    else:
        pass


def install_dependecies()->None:
    """handles all required packages and files """
    pass
