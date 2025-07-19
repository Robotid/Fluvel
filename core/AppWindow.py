# fluvel.core.AppWindow

from project import GlobalConfig
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from core.MenuBar import MenuBar

class AppWindow(QMainWindow, GlobalConfig):
    def __init__(self):
        super().__init__()

        # Inicializar UI
        self.init_ui()

    def init_ui(self):
        """
        This method performs the main configurations of the application's user interface window.
        """
        self.setWindowTitle(f"{self.app_name} - {self.version}")
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Configuring the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout: QVBoxLayout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Configuring the Menu Bar
        self.set_menu_bar()

        # Display Widgets
        self.setUpMainWindow()

    def set_menu_bar(self):
        self.menu_bar = MenuBar(parent=self, menu_file="MenuBar.toml")
        
    def set_layout(self):
        pass

    def setUpMainWindow(self):
        """ Display `components` in the Main Window. """
        ...
