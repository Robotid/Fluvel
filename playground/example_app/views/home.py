from fluvel import View, Router
from views.templates.view_selector import ViewSelector

@Router.route("home")
class Home(View):

    def build_ui(self):
        self.container.setObjectName("home-container")
    
        with self.Vertical(self.container) as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text=["fluvel-welcome-msg"], style="h1 bold", alignment=v.CENTER)
            v.Template(ViewSelector)