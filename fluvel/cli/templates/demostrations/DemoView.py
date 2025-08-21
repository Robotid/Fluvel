from fluvel.core import ViewBuilder
from fluvel.components import FButton, VBoxLayout


class Demo(ViewBuilder):

    def view(self):

        main = VBoxLayout(self.parent)
        main.adjust(
            margins=(20, 20, 20, 20),
            alignment=main.TOP_LEFT,
        )

        # BUTTONS

        main.Label(text="Buttons", style="h1 bold", alignment=main.LEFT)

        with self.Grid(main) as grid:

            buttons = (
                "primary",
                "secondary",
                "info",
                "warning",
                "success",
                "danger",
                "dark",
                "light",
            )

            for i, button in enumerate(buttons, 1):

                normal = button.capitalize() + " Button"
                outlined = button.capitalize() + " Outlined"

                column = grid.Column(i)

                column.add(FButton(text=normal, style=button))
                column.add(FButton(text=outlined, style=f"{button}-outlined"))

        # LABELS

        main.Label(text="Labels", style="h1 bold", alignment=main.LEFT)

        with self.Horizontal(main) as h1:

            h1.Label(text="Info", style="info")
            h1.Label(text="Success", style="success")
            h1.Label(text="Warning", style="warning")
            h1.Label(text="Danger", style="danger")
