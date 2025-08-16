import sys
import importlib
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication

class HReloader:
    
    def __init__(self, root: QApplication, interval: int):
        
        self.app_root = root
        self.interval = interval * 1000 if interval >= 1 else 1000
        
        # Almacenamos una referencia a la instancia de la ventana principal
        self.main_window_instance: QMainWindow = None
        
        # Se inicia el bucle para actualizar la ventana
        self.timer = QTimer()
        self.timer.timeout.connect(self.reload_and_update)
        self.timer.start(self.interval)

        self.initialize_main_window()
        
    def initialize_main_window(self) -> None:
        """Instancia la ventana principal por primera vez y la muestra."""
        main_window_module = importlib.import_module("views.MainWindow")
        
        # Pasamos el reloader a la ventana para que pueda acceder a su estado
        self.main_window_instance = main_window_module.MainWindow(root=self.app_root)
        self.main_window_instance.show()
        
    def reload_and_update(self) -> None:
        """
        Recarga el módulo de vistas y actualiza el contenido de la ventana.
        """
        print("Recargando módulo de vistas...")
        
        # Obtenemos todos los módulos 'views' que deben ser recargados
        modules_to_reload = [m for m in sys.modules.keys() if m.startswith("views")]

        for module in modules_to_reload:
            if module in sys.modules:
                try:
                    # Usamos importlib.reload() para un recargado más seguro
                    importlib.reload(sys.modules[module])
                except ImportError as e:
                    print(f"Error recargando módulo {module}: {e}")
        
        # Una vez recargados los módulos, le pedimos a la ventana que se actualice
        self.main_window_instance.update_ui()