from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from utils.resource_loader import get_resource_path, load_style_sheet
from components.Buttons.PushButtons import PrimaryButton, SecondaryButton, SuccessButton, DangerButton, DarkButton, InfoButton, WarningButton, LightButton


class MainWindow(QMainWindow):
    def __init__(self, app_config: dict):
        super().__init__()

        # Rescatar la Configuración Global de la App en 'self.config'
        self.config = app_config

        # Inicializar UI
        self.init_ui()

    def init_ui(self):
        """Estableciendo las -> Configuraciones <- de la Interfaz de Usuario de la aplicación """

        self.app_name = self.config.get("app_name", "Aplicación Desconocida")
        self.version = self.config.get("version", "N/A")
        self.window_width = self.config.get("window_size", {}).get("width", 640)
        self.window_height = self.config.get("window_size", {}).get("height", 480)
        self.theme = self.config.get("theme", "light")

        self.setWindowTitle(f"{self.app_name} - {self.version}")
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Configurando el Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        print(f"Configuración de la base de datos: {self.config.get('database', 'No configurada')}")
        print(f"Nivel de log: {self.config.get('log_level', 'No definido')}")

        # Display Widgets
        self.setUpMainWindow(layout=layout)
        self.show()

    def setUpMainWindow(self, layout):
        """ Configurar los Wigets de la aplicación """
        label_name = QLabel(f"Nombre de la Aplicación: {self.app_name}")
        label_version = QLabel(f"Versión: {self.version}")
        label_theme = QLabel(f"Tema: {self.theme}")
        label_size = QLabel(f"Tamaño de Ventana: {self.window_width}x{self.window_height}.")


        # Estableciendo el tema de la app con la hoja de estilos (se aplica a toda la app)
        self.setStyleSheet(load_style_sheet("push_button.qss", self.theme))

        primary_button = PrimaryButton("Boton Primario")

        secondary_button = SecondaryButton("Boton Secundario")

        danger_button = DangerButton("Boton Peligro")

        success_button = SuccessButton("Boton Success")

        warning_button = WarningButton("Warning Button")

        info_button = InfoButton("Info Button")

        dark_button = DarkButton("Dark Button")

        light_button = LightButton("Light Button")
    
        layout.addWidget(label_name)
        layout.addWidget(label_version)
        layout.addWidget(label_theme)
        layout.addWidget(label_size)
        layout.addWidget(primary_button)
        layout.addWidget(secondary_button)
        layout.addWidget(danger_button)
        layout.addWidget(success_button)
        layout.addWidget(warning_button)
        layout.addWidget(info_button)
        layout.addWidget(dark_button)
        layout.addWidget(light_button)