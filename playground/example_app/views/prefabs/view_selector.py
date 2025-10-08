from fluvel import View, Router
from fluvel.composer import Factory, Prefab

@Factory.compose("FButton")
def ViewButton(text: str, view_route: str) -> None:

    return {
        "text": text,
        "style": "primary",
        "on_click": lambda: Router.show(view_route)
    }

@Prefab
def ViewSelector(view: View):

    with view.Horizontal() as h:
        h.adjust(alignment=h.CENTER, margins=(50, 50, 50, 50))

        h.ViewButton = h.from_factory(ViewButton, returns=True)
        
        h.ViewButton("Login Page", "login")
        h.ViewButton("Welcome Page", "home")
        h.ViewButton("Hello World", "hello-world")


    return view
