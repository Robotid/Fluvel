import sys
import os
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from utils.resource_loader import get_resource_path, load_style_sheet

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Rescatar la Configuración Global de la App en 'self.config'
        self.config = self.load_config()

        # Inicializar UI
        self.init_ui()

    def load_config(self):
        """ Este método se encarga de cargar la configuración 
        global de la aplicación a través de un archivo JSON """

        # Path del archivo de configuración JSON
        config_path = os.path.join(os.path.dirname(__file__), "appconfig.json")
        try:
            # Se intenta abrir el archivo 'config_path'
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)

        # Si el archivo no se encuentra se retorna una configuración por defecto 'default_config'
        except FileNotFoundError:
            print(f"Error: El archivo de configuración '{config_path}' no se encontró.")
            # Retornando una configuración por defecto
            default_config = {
                "app_name": "Mi Aplicación PySide6",
                "version": "1.0.0",
                "window_size": {
                    "width": 800,
                    "height": 600
                },
                "theme": "light",
                "database": {
                    "host": "localhost",
                    "port": 5432,
                    "user": "admin",
                    "password": "secure_password"
                },
                "log_level": "INFO"
            }
            return default_config

        # Si hay un fallo al decodificar el JSON, se retorna un diccionario vacío
        except json.JSONDecodeError:
            print(f"Error: El archivo '{config_path}' no es un JSON válido.")
            return {} # Retorna un diccionario vacío o configuración por defecto

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

        normal_button = QPushButton("Boton Normal")

        
        stylized_button = QPushButton("Boton Estilizado")
        
        # Estilo del boton (en una variable por si se quiere aplicar a muchos)
        btn_style_content = load_style_sheet("primary_button.qss")

        # Se aplican los estilos
        stylized_button.setStyleSheet(btn_style_content)
        normal_button.setStyleSheet(btn_style_content)

        layout.addWidget(label_name)
        layout.addWidget(label_version)
        layout.addWidget(label_theme)
        layout.addWidget(label_size)
        layout.addWidget(normal_button)
        layout.addWidget(stylized_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())