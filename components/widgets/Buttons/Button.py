from typing import Literal, TypedDict
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

ButtonStyles = Literal["primary", "secondary", "info", "success",
                       "warning", "danger", "dark", "light",
                       "primary-outlined", "secondary-outlined",
                       "info-outlined", "success-outlined",
                       "warning-outlined", "danger-outlined",
                       "dark-outlined", "light-outlined"]

class ButtonKwargs(TypedDict, total=False):
    text: str
    style: ButtonStyles | None

class Button(QPushButton):
    """
    Clase base de **`Fluvel`** para **`QPushButton`**.
    """

    style: ButtonStyles = "primary"

    def __init__(self, text: str, style: ButtonStyles | None = None) -> None:
        super().__init__(text)

        if style:
            self.style = style

        # Nombre Representativo del componente en el archivo 'theme/PushButtons.qss'
        self.setProperty("class", self.style)

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)
        
    def bind(self, event, controller):
        pass
