from fluvel import Page, route, Router

from PySide6.QtWidgets import QSizePolicy

from playground.example_app.ui.pages.login.prefabs.row_of_icons import RowOfIcons
from ui.components.PredefinedIcons import CloseIcon
from ui.components.IconButton import IconButton

@route("sign-in-page")
class SignInPage(Page):

    def build_ui(self):

        self.main_window.menu_bar.hide()

        with self.Horizontal(style="bg-white b-radius[30px]", drag_window=True) as hbody:
            hbody.adjust(margins=(0, 0, 0, 0))

            with self.Vertical(hbody) as left_side:
                left_side.adjust(alignment="center-top", margins=(70, 100, 50, 70), spacing=15)

                left_side.Label(text=["login-title"], style="font-bold f-size[36px]", alignment="center")

                left_side.Prefab(RowOfIcons)

                left_side.Label(text=["use-email"], align="center")

                left_side.LineEdit(placeholder_text=["email-field"])
                left_side.LineEdit(placeholder_text=["password-field"], echo_mode="Password")

                left_side.Label(text=["forget-password"], align="center")

                btn = left_side.Button(text=["btn-sign-in"], style="bg[#5138aa] b[none] rounded-lg w-32", alignment="center")
                btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

                left_side.Label(text=["asmr-prog-credits"], style="f-size[10px]", align="center-bottom")

            with self.Vertical(hbody, style="bg-sign-in-gradient br-left[120px] br-right[30px] b[1px solid #493a96]") as right_side:
                right_side.adjust(alignment="center-top")
            
                right_side.add_widget(CloseIcon("white", self.main_window.close), "top-right")

                with self.Vertical(right_side, style="m-top[150px] p-left-right[50px]") as content_section:

                    content_section.Label(text=["greeting"], style="f-size[38px] font-bold f-color[white]")
                    content_section.Label(text=["sign-up-description"], style="f-size[14px] f-weight[300] f-color[white]", wordwrap=True, align="center")
                    content_section.Button(text=["btn-sign-up"], style="b[1px solid white] rounded-lg w-32 m-top[20px]", alignment="center", on_click=lambda: Router.show("sign-up-page", "slide_in"))

            