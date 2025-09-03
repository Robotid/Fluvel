# fluvel/cli/templates/demostrations/demo.py
import sys

from fluvel.core import App
from .DemoWindow import DemoWindow


def demo_app(theme: str | None):

    config = "appconfig.toml"

    if theme is not None:
        config = {
            "app": {"theme": theme},
            "window_size": {"width": 1280, "height": 720},
        }

    # App
    app = App(sys.argv)

    # Load global settings of the app
    app.load(config)

    # Instantiate and display the demo application window
    window = DemoWindow(root=app)
    window.show()

    # Running the main demo loop
    sys.exit(app.exec())
