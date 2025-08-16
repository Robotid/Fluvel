import click
from .commands.run import run
from .commands.check import check
from .commands.demo import demo
from .commands.debug import debug

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
main.add_command(debug)

if __name__ == "__main__":
    main()
