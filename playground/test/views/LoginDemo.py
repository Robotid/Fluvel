from fluvel.core import ViewBuilder
from fluvel.components.layouts import VBoxLayout
from fluvel.components.gui.StringVar import StringVar
import time
from fluvel.components.widgets.FCheckBox import FCheckBox


class LoginPage(ViewBuilder):

    def view(self):

        # The main structure
        body = VBoxLayout(self.parent)
        body.adjust(alignment=body.CENTER, margins=(50, 50, 50, 50))

        body.Label(
            content_id="title-sign-in", style="h1 bold", alignment=body.CENTER
        )

        body.addSpacing(50)

        with self.Form(body) as form:
            form.adjust(spacing=20)
            user_label, user_input = form.add_row(label="form-user-field")
            pass_label, pass_input = form.add_row(label="form-password-field")

        with self.Horizontal(body) as footer:
            btn_register = footer.Button(content_id="btn-register", style="light-outlined")
            btn_sign_in = footer.Button(content_id="btn-sign-in", style="danger")

            body.Label(
                content_id="lbl-forgotten-password", 
                alignment=footer.CENTER)

        ##############################################################################

        self.string_var = StringVar("StringVar")

        label = body.Label(textvariable=self.string_var, style="h1 w-500")

        s = body.Label(textvariable=self.string_var, style="success h2")

        self.button_change = body.Button(textvariable=self.string_var, style="dark-outlined h1 italic", on_click=self.change_label)

        body.addWidget(FCheckBox(textvariable=self.string_var))


    def change_label(self) -> None:

        self.string_var.value = "Hora actual: {}".format(time.strftime("%H:%M:%S"))
