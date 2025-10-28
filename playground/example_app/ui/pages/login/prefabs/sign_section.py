from typing import Literal
from fluvel.composer import Canvas, Prefab

from PySide6.QtWidgets import QSizePolicy

from ui.pages.login.prefabs.row_of_icons import RowOfIcons

SignTypes = Literal["sign-in", "sign-up"]

@Prefab
def SignSection(canvas: Canvas, _type: SignTypes):

    with canvas.Vertical() as v:
        v.adjust(spacing=15, alignment="center", margins=(50, 50, 50, 50))
        
        # Title
        v.Label(text=[f"title-{_type}"], style="font-bold f-size[36px]", align="center")

        # Rof of Icons
        v.Prefab(RowOfIcons)

        # Subtitle
        v.Label(text=[f"subtitle-{_type}"], align="center")

        # Entry Field "name" (only in 'sign-up' page)
        if _type == "sign-up":
            v.LineEdit(placeholder_text=[f"name-field"])

        # Entry Field "Email"
        v.LineEdit(placeholder_text=[f"email-field"])

        # Entry Field "Password"
        v.LineEdit(placeholder_text=[f"password-field"], echo_mode="Password")

        # Label "Forget your password?" (only in 'sign-in' page)
        if _type == "sign-in":
            v.Label(text=["forget-password"], align="center")
        
        # Sign Button
        btn = v.Button(text=[f"btn-{_type}"], style="bg[#5138aa] b[none] rounded-lg w-32", alignment="center")
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        # Credits
        v.Label(text=["asmr-prog-credits"], style="f-size[10px]", align="center-bottom")

    return canvas