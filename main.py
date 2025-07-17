import sys
from PySide6.QtWidgets import QApplication
from utils.config_loader import load_app_config
from views import MainWindow

"""
# Estructura deseada para el framework Fluvel
# main.py

from fluvel.core import App
from views import MainWindow

def main():
    # App
    app = App(sys.argv)

    # Load settings and theme
    config = App.load("pyproject.toml")

    # Instantiate and display the main application window
    window = MainWindow(app_config=config)
    window.show()

    # Runnig the main loop
    sys.exis(app.exec())

if __name__ = "__main__":
    main()
"""

def main():
    # App
    app = QApplication(sys.argv)

    # Load settings and theme
    config = load_app_config("appconfig.toml")

    # Instantiate and display the main application window
    window = MainWindow(app_config = config)
    window.show()

    # Running the main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()