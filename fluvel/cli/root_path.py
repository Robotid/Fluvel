"""
En este módulo se gestionan los paths usados en el CLI
"""

from pathlib import Path

current_file_path = Path(__file__).resolve()

PROJECT_ROOT = current_file_path.parent.parent

MAINPY_PATH = PROJECT_ROOT / "main.py"