# reloader.py

import sys
from fluvel.core import App
from project import GlobalConfig
from fluvel.cli.reloader.reloader_manager import HReloader

def main(timer: int) -> None:
    app = App(sys.argv)
    config = GlobalConfig("appconfig.toml")
    app.load(config)

    # Solo instanciamos el reloader
    reloader = HReloader(app, interval=timer)

    # Y le pedimos que inicie la ventana principal
    reloader.initialize_main_window()

    sys.exit(app.exec())