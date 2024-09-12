from rich.layout import Layout
from rich.padding import Padding
def make_layout() -> Layout:
    """creates  a layout split into [header ,main ,sggestions , footer]
    Returns:
        Layout: a modified instance of layout 
    """
    layout = Layout(name="root") 
    layout.split(
        Layout(name = "header",size =2),
        Layout(name="main", size = 3),
        Layout(name = "suggestion",size=3),

        Layout(name="view", ratio = 3),
    )

    layout["header"].update("[u]Terminal #[u]")
    return layout

