"""execute code with basic terminal"""

from core import Core

def _get_user_input():
    return input("enter input: ")

if __name__ == "__main__":
    user_input  = _get_user_input()
    core = Core(layout = None)
    core.process(user_input= user_input)
     