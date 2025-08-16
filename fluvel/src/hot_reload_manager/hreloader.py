import time
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fluvel.cli.paths import PROJECT_ROOT, MAINPY_ROOT

VIEWS = PROJECT_ROOT / "views"
STATIC = PROJECT_ROOT / "static"

class EventHandler(FileSystemEventHandler):

    def __init__(self, process):
        self.process = process

    def on_modified(self, event) -> None:
        """
        Manejador de eventos
        """
        # Solo se reinicia si el archivo es de python o de fluml
        file_modified = event.src_path.endswith(".py") or event.src_path.endswith(".fluml")

        if file_modified:
            print(f"Cambio detectado rn {event.src_path}. Reiniciando la aplicación...")
            self.restart()

    def restart(self) -> None:
        """
        Detiene y reinicia el proceso hijo
        """
        # Terminar el proceso actual
        if self.process and self.process.poll() is None:
            self.process.kill()
            self.process.wait() # Espera a que termine
        
        # Inicia un nuevo proceso
        print("Iniciando nuevo proceso...")
        self.process = subprocess.Popen([sys.executable, MAINPY_ROOT])
        print("Proceso iniciado.")

def start_monitoring() -> None:

    print("monitoring...")

    process = subprocess.Popen([sys.executable, MAINPY_ROOT])

    event_handler = EventHandler(process)

    observer = Observer()
    observer.schedule(event_handler, VIEWS, recursive=True)
    observer.schedule(event_handler, STATIC, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(2)
            # Revisa si el proceso hijo ha terminado
            if process.poll() is not None:
                print("El proceso de la aplicación ha terminado. Saliendo del reloader.")
                break
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    if process and process.poll() is None:
        process.kill()
        process.wait()
    