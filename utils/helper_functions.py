import sys
from pathlib import Path

def get_root_path() -> str:
    """
    This function returns the **`APP_ROOT: Path`** of the project.
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

def minify_qss(qss_content: str) -> str:
    """
    -> **TO DO** <-\n
    Minimiza una cadena QSS eliminando espacios en blanco y comentarios.
    """
    ...