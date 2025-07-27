# views.MainWindow

from core import App
from core import AppWindow
from components import InfoCard, WarningCard, SuccessCard, DangerCard
from components import Label, InfoLabel, WarningLabel, DangerLabel, SuccessLabel
from components import PushButton
from PySide6.QtWidgets import QMessageBox, QToolBar, QLabel, QTextEdit
from utils import get_resource_path
from PySide6.QtGui import QIcon, Qt, QKeySequence, QPixmap, QFont, QFontInfo, QDesktopServices
from PySide6.QtCore import QSize, QUrl

import qtawesome as qta

def expect_zero_division_error(controller):
    def wrapper(*args, **kwargs):    
        try:
            return controller(*args, **kwargs)
        except Exception as e:
            print(f"Ha ocurrido un error en {controller.__name__}: {e}")
            message = QMessageBox()
            message.setMinimumSize(700, 700)
            message.setWindowTitle(f"Critical error")
            message.setText(f"An error has ocurred in {controller.__name__}")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            message.setDefaultButton(QMessageBox.Ok)
            ret = message.exec()
            if ret == QMessageBox.Ok:
                print("User chose ok")
            else:
                print("User chose cancel")
    return wrapper

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        components = [
            # Label Alerts De fluvel
            InfoCard(),
            WarningCard(),
            DangerCard(),
            SuccessCard(),
            # Nativas tipo bootstrap
        ]    
        
        for component in components:
            self.layout.addWidget(component)
        
        # self.menu_bar.add_shortcut("quit", "Ctrl+K", self.dividir)

        self.menu_bar.bind("clean_light_theme", "triggered", lambda: self.root.change_theme("clean-light"))
        self.menu_bar.bind("modern_dark_theme", "triggered", lambda: self.root.change_theme("modern-dark"))
        self.menu_bar.bind("modern_dark_esmerald_theme", "triggered", lambda: self.root.change_theme("modern-dark-esmerald"))
        self.menu_bar.bind("bootstrap_theme", "triggered", lambda: self.root.change_theme("bootstrap"))

        self.menu_bar.add_shortcut("undo", "Ctrl+P", self.close)
        self.menu_bar.add_shortcut("new_file", "Ctrl+Alt+N", lambda: print("Ventana para la creación de un nuevo archivo"))

        self.menu_bar.add_shortcut("quit", "Ctrl+S", self.dividir)

        label = SuccessLabel("")

        html_content = (
            "esto es un "
            "<span style='font-style: italic; font-weight: bold;'>PÁRRAFO itálico</span>. Check our "
            "<a href='https://www.youtube.com/watch?v=jeuQ9WRnSjM&t=2179s&ab_channel=NAFTA' style='font-family: consolas; font-weight: bold; color: blue;'>Youtube</a>"
            " channel."
        )

        label.setText(html_content)
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        label.linkActivated.connect(self.open_link)

        self.layout.addWidget(label)

    @expect_zero_division_error
    def dividir(self):
        return 4 / 0

    def open_link(self, link_str):
        print(f"Enlace clicado: {link_str}")    

        QDesktopServices.openUrl(QUrl(link_str))

