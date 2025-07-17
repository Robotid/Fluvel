from typing import Literal
import os
from pathlib import Path
from utils import APP_ROOT

_RESOURCE_FOLDERS = {
        "style":"styles",
        "img":"images",
        "ico":"icons",
        "data":"data",
        "template":"templates",
        "font":"fonts"
}

def get_resource_path(filename: str, resource_type: Literal["style", "img", "ico", "data", "template", "font"]) -> str:
    """
    Construye la ruta absoluta a un recurso específico.

    Args:
        resource_type (Literal): El tipo de recurso (ej. "style", "img").
        filename (str): El nombre del archivo del recurso.

    Returns:
        str: La ruta absoluta al recurso.
    """
    if resource_type not in _RESOURCE_FOLDERS:
        raise ValueError(f"Tipo de recurso '{resource_type}' no soportado. Tipos válidos: {list(_RESOURCE_FOLDERS.keys())}")

    # Construye la ruta completa: APP_ROOT/resources/tipo_de_recurso/filename
    folder_name = _RESOURCE_FOLDERS[resource_type]
    resource_full_path = os.path.join(APP_ROOT, 'resources', folder_name, filename)
    return resource_full_path


def get_theme_path(theme: str) -> Path:
    theme_path = Path()


def load_style_sheet(filename: str, theme: str) -> str:
    """
    Carga el contenido de un archivo de hoja de estilos (QSS).

    Args:
        filename (str): El nombre del archivo de la hoja de estilos (ej. "app_style.qss").

    Returns:
        str: El contenido de la hoja de estilos, o una cadena vacía si no se encuentra.
    """
    # file_path = get_resource_path("style", filename)
    file_path = os.path.join(APP_ROOT, "resources", "styles", "themes", theme, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            style_content = f.read()
            
        return style_content
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {filename} en la ruta {file_path}.")
        return ""
        
    except Exception as e:
        print(f"Error al leer el archivo de hoja de estilos '{filename}': {e}.")
        return ""