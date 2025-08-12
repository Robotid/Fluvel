import click
import shutil
from fluvel.cli.root_path import PROJECT_ROOT, MAINPY_PATH


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

    template_file = PROJECT_ROOT / "cli" / "templates" / "mainpy_template.py"

    exist = MAINPY_PATH.exists()

    try:

        if not exist:
            shutil.copy(template_file, MAINPY_PATH)
            click.echo("'main.py' -----> was successfully restored.")

        else:
            click.echo("All Fluvel files are working correctly.")

    except PermissionError:
        click.echo(
            f"Error: Permission denied to copy 'main.py' template to '{MAINPY_PATH.parent}'"
        )

    except Exception as e:
        click.echo(f"An error has ocurred: {e}")
