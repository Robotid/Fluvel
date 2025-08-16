"""
En este módulo se gestionan los paths usados en la CLI
"""

from pathlib import Path
import os
import sys

# El directorio de trabajo del usuario
PROJECT_ROOT = Path(os.getcwd())

# Añadimos el project_root al sys.path
sys.path.append(str(PROJECT_ROOT))

MAINPY_ROOT = PROJECT_ROOT / "main.py"

CLI_TEMPLATES = Path(__file__).parent / "templates"

RELOADER_TEMPLATE = CLI_TEMPLATES / "reloader_template.py"

