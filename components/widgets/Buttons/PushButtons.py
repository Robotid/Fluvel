from PySide6.QtWidgets import QPushButton
from typing import Literal
from PySide6.QtCore import Qt

# se definen los tipos de botón para el tipado estático
ButtonType = Literal["Normal", "PrimaryButton", "SecondaryButton", "DangerButton", 
                     "SuccessButton", "WarningButton", "InfoButton", 
                     "LightButton", "DarkButton", "OutlinedButton",
                     "LinkButton"]

class PushButton(QPushButton):
    """
    Clase base de **`Fluvel`** para botones estilizados. Las subclases deben definir el atributo **`_button_type`**.
    """

    _button_type: ButtonType = "Normal"

    def __init__(self, text: str = "") -> None:
        super().__init__(text)

        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._button_type) 

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)
    
    def bind(self, event, controller):
        pass

class PrimaryButton(PushButton):
    _button_type: ButtonType = "PrimaryButton"

class SecondaryButton(PushButton):
    _button_type: ButtonType = "SecondaryButton"

class DangerButton(PushButton):
    _button_type: ButtonType = "DangerButton"

class SuccessButton(PushButton):
    _button_type: ButtonType = "SuccessButton"

class WarningButton(PushButton):
    _button_type: ButtonType = "WarningButton"

class InfoButton(PushButton):
    _button_type: ButtonType = "InfoButton"

class LightButton(PushButton):
    _button_type: ButtonType = "LightButton"

class DarkButton(PushButton):
    _button_type: ButtonType = "DarkButton"

class OutlinedButton(PushButton):
    _button_type: ButtonType = "OutlinedButton"

class LinkButton(PushButton):
    _button_type: ButtonType = "LinkButton"
