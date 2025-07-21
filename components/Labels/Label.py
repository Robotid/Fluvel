from PySide6.QtWidgets import QLabel
from typing import Literal

LabelType = Literal["Label", "InfoLabel", "WarningLabel", "SuccessLabel", "DangerLabel"]

class FluvelLabel(QLabel):
    """
    Clase base de **`Fluvel`** para etiquetas estilizadas. Las subclases deben definir el atributo **`_label_type`**.
    """

    _label_type: LabelType = "Label"

    def __init__(self, text: str):
        super().__init__(text)
        
        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._label_type) 

class Label(FluvelLabel):
    def __init__(self, text: str, _type: LabelType = "Label"):
        
        # set the label type
        self._label_type = _type

        super().__init__(text)

class InfoLabel(FluvelLabel):
    _label_type = "InfoLabel"

class WarningLabel(FluvelLabel):
    _label_type = "WarningLabel"

class SuccessLabel(FluvelLabel):
    _label_type = "SuccessLabel"

class DangerLabel(FluvelLabel):
    _label_type = "DangerLabel"

