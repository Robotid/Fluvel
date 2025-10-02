# fluvel/cli/templates/demostrations/demo.py

from fluvel import FluvelApp

def demo_app(theme: str | None):

    # App
    app = FluvelApp("fluvel.cli.templates.demostrations.DemoWindow")
    app.register(
        initial="/demo-widgets",
        views=[
            "fluvel.cli.templates.demostrations.DemoView"
        ]
    )

    if theme:
        app.change_theme(theme)

    app.run()