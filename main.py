import sys
from PySide6.QtWidgets import QApplication
from utils.config_loader import load_app_config
from views.main_window import AppWindow

def main():
    # App
    app = QApplication(sys.argv)

    # Load settings and theme
    config = load_app_config("appconfig.toml")

    # Instantiate and display the main application window
    window = AppWindow(app_config = config)
    window.show()

    # Running the main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()