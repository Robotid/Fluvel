"""
Modulo de Fluvel que habilita el Hot-Reload
en la aplicación PySide6.
por defecto analiza los siguientes directorios:
    - ./views/...
    - ./static/...
"""

import sys
from fluvel.core import App
from fluvel.cli.reloader.reloader_manager import HReloader
from fluvel.cli.paths import PROJECT_ROOT


def main() -> None:

    # App
    app = App(sys.argv)

    # Config Loader
    app.load("appconfig.toml")

    # Hot-Reloader
    reloader = HReloader(root=app, project_path=PROJECT_ROOT)

    sys.exit(app.exec())
