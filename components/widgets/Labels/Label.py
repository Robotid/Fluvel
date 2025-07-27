from PySide6.QtWidgets import QLabel
from typing import Literal

LabelType = Literal["Label", "InfoLabel", "WarningLabel", "SuccessLabel", "DangerLabel"]

class Label(QLabel):
    """
    Clase base de **`Fluvel`** para etiquetas estilizadas. Las subclases deben definir el atributo **`_label_type`**.
    """

    _label_type: LabelType = "Label"

    def __init__(self, text: str = ""):
        super().__init__(text)
        
        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._label_type) 

class InfoLabel(Label):
    _label_type = "InfoLabel"

class WarningLabel(Label):
    _label_type = "WarningLabel"

class SuccessLabel(Label):
    _label_type = "SuccessLabel"

class DangerLabel(Label):
    _label_type = "DangerLabel"

