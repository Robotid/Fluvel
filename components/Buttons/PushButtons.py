from PySide6.QtWidgets import QPushButton
from typing import Literal
from PySide6.QtCore import Qt

# se definen los tipos de botón para el tipado estático
ButtonType = Literal["PrimaryButton", "SecondaryButton", "DangerButton", 
                     "SuccessButton", "WarningButton", "InfoButton", 
                     "LightButton", "DarkButton", "OutlinedButton",
                     "LinkButton"]

class FluvelPushButton(QPushButton):
    """
    Clase base de **`Fluvel`** para botones estilizados. Las subclases deben definir el atributo **`_button_type`**.
    """

    _button_type: ButtonType

    def __init__(self, text: str) -> None:
        super().__init__(text)

        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._button_type) 

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)
    
    def bind(self, event, controller):
        pass

class PushButton(FluvelPushButton):
    def __init__(self, text: str, _type: ButtonType = "PushButton") -> None:

        # set the button type
        self._button_type = _type

        super().__init__(text)

class PrimaryButton(FluvelPushButton):
    _button_type: ButtonType = "PrimaryButton"

class SecondaryButton(FluvelPushButton):
    _button_type: ButtonType = "SecondaryButton"

class DangerButton(FluvelPushButton):
    _button_type: ButtonType = "DangerButton"

class SuccessButton(FluvelPushButton):
    _button_type: ButtonType = "SuccessButton"

class WarningButton(FluvelPushButton):
    _button_type: ButtonType = "WarningButton"

class InfoButton(FluvelPushButton):
    _button_type: ButtonType = "InfoButton"

class LightButton(FluvelPushButton):
    _button_type: ButtonType = "LightButton"

class DarkButton(FluvelPushButton):
    _button_type: ButtonType = "DarkButton"

class OutlinedButton(FluvelPushButton):
    _button_type: ButtonType = "OutlinedButton"

class LinkButton(FluvelPushButton):
    _button_type: ButtonType = "LinkButton"
