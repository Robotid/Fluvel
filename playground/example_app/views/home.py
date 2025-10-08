from fluvel import View, route
from views.prefabs.view_selector import ViewSelector

from fluvel.composer import Prefab

@Prefab
def WarningNote(view: View, *, text: str | list = "default text") -> View:

    with view.Vertical(style="border-l-4 border-solid bcolor-warning") as v:
        v.adjust(spacing=0, margins=(20, 0, 0, 0))

        v.Label(text="Warning", style="text-lg label-warning font-bold")
        
        v.Label(text=text, word_wrap=True)
    
    return view

@route("home")
class Home(View):

    def build_ui(self):

        with self.Vertical(style="bg-slate-100") as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text=["fluvel-welcome-msg"], style="text-4xl font-bold", alignment=v.CENTER)

            v.Prefab(ViewSelector)

            v.Prefab(WarningNote(text="some text"))