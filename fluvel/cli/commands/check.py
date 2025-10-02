import click
from fluvel.cli.paths import MAINPY_ROOT
from fluvel.cli.templates import MAINPY_TEMPLATE


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

    try:

        if not MAINPY_ROOT.exists():

            with open(MAINPY_ROOT, "w", encoding="utf-8") as f:
                f.write(MAINPY_TEMPLATE)

            click.echo("'main.py' -----> was successfully restored.")

        else:
            click.echo("All Fluvel files are working correctly.")

    except PermissionError:
        click.echo(
            f"Error: Permission denied to copy 'main.py' template to '{MAINPY_ROOT.parent}'"
        )

    except Exception as e:
        click.echo(f"An error has ocurred: {e}")
