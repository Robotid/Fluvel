from fluvel.core import ViewBuilder
from fluvel.components import VBoxLayout, StringVar
from functools import partial


class LoginPage(ViewBuilder):

    def view(self):

        # La estructura principal responde a un diseño
        # en orientación Vertical
        body = VBoxLayout(self.parent)
        body.adjust(alignment=body.CENTER, spacing=0)

        body.Label(
            text=["title-sign-in"], style="h1 bold", alignment=body.CENTER_BOTTOM
        )

        body.addSpacing(50)

        with self.Form(body) as form:
            form.adjust(spacing=20)
            user_label, self.user_input = form.add_row(label="form-user-field")
            pass_label, pass_input = form.add_row(label="form-password-field")

        with self.Horizontal(body) as footer:
            footer.adjust(alignment=footer.CENTER, spacing=20, margins=(20, 20, 20, 20))
            btn_register = footer.Button(text=["btn-register"], style="dark")
            btn_sign_in = footer.Button(text=["btn-sign-in"])

            body.Label(text=["lbl-forgotten-password"], alignment=footer.CENTER)

        window_instance = self.parent.parentWidget()
        change_language = window_instance.change_language

        def set_buttons_row(widgets: tuple, layout) -> None:

            for widget in widgets:

                text, language = widget

                command = partial(change_language, language)

                layout.Button(
                    text=text, style="primary-outlined w-500", on_click=command
                )

        with self.Horizontal(body) as bottom_1:
            bottom_1.adjust(
                alignment=bottom_1.CENTER, spacing=10, margins=(20, 20, 20, 20)
            )

            first_row = (
                ("spanish", "es"),
                ("english", "en"),
                ("deutsh", "de"),
                ("japanese", "ja"),
                ("russian", "ru"),
                ("french", "fr"),
            )

            set_buttons_row(first_row, bottom_1)
