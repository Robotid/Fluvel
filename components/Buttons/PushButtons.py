# Componente QPushButton
from PySide6.QtWidgets import QPushButton
from typing import Literal

class PushButton(QPushButton):
    def __init__(self, text: str, _type: Literal["PrimaryButton", "SecondaryButton", "DangerButton", "SuccessButton", "WarningButton", "InfoButton", "LightButton", "DarkButton"]):
        super().__init__(text)

        self.setObjectName(_type) # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
    
class PrimaryButton(PushButton):
    def __init__(self, text: str):
        self.name = "PrimaryButton"

        super().__init__(text, self.name)

class SecondaryButton(PushButton):
    def __init__(self, text: str):
        self.name = "SecondaryButton"

        super().__init__(text, self.name)

class DangerButton(PushButton):
    def __init__(self, text: str):
        self.name = "DangerButton"

        super().__init__(text, self.name)

class SuccessButton(PushButton):
    def __init__(self, text: str):
        self.name = "SuccessButton"

        super().__init__(text, self.name)

class WarningButton(PushButton):
    def __init__(self, text: str):
        self.name = "WarningButton"

        super().__init__(text, self.name)

class InfoButton(PushButton):
    def __init__(self, text: str):
        self.name = "InfoButton"

        super().__init__(text, self.name)

class LightButton(PushButton):
    def __init__(self, text: str):
        self.name = "LightButton"

        super().__init__(text, self.name)

class DarkButton(PushButton):
    def __init__(self, text: str):
        self.name = "DarkButton"
        super().__init__(text, self.name)

class OutlinedButton(PushButton):
    def __init__(self, text: str):
        self.name = "OutlinedButton"
        super().__init__(text, self.name)