from PySide6.QtWidgets import QPushButton
from typing import Literal
from PySide6.QtCore import Qt

# se definen los tipos de botón para el tipado estático
# ButtonType = Literal["PrimaryButton", "SecondaryButton", "DangerButton", "SuccessButton", "WarningButton", "InfoButton", "LightButton", "DarkButton"]

class PushButton(QPushButton):
    """
    Clase base de **`Fluvel`** para botones estilizados. Las subclases deben definir el atributo '_button_type'.
    """

    _button_type = "PushButton"

    def __init__(self, text: str):
        super().__init__(text)

        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._button_type) 

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)
    
    def bind(self, event, controller):
        pass
  
class PrimaryButton(PushButton):
    _button_type = "PrimaryButton"

class SecondaryButton(PushButton):
    _button_type = "SecondaryButton"

class DangerButton(PushButton):
    _button_type = "DangerButton"

class SuccessButton(PushButton):
    _button_type = "SuccessButton"

class WarningButton(PushButton):
    _button_type = "WarningButton"

class InfoButton(PushButton):
    _button_type = "InfoButton"

class LightButton(PushButton):
    _button_type = "LightButton"

class DarkButton(PushButton):
    _button_type = "DarkButton"

class OutlinedButton(PushButton):
    _button_type = "OutlinedButton"
