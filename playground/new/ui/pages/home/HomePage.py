from fluvel import Page, route

from fluvel.components.widgets.FContainer import FContainer
from fluvel.core.MenuBar import MenuBar

MAIN_MENU: dict = {"quit": {"id": "quit", "text": "退出", "icon": None, "checkable": False, "elements": {"export": {"id": "export", "text": "Export", "elements": {"edit": {"id": "edit", "text": "Edit"}}}}}}

@route("home")
class HomeView(Page):

    def build_ui(self):
    
        with self.Vertical(style="bg-stone-200") as body:
            body.adjust(margins=(0, 0, 0, 0))

            menu = MenuBar(structure=MAIN_MENU)

            menu.configure(
                style= "bg-stone-400 br-top[15px] f-size[15px]",
                on_triggered=[
                    ("quit", print, "Hola a todos")
                ],
            )

            body.add_widget(menu, "bottom")