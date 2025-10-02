import click, subprocess, sys, importlib

# Fluvel
from fluvel.cli.paths import MAINPY_ROOT
from fluvel.cli.reloader.reloader_manager import HReloader

# Expect Handler
from fluvel.core.exceptions.expect_handler import expect

@click.command()
@click.option("--debug", "-d", is_flag=True, help="Enable hot-reloading")
def run(debug: bool) -> None:
    """
    Start the Fluvel application by running 'main.py'.
    """

    if not MAINPY_ROOT.exists():
        click.echo(
            "Error: 'main.py' not found. Make sure the main script exists in the project root. "
            "Run the 'fluvel check' command to create the file."
        )
        sys.exit(1)


    # Si se inicializa en modo debug/hot-reloading
    if debug:

        click.echo("Hot Reloading Enabled")
        start_monitoring()

    else:

        # The command to run main.py
        command = [sys.executable, str(MAINPY_ROOT)]

        # Try to run main.py
        try:
            click.echo(f"initializing...")
            subprocess.run(command, check=True)

        except subprocess.CalledProcessError as e:
            click.echo(f"An error has occurred: {e}")
            click.echo("---")
            click.echo("Details of the error from main.py:")
            click.echo(e.stderr)

@expect.ErrorImportingModule(stop=True)
@expect.MismatchedKey(
    msg="Reloader Error: La instancia de <FluvelApp> $e no se encontró. Asegúrate de nombrarla $e en el módulo 'main.py' para poder usar el Hot-Reloader.",
    stop=True
)
def start_monitoring() -> None:
    """
    Comienza la creación de una nueva ventana
    PySide6 a partir del módulo `reloader.py` y
    `fluvel/cli/reloader/reloader_manager`
    """

    main_module = importlib.import_module("main")

    app_root = main_module.__dict__["app"]

    reloader = HReloader(app_root.main_window, app_root._app, app_root)

    app_root.run()
