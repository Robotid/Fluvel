# views.MainWindow

from core import AppWindow
from components import InfoCard, WarningCard, SuccessCard, DangerCard, LineEdit
from components import Label, InfoLabel, WarningLabel, DangerLabel, SuccessLabel
from components import PushButton, DarkButton
from PySide6.QtWidgets import QListView, QTreeView, QToolBar, QLabel, QTextEdit, QLineEdit, QLCDNumber, QProgressBar, QCalendarWidget, QComboBox, QSlider, QTextBrowser
from utils import get_resource_path
from PySide6.QtGui import QIcon, Qt, QStandardItem, QStandardItemModel
from PySide6.QtCore import QSize, QUrl
from components.gui import StyledText
from core import ViewBuilder

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        view = ViewBuilder()

        with view.Horizontal(self.central_widget) as h:

            # Configuraciones 
            h.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            h.setContentsMargins(50, 50, 50, 50)

        with view.Vertical(h) as v:
            # Guardando una referencia al layout
            login_page = v

            # Haciendo las configuraciones de diseño
            v.setAlignment(Qt.AlignmentFlag.AlignCenter)

            label_title = QLabel(StyledText("title-sign-in").text)
            label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_title.setProperty("class", "h1 bold")

            v.addWidget(label_title)
            
            v.addSpacing(50)

            with view.Form(v) as form:
                # Configurando el diseño del formulario
                form.addRow(Label(StyledText("form-user-field")), QLineEdit(placeholderText=StyledText("form-user-field-back").text))
                form.addRow(Label(StyledText("form-pass-field")), QLineEdit(placeholderText=StyledText("form-pass-field-back").text, echoMode=QLineEdit.EchoMode.Password))

            with view.Horizontal(v) as bottom_reg:
                bottom_reg.addWidget(DarkButton(StyledText("btn-register").text))
                bottom_reg.addWidget(PushButton(StyledText("btn-sign-in").text))
            lbl_new_account = Label(StyledText("lbl-forgotten-password"))
            lbl_new_account.setProperty("class", "h5 is-secondary")
            lbl_new_account.setAlignment(Qt.AlignmentFlag.AlignCenter)
            v.addWidget(lbl_new_account)

        # Implementar el uso de @property para encapsular la lógica de validación de estados
        # Implementar algo que permita conectar/enlazar cualquier widget con cualquier propiedad de otro

        bind = self.menu_bar.bind
        theme = self.root.change_theme

        bind("bootstrap_theme", "triggered", lambda: theme("bootstrap"))
        bind("modern_dark_theme", "triggered", lambda: theme("modern-dark"))
        bind("clean_light_theme", "triggered", lambda: theme("clean-light"))