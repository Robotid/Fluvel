# views.MainWindow

from core import AppWindow
from components.Labels.FluvelAlertLabel import InfoAlert, WarningAlert, SuccessAlert, DangerAlert
from components import PushButton

class MainWindow(AppWindow):
    def __init__(self):
        super().__init__()

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """
        
        components = [
            # Label Alerts
            InfoAlert(f"Nombre de la Aplicación: {self.app_name}"),
            WarningAlert(f"Versión: {self.version}"),
            SuccessAlert(f"Tema: {self.theme}"),
            DangerAlert(f"Tamaño de Ventana: {self.window_width}x{self.window_height}."),
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

    def quit_app(self):
        print("Saliendo de la app")