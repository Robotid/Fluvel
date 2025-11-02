from fluvel import Page, route

from ui.components.PredefinedIcons import CloseIcon

from ui.pages.login.prefabs.sign_section import SignSection
from ui.pages.login.prefabs.content_section import ContentSection

@route("sign-in-page")
class SignInPage(Page):

    def build_ui(self):

        # self.main_window.menu_bar.hide()

        with self.Horizontal(style="bg-white br[30px]", drag_window=True) as hbody:
            hbody.adjust(margins=(0, 0, 0, 0))

            hbody.Prefab(SignSection(page="sign-in"))

            with self.Vertical(hbody, style="bg-sign-in-gradient br-left[120px] br-right[30px] b[1px solid #493a96]") as right_side:
            
                right_side.add_widget(CloseIcon("white", self.main_window.close), "right")

                right_side.Prefab(ContentSection(page="sign-in"))

"""
Para los estilos QSS complejos con interacciones tengo algunas ideas de la sintaxis para el preprocesador QSS:

# hover individuales
':h:f-color[white] :h:br[20px]'

# hover grupales
'::h(f-color[white] br[20px])'

# pressed individuales
':p:f-size[12px] :p:bg[red]'

# pressed grupales
'::p(f-size[12px] bg[red])'
"""