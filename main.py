import sys
from PySide6.QtWidgets import QApplication
from utils.config_loader import load_app_config
from views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    # Cargar configuración y tema
    config = load_app_config("appconfig.toml")
    
    # Instanciando la clase principal de la aplicación -> MainWindow <-
    window = MainWindow(app_config = config)

    # Ejecutando el bucle principal de la app
    sys.exit(app.exec())

if __name__ == "__main__":
    main()