from fluvel import View, Router

from playground.example_app.views.templates.language_selector import LanguageSelector
from playground.example_app.views.templates.view_selector import ViewSelector

@Router.route("hello-world")
class HelloWorld(View):

    def build_ui(self):

        with self.Vertical(self.container) as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text="Hello World", style="h1 w-200", alignment=v.CENTER)

            v.Template(LanguageSelector)
            v.Template(ViewSelector)