# main.py

import sys
from core import App
from views import MainWindow

def main():
    # App
    app = App(sys.argv)

    # Load global settings and theme of the app
    app.load("appconfig.toml")

    # Instantiate and display the main application window
    window = MainWindow(root=app)
    window.show()

    # Runnig the main loop
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()