# views.MainWindow

from core import App
from core import AppWindow
from components import FluvelInfoAlert, FluvelWarningAlert, FluvelSuccessAlert, FluvelDangerAlert, FluvelAlert
from components import Label, InfoLabel, WarningLabel, DangerLabel, SuccessLabel
from components import PushButton
from PySide6.QtWidgets import QMessageBox, QToolBar
from utils import get_resource_path
from PySide6.QtGui import QIcon, Qt, QKeySequence
from PySide6.QtCore import QSize

import qtawesome as qta


def expect_zero_division_error(controller):
    def wrapper(*args, **kwargs):    
        try:
            return controller(*args, **kwargs)
        except Exception as e:
            print(f"Ha ocurrido un error en {controller.__name__}:")
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

        button = PushButton("LinkButton", "LinkButton")

        components = [
            # Label Alerts De fluvel
            FluvelInfoAlert(f"Nombre de la Aplicación: {self.app_name}"),
            FluvelWarningAlert(f"Versión: {self.version}"),
            FluvelSuccessAlert(f"Tema: {self.theme}"),
            FluvelDangerAlert(f"Tamaño de Ventana: {self.window_width}x{self.window_height}."),
            # Nativas tipo bootstrap
            # InfoLabel("Texto informativo"),
            # DangerLabel("Esta función está deprecated"),
            # WarningLabel("Advertencia"),
            # SuccessLabel("Éxito!😀"),
            # PushButtons
            PushButton("PrimaryButton", "PrimaryButton"),
            PushButton("SecondaryButton", "SecondaryButton"),
            PushButton("InfoButton", "InfoButton"),
            PushButton("SuccessButton", "SuccessButton"),
            PushButton("WarningButton", "WarningButton"),
            PushButton("DangerButton", "DangerButton"),
            PushButton("DarkButton", "DarkButton"),
            PushButton("LightButton", "LightButton"),
            PushButton("OutlinedButton", "OutlinedButton"),
            button
            
        ]    
        
        for component in components:
            self.layout.addWidget(component)
        
        icon_camera_ban = qta.icon(
            "fa6s.camera",
            color = "blue",
            color_active = "orange"
        )

        btn_stacked = PushButton("Cámara Prohibida", "OutlinedButton")
        btn_stacked.setIcon(icon_camera_ban)

        self.layout.addWidget(btn_stacked)
        
        self.menu_bar.add_shortcut("quit", "Ctrl+K", self.close)

        self.menu_bar.bind("clean_light_theme", "triggered", lambda: self.root.change_theme("clean-light"))
        self.menu_bar.bind("modern_dark_theme", "triggered", lambda: self.root.change_theme("modern-dark"))
        self.menu_bar.bind("modern_dark_esmerald_theme", "triggered", lambda: self.root.change_theme("modern-dark-esmerald"))
        self.menu_bar.bind("bootstrap_theme", "triggered", lambda: self.root.change_theme("bootstrap"))