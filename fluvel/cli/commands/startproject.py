import click
from pathlib import Path

from fluvel.cli.paths import PROJECT_ROOT, MAINPY_ROOT
from fluvel.cli.templates import MAINPY_TEMPLATE, WELCOME_VIEW, WINDOW_TEMPLATE, APPCONFIG_TEMPLATE, HOME_GREETING, COMPACT_BOOTSTRAP

# Folders
from fluvel.utils.paths import CONTENT_DIR, THEMES_DIR, VIEWS_DIR, STATIC_DIR

FOLDERS = [
    STATIC_DIR,
    CONTENT_DIR / "en", 
    THEMES_DIR, 
    VIEWS_DIR,
    PROJECT_ROOT / "assets",
    PROJECT_ROOT / "components",
    THEMES_DIR / "bootstrap"
]

FILE_TEMPLATES = [
    (MAINPY_ROOT, MAINPY_TEMPLATE),
    (VIEWS_DIR / "home.py", WELCOME_VIEW),
    (PROJECT_ROOT / "window.py", WINDOW_TEMPLATE),
    (PROJECT_ROOT / "appconfig.toml", APPCONFIG_TEMPLATE),
    (CONTENT_DIR / "en" / "homepage.fluml", HOME_GREETING),
    (THEMES_DIR / "bootstrap" / "compact-bootstrap.qss", COMPACT_BOOTSTRAP),
]

@click.command
def startproject() -> None:

    create_project_structure()

    create_file_templates()

def create_project_structure() -> None:
    
    for folder in FOLDERS:
        folder.mkdir(parents=True, exist_ok=True)

def create_file_templates():

    for file in FILE_TEMPLATES:
        
        try:

            with open(file[0], "w", encoding="utf-8") as f:

                f.write(file[1])

        except FileNotFoundError as e:
            click.echo(e)