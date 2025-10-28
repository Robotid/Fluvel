from fluvel import Router
from fluvel.composer import Factory, Prefab, Canvas

@Factory.compose("FButton")
def ViewButton(text: str, view_route: str) -> None:

    return {
        "text": text,
        "style": "light",
        "on_click": lambda: Router.show(view_route)
    }

@Prefab
def ViewSelector(canvas: Canvas):

    with canvas.Horizontal() as h:
        h.adjust(alignment="center", margins=(50, 50, 50, 50))

        h.ViewButton = h.from_factory(ViewButton, returns=True)
        
        h.ViewButton("Login Page", "login")
        h.ViewButton("Color Palette", "color-palette")
        h.ViewButton("Github Badges", "github-badges")

    return canvas

