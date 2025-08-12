from fluvel.core import ViewBuilder
from fluvel.components import Button, VBoxLayout


def add_buttons(buttons: tuple | list, layout: any) -> None:
    for button in buttons:
        text, style = button
        layout.add_button(text=text, style=style)


class Demo(ViewBuilder):

    def view(self):

        main = VBoxLayout(self.parent)
        main.adjust(
            margins=(50, 50, 50, 50),
            alignment=main.CENTER,
        )

        # BUTTONS

        main.add_label(text="Buttons", style="h1 bold", alignment=main.CENTER)

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

                column.add(Button(text=normal, style=button))
                column.add(Button(text=outlined, style=f"{button}-outlined"))

        # LABELS

        main.add_label(text="Labels", style="h1 bold", alignment=main.CENTER)

        with self.Horizontal(main) as h1:

            h1.add_label(text="Info", style="info")
            h1.add_label(text="Success", style="success")
            h1.add_label(text="Warning", style="warning")
            h1.add_label(text="Danger", style="danger")
