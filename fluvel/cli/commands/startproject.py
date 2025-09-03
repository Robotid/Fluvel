import click

from fluvel.cli.paths import PROJECT_ROOT, MAINPY_ROOT
from fluvel.cli.templates.mainpy_template import MAINPY_TEMPLATE


@click.command
def startproject() -> None:

    create_mainpy()


def create_mainpy() -> None:

    with open(MAINPY_ROOT, "w", encoding="utf-8") as f:

        f.write(MAINPY_TEMPLATE)
