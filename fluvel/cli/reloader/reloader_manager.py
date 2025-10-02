import sys, importlib

# Watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Fluvel
from fluvel.cli.paths import PROJECT_ROOT
from fluvel.core.Router import Router

# PySide6
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QMainWindow, QApplication


class ReloaderSignalEmmiter(QObject):
    """
    Emisor de señales para la recarga
    """

    fileModified = Signal()

class FileChangeHandler(FileSystemEventHandler):

    def __init__(self, emitter: ReloaderSignalEmmiter):
        super().__init__()
        self.emitter = emitter

    def on_modified(self, event):
        """
        Este método se activa cuando se modifica un archivo.
        """
        if not event.is_directory and not event.src_path.endswith(".pyc"):
            self.emitter.fileModified.emit()


class HReloader(QObject):

    def __init__(self, window: QMainWindow, root: QApplication, fluvel_app):
        super().__init__()

        self.fluvel_app = fluvel_app
        self.app_root = root
        self.main_window = window

        self.observer = Observer()
        self.signal_emitter = ReloaderSignalEmmiter()
        self.signal_emitter.fileModified.connect(self.schedule_reload) # Cambiado de on_file_changed a schedule_reload
        self.event_handler = FileChangeHandler(self.signal_emitter)

        # Timer
        self.reload_timer = QTimer(self)
        self.reload_timer.setSingleShot(True)
        self.reload_timer.setInterval(50)  
        self.reload_timer.timeout.connect(self.on_file_changed) 
        
        self.show_window()

    def show_window(self) -> None:
        """
        Instancia la ventana principal por primera vez y la muestra.
        """
        self.main_window.show()

        self.start_file_monitoring()

    def start_file_monitoring(self) -> None:
        """
        Inicia el monitoreo de archivos en el directorio 'views'.
        """
        try:
            views_path = PROJECT_ROOT / "views"
            static_path = PROJECT_ROOT / "static"

            self.observer.schedule(self.event_handler, str(views_path), recursive=True)
            self.observer.schedule(self.event_handler, str(static_path), recursive=True)
            
            self.observer.start()
            print(f"Monitoring changes in: {views_path}")
            print(f"Monitoring changes in: {static_path}")

        except FileNotFoundError:
            print(
                'Error: The "views/" or "static/" directory does not exist. Cannot monitor.'
            )

        self.app_root.aboutToQuit.connect(self.stop_file_monitoring)

    def stop_file_monitoring(self) -> None:
        """
        Detiene el monitoreo de archivos de forma segura.
        """
        if self.observer.is_alive():
            self.observer.stop()
            self.observer.join()
            print("File monitoring stopped.")

    def schedule_reload(self) -> None:
        """
        Este nuevo slot se activa con cada evento de archivo.
        En lugar de recargar inmediatamente, (re)inicia el temporizador.
        """
        self.reload_timer.start()

    def on_file_changed(self) -> None:
        """
        Slot que se llama cuando cambia un archivo.
        """
        print("Change detected. Reloading the application...")
        self.reload_and_update()

    def reload_and_update(self) -> None:
        """
        Recarga los módulos de vistas y actualiza el contenido de la ventana.
        """
        modules_to_reload = [m for m in sys.modules.keys() if m.startswith("views")]
        modules_to_reload.append("window")

        for module in modules_to_reload:
            if module in sys.modules:
                try:
                    importlib.reload(sys.modules[module])
                except Exception as e:
                    print(f"Error reloading module {module}: {e}")

        # Recargamos los qss
        self.fluvel_app._set_theme()

        # Recargamos el contenido de texto estático
        self.fluvel_app._set_content()

        # Actualizamos la UI
        self.main_window.update_ui(Router)
