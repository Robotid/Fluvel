# views.MainWindow

from core import AppWindow
from components import FluvelAlert, FluvelInfoAlert, FluvelWarningAlert, FluvelSuccessAlert, FluvelDangerAlert
from components import PushButton

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """
        
        components = [
            # Label Alerts
            FluvelAlert("Esto es una alerta de tipo Danger", "FluvelDangerAlert"),
            FluvelInfoAlert(f"Nombre de la Aplicación: {self.app_name}"),
            FluvelWarningAlert(f"Versión: {self.version}"),
            FluvelSuccessAlert(f"Tema: {self.theme}"),
            FluvelDangerAlert(f"Tamaño de Ventana: {self.window_width}x{self.window_height}."),
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
            PushButton("LinkButton", "LinkButton")
        ]    
        
        for component in components:
            self.layout.addWidget(component)

        self.menu_bar.bind("close_all", "triggered", self.close)
        self.menu_bar.set_property("close_all", "shortcut", "Ctrl+G")