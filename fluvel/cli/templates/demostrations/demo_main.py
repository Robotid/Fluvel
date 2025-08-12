# fluvel/cli/templates/demostrations/demo.py
import sys

from fluvel.core import App
from .MainWindow import MainWindow


def demo_app(theme: str | None):

    # default config to load
    config = "appconfig.toml"

    if theme is not None:
        config = {"app": {"theme": theme}}

    # App
    app = App(sys.argv)

    # Load global settings of the app
    app.load(config)

    # Instantiate and display the demo application window
    window = MainWindow(root=app)
    window.show()

    # Running the main demo loop
    sys.exit(app.exec())
