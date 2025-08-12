import click
from fluvel.cli.templates.demostrations.demo_main import demo_app


@click.command("demo")
@click.option("--theme")
def demo(theme: str | None) -> None:
    """
    run an app demo with the chosen '--theme'.
    """

    try:
        click.echo("demo in progress...")

        demo_app(theme)

    except Exception as e:
        click.echo(f"The demo could not be run. Error: {e}")
