# Componente QPushButton
from PySide6.QtWidgets import QPushButton
from typing import Literal
from PySide6.QtCore import Qt

# se definen los tipos de botón para el tipado estático
ButtonType = Literal["PrimaryButton", "SecondaryButton", "DangerButton", "SuccessButton", "WarningButton", "InfoButton", "LightButton", "DarkButton"]

class PushButton(QPushButton):
    def __init__(self, text: str, _type: ButtonType):
        super().__init__(text)

        self.name = _type

        self.setObjectName(_type) # Nombre Representativo del componente en el archivo 'theme/push_button.qss'

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)

class PrimaryButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "PrimaryButton")

class SecondaryButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "SecondaryButton")

class DangerButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "DangerButton")

class SuccessButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "SuccessButton")

class WarningButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "WarningButton")

class InfoButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "InfoButton")

class LightButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "LightButton")

class DarkButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "DarkButton")

class OutlinedButton(PushButton):
    def __init__(self, text: str):

        super().__init__(text, "OutlinedButton")