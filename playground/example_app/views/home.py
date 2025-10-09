from typing import Literal, Unpack
from fluvel import View, route
from views.prefabs.view_selector import ViewSelector

from fluvel.composer import Prefab

NoteTypes = Literal["success", "warning", "info", "danger"]

@Prefab
def Note(view: View, type_: Unpack[NoteTypes], title: str | list, message: str | list):

    with view.Vertical(style=f"border-l-4 border-solid bcolor-{type_}") as v:
        v.adjust(spacing=0, margins=(20, 0, 0, 0))

        v.Label(text=f"Warning! {title}", style=f"text-lg alert-{type_} font-bold")
        
        v.Label(text=message, word_wrap=True, style="font-bold")

    return view

@route("home")
class Home(View):

    def build_ui(self):

        with self.Vertical(style="bg-slate-100") as v:
            v.adjust(alignment=v.CENTER)

            v.Label(text=["fluvel-welcome-msg"], style="text-4xl font-bold", alignment=v.CENTER)

            v.Prefab(Note(type_="warning", title="some warning", message="description of the warning"))
            
            v.Prefab(ViewSelector)