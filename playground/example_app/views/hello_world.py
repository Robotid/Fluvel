from fluvel import View, route

from playground.example_app.views.templates.language_selector import LanguageSelector
from playground.example_app.views.templates.view_selector import ViewSelector


@route("hello-world")
class HelloWorld(View):

    def build_ui(self):

        with self.Vertical(style="bg-pink-300") as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text="Hello World", style="text-4xl font-extralight", alignment=v.CENTER)

            v.Template(LanguageSelector)
            v.Template(ViewSelector)
