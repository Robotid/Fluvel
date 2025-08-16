import click
import subprocess
import sys
import importlib
import shutil

# Fluvel
from fluvel.cli.paths import MAINPY_ROOT, PROJECT_ROOT, RELOADER_TEMPLATE

@click.command()
@click.option("--debug", "-d", is_flag=True, help="Enable hot-reloading")
@click.option("--timer", "-t", type=int, default=2, help="Sets the refresh interval for the main window")
def run(debug: bool, timer: int) -> None:
    """
    Start the Fluvel application by running 'main.py'.
    """

    # Si se inicializa en modo debug/hot-reloading
    if debug:

        click.echo("hot-reloading enabled")
        start_monitoring(timer)


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

def start_monitoring(timer: int) -> None:

    reloader_file = PROJECT_ROOT / "reloader.py"

    if not reloader_file.exists():
        
        shutil.copy(RELOADER_TEMPLATE, reloader_file)

    reloader_module = importlib.import_module("reloader")

    # Se llama a la función main del modulo 
    reloader_module.main(timer)