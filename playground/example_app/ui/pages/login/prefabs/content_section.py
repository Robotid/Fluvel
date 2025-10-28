from typing import Literal
from fluvel.composer import Canvas, Prefab

from fluvel import Router

SignTypes = Literal["sign-in", "sign-up"]

@Prefab
def ContentSection(canvas: Canvas, _type: SignTypes):

    with canvas.Vertical() as v:
        v.adjust(alignment="center", margins=(50, 0, 50, 50))
        
        # Greeting
        v.Label(text=[f"{_type}-greeting"], style="f-size[38px] font-bold f-color[white]")

        # Description
        v.Label(text=[f"{_type}-description"], style="f-size[14px] f-weight[300] f-color[white]", wordwrap=True, align="center")

        # Button to change into pages 'sign-in', 'sign-up'
        btn = v.Button(text=[f"btn-{_type}"], style="b[1px solid white] rounded-lg w-32 m-top[20px]", alignment="center")

        # Configuring button functionality to allow change into pages
        page, animation = ("sign-in-page", "fade_in") if _type == "sign-up" else ("sign-up-page", "slide_in")
        btn["on_click"] = lambda: Router.show(page, animation)

    return canvas