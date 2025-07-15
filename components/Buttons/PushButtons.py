# Componente QPushButton
from PySide6.QtWidgets import QPushButton

class PushButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "PrimaryButton"
    
        self.instantiate() 
    
    def instantiate(self):
        self.setObjectName(self.name) # Nombre Representativo del componente en el archivos 'theme/push_button.qss'
    
class PrimaryButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "PrimaryButton"

        self.instantiate()

class SecondaryButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "SecondaryButton"

        self.instantiate()

class DangerButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "DangerButton"

        self.instantiate()

class SuccessButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "SuccessButton"

        self.instantiate()

class WarningButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "WarningButton"

        self.instantiate()

class InfoButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "InfoButton"

        self.instantiate()

class LightButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "LightButton"

        self.instantiate()

class DarkButton(PushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.name = "DarkButton"

        self.instantiate()