# views.MainWindow

from core import AppWindow
from components import Label, InfoAlert, WarningAlert, SuccessAlert, DangerAlert

class MainWindow(AppWindow):
    def __init__(self):
        super().__init__()

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        label_name = InfoAlert(f"Nombre de la Aplicación: {self.app_name}")
        label_version = WarningAlert(f"Versión: {self.version}")
        label_theme = SuccessAlert(f"Tema: {self.theme}")
        label_size = DangerAlert(f"Tamaño de Ventana: {self.window_width}x{self.window_height}.")

        label = Label("Todo salió bien", "SuccessAlert")

        self.layout.addWidget(label_name)
        self.layout.addWidget(label_version)
        self.layout.addWidget(label_theme)
        self.layout.addWidget(label_size)
        self.layout.addWidget(label)