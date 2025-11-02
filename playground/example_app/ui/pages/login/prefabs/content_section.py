from typing import Literal
from fluvel import Router
from fluvel.composer import Canvas, Prefab

LoginPages = Literal["sign-in", "sign-up"]

@Prefab
def ContentSection(canvas: Canvas, page: LoginPages):

    with canvas.Vertical() as v:
        v.adjust(alignment="center", margins=(50, 0, 50, 50))
        
        # Greeting
        v.Label(text=[f"{page}-greeting"], style="f-size[38px] font-bold f-color[white]")

        # Description
        v.Label(text=[f"{page}-description"], style="f-size[14px] f-weight[300] f-color[white]", wordwrap=True, align="center")

        # Button to change into pages 'sign-in', 'sign-up'
        btn = v.Button(text=[f"btn-{page}"], style="b[1px solid white] rounded-lg w-32 m-top[20px]", alignment="center")

        # Configuring button functionality to allow change into pages
        page, animation = ("sign-in-page", "fade_in") if page == "sign-up" else ("sign-up-page", "slide_in")
        btn["on_click"] = lambda: Router.show(page, animation)

    return canvas