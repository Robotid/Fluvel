import click, json
from fluvel.utils.paths import CONTENT_DIR, PROD_CONTENT_DIR, THEMES_DIR
from fluvel.core.tools import load_style_sheet

from fluvel.controllers.ContentHandler import ContentHandler

from fluvel.utils.paths import PROD_THEMES_DIR

@click.command
def build() -> None:
    
    generate_json_files()
    generate_themes()
    
    # Mensaje personalizado
    msg = click.style("[LOG] DO NOT FORGET TO CHANGE THE STATUS TO ", fg="green")
    dev_msg = click.style("'appconfig.toml/DEV_MODE=false'", fg="bright_blue")
    continue_msg = click.style(" TO RUN THE APPLICATION WITH THE OPTIMIZED FILES.", fg="green")

    click.echo(msg + dev_msg + continue_msg)

def generate_json_files() -> None:

    for lang in CONTENT_DIR.iterdir():

        prod_lang_dir = PROD_CONTENT_DIR / lang.name
        prod_lang_dir.mkdir(parents=True, exist_ok=True)

        menus_folder = prod_lang_dir / "menus"
        menus_folder.mkdir(parents=True, exist_ok=True)

        ContentHandler.load_content("development", lang.name)

        menus_json = menus_folder / "menus.json"
        content_json = prod_lang_dir / f"{lang.name}.json"

        with open(menus_json, "w", encoding="utf-8") as f:
            json.dump(ContentHandler.MENU_CONTENT, f, indent=4, ensure_ascii=False)

        with open(content_json, "w", encoding="utf-8") as f:
            json.dump(ContentHandler.STATIC_CONTENT, f, indent=4, ensure_ascii=False)

        click.echo(f"[LANG] {lang.name} successfully optimized.")

def generate_themes() -> None:

    PROD_THEMES_DIR.mkdir(parents=True, exist_ok=True)

    for theme in THEMES_DIR.iterdir():

        theme_file = PROD_THEMES_DIR / f"{theme.name}.qss"
        
        # Lista con los archivos .qss
        qss_files: list = theme.rglob("*.qss")

        # Contenido que se cargará a la ui
        qss_content: str = ""

        # Iterando y concatenando el contenido QSS de los archivos
        for qss_file in qss_files:
            qss_content += load_style_sheet(qss_file)

        with open(theme_file, "w", encoding="utf-8") as f:
            f.write(qss_content)

        click.echo(f"[THEME] adding {theme.name}.")