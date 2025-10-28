from fluvel import Page, route

from ui.components.PredefinedIcons import CloseIcon

from ui.pages.login.prefabs.sign_section import SignSection
from ui.pages.login.prefabs.content_section import ContentSection

@route("sign-in-page")
class SignInPage(Page):

    def build_ui(self):

        self.main_window.menu_bar.hide()

        with self.Horizontal(style="bg-white b-radius[30px]", drag_window=True) as hbody:
            hbody.adjust(margins=(0, 0, 0, 0))

            hbody.Prefab(SignSection(_type="sign-in"))

            with self.Vertical(hbody, style="bg-sign-in-gradient br-left[120px] br-right[30px] b[1px solid #493a96]") as right_side:
            
                right_side.add_widget(CloseIcon("white", self.main_window.close), "right")

                right_side.Prefab(ContentSection(_type="sign-in"))