from fluvel import View, route

from views.prefabs.language_selector import LanguageSelector
from views.prefabs.view_selector import ViewSelector


@route("hello-world")
class HelloWorld(View):

    def build_ui(self):

        with self.Vertical(style="bg-pink-300") as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text="Hello World", style="text-4xl font-extralight", alignment=v.CENTER)

            v.Prefab(LanguageSelector)
            v.Prefab(ViewSelector)
