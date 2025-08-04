# views.MainWindow

from core import AppWindow
from components import InfoCard, WarningCard, SuccessCard, DangerCard, LineEdit
from components import Label, InfoLabel, WarningLabel, DangerLabel, SuccessLabel
from components import Button
from PySide6.QtGui import Qt
from components.gui import StyledText
from core import ViewBuilder
from components import FormLayout

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        view = ViewBuilder()

        with view.Horizontal(self.central_widget) as h:
            # Configuraciones 
            h.setAlignment(Qt.AlignmentFlag.AlignCenter)
            h.setContentsMargins(50, 50, 50, 50)

        with view.Vertical(h) as v:
            # Guardando una referencia al layout
            login_page = v

            # Haciendo las configuraciones de diseño
            v.setAlignment(Qt.AlignmentFlag.AlignCenter)

            label_title = Label(text=StyledText("title-sign-in"))
            label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_title.setProperty("class", "h1 bold")

            v.add_label(widget=label_title)
            
            v.addSpacing(50)

            with view.Form(v) as form:

                user_input = form.add_row(label="form-user-field")[1]
                pass_label, pass_input = form.add_row(label="form-password-field")
                          
            with view.Horizontal(v) as bottom:
                btn_register = bottom.add_button(text=StyledText("btn-register").text, style="dark")
                btn_sign_in = bottom.add_button(text=StyledText("btn-sign-in").text)

            lbl_new_account = v.add_label(text=StyledText("lbl-forgotten-password"))
            lbl_new_account.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bind = self.menu_bar.bind
        theme = self.root.change_theme

        bind("bootstrap_theme", "triggered", lambda: theme("bootstrap"))
        bind("modern_dark_theme", "triggered", lambda: theme("modern-dark"))
        bind("clean_light_theme", "triggered", lambda: theme("clean-light"))

        self.menu_bar.add_shortcut("quit", "Close", self.close)