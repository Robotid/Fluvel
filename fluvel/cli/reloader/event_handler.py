
# HReloader Observer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time

# Fluvel
from fluvel.cli.paths import PROJECT_ROOT

VIEWS = PROJECT_ROOT / "views"
STATIC = PROJECT_ROOT / "static"

ObservableFiles = [".py", ".fluml"]

def init_event_handler(MainWindowInstance):
                
    e_handler = EventHandler(MainWindowInstance)
    
    observer = Observer()

    observer.schedule(e_handler, VIEWS, recursive=True)
    observer.schedule(e_handler, STATIC, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


class EventHandler(FileSystemEventHandler):

    def __init__(self, MainWindowInstance):

        self.MainWindowInstance = MainWindowInstance

    def on_modified(self, event) -> None:
        """
        Manejador de eventos
        """
        # Solo se reinicia si el archivo es de python o de fluml
        file_suffix = Path(event.src_path).suffix

        if file_suffix in ObservableFiles:
            print(f"Cambio detectado en {event.src_path}. Reiniciando la aplicación...")
            self.restart()

    def restart(self) -> None:
        """
        Detiene y reinicia el proceso hijo
        """
        
        print(self.MainWindowInstance.root.config.app_name)