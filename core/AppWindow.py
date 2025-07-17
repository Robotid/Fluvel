from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from utils.resource_loader import load_style_sheet

class AppWindow(QMainWindow):
    def __init__(self, config: dict):
        """
        The constructor method performs the main configurations of the application's user interface window.\n
        The application configuration **`appconfig`** is stored in the ***`self.config: dict`*** property of the **`CMainWindow`** Class.\n
        Properties:\n
         - self.config: dict -> Saves the provided application settings.\n
         - self.app_name: str -> Saves the name of the app from self.config['app_name'].\n
         - self.version: str -> Saves the version of the app from self.config['version'].\n
         - self.window_width: str -> Saves the width of the window from self.config['window_size']['width'].\n
         - self.window_height: str -> Saves the height of the window from self.config['window_size']['height'].\n
         - self.theme: str -> Global theme of the app from self.config['theme'].
        """
        super().__init__()

        # Rescatar la Configuración Global de la App en 'self.config'
        self.config = config

        # Configuring the global properties 
        self.app_name = self.config.get("app_name", "Aplicación Desconocida")
        self.version = self.config.get("version", "N/A")
        self.window_width = self.config.get("window_size", {}).get("width", 640)
        self.window_height = self.config.get("window_size", {}).get("height", 480)
        self.theme = self.config.get("theme", "clean-light")

        # Configuring the database data
        self.db = self.config.get("database", {})

        # Inicializar UI
        self.init_ui()

    def init_ui(self):
        """
        
        """
        self.setWindowTitle(f"{self.app_name} - {self.version}")
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Configurando el Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout: QVBoxLayout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        print(f"Configuración de la base de datos: {self.config.get('database', 'No configurada')}")
        print(f"Nivel de log: {self.config.get('log_level', 'No definido')}")

        # Estableciendo el tema de la app con la hoja de estilos (se aplica a toda la app)
        self.set_theme()

        # Display Widgets
        self.setUpMainWindow()
    
    def set_theme(self):
        label_content = load_style_sheet("Label.qss", self.theme)
        push_button_content = load_style_sheet("PushButton.qss", self.theme)
        check_button_content = load_style_sheet("CheckButton.qss", self.theme)
        full_content = f"{label_content}{push_button_content}{check_button_content}"
        self.setStyleSheet(full_content)

    def setUpMainWindow(self):
        """ Display `components` in the Main Window. """
        ...
    