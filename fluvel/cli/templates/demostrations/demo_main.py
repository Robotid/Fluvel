# fluvel/cli/templates/demostrations/demo.py
import sys

from fluvel.core import App
from .DemoWindow import DemoWindow
from fluvel.cli.paths import PROJECT_ROOT
import importlib


def demo_app(theme: str | None):

    module_path = "project.GlobalConfig"

    gc_module = importlib.import_module(module_path)

    # default config to load
    appconfig = PROJECT_ROOT / "appconfig.toml"

    if theme is not None:
        appconfig = {
            "app": {
                "theme": theme
            },
            "window_size": {
                "width": 1280,
                "height": 720
            }
        }

    # App
    app = App(sys.argv)

    config = gc_module.GlobalConfig(appconfig)

    # Load global settings of the app
    app.load(config)

    # Instantiate and display the demo application window
    window = DemoWindow(root=app)
    window.show()

    # Running the main demo loop
    sys.exit(app.exec())