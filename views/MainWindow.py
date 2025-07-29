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
from components.gui import StyledText

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        components = [
            # Label Alerts De fluvel
            InfoCard(StyledText("py-gui", placeholders=["juan", "maría"])),
            WarningCard(StyledText("warning-card-2")),
            DangerCard(StyledText("info-card-2", placeholders=["juan"])),
            SuccessCard(StyledText("info-card-1", placeholders=["Watashi wa"])),
        ]    
        
        for component in components:
            self.layout.addWidget(component)


        bind = self.menu_bar.bind
        add_shortcut = self.menu_bar.add_shortcut
        set_property = self.menu_bar.set_property

        theme = self.root.change_theme

        bind("modern_dark_theme", "triggered", lambda: theme("modern-dark"))
        bind("bootstrap_theme", "triggered", lambda: theme("bootstrap"))
        bind("custom_theme", "triggered", lambda: theme("my-custom-theme"))

        add_shortcut("copy", "Ctrl+C", self.close)

        set_property("quit", "ToolTip", "Salir de la aplicación")

        label = SuccessLabel()

        html_content = (
            "esto es un "
            "<span style='font-style: italic; font-weight: bold;'>PÁRRAFO itálico</span>. Check our "
            "<a href='https://youtube.com' style='font-family: consolas; font-weight: bold; color: blue;'>Youtube</a>"
            " channel."
        )

        label.setText(html_content)

        label.setTextFormat(Qt.TextFormat.RichText)
        label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        label.linkActivated.connect(self.open_link)

        self.layout.addWidget(label)

        toolbar = QToolBar("My toolbar")
        self.addToolBar(toolbar)
        
        self.menu_bar.bind("quit", "triggered", self.close)

        toolbar.addAction(self.menu_bar.quit)
        toolbar.setMovable(False)


    def open_link(self, link_str):
        print(f"Enlace clicado: {link_str}")    

        QDesktopServices.openUrl(QUrl(link_str))

