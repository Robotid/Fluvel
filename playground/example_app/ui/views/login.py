from fluvel import View, route

from ui.prefabs.view_selector import ViewSelector
from ui.prefabs.language_selector import LanguageSelector


@route("login")
class LoginPage(View):

    def build_ui(self):

        with self.Vertical(style="bg-slate-200") as vbody:

            vbody.Label(text=["title-sign-in"], style="text-4xl font-bold m-8", alignment=vbody.CENTER)

            with self.Form(vbody, style="bg-blue-200 rounded-lg p-8") as form:
                form.adjust(spacing=20)

                _, user_field = form.Row(label="form-user-field")
                _, pass_field = form.Row(label="form-password-field")

                pass_field.setEchoMode(pass_field.EchoMode.Password)

            with self.Horizontal(vbody) as h:
                h.adjust(alignment=h.CENTER, spacing=20, margins=(20, 20, 20, 20))

                h.Button(text=["btn-register"], style="dark")
                h.Button(text=["btn-sign-in"], style="primary")

            vbody.Label(text=["lbl-forgotten-password"], alignment=h.CENTER)

            vbody.Prefab(LanguageSelector)
            vbody.Prefab(ViewSelector)