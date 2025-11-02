from fluvel import Page, route

from ui.components.PredefinedIcons import CloseIcon

from ui.pages.login.prefabs.sign_section import SignSection
from ui.pages.login.prefabs.content_section import ContentSection

@route("sign-up-page")
class SignUpPage(Page):

    def build_ui(self):

        self.main_window.menu_bar.hide()
        
        with self.Horizontal(style="bg-white br[30px]", drag_window=True) as hbody:
            hbody.adjust(margins=(0, 0, 0, 0))

            with self.Vertical(hbody, style="bg-sign-up-gradient br-right[120px] br-left[30px] b[1px solid #4b4792]") as left_side:
                left_side.adjust(margins=(0, 30, 0, 0))

                left_side.Prefab(ContentSection(page="sign-up"))

            with self.Vertical(hbody) as right_side:

                right_side.add_widget(CloseIcon("black", self.main_window.close), "right")

                right_side.Prefab(SignSection(page="sign-up"))