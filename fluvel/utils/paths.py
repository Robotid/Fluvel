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


# =========
# ROOT PATH
# =========

APP_ROOT = get_root_path()

# ===================================
# PATHS ON PRODUCTION (DEV_MODE=true)
# ===================================

# ==========
# STATIC DIR
# ==========

STATIC_DIR = APP_ROOT / "static"

CONTENT_DIR: Path = STATIC_DIR / "content"

THEMES_DIR: Path = STATIC_DIR / "themes"

# ======
# UI DIR
# ======

UI_DIR: Path = APP_ROOT / "ui"

PAGES_DIR: Path = UI_DIR / "pages"

# ====================================
# PATHS ON PRODUCTION (DEV_MODE=false)
# ====================================

# Text content
PROD_CONTENT_DIR: Path = APP_ROOT / "build_resources"

# Themes
PROD_THEMES_DIR: Path = PROD_CONTENT_DIR / "_themes"