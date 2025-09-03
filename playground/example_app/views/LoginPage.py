from functools import partial
from PySide6.QtWidgets import QSizePolicy

from fluvel.core import ViewBuilder
from fluvel.components import VBoxLayout, FButton

class LoginPage(ViewBuilder):

    def view(self):

        # La estructura principal responde a un diseño
        # en orientación Vertical
        body = VBoxLayout(self.parent)
        body.adjust(alignment=body.CENTER, spacing=0)

        body.Label(text=["title-sign-in"], style="h1 bold", alignment=body.CENTER)

        body.addSpacing(50)

        with self.Form(body) as form:
            form.adjust(spacing=20)

            _, user_field = form.add_row(label="form-user-field")
            _, pass_field = form.add_row(label="form-password-field")

        with self.Horizontal(body) as h:
            h.adjust(alignment=h.CENTER, spacing=20, margins=(20, 20, 20, 20))

            h.Button(text=["btn-register"], style="dark")
            h.Button(text=["btn-sign-in"])

        body.Label(text=["lbl-forgotten-password"], alignment=h.CENTER)

        # Buttons to change the language of the application

        # The fluvel.MainWindow instance
        window_instance = self.parent.parentWidget()

        # The MainWindow.change_language method
        change_language = window_instance.change_language

        def Button(text: str, change_to: str) -> FButton:

            command = partial(change_language, change_to)

            button = FButton(
                text=text, 
                style="primary-outlined w-500", 
                on_click=command
            )

            button.setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
            )

            return button

        with self.Grid(body) as grid:
            grid.adjust(spacing=10, margins=(20, 20, 20, 20))

            c1, c2, c3, c4, c5, c6 = grid.Columns(6)

            # First Row
            c1.add(Button("spanish", "es"))
            c2.add(Button("english", "en"))
            c3.add(Button("deutsch", "de"))
            c4.add(Button("japanese", "ja"))
            c5.add(Button("french", "fr"))
            c6.add(Button("russian", "ru"))

            # Second Row
            c1.add(Button("arab", "ar"))
            c2.add(Button("hindi", "hi"))
            c3.add(Button("korean", "ko"))
            c4.add(Button("chinese", "zh"))
            c5.add(Button("portuguese", "pt"))
            c6.add(Button("telugu", "te"))