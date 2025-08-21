"""
En este módulo se gestionan los paths usados en la CLI
"""

from pathlib import Path
import os, sys

# El directorio de trabajo del usuario
PROJECT_ROOT = Path(os.getcwd())

# Añadimos el project_root al sys.path
sys.path.append(str(PROJECT_ROOT))

MAINPY_ROOT = PROJECT_ROOT / "main.py"


# TEMPLATES
CLI_TEMPLATES = Path(__file__).parent / "templates"
from fluvel.cli.templates.mainpy_template import MAINPY_TEMPLATE
from fluvel.cli.templates.reloader_template import RELOADER_TEMPLATE
