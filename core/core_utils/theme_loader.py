import os
from utils import APP_ROOT

def load_style_sheet(filename: str, theme: str) -> str:
    """
    Esta función carga y devuelve en forma de *`string`* el contenido de un archivo de hoja de estilos (QSS).
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