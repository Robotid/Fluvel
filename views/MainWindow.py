# views.MainWindow

from core import AppWindow
from components.Labels.FluvelAlertLabel import InfoAlert, WarningAlert, SuccessAlert, DangerAlert
from components import PushButton

class MainWindow(AppWindow):
    def __init__(self):
        super().__init__()

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        label_name = InfoAlert(f"Nombre de la Aplicación: {self.app_name}")
        label_version = WarningAlert(f"Versión: {self.version}")
        label_theme = SuccessAlert(f"Tema: {self.theme}")
        label_size = DangerAlert(f"Tamaño de Ventana: {self.window_width}x{self.window_height}.")

        # label = Label("Todo salió bien", "WarningAlert")

        button1 = PushButton("PrimaryButton", "PrimaryButton")
        button2 = PushButton("SecondaryButton", "SecondaryButton")
        button3 = PushButton("InfoButton", "InfoButton")
        button4 = PushButton("SuccessButton", "SuccessButton")
        button5 = PushButton("WarningButton", "WarningButton")
        button6 = PushButton("DangerButton", "DangerButton")
        button7 = PushButton("DarkButton", "DarkButton")
        button8 = PushButton("LightButton", "LightButton")
        button9 = PushButton("OutlinedButton", "OutlinedButton")

        # labelInfo = AlertLabel("Todo salió bien", "SuccessAlert")

        components = [label_name, label_version, label_theme, label_size,
                      button1, button2, button3, button4, button5, button6,
                      button7, button8, button9]    
        
        for component in components:
            self.layout.addWidget(component)

        # menubar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.close)
        
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Redo")

    def quit_app(self):
        print("Saliendo de la app")