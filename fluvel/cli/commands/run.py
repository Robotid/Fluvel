import click
import subprocess
import sys
from fluvel.cli.root_path import MAINPY_PATH


@click.command()
@click.option("--debug", "-d", is_flag=True, help="Enable hot-reloading")
def run(debug: bool) -> None:
    """
    Start the Fluvel application by running 'main.py'.
    """

    # First check if the file exists
    if not MAINPY_PATH.exists():
        click.echo(
            "Error: 'main.py' not found. Make sure the main script exists in the project root. "
            "Run the 'fluvel check' command to create the file."
        )
        sys.exit(1)

    # TODO Hot-Reloading
    if debug:
        click.echo("hot-reloading enabled")

    # The command to run main.py
    command = [sys.executable, str(MAINPY_PATH)]

    # Try to run main.py
    try:

        click.echo("initializing...")
        subprocess.run(command, check=True, text=True, capture_output=True)

    except subprocess.CalledProcessError as e:
        click.echo(f"An error has occurred: {e}")
        click.echo("---")
        click.echo("Details of the error from main.py:")
        click.echo(e.stderr)
