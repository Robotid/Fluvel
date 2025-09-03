import click
from .commands.run import run
from .commands.check import check
from .commands.demo import demo
from .commands.reset import reset
from .commands.startproject import startproject
from .commands.build import build


@click.group()
def main() -> None:
    """
    CLI para Fluvel
    """
    pass


# Agregar comandos
main.add_command(run)
main.add_command(check)
main.add_command(demo)
main.add_command(reset)
main.add_command(startproject)
main.add_command(build)


if __name__ == "__main__":
    main()
