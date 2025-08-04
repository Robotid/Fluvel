from typing import Literal, TypedDict

# Fluvel
from components.gui import StyledText

# PySide 6
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices


LabelType = Literal["Label", "InfoLabel", "WarningLabel", "SuccessLabel", "DangerLabel"]

class LabelKwargs(TypedDict, total=False):
    id_: StyledText | None
    text: str | None

class Label(QLabel):
    """
    Clase base de **`Fluvel`** para **`QLabel`**.
    """

    _label_type: LabelType = "Label"

    def __init__(self, id_: str | None = None, text: str | StyledText = None):
        super().__init__()

        # Set the Text
        if isinstance(text, StyledText):
            text = text.text
            self.setTextFormat(Qt.TextFormat.RichText)
            self.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
            self.linkActivated.connect(self.open_link)
        
        self.setText(text)
        
        # Nombre Representativo del componente en el archivo './project/static/themes/theme/PushButton.qss'
        self.setObjectName(self._label_type) 

    def open_link(self, link) -> None:
        """
        Abre un enlace externo utilizando los servicios de escritorio del sistema.
        Se invoca cuando el usuario hace clic en un enlace dentro de un Label.
        """

        QDesktopServices.openUrl(QUrl(link))

class InfoLabel(Label):
    _label_type = "InfoLabel"

class WarningLabel(Label):
    _label_type = "WarningLabel"

class SuccessLabel(Label):
    _label_type = "SuccessLabel"

class DangerLabel(Label):
    _label_type = "DangerLabel"

