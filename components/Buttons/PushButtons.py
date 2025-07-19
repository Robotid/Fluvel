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

    def __init__(self, text: str):
        super().__init__(text)

        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._button_type) 

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)
    
    def bind(self, event, controller):
        pass

class PushButton(FluvelPushButton):
    def __init__(self, text: str, _type: ButtonType = "PushButton"):

        # set the button type
        self._button_type = _type

        super().__init__(text)

class PrimaryButton(FluvelPushButton):
    _button_type = "PrimaryButton"

class SecondaryButton(FluvelPushButton):
    _button_type = "SecondaryButton"

class DangerButton(FluvelPushButton):
    _button_type = "DangerButton"

class SuccessButton(FluvelPushButton):
    _button_type = "SuccessButton"

class WarningButton(FluvelPushButton):
    _button_type = "WarningButton"

class InfoButton(FluvelPushButton):
    _button_type = "InfoButton"

class LightButton(FluvelPushButton):
    _button_type = "LightButton"

class DarkButton(FluvelPushButton):
    _button_type = "DarkButton"

class OutlinedButton(FluvelPushButton):
    _button_type = "OutlinedButton"

class LinkButton(FluvelPushButton):
    _button_type = "LinkButton"
