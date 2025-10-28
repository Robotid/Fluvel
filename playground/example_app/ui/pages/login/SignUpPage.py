from fluvel import Page, route, Router

from .prefabs.row_of_icons import RowOfIcons

from PySide6.QtWidgets import QSizePolicy

from ui.components.PredefinedIcons import CloseIcon

@route("sign-up-page")
class SignUpPage(Page):

    def build_ui(self):

        self.main_window.menu_bar.hide()
        
        with self.Horizontal(style="bg-white b-radius[30px]", drag_window=True) as h:
            h.adjust(margins=(0, 0, 0, 0))

            with self.Vertical(h, style="bg-sign-up-gradient br-right[120px] br-left[30px] p[40px] b[1px solid #4b4792]") as v1:
                v1.adjust(alignment="center")

                v1.Label(text=["welcome-back"], style="f-size[38px] font-bold f-color[white]")
                v1.Label(text=["sign-in-description"], style="f-size[14px] f-weight[300] f-color[white]", wordwrap=True, align="center")
                v1.Button(text=["btn-sign-in"], style="b[1px solid white] rounded-lg w-32 m-top[20px]", alignment="center", on_click=lambda: Router.show("sign-in-page"))
            
            with self.Vertical(h) as v2:
                v2.adjust(alignment="center-top")

                v2.add_widget(CloseIcon("black", self.main_window.close), "top-right")

                with self.Vertical(v2) as content_section:
                    content_section.adjust(spacing=15, margins=(40, 60, 50, 15))

                    content_section.Label(text=["title-sign-up"], style="font-bold f-size[36px]", alignment="center")

                    content_section.Prefab(RowOfIcons)

                    content_section.Label(text=["use-email-registration"], align="center")

                    content_section.LineEdit(placeholder_text=["name-field"])
                    content_section.LineEdit(placeholder_text=["email-field"])
                    
                    content_section.LineEdit(placeholder_text=["password-field"], echo_mode="Password")

                    btn = v2.Button(text=["btn-sign-up"], style="bg[#5138aa] b[none] rounded-lg w-32", alignment="center")
                    btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

