from fluvel.core import ViewBuilder
from fluvel.components.layouts import VBoxLayout


class LoginPage(ViewBuilder):

    def view(self):

        # The main structure
        body = VBoxLayout(self.parent)
        body.adjust(alignment=body.CENTER, margins=(50, 50, 50, 50))

        body.add_label(
            content_id="title-sign-in", style="h1 bold", alignment=body.CENTER
        )

        body.addSpacing(50)

        with self.Form(body) as form:
            form.adjust(spacing=20)
            user_label, user_input = form.add_row(label="form-user-field")
            pass_label, pass_input = form.add_row(label="form-password-field")

        with self.Horizontal(body) as footer:
            btn_register = footer.add_button(content_id="btn-register", style="light")
            btn_sign_in = footer.add_button(content_id="btn-sign-in")

        body.add_label(content_id="lbl-forgotten-password", alignment=footer.CENTER)
