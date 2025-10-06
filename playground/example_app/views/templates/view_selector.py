from fluvel import Template, Router

"""
@Base.wraps("/login")
class Login(View):
    def build_ui(self):
        with self.Vertical(styles="bg-black") as vbody:
            vbody.Label(text="Hola!")
            
"""

class ViewSelector(Template):

    def build_ui(self):

        with self.Horizontal(self.container) as h:
            h.adjust(alignment=h.CENTER)

            h.Button(text="Login Page", on_click=lambda: Router.show("login"))
            h.Button(text="Welcome Page", on_click=lambda: Router.show("home"))
            h.Button(text="Hello World", on_click=lambda: Router.show("hello-world"))