from fluvel import View, route
from views.templates.view_selector import ViewSelector

@route("home")
class Home(View):

    def build_ui(self):

        with self.Vertical(style="bg-slate-100") as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text=["fluvel-welcome-msg"], style="text-4xl font-bold", alignment=v.CENTER)
            v.Template(ViewSelector)