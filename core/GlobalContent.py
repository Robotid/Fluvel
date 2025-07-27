# core.GlobalContent.py
from utils import filter_by_extension, APP_ROOT

class GlobalContent:
    
    files: list
    content: dict

    def get_content_files(self) -> None:
        """
        Esta función carga los archivos de contenido de la aplicación.
        """
        ...