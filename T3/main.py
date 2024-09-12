"""main file : handles core and layout initialization"""
from pynput.keyboard  import Listener
from rich.live import Live
from rich.panel import Panel
from rich.padding import Padding
from rich.console import Console,Group
from rich.table import Table
import time
from dependecies import check_dependencies
from layout import make_layout
from core import Core

def main():
    "start program"
    console = Console()

    layout = make_layout()
    core = Core(layout= layout)

    core.table =  Table(expand=True,show_edge=False)
    core.table.add_column()
    layout["view"].update(Padding(core.table,pad =(0,40),expand=True))
    #listens for keyboard presses and 

    with Listener(on_press= core.save_key) as L:

        with Live(layout, refresh_per_second=10):  # update 4 times a second to feel fluid
            #while the app hase not been terminated
            while core.running:
                layout["main"].update(Padding(Panel(core.formated_text),pad =(0,20)))
                layout["suggestion"].update(Padding(core.suggestion,pad =(0,20),expand=True))

                # Handle cursor blinking
                core.update_cursor()
        L.join()
        
if __name__ == "__main__":
    check_dependencies()
    main()