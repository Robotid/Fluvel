import click

# Defaults
from fluvel.core.core_utils.generate_menu_options import (
    _DEFAULT_MENU_OPTIONS,
    USER_FOLDER,
)

@click.command(name="reset", hidden=True)
def reset() -> None:
    """
    Reinicia la configuración de Archivos y Directorios antes de una publicación.
    """

    # Resetear las opciones del menú
    reset_menu_options()

def reset_menu_options() -> None:
    """
    Resetea el archivo fluvel._user.MenuOptions.py
    con su configuración _DEFAULT_MENU_OPTIONS.
    """

    file_path = USER_FOLDER / "MenuOptions.py"

    try:

        with open(file_path, "w") as f:

            f.write(_DEFAULT_MENU_OPTIONS)

        click.echo("_user.MenuOptions.py reseteado exitosamente")

    except Exception as e:

        click.echo(f"Ha ocurrido un error: {e}")