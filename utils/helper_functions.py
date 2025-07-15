import sys
from pathlib import Path

def get_root_path() -> str:
    """
    Esta función devuelve el Root Path del proyecto
    """

    APP_ROOT: str

    if getattr(sys, "frozen", False):
        # Si la app está empaquetada
        APP_ROOT = Path(sys.executable).parent
    else:
        # Si se ejecuta desde el código fuente
        # Path desde este archivo. 
        # parent 1 -> .../utils/
        # parent 2 -> .../PySide-Course  <carpeta raíz de la aplicación>
        APP_ROOT = Path(__file__).parent.parent

    return APP_ROOT