import os
from utils import APP_ROOT
from pathlib import Path

def get_theme_path(theme: str):
    """
    Esta función retorna la ruta absoluta de un tema qss determinado.
    """
    theme_path = APP_ROOT / "resources" / "styles" / theme 

    return theme_path

def load_style_sheet(file_path: str | Path) -> str:
    """
    Esta función carga y devuelve en forma de *`string`* el contenido de un archivo de hoja de estilos (QSS).
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            style_content = f.read()
            
        return style_content
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path.name} en la ruta {file_path}.")
        return ""
        
    except Exception as e:
        print(f"Error al leer el archivo de hoja de estilos '{file_path.name}': {e}.")
        return ""
    