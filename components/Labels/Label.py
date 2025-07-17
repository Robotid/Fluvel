from PySide6.QtWidgets import QLabel
from typing import Literal

LabelType = Literal["InfoAlert", "WarningAlert", "SuccessAlert", "DangerAlert"]

class Label(QLabel):
    def __init__(self, text: str, _type: LabelType):
        super().__init__(text)
        self.name = _type

        self.setObjectName(_type) # Nombre Representativo del componente en el archivo 'theme/push_button.qss'

class InfoAlert(Label):
    def __init__(self, text: str):

        super().__init__(text, "InfoAlert")

class WarningAlert(Label):
    def __init__(self, text: str):

        super().__init__(text, "WarningAlert")

class SuccessAlert(Label):
    def __init__(self, text: str):

        super().__init__(text, "SuccessAlert")

class DangerAlert(Label):
    def __init__(self, text: str):
        
        super().__init__(text, "DangerAlert")

