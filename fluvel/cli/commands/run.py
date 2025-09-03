import click, subprocess, sys, importlib, os

# Fluvel
from fluvel.cli.paths import MAINPY_ROOT, PROJECT_ROOT, RELOADER_TEMPLATE

@click.command()
@click.option("--debug", "-d", is_flag=True, help="Enable hot-reloading")
def run(debug: bool) -> None:
    """
    Start the Fluvel application by running 'main.py'.
    """

    # Si se inicializa en modo debug/hot-reloading
    if debug:

        click.echo("Hot Reloading Enabled")
        start_monitoring()

    else:

        # First check if the file exists
        if not MAINPY_ROOT.exists():
            click.echo(
                "Error: 'main.py' not found. Make sure the main script exists in the project root. "
                "Run the 'fluvel check' command to create the file."
            )
            sys.exit(1)

        # The command to run main.py
        command = [sys.executable, str(MAINPY_ROOT)]

        # Try to run main.py
        try:
            click.echo("initializing...")
            subprocess.run(command, check=True)

        except subprocess.CalledProcessError as e:
            click.echo(f"An error has occurred: {e}")
            click.echo("---")
            click.echo("Details of the error from main.py:")
            click.echo(e.stderr)

def start_monitoring() -> None:
    """
    Comienza la creación de una nueva ventana
    PySide6 a partir del módulo `reloader.py` y
    `fluvel/cli/reloader/reloader_manager`
    """

    reloader_file = PROJECT_ROOT / "reloader.py"

    if not reloader_file.exists():

        with open(reloader_file, "w", encoding="utf-8") as f:
            f.write(RELOADER_TEMPLATE)

    reloader_module = importlib.import_module("reloader")

    # Al finalizar, se borra el archivo reloader.py
    os.remove(reloader_file)

    # Se llama a la función main del modulo
    reloader_module.main()
