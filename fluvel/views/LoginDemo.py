from core import ViewBuilder
from components.layouts import VBoxLayout

class LoginPage(ViewBuilder):

    def view(self):
        
        # The main structure
        main = VBoxLayout(self.parent)
        main.adjust(alignment=main.CENTER, margins=(50, 50, 50, 50))

        main.add_label(content_id="title-sign-in", style="h1 bold", alignment=main.CENTER)
        
        main.addSpacing(50)

        with self.Form(main) as form:
            form.adjust(spacing=20)
            user_input = form.add_row(label="form-user-field")[1]
            pass_label, pass_input = form.add_row(label="form-password-field")

        with self.Horizontal(main) as bottom_side:
            btn_register = bottom_side.add_button(content_id="btn-register", style="dark-outlined")
            btn_sign_in = bottom_side.add_button(content_id="btn-sign-in")

        lbl_new_account = main.add_label(content_id="lbl-forgotten-password")
        lbl_new_account.setAlignment(bottom_side.CENTER)

