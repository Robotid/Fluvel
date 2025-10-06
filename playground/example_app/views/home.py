from fluvel import View, route
from views.templates.view_selector import ViewSelector

@route("home")
class Home(View):

    def build_ui(self):

        with self.Vertical(style="bg-green-300") as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text=["fluvel-welcome-msg"], style="h1 bold", alignment=v.CENTER)
            v.Template(ViewSelector)
