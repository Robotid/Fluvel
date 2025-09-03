import sys, importlib

# Watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# PySide6
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow, QApplication


class ReloaderSignalEmitter(QObject):
    """
    Emisor de señales para la recarga
    """

    fileModified = Signal()


class FileChangeHandler(FileSystemEventHandler):

    def __init__(self, emitter: ReloaderSignalEmitter):
        super().__init__()
        self.emitter = emitter

    def on_modified(self, event):
        """
        Este método se activa cuando se modifica un archivo.
        """
        if not event.is_directory and not event.src_path.endswith(".pyc"):
            self.emitter.fileModified.emit()


class HReloader(QObject):

    def __init__(self, root: QApplication, project_path: str):
        super().__init__()

        self.app_root = root
        self.project_path = project_path

        self.main_window_instance: QMainWindow = None

        # Objeto para monitorear archivos
        self.observer = Observer()

        # Creamos el emisor de señales y conectamos su señal
        self.signal_emitter = ReloaderSignalEmitter()
        self.signal_emitter.fileModified.connect(self.on_file_changed)

        # El manejador de eventos ahora recibe el emisor como argumento
        self.event_handler = FileChangeHandler(self.signal_emitter)

        # Se instancia la ventana principal por primera vez
        self.initialize_main_window()

    def initialize_main_window(self) -> None:
        """
        Instancia la ventana principal por primera vez y la muestra.
        """
        main_window_module = importlib.import_module("window")

        self.main_window_instance = main_window_module.MainWindow(root=self.app_root)
        self.main_window_instance.show()

        self.start_file_monitoring()

    def start_file_monitoring(self) -> None:
        """
        Inicia el monitoreo de archivos en el directorio 'views'.
        """
        try:
            views_path = self.project_path / "views"
            static_path = self.project_path / "static"

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

        for module in modules_to_reload:
            if module in sys.modules:
                try:
                    importlib.reload(sys.modules[module])
                except Exception as e:
                    print(f"Error reloading module {module}: {e}")

        # Recargamos los qss
        self.main_window_instance.root._set_theme()

        # Recargamos el contenido de texto estático
        self.main_window_instance.root._set_content()

        # Actualizamos la UI
        self.main_window_instance.update_ui()
