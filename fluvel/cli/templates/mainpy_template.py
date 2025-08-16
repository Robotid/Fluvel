# main.py

import sys
from fluvel.core import App
from views import MainWindow
from project import GlobalConfig


def main():
    # App
    app = App(sys.argv)

    # An instance of the app's global configuration is created
    config = GlobalConfig("appconfig.toml")

    # Load global settings of the app
    app.load(config)

    # Instantiate and display the main application window
    window = MainWindow(root=app)
    window.show()

    # Runnig the main loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
