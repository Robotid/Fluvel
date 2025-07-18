# fluvel.core.AppWindow

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from project import GlobalConfig

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

        # Display Widgets
        self.setUpMainWindow()

    def set_layout(self):
        pass

    def setUpMainWindow(self):
        """ Display `components` in the Main Window. """
        ...
