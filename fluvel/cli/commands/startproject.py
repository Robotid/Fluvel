"""
This module implements the `fluvel startproject` command to initialize a new Fluvel project.

The command generates the essential folder and file architecture, providing a 
functional starting point that includes a main window, TOML configuration, 
a welcome view, and the default QSS theme.

Proposed architecture generated:

root:
├───assets                  # Binary resources (images, fonts, etc.)
├───static  
│   ├───content             # Fluml and i18n content files
│   │   └───en              # (Example) Language files for English
│   └───themes              # QSS stylesheets (.qss)
│       └───bootstrap       # Initial theme (e.g., compact-bootstrap.qss)
├───ui                      # UI source code
│   ├───components          # Simple, reusable widgets @Factory.compose
│   ├───prefabs             # Complex components decorated with @Prefab
│   └───pages               # Main application pages       
│       └───home            # Dedicated directory for the composition of the home page
|           └───HomePage.py # Example page (Home) 
│   appconfig.toml          # Global application configuration file
│   main.py                 # Application entry point
│   window.py               # Custom AppWindow(QMainWindow) class
"""

from typing import List, Tuple
from pathlib import Path
import click

# Fluvel CLI/Utils Paths
from fluvel.cli.paths import PROJECT_ROOT, MAINPY_ROOT
from fluvel.cli.templates import MAINPY_TEMPLATE, WELCOME_VIEW, WINDOW_TEMPLATE, APPCONFIG_TEMPLATE, HOME_GREETING, COMPACT_BOOTSTRAP

# Folders
from fluvel.utils.paths import CONTENT_DIR, THEMES_DIR, PAGES_DIR, STATIC_DIR, UI_DIR

FOLDERS: List[Path] = [
    STATIC_DIR,
    CONTENT_DIR / "en", 
    THEMES_DIR, 
    PROJECT_ROOT / "assets",
    UI_DIR,
    UI_DIR / "components",
    UI_DIR / "prefabs",
    PAGES_DIR,
    PAGES_DIR / "home",
    THEMES_DIR / "bootstrap"
]

FILE_TEMPLATES: List[Tuple[Path, str]] = [
    (MAINPY_ROOT, MAINPY_TEMPLATE),
    (PAGES_DIR / "home" / "HomePage.py", WELCOME_VIEW),
    (PROJECT_ROOT / "window.py", WINDOW_TEMPLATE),
    (PROJECT_ROOT / "config.toml", APPCONFIG_TEMPLATE),
    (CONTENT_DIR / "en" / "homepage.fluml", HOME_GREETING),
    (THEMES_DIR / "bootstrap" / "compact-bootstrap.qss", COMPACT_BOOTSTRAP),
]

def create_project_structure() -> None:
    """
    Create all necessary folders for the Fluvel architecture.

    Use `Path.mkdir` with `parents=True` to create nested directories 
    and `exist_ok=True` to avoid failure if the folder already exists.
    """
    
    for folder in FOLDERS:
        folder.mkdir(parents=True, exist_ok=True)

def create_file_templates():
    """
    Generates the initial code and configuration files from templates.

    This includes the entry point (main.py), the example view (home.py), 
    and the initial styles file. If the file already exists, it will be overwritten.
    """

    for file in FILE_TEMPLATES:
        
        try:

            with open(file[0], "w", encoding="utf-8") as f:

                f.write(file[1])

        except FileNotFoundError as e:
            click.echo(e)

def display_welcome_message() -> None:

    project_path = PROJECT_ROOT.resolve()
    TREE_STRUCTURE = """root:
├───assets                  # Binary resources (images, fonts, etc.)
├───static  
│   ├───content             # Fluml and i18n content files
│   │   └───en              # (Example) Language files for English
│   └───themes              # QSS stylesheets (.qss)
│       └───bootstrap       # Initial theme (e.g., compact-bootstrap.qss)
├───ui                      # UI source code
│   ├───components          # Simple, reusable widgets @Factory.compose
│   ├───prefabs             # Complex components decorated with @Prefab
│   └───pages               # Main application pages       
│       └───home            # Dedicated directory for the composition of the home page
│           └───homepage.py # Example page (Home) 
│   appconfig.toml          # Global application configuration file
│   main.py                 # Application entry point
│   window.py               # Custom AppWindow(QMainWindow) class
"""

    # Mensaje Final Estilizado

    proj_path = click.style(project_path, fg="bright_blue")
    
    click.echo(click.style(f"\nWelcome to Fluvel Framework (v0.1.2b1)", fg='bright_yellow',))
    click.echo(f"{"="*38}")
    click.echo(click.style(f"\nApp successfully created in: {proj_path}", fg='bright_green'))

    url = click.style("https://github.com/Robotid/Fluvel.", fg="bright_blue")
    click.echo(click.style(f"You can consult the documentation and tutorials at {url}", fg="bright_green"))

    # Estructura del Proyecto (Con color para destacar rutas)
    click.echo(click.style("\nStructure of Fluvel Architecture:", bold=True, fg='yellow'))
    click.echo(click.style("--------------------------------------", fg='yellow'))
    
    # Imprimir el árbol de estructura con colores: 
    # Usaremos 'blue' para directorios lógicos y 'white' para comentarios/archivos.
    styled_tree = TREE_STRUCTURE.replace("├───", click.style("├───", fg='blue'))
    styled_tree = styled_tree.replace("└───", click.style("└───", fg='blue'))
    styled_tree = styled_tree.replace("│", click.style("│", fg='blue'))
    styled_tree = styled_tree.replace("root:", click.style("root:", fg='blue', bold=True))
    
    click.echo(styled_tree)

@click.command
def startproject() -> None:
    """
    Main CLI command to initialize a new Fluvel project.

    This command is executed via `fluvel startproject`.

    Flow:
    1. Calls :py:func:`create_project_structure` to generate the folder hierarchy.
    2. Calls :py:func:`create_file_templates` to populate the initial files.
    """
    create_project_structure()
    create_file_templates()
    display_welcome_message()

