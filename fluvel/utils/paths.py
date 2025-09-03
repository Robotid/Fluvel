import os, sys
from pathlib import Path

def get_root_path() -> Path:
    """
     **`ROOT FUNCTION`** This function *returns* the **`APP_ROOT: Path`** of the project.\n
    *Handles both source code execution and packaged executables.*
    """

    if getattr(sys, "frozen", False):
        # Si la app está empaquetada 
        # --onefile
        # --onedir
        return Path(getattr(sys, '_MEIPASS', Path(sys.executable).parent))
    else:
        # Obtener el directorio de trabajo del usuario
        # --dev
        return Path(os.getcwd())

APP_ROOT = get_root_path()

# Common project routes
CONTENT_DIR: Path = APP_ROOT / "static" / "content"

THEMES_DIR: Path = APP_ROOT / "static" / "themes"

# Paths on Prod

PROD_CONTENT_DIR: Path = APP_ROOT / "build_resources"
