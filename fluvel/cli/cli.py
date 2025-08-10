import click
from fluvel.cli.commands.run import run
from fluvel.cli.commands.check import check

@click.group()
def main() -> None:
    """
    CLI para Fluvel
    """
    pass

# Agregar comandos
main.add_command(run)
main.add_command(check)

if __name__ == "__main__":
    main()