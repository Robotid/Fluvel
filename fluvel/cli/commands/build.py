import click, json, os
from fluvel.utils.paths import CONTENT_DIR, PROD_CONTENT_DIR

from fluvel.controllers.ContentHandler import ContentHandler

@click.command
def build() -> None:
    
    generate_json_files()
    
    # Mensaje personalizado
    msg = click.style("[LOG] DO NOT FORGET TO CHANGE THE STATUS TO ", fg="green")
    dev_msg = click.style("'appconfig.toml/DEV_MODE=false'", fg="bright_blue")
    continue_msg = click.style(" TO RUN THE APPLICATION WITH THE OPTIMIZED FILES.", fg="green")

    click.echo(msg + dev_msg + continue_msg)

def generate_json_files() -> None:

    for lang in CONTENT_DIR.iterdir():

        lang = PROD_CONTENT_DIR / lang.name
        lang.mkdir(parents=True, exist_ok=True)

        ContentHandler.load_content("development", lang.name)

        menu_json = lang / "menu.json"
        content_json = lang / f"{lang.name}.json"

        with open(menu_json, "w", encoding="utf-8") as f:
            json.dump(ContentHandler.MENU_CONTENT, f, indent=4, ensure_ascii=False)

        with open(content_json, "w", encoding="utf-8") as f:
            json.dump(ContentHandler.STATIC_CONTENT, f, indent=4, ensure_ascii=False)

        click.echo(f"[LANG] {lang.name} successfully optimized.")
        