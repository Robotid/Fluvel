WELCOME_VIEW = """from fluvel import View, route
from fluvel._user import AppConfig

@route("home")
class HomeView(View):

    def build_ui(self):
    
        with self.Vertical(style="bg-slate-100") as v:
            v.adjust(alignment="center", spacing=0)

            v.Label(text=["welcome-greeting"], style="text-4xl")
            v.Label(text=AppConfig.app.copyright, style="f-size[12px]", alignment="center")
"""