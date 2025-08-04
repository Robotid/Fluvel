from PySide6.QtWidgets import QPushButton
from typing import Literal
from PySide6.QtCore import Qt

# se definen los tipos de botón para el tipado estático
ButtonType = Literal["primary", "secondary", "danger", 
                     "success", "warning", "info", "light", 
                     "dark"]

class PushButton(QPushButton):
    """
    Clase base de **`Fluvel`** para **`QPushButton`**.
    """

    style: ButtonType = "primary"

    def __init__(self, text: str, style: ButtonType | None = None) -> None:

        if style:
            self.style = style

        super().__init__(text)

        # Nombre Representativo del componente en el archivo 'theme/PushButtons.qss'
        self.setProperty("class", self.style)

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)
        
    def bind(self, event, controller):
        pass

class PrimaryButton(PushButton):
    style: ButtonType = "primary"

class SecondaryButton(PushButton):
    style: ButtonType = "secondary"

class DangerButton(PushButton):
    style: ButtonType = "danger"

class SuccessButton(PushButton):
    style: ButtonType = "success"

class WarningButton(PushButton):
    style: ButtonType = "warning"

class InfoButton(PushButton):
    style: ButtonType = "info"

class LightButton(PushButton):
    style: ButtonType = "light"

class DarkButton(PushButton):
    style: ButtonType = "dark"