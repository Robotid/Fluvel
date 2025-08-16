import click
import importlib

@click.command()
@click.option("--timer", is_flag=2, help="Enable hot-reloading")
def debug(debug: bool, timer: int):

    # Obtener el módulo reloader de ProjectRoot
    reloader_module = importlib.import_module("reloader")

    reloader_module.main(timer)

