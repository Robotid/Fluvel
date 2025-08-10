import click
import shutil
from fluvel.cli.root_path import PROJECT_ROOT, MAINPY_PATH

template_file = PROJECT_ROOT / "cli" / "templates" / "main.py"

@click.command()
def check() -> None:
    """
    Revisa el sistema de directorios del usuario
    para verificar la integridad de los archivos.
    """

    check_mainpy()

def check_mainpy() -> None:
    """
    Si el archivo 'main.py' no es encontrado
    copia la plantilla a la ruta del proyecto
    """

    exist = MAINPY_PATH.exists()

    try:

        if not exist:
            shutil.copy(template_file, MAINPY_PATH)

        else:
            click.echo("All Fluvel files are working correctly.")

    except PermissionError:
        click.echo(f"Error: Permission denied to copy 'main.py' template to '{MAINPY_PATH.parent}'")
    
    except Exception as e:
        click.echo(f"An error has ocurred: {e}") 
