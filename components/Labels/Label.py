from PySide6.QtWidgets import QLabel
from typing import Literal

class Label(QLabel):
    def __init__(self, text: str, _type: Literal["InfoAlert", "WarningAlert", "SuccessAlert", "DangerAlert"]):
        super().__init__(text)

        self.setObjectName(_type) # Nombre Representativo del componente en el archivo 'theme/push_button.qss'

class InfoAlert(Label):
    def __init__(self, text: str):
        self.name = "InfoAlert"

        super().__init__(text, self.name)

class WarningAlert(Label):
    def __init__(self, text: str):
        self.name = "WarningAlert"

        super().__init__(text, self.name)

class SuccessAlert(Label):
    def __init__(self, text: str):
        self.name = "SuccessAlert"

        super().__init__(text, self.name)

class DangerAlert(Label):
    def __init__(self, text: str):
        self.name = "DangerAlert"

        super().__init__(text, self.name)

