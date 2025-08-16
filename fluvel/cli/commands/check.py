import click
import shutil
from fluvel.cli.paths import CLI_TEMPLATES, MAINPY_ROOT


@click.command()
def check() -> None:
    """
    verifies the integrity of files in the file system.
    """

    check_mainpy()


def check_mainpy() -> None:
    """
    If the 'main.py' file is not found,
    copy the template to the project path
    """

    template_file = CLI_TEMPLATES / "mainpy_template.py"

    exist = MAINPY_ROOT.exists()

    try:

        if not exist:
            shutil.copy(template_file, MAINPY_ROOT)
            click.echo("'main.py' -----> was successfully restored.")

        else:
            click.echo("All Fluvel files are working correctly.")

    except PermissionError:
        click.echo(
            f"Error: Permission denied to copy 'main.py' template to '{MAINPY_ROOT.parent}'"
        )

    except Exception as e:
        click.echo(f"An error has ocurred: {e}")
