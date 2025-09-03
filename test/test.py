from pathlib import Path

# Templates
from fluvel.cli.templates.mainpy_template import MAINPY_TEMPLATE

current_dir = Path(__file__).parent
# Folders
STATIC = current_dir / "static"
CONTENT = STATIC / "content"
THEMES = STATIC / "themes"
VIEWS = current_dir / "views"
PROJECT = current_dir / "project"

folders = [STATIC, CONTENT, THEMES, VIEWS, PROJECT]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Files
APPCONFIG = current_dir / "appconfig.toml"
MAINPY = current_dir / "main.py"

appconfig_template = "prueba toml"

files = ((APPCONFIG, appconfig_template), (MAINPY, MAINPY_TEMPLATE))


def set_files(files: tuple) -> None:

    for file in files:

        path, template = file

        with open(path, "w") as f:
            f.write(template)

set_files(files)