from core import AppWindow
from components import PushButton, OutlinedButton, PrimaryButton, SecondaryButton, SuccessButton, DangerButton, DarkButton, InfoButton, WarningButton, LightButton
from components import Label, InfoAlert, WarningAlert, SuccessAlert, DangerAlert

class MainWindow(AppWindow):
    def __init__(self, app_config: dict):
        super().__init__(app_config)

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        label_name = InfoAlert(f"Nombre de la Aplicación: {self.app_name}")
        label_version = WarningAlert(f"Versión: {self.version}")
        label_theme = SuccessAlert(f"Tema: {self.theme}")
        label_size = DangerAlert(f"Tamaño de Ventana: {self.window_width}x{self.window_height}.")

        primary_button = PrimaryButton("PrimaryButton")

        secondary_button = SecondaryButton("SecondaryButton")

        danger_button = DangerButton("DangerButton")

        success_button = SuccessButton("SuccessButton")

        warning_button = WarningButton("WarningButton")

        info_button = InfoButton("InfoButton")

        dark_button = DarkButton("DarkButton")

        light_button = LightButton("LightButton")

        outlined_button = OutlinedButton("OutlinedButton")

        label = Label("Todo salió bien", "SuccessAlert")

        self.layout.addWidget(label_name)
        self.layout.addWidget(label_version)
        self.layout.addWidget(label_theme)
        self.layout.addWidget(label_size)
        self.layout.addWidget(primary_button)
        self.layout.addWidget(secondary_button)
        self.layout.addWidget(danger_button)
        self.layout.addWidget(success_button)
        self.layout.addWidget(warning_button)
        self.layout.addWidget(info_button)
        self.layout.addWidget(dark_button)
        self.layout.addWidget(light_button)
        self.layout.addWidget(outlined_button)
        self.layout.addWidget(label)