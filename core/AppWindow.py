# fluvel.core.AppWindow

from core.GlobalConfig import GlobalConfig
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class AppWindow(QMainWindow, GlobalConfig):
    def __init__(self):
        """
        Global Main Properties:\n
            - self.config: dict -> Saves the provided application settings.\n
            - self.app_name: str -> Saves the name of the app from appconfig['app']['app_name'].\n
            - self.version: str -> Saves the version of the app from appconfig['app']['version'].\n
            - self.window_width: str -> Saves the width of the window from appconfig['window_size']['width'].\n
            - self.window_height: str -> Saves the height of the window from appconfig['window_size']['height'].\n
            - self.theme: str -> Global theme of the app from appconfig['app']['theme'].\n
        Global Database Properties:\n
            - self.db_host: str -> Saves the host of the DB from appconfig['database']['host'].\n
            - self.db_port: int -> Saves the port of the DB from appconfig['database']['port'].\n
            - self.db_user: str -> Saves the user of the DB from appconfig['database']['user'].\n
            - self.db_password: any -> -> Saves the password of the DB from appconfig['database']['password']\n
        """
        super().__init__()

        # Inicializar UI
        self.init_ui()

    def init_ui(self):
        """
        This method performs the main configurations of the application's user interface window.
        """
        self.setWindowTitle(f"{self.app_name} - {self.version}")
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Configurando el Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout: QVBoxLayout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Display Widgets
        self.setUpMainWindow()

    def setUpMainWindow(self):
        """ Display `components` in the Main Window. """
        ...
    