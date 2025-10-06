from fluvel import View, route
from fluvel.components import VBoxLayout
from views.templates.view_selector import ViewSelector
from views.templates.language_selector import LanguageSelector


@route("login")
class LoginPage(View):

    def build_ui(self):

        vbody = VBoxLayout(self.container)
        vbody.adjust(alignment=vbody.CENTER)

        vbody.Label(text=["title-sign-in"], style="h1 bold", alignment=vbody.CENTER)

        vbody.addSpacing(50)

        with self.Form(vbody) as form:
            form.adjust(spacing=20)

            _, user_field = form.Row(label="form-user-field")
            _, pass_field = form.Row(label="form-password-field")

            pass_field.setEchoMode(pass_field.EchoMode.Password)

        with self.Horizontal(vbody) as h:
            h.adjust(alignment=h.CENTER, spacing=20, margins=(20, 20, 20, 20))

            h.Button(text=["btn-register"], style="dark")
            h.Button(text=["btn-sign-in"], style="shadow-md")

        vbody.Label(text=["lbl-forgotten-password"], alignment=h.CENTER)

        vbody.Template(LanguageSelector)
        vbody.Template(ViewSelector)
