import click
import subprocess
import sys
from fluvel.cli.root_path import MAINPY_PATH

@click.command()
def run() -> None:
    """
    Start the Fluvel application by running 'main.py'.
    """

    click.echo("initializing...")

    # The command to run main.py
    command = [sys.executable, str(MAINPY_PATH)]

    # Try run main.py
    try:

        subprocess.run(command, check=True)

    except FileNotFoundError:
        click.echo(
            "Error: 'main.py' not found. Make sure the main script exists in the project root."
            "Run the 'fluvel check' command to create the file."
        )

    except subprocess.CalledProcessError as e:
        click.echo(f"An error has ocurred: {e}")