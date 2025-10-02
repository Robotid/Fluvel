WELCOME_VIEW = """from fluvel import View, Router
from fluvel._user import AppConfig

@Router.route("home")
class HomeView(View):

    def build_ui(self):
    
        with self.Vertical(self.container) as v:
            v.adjust(alignment=v.CENTER, spacing=0)

            v.Label(text=["welcome-greeting"], style="h1")
            v.Label(text=AppConfig.app.copyright, style="h7", alignment=v.CENTER)
"""